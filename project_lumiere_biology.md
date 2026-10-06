# Project Lumiere Biology

Subdomain: Biochemistry. Authoring and adversarial attack kit, built from the five uploaded
instruction documents and the five golden examples.

---

## 0. Read this first: the image

I could not source an image in this session. Outbound access is governed by the environment
network policy, and the policy returned a 403 denial on every scientific host I tried: PubMed
Central, doi.org, PLoS, Frontiers, MDPI, eLife, Europe PMC, Wikimedia Commons, Image Data
Resource, EMBL EBI, Figshare and Harvard Dataverse. Only package registries and GitHub are
permitted. You can widen this under Network access in the environment settings, either by raising
the access level or by choosing Custom and adding the hosts you need while keeping the default
package manager list. The steps are at
https://code.claude.com/docs/en/cloud-environments#network-access

I also did not draw a figure. Two rules in the guide forbid it. No synthetic or schematic data of
any kind is allowed in the Life Science domain, and images must be real lab captures that may carry
artifacts a researcher would recognise. A figure I generated would be a hard reject and would also
be a fabricated result presented as real data.

So the image comes from you. The guide already prefers that: your own lab images are the strongly
preferred source, and failed or subpar assays are explicitly encouraged. Section 6 below is the
exact specification. Sections 2 and 3 are the part that actually decides whether the model fails,
and they are complete and ready to apply the moment you have the file.

---

## 1. What the task has to contain

| Field | Requirement |
|---|---|
| Image or images | Real lab capture, up to five, PNG or JPEG |
| Prompt | One analysis, single unambiguous answer, no options listed |
| Step by step solution | Numbered, visual evidence first, arithmetic shown, ends with the answer |
| GTFA | Written out verbatim, unambiguous when read alone |
| Answer format | Integer, decimal, ordered list, unordered list |
| Image description | One per image or panel, derives the answer without the image |
| Distractors | Five, each mapped to one named reasoning error |
| Model answers | Two responses, both wrong |
| Failure reason | One to three sentences diagnosing the error |
| Source and license | Original internal lab image, or source URL or DOI plus license |

---

## 2. Model weakness profile

This is the evidence base. Every row is taken from a documented failure in the golden examples,
not from my own guesswork. These are the levers to pull.

### W1. Correct reasoning, wrong measurement

The strongest and most repeatable weakness in the set.

Golden example 1, neurobiology. The response labelled the four panels correctly, stated the right
criterion for the ventricular zone, and correctly excluded panel C for lacking GFAP in that zone.
It then mismeasured the radial width and returned D then A then B. The truth was D then B then A.
The failure reason records exactly this: it described how to measure the thickness, then failed to
measure it.

Read: the model can hold the biology and still lose a magnitude comparison. Any prompt whose final
step is a fine grained spatial ranking is a high yield attack.

### W2. Counting ink instead of counting positions

Golden example 2, genetics. The prompt said that every regularly spaced location represents one
animal, including locations at zero where no bar is drawn. The response wrote that it had counted
the zero height positions, then counted only the visible bars and reported eighteen where the group
holds twenty. It also reported fourteen in a group of thirteen.

| Group | Truth | Model |
|---|---|---|
| Distant relatives | 8 | 8 |
| Close relatives | 13 | 14 |
| Affected | 20 | 18 |

Read: the model counts drawn objects. State a convention that makes absent objects countable and it
will acknowledge the convention in prose and then ignore it in the arithmetic.

### W3. Collapsing near zero to zero, and skipping the cross check

Golden example 3, cell biology. The response called the fifth data point baseline and excluded it.
The point sat clearly above the axis, and the matching gel lane in the other panel carried a
detectable product band that confirmed non zero activity. Excluding one concentration moved the
answer from fifteen to twelve.

Read: two weaknesses stack here. The model rounds a small positive value to zero, and it does not
corroborate a plot reading against the gel in the same figure. Build the figure so one panel
settles what another panel leaves ambiguous.

### W4. Nearest number instead of the correct node or feature

Golden example 4, ecology. Asked for the most recent common ancestor of named pairs, the response
took nearby and more inclusive nodes. It read thirty six where the first shared node was four, and
seventy six where it was sixty two. The failure reason states it selected nearby ancestral nodes
instead of the first shared node.

Read: in a crowded field of printed values the model attaches the value that is physically closest
to the named objects rather than the value that satisfies the definition. Crowd the region with
competing numbers and define the target by a rule rather than by proximity.

### W5. Losing sample identity across panels

Golden example 5, biochemistry, your own subdomain. Two preparations were on test, one assembled
during coexpression and one reconstituted from separate subunits. The response took the weak
binding seen with the reconstituted material and attributed it to the species that only the
coexpressed material contains. It then dropped one species from the answer and returned one name
where two were required.

Read: when a figure carries two preparations and several panels, the model merges them. This is the
single best lever available in biochemistry, because our figures almost always compare preparations.

### W6. Axis and scale handling

Named in the guide as a target, and exercised throughout the golden set. Logarithmic concentration
axes with only the endpoints labelled, unlabelled minor ticks that have to be counted, a wedge
triangle over a titration that implies the per lane concentration, and the conversion from standard
deviation to standard error at a stated replicate count. Golden example 3 required the reader to
recall that standard error equals standard deviation divided by the square root of three.

### W7. Over reliance on text over pixels

Named in the guide. The model reads the caption, the axis title and the printed fitted parameters,
then answers from those rather than from the marks. Golden example 3 defeats this by telling the
responder that the fitted curve is a visual guide only, which forces the answer out of the printed
IC50 and into the data points.

### W8. Signal versus artifact

Named in the guide and in the image standards. Real captures carry bubbles, scratches, dust,
background speckle, torn tissue and uneven loading. Golden example 1 depended on calling two red
specks background rather than signal.

### W9. The one that is not a model weakness at all

This is a lesson from two failed attempts, not from the golden examples, and it governs everything
above.

Two tasks were built on a shift assay figure. The first asked for the occupancy predicted by a single
site isotherm at the concentration in a named lane. The second asked for the ratio of two such
predictions in two different groups. Both were checked for every rule in the guide and both were
solved correctly by a model on the first attempt.

The reason is the same in each case. The answer never depended on the picture. The dilution series
was stated in the prompt, because an exact answer needed it. The binding constants were printed in
the legend as three short numbers. The lane mapping was an ordinal count. A model that knows the
binding relation can answer from the prompt text plus three legend values, and current models know
the binding relation perfectly well.

The rule that follows. A quantity that is printed on the figure or stated in the prompt is a quantity
the model already has. Adversarial difficulty lives only in quantities that must be measured off the
pixels and appear nowhere in text. Every golden example obeys this. Zone thickness in the organoid
panels is nowhere printed. Bar heights against a gridline are nowhere printed. Whether a point sits
on the axis or just above it is nowhere printed. Which node two taxa first share is nowhere printed.

Before building a task, ask one question: if the image were replaced by its caption and its printed
values, could the question still be answered? If yes, the task will not fail a model, however much
domain knowledge the arithmetic appears to need. Arithmetic is not a weakness. Measurement is.

This cuts against a second pressure. Visual magnitudes are what break models, and they are also what
make an answer arguable. The way through is a visual judgement that is coarse and categorical rather
than fine and continuous: a band that clearly dominates rather than one that marginally exceeds, a
point clearly clear of an axis rather than one that brushes it. Pick the comparison where the gap is
large enough that two experts cannot disagree, then make the count or the call feed a calculation so
the prompt is not a bare observation.

---

## 3. Three prompt architectures for biochemistry

Each one stacks several weaknesses from section 2. Each produces a short unambiguous answer that the
source publication never states, which satisfies the rule that the answer must not be findable in
the paper. Pick the one that matches the image you have.

### Architecture A. Replication planning under an inclusion rule

This is the shape that broke the model in golden example 3, rebuilt so it is a new task.

Weaknesses attacked: W3, W6, W7, W2, and arithmetic.

Image required. One figure carrying two things. First, a titration series on a gel or blot where
the lanes are tied to concentrations only by a wedge triangle and a stated range such as the lowest
and highest value, so the intermediate concentrations have to be deduced rather than read. Second, a
quantified plot of the same series with symbols and error bars, at least one point sitting just
above the axis and at least one point whose error interval touches the upper control level.

Prompt skeleton, with every convention spelled out as the rules demand:

> State the replicate count used for the plotted summary and whether the bars are standard
> deviation. Name the two controls the planned experiment will carry and nothing else. Instruct the
> responder to treat the fitted curve as a visual guide only. Instruct them to estimate error
> magnitudes from the image, and to treat an error bar that cannot be distinguished as equal to the
> diameter of the symbol. Define the inclusion rule: keep only those concentrations whose plotted
> value plus and minus its standard error does not overlap either control level. Add the tie rule:
> if the intervals overlap at two or more concentrations, only one of those is carried forward.
> Then ask for the total number of samples that will be generated and loaded.

Why it fails. The responder must convert standard deviation to standard error at the stated
replicate count, judge a point that sits just above the axis as non zero, corroborate that judgement
against the matching lane on the gel, exclude the point the axis actually crosses, and only then
multiply conditions by replicates. The documented model error was exactly one wrong call on the near
baseline point, which shifted the final integer.

Answer format: integer. The count feeds a multiplication, so this is not a pure counting prompt.

Distractor map:

| Distractor | Error it encodes |
|---|---|
| One condition fewer, times replicates | Calls the near baseline point zero, the documented failure |
| One condition more, times replicates | Keeps the point the axis crosses |
| Conditions without the controls | Drops the two controls |
| Conditions times one | Forgets the replicates |
| Uses standard deviation, not standard error | Skips the square root conversion |

### Architecture B. Which species can account for the activity

This is the shape that broke the model in golden example 5. Highest yield of the three because it
attacks W5 directly.

Weaknesses attacked: W5, W6, W3, W4.

Image required. Up to three images, numbered to match how the prompt refers to them. One showing the
species present in two preparations, such as a mass photometry histogram, a size exclusion trace or
a native gel, with the species labelled on the figure. One showing a binding or activity readout
with several series on a logarithmic concentration axis, where the series separate at a specific
concentration. One showing a functional readout per lane, with the lane concentrations implied by a
wedge and a stated range.

Prompt skeleton:

> Give the incubation and dilution conditions for each image as plain method text. Fix one specific
> concentration in the functional panel. Ask which of the labelled species could be responsible for
> the activity seen at that concentration. Require the species to be named as they are labelled in
> the species panel, without molecular weights, in any order.

Why it fails. The responder must deduce the per lane concentration from the wedge, find which series
are above baseline at that concentration, keep the two preparations separate, and recognise that a
species present before mixing in one preparation is not interchangeable with the same species formed
on demand in the other. The documented model error was precisely this merge, costing one species
from the list.

Answer format: unordered list. Keep it to two or three names so it stays short and unambiguous.

Distractor map: the full list of every labelled species, a single species, the correct pair plus the
catalytic subunit alone, a pair drawn from the wrong preparation, and the correct answer plus one
species that cannot bind at that concentration.

### Architecture C. Interpolation on a ladder with an artifact exclusion rule

Use this when what you have is a gel or a blot and nothing else.

Weaknesses attacked: W1, W8, W6, W4.

Image required. A blot or gel with an intact molecular weight ladder, several sample lanes, uneven
loading, and at least one ambiguous feature such as a bubble, a scratch, a speckle or a doublet
whose two bands are partly joined. All on image labels kept.

Prompt skeleton:

> Define what counts as a band rather than an artifact, by a stated criterion such as spanning the
> full lane width and being continuous across it. Define the ladder behaviour, that migration is
> linear in the logarithm of mass between adjacent markers. Ask for a derived quantity: the
> apparent mass of one specified feature to the nearest stated unit, or the rank order of the
> qualifying lanes by a defined property.

Why it fails. The model reads the nearest printed marker value rather than interpolating, and it
promotes an artifact to a band. Both are documented: nearest value substitution in golden example 4,
artifact versus signal in golden example 1.

Answer format: decimal to a stated number of places, or ordered list.

Distractor map: the nearest marker value rather than the interpolated one, linear interpolation in
mass rather than in the logarithm of mass, the value obtained by counting the artifact as a band,
the value from the adjacent marker on the other side, and a correct interpolation on the wrong lane.

---

## 4. Prompt rules to obey

These come straight from the pitfalls document. Breaking any of them is a major error at review.

1. No answer options in the prompt. Ask for the answer directly. If the answer space is implicitly
   bounded, it must hold at least ten possibilities.
2. One analysis only. Do not bundle an identification and a calculation. Split them into two tasks.
3. A count may not be the whole prompt. It has to feed a grade, a ratio, a classification or a
   further calculation.
4. The prompt must be answerable only from the image. If the assay class alone gets you there, the
   prompt is not testing anything.
5. Spell out every convention: what counts as positive, how to handle an indistinguishable error
   bar, whether the fitted line is a guide, how to label panels, what to do on a tie, the answer
   format and the number of decimal places.
6. If the image is published, the answer must be something the publication does not state. Derived
   integers, ratios, rank orders and counts of qualifying conditions all work.
7. Keep the wording on the interpretation side. The resources document lists terms that trip model
   safety filters and get a task refused. Reword toward reading the image rather than toward making
   or handling material.

---

## 5. Solution, description and distractor standards

### Step by step solution

Numbered. The opening steps record only what is visible, with no interpretation. Move every
hypothesis to a later step. Name the biochemistry explicitly, the pathway, the enzyme behaviour, the
control logic. Show all arithmetic in full, including unit conversions, the standard error
conversion and the final multiplication. Close with the answer on its own line.

Golden example 3 is the model to copy. It evaluates each data point in its own numbered step, states
the inclusion verdict for that point, and only then multiplies conditions by replicates.

### Image description

One per image or panel. Usually two hundred words or more. The test is strict: a reader who has the
prompt and your description, and who never sees the image, must be able to reach the answer. Report
only what is visible. Never state the answer in the description.

For a dense or crowded frame, walk it region by region, quadrant by quadrant, and flag every joined
or overlapping pair that the reader has to resolve, without ever stating the resulting count or the
answer. Golden example 2 does this by listing every bar position in order with its height described
against the gridlines. Golden example 3 does it by giving each symbol its position against named
ticks and its error bar length in units of symbol diameters.

Describe positions against labelled ticks, and sizes relative to another feature in the image.
Never against absolute pixels.

### Distractors

Five. Each one plausible to a nonexpert and dismissable only by an expert. Each anchored to a
specific error from section 2, not invented to fill the slot. The tables in section 3 are already
built this way.

### Model testing and failure reason

Both responses must be wrong. If a model gets it right first try, redesign the prompt, swap in a
harder image, or retire the task. Do not deliver it.

Write the failure reason in one to three sentences using the structure golden example 4 uses: where
the error occurs, what the model said against what is true, why the correct reading differs, and
what it cost in the final answer.

---

## 6. Image specification

| Property | Requirement |
|---|---|
| Format | PNG or JPEG only |
| Size | Under 5 MB |
| Long edge | Around 2000 pixels |
| Count | Five maximum per task |
| Resolution | Enough that a human reviewer can reach the answer |
| Naming | Image 1, Image 2 and so on, matching exactly how the prompt refers to them |
| Background | Not transparent |

Keep every on image label: axis labels, lane labels, scale bars, colour legends, ladder markings,
magnification indicators. Do not crop them out. Use the original capture resolution, never a
screenshot of a screenshot, and never a dark mode screenshot where coloured text goes unreadable. Do
not sharpen, enhance or colour correct beyond the original.

Add nothing after capture. No arrows, circles, boxes, text callouts, highlighting or segmentation
overlays. Markings that are naturally part of the bench workflow are fine, including handwritten
lane labels, sample identifiers, grids and dates. Elements the instrument itself burned in are fine.

The model must not be able to read the answer straight off the image.

### Licensing

| Source | Allowed |
|---|---|
| Original internal lab image | Yes, and preferred. Failed assays are a great fit |
| CC BY 2.0, 3.0, 4.0 | Yes, with attribution, do not modify the image |
| CC BY SA | Yes, derivatives keep the same license |
| CC0 | Yes |
| CC BY NC, CC BY ND, CC BY NC ND | No |
| All rights reserved, or no license stated | No |
| BioRender figures | No, hard block even inside a CC BY paper |
| bioRxiv and other preprints | No, not peer reviewed |
| Intended for a future publication | No |

Licensing is the single most common reason a delivered task is rejected. Verify before you author
around the image. If you cannot find clear license information, treat it as all rights reserved and
drop it. Open reading access is not reuse permission, and the figure license can differ from the
article license, so check the figure caption itself. A figure used as the only image in one task
cannot be the only image in another, though it can be reused alongside previously unused figures.

### Where to look, once network access allows it

From the resources document. Your own bench images stay the preferred source.

Repositories: BioImage Archive at EMBL EBI, Image Data Resource, Figshare filtered to CC BY or CC0,
Harvard Dataverse, NIH Open i, PubMed Central open access subset, Wikimedia Commons checked per
file, The Cancer Imaging Archive, PIDAR.

Journals, always checking the per article license: PLoS, eLife, Frontiers, MDPI, and the open access
articles only at Nature.

---

## 7. Review bar

Three and above passes. A score of three still needs fixes before delivery.

| Score | Meaning |
|---|---|
| 5 | No errors at all, delivery ready |
| 4 | One or two minor errors |
| 3 | Three or four minor errors |
| 2 | Any major error, or more than four minor ones |
| 1 | No effort, or three or more major errors, flag to a lead |

Major error tags: prompt with multiple answers, invalid prompt, no or invalid image source,
incorrect answer, ambiguous answer, answer that runs to a long sentence, unclear image, wrong image
format, heavily edited image, invalid license for an online image, invalid model failure, not enough
model failures, wrong subtype.

Minor error tags: missing or incorrect failure justification, partial or incorrect solution steps,
mismatched distractors, wrong answer format or decimal places, grammar.

---

## 8. Submission checklist

Image parameters
- [ ] Matches the assigned supertype and subtype
- [ ] PNG or JPEG
- [ ] Original resolution, labelled Image 1, Image 2 and so on

Licensing
- [ ] License row filled for every external image with type, source URL or DOI, and attribution
- [ ] Original lab images marked as original internal lab image
- [ ] License is CC BY, CC BY SA or CC0
- [ ] No BioRender or other noncommercial creation tool
- [ ] Source article peer reviewed and within the date cutoff
- [ ] Not previously used as the only image in another task

Prompt, solution and answer
- [ ] Answerable only from the image
- [ ] Specific, unambiguous, every convention stated
- [ ] Solution numbered, anchored in visual evidence, names the biochemistry, shows the arithmetic
- [ ] Answer written out verbatim and unambiguous read alone

Model testing
- [ ] Both responses failed
- [ ] Failure reason written, one to three sentences
- [ ] Nothing delivered that a model answered correctly first try

Image description
- [ ] Present for every image and panel
- [ ] Sufficient to reach the answer without the image
- [ ] Reports only what is visible, never states the answer
- [ ] Matches the image, no mismatched features, labels or values

Distractors
- [ ] Five, each plausible to a nonexpert and each mapped to a named error

---

## 9. What I need from you to finish the task

Upload one biochemistry image set and I will write the whole task against it: prompt, numbered
solution, answer, answer format, image description per panel, five mapped distractors, and the
failure reason template ready for the two model responses.

Best fit, in order:

1. Your own titration gel or blot photographed with the wedge and the concentration range on it,
   plus the quantified plot from the same experiment. This feeds Architecture A.
2. Your own species panel plus binding curve plus activity gel across two preparations, one
   assembled and one reconstituted. This feeds Architecture B and is the strongest attack.
3. A single blot or gel with an intact ladder, uneven loading and a real artifact. This feeds
   Architecture C.

Failed and subpar assays are welcome and explicitly encouraged by the guide.

One thing I will not do: invent the numbers. The solution has to be read off the real image, because
a fabricated set of values would fail review on the answer and would make the whole task worthless
as an evaluation item.
