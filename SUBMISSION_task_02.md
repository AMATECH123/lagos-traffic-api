# Submission pack, Project Lumiere Biology, Task 02

Gel electrophoresis. A fingerprinting gel where the answer exists nowhere in text and has to be read
off the pixels. Built after the first task was solved by a model.

---

## 1. Image

```
Image_1_RAPD_gel.jpg
```

JPEG, 723 by 670, 80 KB. See section 16, resolution is the one open risk on this task.

## 2. Image source

```
External, open access. PubMed Central open access subset, PMCID PMC9778174, Figure 1.
```

## 3. Source URL or DOI

```
https://doi.org/10.3390/gels8120760
```

## 4. License

```
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
```

Attribution if a separate field asks:

```
Gels 2022, 8(12), 760, Figure 1. © 2022 by the authors. Licensee MDPI, Basel, Switzerland. CC BY 4.0.
```

## 5. Reference material, full article title

Paste verbatim, dashes included.

```
Agarose Gel Electrophoresis-Based RAPD-PCR—An Optimization of the Conditions to Rapidly Detect Similarity of the Alert Pathogens for the Purpose of Epidemiological Studies
```

## 6. Published in

```
Gels (MDPI, Basel), Vol. 8, Issue 12, 2022, article 760. ISSN 2310-2861.
```

## 7. Profession

```
Microbiologists
```

Confirm the O*NET code before submitting. The site is blocked from this session.

## 8. Task type

```
Supertype: Gel Electrophoresis and Western Blots
Subtype: Agarose gels (DNA/RNA)
```

---

## 9. Prompt

```
Image 1 shows an agarose gel of RAPD PCR products. The lane marked LL is a DNA size marker, the lane marked K(-) is a no template control, and the nineteen numbered lanes are the amplification profiles of nineteen bacterial strains, all run with the same single primer under identical conditions.

Most bands in this gel appear in every numbered lane and so carry no discriminating information. One band position behaves differently. At that position the band is solid and dark in some of the numbered lanes, comparable in intensity to the strongest band in those same lanes, while every other numbered lane shows at most a faint smudge at the same position. No other band position in the gel behaves this way.

Give the numbers of the strain lanes in which that band is solid and dark. Return them as a comma separated list in ascending order.
```

## 10. Answer format

```
Ordered list
```

## 11. Ground truth final answer

```
16, 17
```

---

## 12. Step by step solution

```
Step 1: Establish which lanes are strain lanes. Reading the labels along the top, the leftmost lane is LL, then nineteen lanes numbered 1 to 19, then a final lane marked K(-). LL is the size marker and K(-) is the no template control, so neither is a strain profile and neither can carry an answer. The strain lanes are the nineteen numbered ones.

Step 2: Confirm the control is clean. The K(-) lane shows no amplification product anywhere along its length. Any band seen in the numbered lanes is therefore a genuine amplification product rather than primer artefact or carry over contamination.

Step 3: Establish the shared background pattern. Scanning across the numbered lanes, the same series of bands recurs in every one of them: a very strong band a little below the 2000 position, a strong band around 1500, a strong band near 600, and several fainter bands. Bands shared by all nineteen strains are monomorphic and cannot separate one strain from another, so they are set aside.

Step 4: Look for a position where the pattern breaks. Working down each lane and comparing the same height across all nineteen, one position behaves differently from the rest. It lies between the 1000 and 1500 marks of the size marker, closer to 1000.

Step 5: Read that position across every numbered lane. In lanes 1 to 15, 18 and 19 the position carries at most a faint grey smudge, much weaker than the strong bands in those same lanes. In two adjacent lanes it is instead a solid dark band, as intense as the strongest band in its own lane.

Step 6: Identify those two lanes by their printed numbers. Counting the numerals along the top of the gel, and not counting the marker lane LL, they are lane 16 and lane 17.

Step 7: Check no other position behaves the same way. Every other band in the gel is either present across all nineteen strains or faint across all nineteen. The band between 1000 and 1500 is the only polymorphic one, and it marks strains 16 and 17 as a pair.

Step 8: Report in ascending order as asked.

Final Answer: 16, 17
```

---

## 13. Image description

```
The image is a photograph of an agarose gel, printed as dark bands on a pale background. Twenty one lanes run vertically. Labels in red along the top read, from left to right, LL, then the numbers 1 to 19 in order, then K(-). A column of red size labels runs down the left margin, reading from top to bottom 3000, 2000, 1500, 1000, 800, 500, 300 and 100, followed by the unit bp. Each of these labels sits level with a corresponding band in the LL lane, which contains a regular ladder of evenly spaced bands spanning the full height of the gel.

Small dark specks and short scratches are scattered across the whole image, including in the empty regions between lanes. These are debris on the gel or the imaging surface rather than bands, as they are irregular in shape and do not span the width of a lane.

The nineteen numbered lanes all carry a similar pattern. In every one of them there is a very intense thick band a little below the 2000 level, a strong band close to the 1500 level, a strong compact band a little above the 500 level, and a series of fainter bands between those, together with faint material near the 300 level. The whole pattern drifts gradually downward from left to right across the gel, so that the same band sits slightly lower in the higher numbered lanes than in the lower numbered ones.

One position departs from this shared pattern. It lies between the 1000 and 1500 labels, closer to 1000. In lanes 1 to 15 and in lanes 18 and 19 this position shows only a faint grey smudge, far weaker than the strong bands in the same lanes. In lanes 16 and 17 the same position instead carries a solid dark band of a thickness and darkness comparable to the strongest band in those lanes. Lanes 16 and 17 also show a slightly weaker band than their neighbours at the position just above it.

The K(-) lane at the far right is blank. It carries no band at any height, only the pale background and a few of the same scattered specks.
```

Note for the reviewer check: the description gives enough to reach the answer without the image,
and never names lanes 16 and 17 as the answer, only as a description of what is visible.

---

## 14. Distractors

```
17, 18
```
```
15, 16
```
```
16
```
```
13, 14, 15
```
```
16, 17, 18
```

| Value | Error it encodes |
|---|---|
| 17, 18 | Counts the marker lane LL as lane 1, shifting every printed number up by one |
| 15, 16 | Miscounts the lane numerals in the opposite direction |
| 16 | Spots only one of the two lanes and stops |
| 13, 14, 15 | Picks the region where the shared band of three neighbouring lanes happens to align, mistaking gel drift for a polymorphism |
| 16, 17, 18 | Includes a neighbouring lane whose band at that position is only faint |

---

## 15. Why this should fail a frontier model

This task was built directly from why the previous one failed to fail. Nothing here is printed. The
answer is not in the article, which mentions base pairs only for the marker range and the primer
length and discusses the band patterns only qualitatively, saying they were not sufficient to
distinguish strains of great similarity. Replacing the image with its caption leaves the question
unanswerable, which is the test the previous task could not pass.

What it attacks:

- Dense field discrimination. Nineteen near identical lanes must be compared position by position.
  Golden example 1 showed a model reasoning correctly about which panels qualified and then
  misjudging the magnitudes, and golden example 2 showed it miscounting positions in a crowded row.
- Lane indexing. The marker lane sits left of lane 1 and is not numbered. Counting from the left edge
  rather than from the printed numerals shifts the whole answer by one, which is the same off by one
  that broke the model in golden example 2.
- Signal against artefact. The gel carries scattered specks and scratches, named in the guide as a
  target and exercised in golden example 1, where two red specks had to be called background.
- Drift. The pattern slides downward from left to right, so a model comparing a fixed height across
  the gel rather than tracking each lane's own pattern will land on lanes 13 to 15.

The answer is categorical rather than marginal, which keeps it unambiguous. Measured against the
background of each lane, the band reads about 232 in lanes 16 and 17 and between 34 and 57 in all
seventeen other numbered lanes, with nothing in between. The strongest band in lanes 16 and 17 reads
about 239, so the distinguishing band really is comparable to it.

---

## 16. Open risk, read before submitting

The publisher's own figure file is 723 by 670. That is the largest version that exists, both in the
article page and inside the article PDF, so it cannot be improved without upscaling, and upscaling is
post processing that the guide forbids. The project asks for roughly 2000 pixels on the long edge.

The band that decides the answer is clearly visible at native size, and the lane numerals and size
labels are legible, so a human reviewer can reach 16, 17. The risk is that a reviewer applies the
pixel guidance as a hard floor and marks the image unclear.

Decide before you invest in the model runs. If your reviewers enforce the pixel count strictly, say
so and I will find another gel. If they apply it as guidance where the answer is legible, this task
is ready.

Other checks before submitting:

- Open the DOI and confirm it resolves and shows CC BY 4.0.
- Confirm a 2022 article sits inside the current date cutoff.
- Confirm the subtype, agarose gels for DNA and RNA, matches what you were assigned.
- Both models must fail. If a model answers 16, 17 first time, do not submit it.
