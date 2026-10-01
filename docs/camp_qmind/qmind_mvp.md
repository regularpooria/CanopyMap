# Camp QMIND Demo Day!

Welcome everyone! Today we will be working on a little demo of our project to showcase that it is viable & computable.

## What we will be doing

CanopyMap is made up of 3 main segments:

- Data
- Segmentation Model
- Tracking
- (OPTIONAL) UI Interface

We are going to make an MVP of our project
> *What is MVP you ask?* it stands for Minimum Viable Product; It asks us to boil down our project to its defining features, that are essential to its meaning and cannot be removed. 

We are going to use a BIG ASS image segmentation model to pick out parts of the pictures that have plants in them, and using that we will _try_ to estimate growth using highschool formulas.

### 1. Data

We are going to make a small dataset of plants growing over time, bonus if it's in a vertical farm. 

### 2. Segmentation Model

We are going to try to run `SAM3` from facebook on a colab notebook and mess around with it to try to get it to segment things for us

#### SAM? who let sam cook

- SAM stands for *Segment Anything Model* which means you can throw anything at it.
- SAM3 takes in a text prompt as an additional input which lets us prompt the model about what to segment. For example the text prompt can be "nose" and we give it a portrait, it will segment the portion of the image that is the nose and give it back to us.

[sam meme](../assets/sam_meme.jpg)


### 3. Tracking

For our actual project we are going to use more sphosticated tracking algorithms that include factors such as pixel matching, pixel adaptation and require individual segments of a single plant (stem, root, leaves, ...) to work properly as we are tracking each individual segment. This require more knowledge and time to get setup and get working properly, so as an MVP we are going to take a simpler approach.

#### ok so what is the simpler approach?

We are going to figure this out together! we need to find a dataset or reference that has pictures of plants and their respective biomass. Using this we can make a simple linear/non-linear regression based off of how big the mask is in the picture. It won't be super duper accurate, but it will be good enough for an MVP. Alternatively we could also find a github repo that does this already and we'd save ourselves a lot of time.


### What are we going to use?

... to be filled out later