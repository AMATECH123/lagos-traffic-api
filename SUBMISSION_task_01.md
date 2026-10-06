# Submission pack, Project Lumiere Biology, Task 01

Every platform field, in order, ready to paste. Copy the block under each heading.

---

## 1. Image

Upload one file only.

```
Image_1_EMSA_rELAV.jpg
```

JPEG, 2000 by 1037, 336 KB. Backup at publisher resolution kept as
`Image_1_EMSA_rELAV_original_3102px.jpg` if a reviewer asks.

---

## 2. Image source

```
External, open access. PubMed Central open access subset, PMCID PMC13293991, Figure 4.
```

---

## 3. Source URL or DOI

```
https://doi.org/10.21769/BioProtoc.5583
```

---

## 4. License

```
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
```

Attribution, if a separate field asks for it:

```
Bio-protocol 2026;16(12):e5583, Figure 4. © 2026 The Authors. CC BY 4.0.
```

---

## 5. Reference material, the full article title

Paste verbatim, dashes included.

```
Electrophoretic Mobility Shift Assay (EMSA) for Assessing RNA–Protein Binding and Complex Formation Using Recombinant RNA-Binding Proteins and In Vitro–Transcribed RNA
```

---

## 6. Published in

```
Bio-protocol (Bio-protocol, LLC), Vol. 16, Issue 12, 2026, article e5583. ISSN 2331-8325.
```

---

## 7. Profession

```
Biochemists and Biophysicists
```

The O*NET code for this title is 19-1021.00. Confirm it on O*NET before you submit, because the
network policy here blocks that site and I could not open it.

---

## 8. Task type

```
Supertype: Gel Electrophoresis and Western Blots
Subtype: Native and non denaturing PAGE, electrophoretic mobility shift assay
```

Match these to whatever the platform pre assigned. If the assignment differs, tell me and I will
re cut the task to fit it.

---

## 9. Prompt

```
In the experiment shown, a radiolabelled RNA probe was held at 100 pM, roughly one hundred fold below the dissociation constants measured here, and recombinant ELAV was added from a serial dilution prepared at 1 µM, 250 nM, 62.5 nM, 15.6 nM and 3.9 nM, alongside a buffer only control containing no protein.

Panel A shows the resulting gel. The eighteen numbered lanes form three consecutive groups, one group per RNA, in the order RNA 1, RNA 2, RNA 3 from left to right. Within each group the minus sign marks the control lane, and the wedge marks the lanes that received protein, rising from left to right. Panel B reports the quantification for the same three RNAs together with the fitted dissociation constant of each.

Treating the interaction as a single site equilibrium, and taking the free protein concentration to be well approximated by the total protein concentration under these conditions, calculate the percentage of RNA 2 predicted to be bound in lane 10. Report the percentage to two significant figures.
```

---

## 10. Answer format

```
Integer
```

---

## 11. Ground truth final answer

```
42
```

---

## 12. Step by step solution

```
Step 1: Locate the RNA 2 group in panel A. The numerals below the gel run from one to eighteen, and the three group labels above it read RNA 1, RNA 2 and RNA 3, each centred over six lanes. The RNA 2 group is lanes seven to twelve.

Step 2: Identify the control lane of that group. A minus sign sits above lane seven, and the wedge begins at lane eight and widens to lane twelve. Lane seven received buffer and no protein.

Step 3: Assign a protein concentration to each lane that received protein. Five concentrations were prepared and five lanes per group received protein, so the assignment is one to one. The wedge rises from left to right, so the lowest concentration sits in the leftmost of those lanes. Lane 8 is 3.9 nM, lane 9 is 15.6 nM, lane 10 is 62.5 nM, lane 11 is 250 nM and lane 12 is 1 micromolar. The control lane carries no concentration at all, so it must not be counted as the first step of the dilution series. Lane ten therefore received 62.5 nM.

Step 4: Read the dissociation constant for RNA 2 from the legend of panel B. It is 86 nanomolar, with a standard error of 12.6. RNA 1 is 20 nanomolar and RNA 3 is 335 nanomolar, so the right series must be chosen by its legend entry, the filled cyan square on a solid black line.

Step 5: Justify the approximation. The probe is held at 100 pM while the protein is in the nanomolar range, so protein exceeds RNA by about three orders of magnitude. Essentially none of the added protein is consumed by complex formation, so the free protein concentration is well approximated by the total added concentration.

Step 6: Write the single site binding isotherm. For a one to one interaction at equilibrium, the fraction of RNA carrying bound protein equals the free protein concentration divided by the sum of the free protein concentration and the dissociation constant.

Step 7: Substitute. The protein concentration is 62.5 nanomolar and the dissociation constant is 86 nanomolar, so the fraction bound is 62.5 divided by the sum of 62.5 and 86, that is 62.5 divided by 148.5.

Step 8: Evaluate. 62.5 divided by 148.5 is 0.420875, which is 42.0875 per cent.

Step 9: Round to the precision the data support. The fitted constant is reported as 86 nanomolar, which carries two significant figures, and its standard error of 12.6 nanomolar alone moves the predicted occupancy across roughly 39 to 46 per cent. Two significant figures is the honest precision, so 42.0875 becomes 42.

Step 10: Sanity check against the figure. The measured point for RNA 2 at this concentration sits at roughly 36 per cent, below the predicted 42 per cent. A measured occupancy slightly below the equilibrium prediction is the expected direction for a gel shift assay, because some complex dissociates during electrophoresis. Prediction and measurement are consistent, and the question asks for the prediction.

Final Answer: 42
```

---

## 13. Image description

```
The image has two panels side by side, labelled A on the left and B on the right.

Panel A is a greyscale autoradiograph of a native gel, printed as dark bands on a pale background. Eighteen lanes are numbered one to eighteen in a single row beneath the gel box. Three group labels run above the gel and read RNA 1, RNA 2 and RNA 3 from left to right, each centred over six lanes. Beneath each group label is a short minus sign above the leftmost lane of that group, followed by a solid black wedge triangle that starts narrow at the next lane and widens to the right across the remaining five lanes of the group. A label to the right of the three wedges reads rELAV. The background of the first six lanes is noticeably paler than the background of the remaining twelve, and a faint vertical seam runs between lane six and lane seven.

Two features are labelled on the right of the gel. A solid triangular arrowhead at the upper right points to a band region labelled as the protein and RNA complex. Below it a tall vertical bracket marks a lower band region labelled free RNA.

Within the first group, the complex region is empty in lane one and darkens progressively from lane two to lane six, while the free RNA region is darkest in lane one and fades towards lane six. Within the second group the complex region is faint in lanes seven through ten and becomes strongly dark in lanes eleven and twelve, while the free RNA region stays dark in lanes seven through ten and drops away sharply at lanes eleven and twelve. Within the third group the complex region is faint in lanes thirteen through sixteen and strongly dark in lanes seventeen and eighteen, with the free RNA region following the opposite pattern.

Panel B is a line plot inside a black rectangular frame. The vertical axis is labelled Bound RNA in per cent, with labelled ticks at zero, twenty five, fifty, seventy five and one hundred. The horizontal axis is labelled log of protein concentration in molar, with labelled ticks at ten to the minus eight, ten to the minus seven and ten to the minus six, evenly spaced, and minor ticks between them. A legend above the frame lists three entries, each with a symbol, a name, a dissociation constant and a standard error: an open white square on a grey line for RNA 1 at twenty nanomolar plus or minus two, a filled cyan square on a solid black line for RNA 2 at eighty six nanomolar plus or minus twelve point six, and a filled grey square on a dashed black line for RNA 3 at three hundred and thirty five nanomolar plus or minus thirty six point nine.

Each series carries five symbols with vertical error bars, and the five symbols of every series sit at the same five horizontal positions, evenly spaced along the logarithmic axis, with the rightmost sitting on the ten to the minus six tick and each step to the left being a little under two thirds of a decade.

Reading each series from the leftmost symbol to the rightmost, against the labelled vertical ticks, RNA 1 as the open white square runs about 18, 43, 75, 92 and 96. RNA 2 as the filled cyan square runs about 12, 18, 36, 86 and 97. RNA 3 as the filled grey square runs about 9, 11, 24, 37 and 96.

A horizontal red dashed line runs across the frame at the fifty per cent level. Three red dashed vertical lines drop from it to the baseline. The leftmost sits between the second and third horizontal positions, the middle one sits just left of the ten to the minus seven tick and between the third and fourth horizontal positions, and the rightmost sits between the fourth and fifth horizontal positions.
```

---

## 14. Distractors

Paste one per field.

```
74
```
```
76
```
```
16
```
```
58
```
```
36
```

What each one encodes, for your own reference, not for pasting:

| Value | Error |
|---|---|
| 74 | Counts the buffer control as the first dilution step, so lane 10 reads as 250 nM |
| 76 | Takes the dissociation constant of RNA 1, 20 nM |
| 16 | Takes the dissociation constant of RNA 3, 335 nM |
| 58 | Inverts the isotherm, computing the constant over the sum |
| 36 | Reports the plotted measurement instead of the predicted value |

---

## 15. Model answers and failure reason

Run both models on the prompt and the image, paste their replies, then write the diagnosis in one to
three sentences. Template for the failure I expect most often:

```
The response correctly selects the dissociation constant of 86 nanomolar for RNA 2 and correctly applies the single site isotherm, but it assigns 250 nanomolar to lane 10 because it counts the buffer control in lane 7 as the first step of the dilution series. Lane 7 holds no protein and so carries no concentration, which places 62.5 nanomolar in lane 10 and gives 42 rather than 74.
```

If a model answers 42 on the first attempt, do not submit. Redesign the prompt, swap the image, or
retire the task.

---

## 16. Before you hit submit

- Open the DOI once in your browser and confirm it resolves and shows CC BY 4.0.
- Confirm a June 2026 article sits inside the current date cutoff.
- Confirm the pre assigned supertype and subtype match section 8.
- Confirm the O*NET code in section 7.
- Both models must have failed, with the failure reason filled in.
