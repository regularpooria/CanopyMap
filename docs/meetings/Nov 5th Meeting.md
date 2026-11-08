# Nov 5th meeting notes

## Yolo26 experiment
We tried to run Yolo26 on all of our images, there are a bunch of models within yolo26 such as nano (n), medium (m), extra large (x)

We were running it nano and were getting bad results, now we are running it on large and get better results on detecting people and parts of the hand.

The experiment is implemented in [`filter_out_bad_things_yolo26.ipynb`](../../src/dataset/filter_out_bad_things_yolo26.ipynb), which runs `yolo26x.pt` over the dataset to detect and filter out images containing blacklisted classes.

## De-fisheye-ing

We are able to somewhat fix the distortion in the pictures with trial and error. The approach is explored in [`de_fish_eye.ipynb`](../../src/dataset/de_fish_eye.ipynb), which uses the `defisheye` library with trial-and-error correction parameters (e.g. FOV 116, PFOV 100, equal-area).

## YOLOE Real-Time Open-Vocabulary Detection and Segmentation

We're going to each draw bounding boxes for 50 images and report back the result by Monday Nov 9th. 

## Tasks:

1. Andy: Check the 360-camera repo for distortion compensation related code. 400-450
2. Pooria: send Andy & Geet the 360-camera repo and report. 500-550
3. Jesuni: 1500-1550
4. Kinnel: 2000-2050
6. Geet: 2500-2550

