"""
Lagos Traffic Congestion Predictor API
Wraps the trained model so external tools like n8n, Zapier, or Make can call it over HTTP.

Run locally:
    pip install -r requirements_api.txt
    python api.py

Then it listens on http://localhost:5000

Endpoints:
    GET  /health              simple check that the API and model are up
    POST /predict              single prediction
    POST /predict_batch        multiple predictions in one call, useful for daily reports
"""

from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

MODEL_PATH = "lagos_traffic_model.joblib"
model = joblib.load(MODEL_PATH)

REQUIRED_FIELDS = [
    "route", "day_of_week", "hour", "is_weekend", "is_public_holiday",
    "is_school_day", "lanes", "length_km", "has_toll", "rain_intensity",
    "visibility_km", "has_accident", "has_roadwork", "has_police_checkpoint",
    "has_event_nearby", "fuel_scarcity", "is_market_day_route",
    "vehicle_count_est", "month", "day_of_month",
]

# Sensible defaults so n8n only has to send the fields that actually matter
# for a given use case, for example just route and hour for a quick alert check.
DEFAULTS = {
    "day_of_week": "Monday", "is_weekend": 0, "is_public_holiday": 0,
    "is_school_day": 1, "lanes": 4, "length_km": 15.0, "has_toll": 0,
    "rain_intensity": 0, "visibility_km": 8.0, "has_accident": 0,
    "has_roadwork": 0, "has_police_checkpoint": 0, "has_event_nearby": 0,
    "fuel_scarcity": 0, "is_market_day_route": 0, "vehicle_count_est": 600,
    "month": 8, "day_of_month": 15,
}


def build_record(payload: dict) -> dict:
    """Fill in defaults for any missing optional fields, keep required ones strict."""
    record = {**DEFAULTS, **payload}
    missing = [f for f in ["route", "hour"] if f not in record]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    return {field: record[field] for field in REQUIRED_FIELDS}


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(force=True, silent=True)
    if not payload:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        record = build_record(payload)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    row = pd.DataFrame([record])
    prediction = model.predict(row)[0]
    proba = model.predict_proba(row)[0]
    classes = model.named_steps["clf"].classes_

    return jsonify({
        "route": record["route"],
        "hour": record["hour"],
        "prediction": prediction,
        "probabilities": {cls: round(float(p), 3) for cls, p in zip(classes, proba)},
    })


@app.route("/predict_batch", methods=["POST"])
def predict_batch():
    """
    Accepts a list of payloads, useful for n8n looping through all routes
    for a daily report in a single call instead of many HTTP requests.
    Body: {"records": [{...}, {...}, ...]}
    """
    payload = request.get_json(force=True, silent=True)
    if not payload or "records" not in payload:
        return jsonify({"error": "Request body must be JSON with a 'records' list"}), 400

    results = []
    for item in payload["records"]:
        try:
            record = build_record(item)
        except ValueError as e:
            results.append({"error": str(e), "input": item})
            continue

        row = pd.DataFrame([record])
        prediction = model.predict(row)[0]
        proba = model.predict_proba(row)[0]
        classes = model.named_steps["clf"].classes_

        results.append({
            "route": record["route"],
            "hour": record["hour"],
            "prediction": prediction,
            "probabilities": {cls: round(float(p), 3) for cls, p in zip(classes, proba)},
        })

    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
