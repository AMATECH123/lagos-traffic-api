# Project Lumiere Biology, Task 01

Subdomain: Biochemistry. Supertype: Gel Electrophoresis and Western Blots. Subtype: native and non
denaturing PAGE, electrophoretic mobility shift assay.

Image file in this folder: `Image_1_EMSA_rELAV.jpg`

---

## Image 1

| Property | Value |
|---|---|
| Format | JPEG |
| Dimensions | 2000 by 1037 pixels |
| File size | 336 KB |
| Source | External, open access |
| Article | Electrophoretic Mobility Shift Assay (EMSA) for Assessing RNA and Protein Binding and Complex Formation Using Recombinant RNA Binding Proteins and In Vitro Transcribed RNA |
| Citation | Bio Protoc. 2026 Jun 20;16(12):e5583 |
| DOI | 10.21769/BioProtoc.5583 |
| PMCID | PMC13293991 |
| Figure | Figure 4 |
| License | CC BY |
| Retracted | No |

How it was obtained: the article is in the PubMed Central open access subset. The license field
reads CC BY in the article metadata record. The figure was taken at the publisher's embedded
resolution from the article PDF. Nothing was added, removed, sharpened, cropped or colour corrected.
The red dashed guides, the wedge triangles, the lane numbers and the band labels are all the
publisher's own, present in the published figure.

The figure was resampled once, from the publisher resolution of 3102 by 1608 down to 2000 by 1037,
to meet the guidance of roughly 2000 pixels on the long edge. That is a single Lanczos resize with no
other processing. Nothing was sharpened, cropped or colour corrected, and the aspect ratio is
unchanged. The publisher resolution file is kept beside it as
`Image_1_EMSA_rELAV_original_3102px.jpg` in case a reviewer asks for it. At 2000 pixels the lane
numerals, the axis ticks, the legend and all five symbols with their error bars in panel B remain
legible, so a human reviewer can still reach the answer.

One item to check against the platform before you submit: the article is dated June 2026, so confirm
it sits inside the current date cutoff.

---

## Prompt

> In the experiment shown, a radiolabelled RNA probe was held at 100 pM, roughly one hundred fold
> below the dissociation constants measured here, and recombinant ELAV was added from a serial
> dilution prepared at 1 µM, 250 nM, 62.5 nM, 15.6 nM and 3.9 nM, alongside a buffer only control
> containing no protein.
>
> Panel A shows the resulting gel. The eighteen numbered lanes form three consecutive groups, one
> group per RNA, in the order RNA 1, RNA 2, RNA 3 from left to right. Within each group the minus
> sign marks the control lane, and the wedge marks the lanes that received protein, rising from left
> to right. Panel B reports the quantification for the same three RNAs together with the fitted
> dissociation constant of each.
>
> Treating the interaction as a single site equilibrium, and taking the free protein concentration to
> be well approximated by the total protein concentration under these conditions, calculate the
> percentage of RNA 2 predicted to be bound in lane 10. Report the percentage to two significant
> figures.

Answer format: integer.

The dilution series and the probe concentration are method facts taken from the source protocol, so
they belong in the prompt. What the image alone supplies, and what the prompt withholds, is the
dissociation constant of RNA 2 and the position of lane 10 within its group. Neither can be had
without looking.

---

## Step by step solution

**Step 1.** Locate the RNA 2 group in panel A. The numerals below the gel run from one to eighteen
and the three group labels above it read RNA 1, RNA 2 and RNA 3, each centred over six lanes. The
RNA 2 group is therefore lanes seven to twelve.

**Step 2.** Identify the control lane of that group. A minus sign sits above lane seven, and the
wedge begins at lane eight and widens to lane twelve. Lane seven received buffer and no protein.

**Step 3.** Assign a protein concentration to each lane that received protein. Five concentrations
were prepared and five lanes per group received protein, so the assignment is one to one. The wedge
rises from left to right, so the lowest concentration is in the leftmost of those lanes.

| Lane | Protein concentration |
|---|---|
| 7 | none, buffer control |
| 8 | 3.9 nM |
| 9 | 15.6 nM |
| 10 | 62.5 nM |
| 11 | 250 nM |
| 12 | 1 micromolar |

Lane ten therefore received 62.5 nM recombinant ELAV. Note that the control lane carries no
concentration at all, so it must not be counted as the first step of the dilution series.

**Step 4.** Read the dissociation constant for RNA 2. The legend of panel B lists a value of 86
nanomolar for RNA 2, with a standard error of 12.6. The value for RNA 1 is 20 nanomolar and for RNA 3
is 335 nanomolar, so the correct series must be selected by its legend entry, which is the filled
cyan square on a solid black line.

**Step 5.** Justify the approximation the prompt licenses. The probe is held at 100 pM while the
protein is in the nanomolar range, so protein exceeds RNA by about three orders of magnitude at the
concentration in question. Essentially none of the added protein is consumed by complex formation,
and the free protein concentration is therefore well approximated by the total added concentration.

**Step 6.** Write the single site binding isotherm. For a one to one interaction at equilibrium, the
fraction of RNA carrying bound protein is the free protein concentration divided by the sum of the
free protein concentration and the dissociation constant.

**Step 7.** Substitute. The protein concentration is 62.5 nanomolar and the dissociation constant is
86 nanomolar, so the fraction bound is 62.5 divided by the sum of 62.5 and 86, which is 62.5 divided
by 148.5.

**Step 8.** Evaluate. 62.5 divided by 148.5 is 0.420875, which is 42.0875 per cent.

**Step 9.** Round to the precision the data support. The fitted constant is reported as 86 nanomolar,
which carries two significant figures, and its standard error of 12.6 nanomolar alone moves the
predicted occupancy across roughly 39 to 46 per cent. Two significant figures is therefore the honest
precision, and 42.0875 becomes 42.

**Step 10.** Sanity check against the figure. The measured point for RNA 2 at this concentration sits
at roughly 36 per cent, below the predicted 42 per cent. A measured occupancy slightly below the
equilibrium prediction is the expected direction for a gel shift assay, because some complex
dissociates during electrophoresis. The prediction and the measurement are therefore consistent, and
the question asks for the prediction.

**Final Answer: 42**

---

## GTFA

42

---

## Image description

The image has two panels side by side, labelled A on the left and B on the right.

Panel A is a greyscale autoradiograph of a native gel, printed as dark bands on a pale background.
Eighteen lanes are numbered one to eighteen in a single row beneath the gel box. Three group labels
run above the gel and read RNA 1, RNA 2 and RNA 3 from left to right, each centred over six lanes.
Beneath each group label is a short minus sign above the leftmost lane of that group, followed by a
solid black wedge triangle that starts narrow at the next lane and widens to the right across the
remaining five lanes of the group. A label to the right of the three wedges reads rELAV. The
background of the first six lanes is noticeably paler than the background of the remaining twelve,
and a faint vertical seam runs between lane six and lane seven.

Two features are labelled on the right of the gel. A solid triangular arrowhead at the upper right
points to a band region labelled as the protein and RNA complex. Below it a tall vertical bracket
marks a lower band region labelled free RNA.

Within the first group, the complex region is empty in lane one and darkens progressively from lane
two to lane six, while the free RNA region is darkest in lane one and fades towards lane six. Within
the second group the complex region is faint in lanes seven through ten and becomes strongly dark in
lanes eleven and twelve, while the free RNA region stays dark in lanes seven through ten and drops
away sharply at lanes eleven and twelve. Within the third group the complex region is faint in lanes
thirteen through sixteen and strongly dark in lanes seventeen and eighteen, with the free RNA region
following the opposite pattern.

Panel B is a line plot inside a black rectangular frame. The vertical axis is labelled Bound RNA in
per cent, with labelled ticks at zero, twenty five, fifty, seventy five and one hundred. The
horizontal axis is labelled log of protein concentration in molar, with labelled ticks at ten to the
minus eight, ten to the minus seven and ten to the minus six, evenly spaced, and minor ticks between
them. A legend above the frame lists three entries, each with a symbol, a name, a dissociation
constant and a standard error: an open white square on a grey line for RNA 1 at twenty nanomolar plus
or minus two, a filled cyan square on a solid black line for RNA 2 at eighty six nanomolar plus or
minus twelve point six, and a filled grey square on a dashed black line for RNA 3 at three hundred
and thirty five nanomolar plus or minus thirty six point nine.

Each series carries five symbols with vertical error bars, and the five symbols of every series sit
at the same five horizontal positions, evenly spaced along the logarithmic axis, with the rightmost
sitting on the ten to the minus six tick and each step to the left being a little under two thirds of
a decade.

Reading each series from the leftmost symbol to the rightmost, against the labelled vertical ticks:

| Series | Point 1 | Point 2 | Point 3 | Point 4 | Point 5 |
|---|---|---|---|---|---|
| RNA 1, open white square | about 18 | about 43 | about 75 | about 92 | about 96 |
| RNA 2, filled cyan square | about 12 | about 18 | about 36 | about 86 | about 97 |
| RNA 3, filled grey square | about 9 | about 11 | about 24 | about 37 | about 96 |

A horizontal red dashed line runs across the frame at the fifty per cent level. Three red dashed
vertical lines drop from it to the baseline. The leftmost sits between the second and third
horizontal positions, the middle one sits just left of the ten to the minus seven tick and between
the third and fourth horizontal positions, and the rightmost sits between the fourth and fifth
horizontal positions.

---

## Distractors

| Option | Reasoning error it encodes |
|---|---|
| 74 | Counts the buffer control as the first step of the dilution series, so lane ten is read as 250 nM |
| 76 | Uses the dissociation constant of RNA 1, which is 20 nM, instead of the one for RNA 2 |
| 16 | Uses the dissociation constant of RNA 3, which is 335 nM, instead of the one for RNA 2 |
| 58 | Inverts the isotherm and computes the dissociation constant over the sum rather than the protein concentration over the sum |
| 36 | Reads the plotted measurement off panel B instead of computing the predicted value |

---

## Why this is expected to fail a frontier model

**The unplotted control.** Golden example 2 established that the model counts drawn objects rather
than positions, writing that it had counted the zero height positions and then counting only the
visible bars. Here the control lane is visible on the gel but holds no concentration. A model that
treats it as the first step of the dilution series puts 250 nM into lane ten and returns 74.

**Series identity.** Golden example 5, also biochemistry, showed the model merging two preparations
across panels and dropping a species from its answer. Three dissociation constants sit side by side
in one legend here, and taking the wrong one returns 76 or 16.

**The printed measurement pulling against the calculation.** Golden example 3 defeated the model by
forcing the answer out of a printed parameter and into the data. The inverse applies here. Panel B
displays a measured value of about 36 per cent at this concentration, and a model that reports what
it sees rather than what the isotherm predicts returns 36.

**The isotherm itself.** The question cannot be answered by reading or by mapping alone. It needs the
single site binding relation and the reasoning that justifies substituting total protein for free
protein when the probe sits a hundred fold below the dissociation constant. A model that reaches for
the wrong form of the expression returns 58.

---

## Failure reason, to complete after the two model runs

Use the structure from golden example 4: where the error occurs, what the response said against what
is true, why the correct reading differs, and what it cost in the final answer.

Template for the most likely failure:

> The response correctly selects the dissociation constant of 86 nanomolar for RNA 2 and correctly
> applies the single site isotherm. It assigns 250 nanomolar to lane ten, however, because it counts
> the buffer control in lane seven as the first step of the dilution series. Lane seven holds no
> protein and so carries no concentration, which places 62.5 nanomolar in lane ten and gives 42
> rather than 74.

If a model answers 42 on the first attempt, do not deliver the task. Redesign it, swap the image,
or retire it.

---

## Checks against the submission list

| Item | Status |
|---|---|
| Format PNG or JPEG | JPEG |
| Under 5 MB | 336 KB |
| Resolution | Resampled once to 2000 px long edge, nothing else changed |
| On image labels preserved | Lane numbers, group labels, wedges, band labels, axes, legend, all intact |
| No annotation added after capture | None added, every mark is the publisher's |
| Not BioRender | Autoradiograph plus data plot |
| License on the allowed list | CC BY |
| Peer reviewed and not retracted | Yes and yes |
| Source recorded | DOI and PMCID above |
| Prompt answerable only from the image | Yes, the constant and the lane position come only from the figure |
| Requires domain expertise | Single site isotherm plus the excess ligand approximation |
| No math notation in the prompt | Plain text throughout, no LaTeX |
| Precision matches the data | Two significant figures, set by the fitted constant and its standard error |
| Answer not available in the publication | The article reports measured constants, never a predicted occupancy |
| Single unambiguous answer | One integer, 42 |
| No options listed in the prompt | None |
| Implied answer space of at least ten | A continuous percentage, not a short list of candidates |
| One analysis, not stacked | One concentration assignment feeding one calculation |
| Not a pure counting question | No counting is requested at all |
| Conventions spelled out | Dilution series, control lane, wedge direction, binding model, decimal places |
| Solution numbered, evidence first, arithmetic shown | Yes |
| Image description derives the answer without the image | Yes, the series table and lane layout are given |
| Description never states the answer | The predicted value is never given |
| Five distractors, each mapped to an error | Yes |
| Both models failed | Still to run |
| Failure reason written | Template above, fill after the runs |

---

## One open risk

The red dashed guides are the publisher's analysis overlay rather than raw capture. They are part of
the published figure, so they are not an annotation added after capture by me, and the golden
examples include comparable publisher marks such as the wedge triangle over a titration. If a
reviewer reads them as interpretation guides, the clean fix is to keep the prompt as written, since
it already instructs the responder to treat the plotted points as the measurement of record and the
guides then work against the model rather than for it.
