# Oct 29th meeting notes


## What is YOLO

It stands for "You only look once" a model by ultralytics for images (detection, segmentation, semantic segmentation, depth estimation, classification, pose estimation, and OBB.): More details here: https://docs.ultralytics.com/tasks

We're going to use Object detection for cleaning the dataset from things we don't want (aka. hands, people, scissors)

## YOLO model dataset

1. Run YOLO ("You Only Look Once") https://docs.ultralytics.com/ on the "cleaned" dataset
2. Detect foreign objects in the dataset
3. Make a blacklist of objects we want to flag for removal
4. Remove the pictures associated with those objects that are in the blacklist


### How do we make the blacklist:

We're going to look at the results and write down what we get



## Tasks:

1. Jesuni: Will de-fish-eye the images, through trial and error
2. Kinnel: Running the "Yolo tutorial.ipynb" on discord on the yolo26**x**.pt and updating the blacklist list.

 