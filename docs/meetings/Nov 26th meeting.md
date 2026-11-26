# Nov 26th meeting

> **Recording:** [YouTube link](https://youtu.be/95OPxg06JFs)

---

## Recap (from Nov 19th)

In our previous meeting (Nov 19th) we showed how a simple graphing method could visualize plant growth. It surfaced how important it is to have **dividers** and **multipliers** for different plants that are the _same size_ but at _different locations_ in the frame (perspective correction). We also noticed that the **camera itself affects how "green" something is detected** — different cameras capture color slightly differently, so a fixed greenness threshold is fragile.

---

## Key discussion

### Camera vs. "greenness" and IoU

Geet walked through a synthetic example to show that we need a robust way to measure how well we're segmenting a plant, independent of camera/color variation.

- The metric is **IoU** (_Intersection over Union_): `area of overlap / area of union`. `1.0` is a bullseye; lower means less accurate.
- Takeaway: **we should not rely only on HSV or a fixed "green" threshold.** We should look at alternative detection methods.

### Alternative segmentation methods mentioned

Geet flagged a few approaches he's aware of (not all fully explored yet) as _different ways to correct for color/greenness_:

| Method       | What it is                                                                                                                                                                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HSV**      | Hue–Saturation–Value color space; naive green ranges give inconsistent results across cameras.                                                                                          |
| **Otsu**     | Automatic thresholding that picks the optimal split between foreground/background ([Wikipedia](https://en.wikipedia.org/wiki/Otsu%27s_method)).                                         |
| **ExG**      | _Excess Green Index_: `ExG = 2g − r − b` on normalized RGB; highlights green vegetation ([reference](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ExG)). |
| **LabOTS**   | Otsu thresholding applied in the **Lab** color space (a.k.a. LAB-Otsu, common in plant-phenotyping pipelines).                                                                          |
| **Ensemble** | Combining multiple methods rather than relying on one.                                                                                                                                  |

---

## The green-filter prototype (ChaiNNer)

Pooria introduced **ChaiNNer** (he called it "Chainer") — a free, open-source, **node-based image-processing app** (think Blender/Scratch-style node programming). It's purpose-built for trying out different algorithms to see what works for your image, and supports **batch processing** over folders.

> 🔗 [chaiNNer on GitHub](https://github.com/chaiNNer-org/chaiNNer) · [chaiNNer.app](https://chaiNNer.app/)

The prototype lives in [`src/tracking/look_for_green_in_segments_chain.chn`](../../src/tracking/look_for_green_in_segments_chain.chn).

### Pipeline (what the `.chn` file does)

1. **Load** a segmented plant image (the alpha channel _is_ the segmentation mask).
2. **Split** into RGB + alpha channels.
3. **Blur** to remove surface texture from the tray/lid — texture is a real problem for both edge detection and color keying. Pooria tried several blurs (surface, lens, Gaussian, box) and found **median blur** works best; a radius of **3** was good enough. The blur flattens the color gradient into a plain color, which is what keying wants.
4. Two competing routes were compared:
   - **Output A — two chroma keys:** key out the dark parts, then key out the less-dark parts, and stack/combine the two results to keep what's common.
   - **Output B — green channel only (simpler):** after the blur, split channels and just look at the **green channel** (green parts are brighter), then run a **threshold** ("if it's bigger than this value, show it") and recombine with the original image.

### Result

Compared side-by-side across 200 frames, **Output B (the green-channel route) was preferred** — the simpler route turned out a little better. It's more resilient because it doesn't care _what kind of green_ it is. The threshold still needs tuning, but it should be less sensitive than a fixed green range.

---

## Turning it into Python

The problem: ChaiNNer has **no "save as Python"** export, but it _runs_ Python under the hood (all dependencies are Python packages). The plan:

- Feed the `.chn` file (it's just a long JSON) to **AI** and ask it to convert the node graph into **Python using NumPy and/or OpenCV** — then **manually verify** the output against reference images.
- Make it a **utility file** (like we already do with [`src/utils/distortion.py`](../../src/utils/distortion.py) for de-fisheyeing) so other parts of the pipeline can `import` it.

> 📌 **Reference data for verification** (provided by Pooria): [`src/assets/tracking/green filter/input.zip`](../../src/assets/tracking/green%20filter/input.zip) and [`output.zip`](../../src/assets/tracking/green%20filter/output.zip) — **11 frames (frames 211–221)**, input segments vs. expected output. If your Python output matches, you did it right.

---

## Stem handling

Decision: **we don't care about the stem.**

- Every plant has one, so if we miss _all_ of them we haven't really missed anything.
- The stem is near-black and turns brown as it grows, so it often isn't captured by segmentation anyway.
- In later frames the stem is covered by leaves, so it disappears from view.

---

## Tracking plan (the growth algorithm)

1. **Count green-ish pixels robustly** — using the green-channel method above (this is where we are now).
2. **Fit the growth curve.** The existing graphing code does _fitting_ (not generating points from an equation). Growth isn't linear (it's polynomial with unknown degree, and the area curve looked roughly **logarithmic**). Two options to explore:
   - **Piecewise linear estimation** — fit a small linear model over a sliding window of frames (make the window size a variable).
   - **Logarithmic (or polynomial) fit** over the whole graph, plus a **halfway-through** version (fit using only the first half and see if it predicts the rest).
3. **Normalize areas** so one day doesn't dominate the plot — otherwise the "day one" data swamps everything else.

> **Important invariant:** plant area should realistically **never go down**. Any downward movement in the data is a segmentation/camera artifact to be compensated for.

---

## Handling movement & downward data

The team discussed why the curve sometimes drops and how to fix it:

- **Plant movement + low-confidence frames** make segmentation wobble ("slightly below, slightly above, again and again").
- **Averaging** — _"progress over perfection"_: every **10 frames**, take the average of the segmentations. Removes small fluctuations, but a sustained drop still drags the average down.
- **Overlaying (union)** — overlay **all previous frames' segmentations** on top of each other and count green pixels in the resulting union. This isn't double-counting (you layer images, not sum numbers) and it "remembers" where the plant _used_ to be. Risk: it inflates if the plant actually moves.

**Decision — go two routes in parallel:**

1. **Overlay all previous frames** (union) and count green pixels. If a frame fully covers an earlier one, you don't even need to drop it — the union just absorbs it.
2. As an extension, still do the **averaging** (every 10 frames) and compare.

### Visual checkpoints

Plot the **final (overlaid) segmentation at frames 300, 500, 700, and 1000** (≈ the last masked row, 999) to visually confirm the approach is on the right track.

---

## Action items

| #   | Task                                                                                                                                          | Owner                   | Deadline  |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | --------- |
| 1   | Turn the `.chn` file into a Python **utility file** (NumPy or OpenCV); verify against `input.zip`/`output.zip`                                | **Geet**                | Tue night |
| 2   | Graph the **area** like before (base: [`kinnel_graphing_simple_nov19.ipynb`](../../src/tracking/graphing/kinnel_graphing_simple_nov19.ipynb)) | **Andy**                | Tue night |
| 2.1 | **Piecewise linear** estimation every 20 frames (make the window a **variable**)                                                              | **Andy**                | Tue night |
| 2.2 | **Logarithmic (or polynomial)** fit on the whole graph + a halfway-through fit                                                                | **Kinnel**              | Tue night |
| 3   | **Overlay** all previous frame segmentations (union) and count green pixels                                                                   | **Pooria** & **Jesuni** | TBD       |
| 4   | **Averaging** every 10 frames (alternative to overlay)                                                                                        | **Jesuni**              | TBD       |
| 5   | Plot final segmentation at frames 300, 500, 700, and 1000 (≈ last masked row 999)                                                             | **Pooria** & **Jesuni** | TBD       |

### Collaboration flow

- **Geet** finishes the utility file → send to **Discord** → **Andy** builds the area-graphing on top of it → that feeds the overlay/averaging work (Pooria/Jesuni).
- Use **AI** to convert the `.chn` JSON to Python, then **verify manually** against the reference images.
- **Pooria** will clean up the plan and push it to **GitHub** so everyone has a better reference.

### Deadline notes

- Pooria offered to help out if any piece is too heavy — coordinate in the group chat.

---

## Files & references (resolved)

- ChaiNNer graph: [`src/tracking/look_for_green_in_segments_chain.chn`](../../src/tracking/look_for_green_in_segments_chain.chn)
- Reference input/output for the green filter: [`src/assets/tracking/green filter/input.zip`](../../src/assets/tracking/green%20filter/input.zip) and [`output.zip`](../../src/assets/tracking/green%20filter/output.zip)
- Graphing notebooks: [`src/tracking/graphing/kinnel_graphing_simple_nov19.ipynb`](../../src/tracking/graphing/kinnel_graphing_simple_nov19.ipynb) and [`src/tracking/graphing/geet_graphing_simple_nov19.ipynb`](../../src/tracking/graphing/geet_graphing_simple_nov19.ipynb)
- De-fisheye utility: [`src/utils/distortion.py`](../../src/utils/distortion.py)

## External links / glossary

- [ChaiNNer (GitHub)](https://github.com/chaiNNer-org/chaiNNer) · [chaiNNer.app](https://chaiNNer.app/)
- [OpenCV](https://opencv.org/) · [NumPy](https://numpy.org/)
- [Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method)
- [Excess Green Index (ExG)](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ExG)
- [Intersection over Union (IoU)](https://en.wikipedia.org/wiki/Jaccard_index)
- [Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter)
- [Piecewise linear function](https://en.wikipedia.org/wiki/Piecewise_linear_function)
- [Median filter](https://en.wikipedia.org/wiki/Median_filter)
- [Chroma key (green screen)](https://en.wikipedia.org/wiki/Chroma_key)
- [HSV color space](https://en.wikipedia.org/wiki/HSL_and_HSV)
- [SAM 3 (Segment Anything Model 3)](https://github.com/facebookresearch/sam3)
- [Hugging Face `datasets`](https://huggingface.co/docs/datasets)
