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

> The attached image shows an electrophoretic mobility shift assay in which three synthetic RNAs were
> each titrated with recombinant ELAV protein, together with the quantification of that experiment.
>
> In panel A the gel carries eighteen numbered lanes arranged as three consecutive groups of six, one
> group per RNA, in the order RNA 1, RNA 2, RNA 3 from left to right. Within each group the minus
> sign marks the lane that received no protein, and the wedge marks the lanes that received
> recombinant ELAV, increasing from left to right.
>
> In panel B, bound RNA is plotted against protein concentration, with one point per protein
> concentration tested for each RNA. All three RNAs were tested at the same concentrations, and the
> points of each series run in the same left to right order as the corresponding lanes of that RNA in
> panel A.
>
> Treat the plotted points in panel B as the measurement of record, and treat an RNA as more than
> half bound when its bound RNA value is greater than $50\%$.
>
> Give the number of the lane in panel A that received the lowest concentration of recombinant ELAV
> at which RNA 2 is more than half bound.

Answer format: integer.

The prompt deliberately stops short of saying that the lane without protein contributes no point to
panel B. That inference is the task. It is forced rather than open, because each group holds six
lanes while each series holds five points, only one lane per group received no protein, and a binding
curve cannot carry a point for a concentration that was never tested. A biochemist resolves it in
seconds. A model that does not make the inference lands one lane low.

---

## Step by step solution

**Step 1.** Record the lane layout in panel A. The numerals printed below the gel run from one to
eighteen without a gap. The group labels above the gel read RNA 1, RNA 2 and RNA 3, and three wedge
triangles sit below those labels, one per group. Each group therefore holds six lanes: lanes one to
six are RNA 1, lanes seven to twelve are RNA 2, and lanes thirteen to eighteen are RNA 3.

**Step 2.** Record which lane in each group carries no protein. A short minus sign sits above the
first lane of each group, that is above lanes one, seven and thirteen. The wedge in each group begins
at the second lane of the group and widens to the right, so lanes two to six, eight to twelve and
fourteen to eighteen carry recombinant ELAV at five increasing concentrations.

**Step 3.** Record the structure of panel B. The vertical axis is bound RNA as a percentage, with
labelled ticks at zero, twenty five, fifty, seventy five and one hundred. The horizontal axis is the
logarithm of protein concentration in molar, with labelled ticks at ten to the minus eight, ten to
the minus seven and ten to the minus six. The legend gives RNA 1 as an open white square on a grey
line, RNA 2 as a filled cyan square on a solid black line, and RNA 3 as a filled grey square on a
dashed black line.

**Step 4.** Count the plotted points per series and deduce the correspondence. Each of the three
series carries five points, while each gel group holds six lanes. One lane per group must therefore
be unplotted. The only lane in each group that received no protein is the one marked by the minus
sign, and a binding curve plots bound RNA against protein concentration, so no point can exist for a
lane in which no protein was present. The unplotted lane is the minus lane, and the first plotted
point of a series belongs to the second lane of its group, not the first.

**Step 5.** Fix the correspondence for RNA 2. The RNA 2 group runs from lane seven to lane twelve.
Lane seven received no protein. The five plotted RNA 2 points therefore map in order onto lanes
eight, nine, ten, eleven and twelve.

**Step 6.** Read the five RNA 2 points off the vertical axis. Taking the fifty per cent gridline and
the zero baseline as the calibration, the filled cyan squares sit at approximately twelve, eighteen,
thirty six, eighty six and ninety seven per cent bound, in order of increasing protein concentration.

**Step 7.** Apply the threshold. The first three RNA 2 points lie below fifty per cent. The fourth
point, at about eighty six per cent, is the first to exceed fifty per cent.

**Step 8.** Do not take the crossing from the printed dissociation constant or from the red dashed
guides. The legend prints a dissociation constant of eighty six nanomolar for RNA 2 and a red dashed
vertical guide marks that concentration, which falls between the third and fourth plotted points. The
prompt makes panel B's plotted points the measurement of record, and the first plotted point above
fifty per cent is the fourth, not the third.

**Step 9.** Convert the fourth RNA 2 point back to a lane. From step 5 the fourth point corresponds
to the fourth protein containing lane of the RNA 2 group, which is lane eleven.

**Step 10.** Check the answer against the gel itself. In the RNA 2 group the upper band labelled as
the protein and RNA complex is faint through lanes eight, nine and ten, where free RNA still
dominates, and becomes the dominant species at lane eleven, where the free RNA band drops sharply.
The gel and the plot agree.

**Final Answer: 11**

---

## GTFA

11

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
| 10 | Maps the first plotted point onto lane seven, the lane that received no protein, so every lane assignment is one too low |
| 12 | Takes the highest concentration lane rather than the lowest lane that clears the threshold |
| 9 | Takes the crossing from the printed dissociation constant of eighty six nanomolar and the red dashed vertical guide, landing on the third concentration |
| 4 | Applies the criterion to RNA 1 instead of RNA 2 |
| 18 | Applies the criterion to RNA 3 instead of RNA 2 |

---

## Why this is expected to fail a frontier model

Each lever is one documented in the golden examples.

**The unplotted lane.** Golden example 2 established that the model counts drawn objects rather than
positions. Its response wrote that it had counted the zero height positions and then counted only the
visible bars, reporting eighteen where the group held twenty. Here the lane that received no protein
appears on the gel but contributes no point to the plot. A model that pairs the first plotted point
with the first lane of the group returns ten.

**The printed value pulling against the marks.** Golden example 3 defeated the model by telling the
responder that the fitted curve was a visual guide only, which forced the answer out of the printed
parameter and into the data points. Here the legend prints a dissociation constant of eighty six
nanomolar and a red dashed guide marks it, both of which sit between the third and fourth points. A
model that answers from the printed number rather than the plotted symbols returns nine.

**Series identity.** Golden example 5, also biochemistry, showed the model merging two preparations
across panels and dropping a species from its answer. Here three series share one frame and three
groups share one gel. A model that drifts onto the open white squares or the filled grey squares
returns four or eighteen.

**Cross panel corroboration.** Golden example 3 also showed the model failing to check a plot reading
against the matching gel lane. Here the gel independently confirms lane eleven, so a model that never
looks at panel A has no way to catch its own error.

---

## Failure reason, to complete after the two model runs

Use the structure from golden example 4: where the error occurs, what the response said against what
is true, why the correct reading differs, and what it cost in the final answer.

Template for the most likely failure:

> The response correctly identifies the three groups of six lanes and correctly reads the RNA 2
> series as crossing fifty per cent at its fourth plotted point. It then assigns that point to lane
> ten because it pairs the first plotted point with lane seven, the lane that received no protein and
> that contributes no point to panel B. Counting from lane eight, the first protein containing lane,
> the fourth point falls on lane eleven, so the response is one lane low.

If a model answers eleven on the first attempt, do not deliver the task. Redesign it, swap the image,
or retire it.

---

## Checks against the submission list

| Item | Status |
|---|---|
| Format PNG or JPEG | JPEG |
| Under 5 MB | 195 KB |
| Resolution | Resampled once to 2000 px long edge, nothing else changed |
| On image labels preserved | Lane numbers, group labels, wedges, band labels, axes, legend, all intact |
| No annotation added after capture | None added, every mark is the publisher's |
| Not BioRender | Autoradiograph plus data plot |
| License on the allowed list | CC BY |
| Peer reviewed and not retracted | Yes and yes |
| Source recorded | DOI and PMCID above |
| Prompt answerable only from the image | Yes, the lane mapping appears nowhere in the text |
| Answer not available in the publication | The article reports dissociation constants, not this lane |
| Single unambiguous answer | One integer |
| No options listed in the prompt | None |
| Implied answer space of at least ten | Eighteen lanes |
| One analysis, not stacked | One mapping and one threshold |
| Not a pure counting question | The count feeds a lane assignment |
| Conventions spelled out | Lane layout, the unplotted lane, the measurement of record, the threshold |
| Solution numbered, evidence first, arithmetic shown | Yes |
| Image description derives the answer without the image | Yes, the series table and lane layout are given |
| Description never states the answer | Lane eleven is never named |
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
