# Task 01, variant B, hardened

Same image, `Image_1_EMSA_rELAV.jpg`. Same source, licence and reference fields as the main pack.
Use this if a model solved the first version.

## What changed and why

Variant A asked for one occupancy from one isotherm. A model that knows the binding relation clears
it in a single step, and the only trap was the control lane. Variant B keeps the same physics but
doubles the surface a response has to cross without making any single reading harder.

- Two lane assignments instead of one, in two different groups, so the control lane error has two
  chances to fire.
- Two different dissociation constants pulled from a legend that holds three, so series identity
  matters twice.
- A ratio on top, which punishes an inverted isotherm instead of hiding it.
- The prompt no longer says what the minus sign means. It names only the wedge. The assignment stays
  forced, because five concentrations were prepared and six lanes sit in each group, so one lane per
  group holds none. Working out which one is now the responder's job.

## Prompt

```
In the experiment shown, a radiolabelled RNA probe was held at 100 pM, roughly one hundred fold below the dissociation constants measured here, and recombinant ELAV was added from a serial dilution prepared at 1 µM, 250 nM, 62.5 nM, 15.6 nM and 3.9 nM, alongside a buffer only control containing no protein.

Panel A shows the resulting gel. The eighteen numbered lanes form three consecutive groups, one group per RNA, in the order RNA 1, RNA 2, RNA 3 from left to right. Within each group the wedge marks the lanes that received protein, rising from left to right. Panel B reports the quantification for the same three RNAs together with the fitted dissociation constant of each.

Treating each interaction as a single site equilibrium, and taking the free protein concentration to be well approximated by the total protein concentration under these conditions, calculate the predicted bound percentage of RNA 1 in lane 4 divided by the predicted bound percentage of RNA 3 in lane 16. Report the ratio to two significant figures.
```

## Answer format

```
Decimal
```

## Ground truth

```
4.8
```

## Step by step solution

```
Step 1: Split the gel into its three groups. The numerals below the gel run from one to eighteen and the labels above it read RNA 1, RNA 2 and RNA 3, each centred over six lanes. RNA 1 is lanes one to six, RNA 2 is lanes seven to twelve, RNA 3 is lanes thirteen to eighteen.

Step 2: Find the lane in each group that holds no protein. Five concentrations were prepared but each group holds six lanes, so exactly one lane per group received none. In each group a short minus sign sits above the leftmost lane and the wedge begins at the next lane and widens to the right. The lane without protein is therefore the first of each group, that is lanes one, seven and thirteen, and these carry no concentration at all.

Step 3: Assign concentrations in the RNA 1 group. Lanes two to six received protein, rising left to right, so lane 2 is 3.9 nM, lane 3 is 15.6 nM, lane 4 is 62.5 nM, lane 5 is 250 nM and lane 6 is 1 micromolar. Lane 4 therefore received 62.5 nM.

Step 4: Assign concentrations in the RNA 3 group the same way. Lanes fourteen to eighteen received protein, so lane 14 is 3.9 nM, lane 15 is 15.6 nM, lane 16 is 62.5 nM, lane 17 is 250 nM and lane 18 is 1 micromolar. Lane 16 also received 62.5 nM.

Step 5: Read the two dissociation constants from the legend of panel B. RNA 1, the open white square on a grey line, is 20 nanomolar. RNA 3, the filled grey square on a dashed black line, is 335 nanomolar. The middle entry, 86 nanomolar, belongs to RNA 2 and is not used here.

Step 6: Justify the approximation. The probe is at 100 pM while the protein is at 62.5 nM, so protein exceeds RNA by more than two orders of magnitude and almost none of it is consumed by complex formation. Free protein is therefore well approximated by total protein.

Step 7: Write the isotherm. For a one to one interaction at equilibrium the bound fraction is the free protein concentration divided by the sum of the free protein concentration and the dissociation constant.

Step 8: Evaluate RNA 1 in lane 4. 62.5 divided by the sum of 62.5 and 20 is 62.5 divided by 82.5, which is 0.757576, that is 75.7576 per cent.

Step 9: Evaluate RNA 3 in lane 16. 62.5 divided by the sum of 62.5 and 335 is 62.5 divided by 397.5, which is 0.157233, that is 15.7233 per cent.

Step 10: Form the ratio. 75.7576 divided by 15.7233 is 4.8182. Because both lanes carry the same protein concentration, the ratio reduces exactly to the sum of 335 and 62.5 over the sum of 20 and 62.5, that is 397.5 over 82.5, which confirms 4.8182.

Step 11: Round to the precision the data support. The constants are reported to two significant figures, so the ratio is 4.8.

Final Answer: 4.8
```

## Distractors

```
2.2
```
```
0.21
```
```
3.1
```
```
0.29
```
```
17
```

| Value | Error it encodes |
|---|---|
| 2.2 | Counts the control lane as the first dilution step in both groups, putting 250 nM in lanes 4 and 16 |
| 0.21 | Swaps the two constants between the RNAs |
| 3.1 | Reads the measured points off panel B instead of computing the predicted values |
| 0.29 | Inverts the isotherm, using the constant over the sum rather than the concentration over the sum |
| 17 | Divides one constant by the other and ignores the protein concentration entirely |

## Image description

Unchanged. Use the description from the main submission pack. It already gives the lane layout, the
group boundaries, the minus signs, the wedges and all three legend entries with their constants, so a
reader can still reach 4.8 from the prompt and the description alone, and it never states the ratio.

## Failure reason template

```
The response correctly reads both dissociation constants and applies the single site isotherm to each RNA, but it assigns 250 nanomolar to lanes 4 and 16 because it counts the lane marked with a minus sign as the first step of the dilution series. That lane received buffer alone and carries no concentration, so both lanes hold 62.5 nanomolar, and the ratio is 4.8 rather than 2.2.
```

If a model answers 4.8 on the first attempt as well, the image has been exhausted for this style of
question. Say so and I will cut a different task, either on a second figure from the same article or
on a new source.
