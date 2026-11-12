# Nov 12th meeting

We now have data for segmentations of each individual plant given a box in our growth platform. The segmentations track the same id through time but may "shrink" as another plant covers the area of one plant.

We are now focusing on building an algorithm to track the plant growth based on the segmentation data we have computed using SAM 3 and a reference picture.

## Plant growth algorithm

### Requirements:

1. Track & Measure growth over time of a single plant (Growth's metric could be anything)
2. We want the plant growth to not go down as a result of poor segmentation
3. We want to consider multiple frames of the segmentation in our growth algorithm and not rely on the last frame.
4. We assume plants get enough water to stay fresh.
5. For each plant, the ones further away from the camera need a "growth multiplier" and the ones that are close to the camera need a "growth divider" . Some way to standardize growth regardless of perspective.

### Functions:

1. We need a plot (x axis is time, y axis is growth)
2.

### Algorithm ideas:

1. Count the number of green-ish pixels in the segmented area
2. Linear regression at each timestep and continuous fitting (upper and lower bound set)
3. Some sort of averaging with the segmentations to filter out tiny movements and inconsistencies in the segments + have
4. Overlaying different segments on top of each other to preserve parts of the plant that are covered later on in the experiment.

## Image Annotator

pip install digitalsreeni-image-annotator
run with "./digitalsreeni-image-annotator"

## Tasks (for everyone)

1. Count the number of green-ish pixels in the segmented area
2. Plot the different plants naively.
