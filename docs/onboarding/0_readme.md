# What is CanopyMap?

Two of the biggest pain points for agricultural tech and a barrier to automation is measuring plant growth and obtaining quality training data at a large scale. Farming environments can vary _a lot_ and the hardware that is used to monitor such environments can often be in very different conditions which makes adapting a single model to different environments very challenging.

Lots of research papers cover outdoor farming, very few try to fix the gap in training data for indoor environments. That's what we're trying to fix with CanopyMap. We have access to an aeroponic farm with lots of cameras, we are going to use existing models to run image segmentation on the plants and using that try to measure the plant growth over time. This will eventually help the farm automate their growth optimization algorithm.

## What is a Aeroponic Farm?

An aeroponic farm is a type of soilless farming system, often operated indoors, where plants are grown with their roots suspended in the air. Instead of soil, the roots receive water and nutrients through a carefully controlled mist or spray.

Many environmental and growth factors can be adjusted, including oxygen levels, nutrient concentration, water pH and acidity, humidity, grow-light duration and intensity, and watering frequency and duration. Each of these variables can affect plant growth, and finding the right combination can be complex.

Because there are so many possible combinations of conditions, identifying the optimal growing environment can be challenging. Automating and intelligently controlling an aeroponic farm can therefore help maintain ideal conditions and improve plant growth and efficiency.

|                                 Farm Overview                                  |                                                                         Plants                                                                         |
| :----------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="../assets/farm_overview.jpg" title="" alt="Description" width="400"> | <img src="../assets/roots.jpg" title="" alt="Description" width="264"> <img src="../assets/holder + roots.jpg" title="" alt="Description" width="148"> |

## bro who cares?

I care 😝. Food is what holds the world together, so if we can optimize its growth with minimal resources, we can have more food :)... And of course... lots of money hehe.

|              Easy to segment               |             Hard to segment              |
| :----------------------------------------: | :--------------------------------------: |
| ![Description](../assets/plants_small.jpg) | ![Description](../assets/plants_big.jpg) |

## Who is our advisor?

Our supervisor is Dr. Christian Muise. He is a Computing professor that has built a Aeroponic farm and has let us work on a small research project. This project is a building block for other projects to come. Dr. Muise will attend some of our meetings to guide us in our research.

Here's the link to his lab: [mulab.ai](https://mulab.ai/)

Email: christian.muise@queensu.ca

## What's the final result?

In second semester, after CUCAI we will have achieved:

- A paper 5-6 pages in length
- Presented our project in at least 2 occasions to different audiences[^1]
- A pipeline to automate this process and deploy it to mulab's farm

Depending on what part of the project you take, how much time dedicate, and how curious you are you will learn:

- How to use HuggingFace
- How to use GitHub
- How to load models and use them for inference[^2]
- How to work with Google Colab for training, inference, and workflows
- How to use python to make scripts and workflows
- How to make a website/interface with python and HTML/CSS/JS
- How to use agentic coding tools to help us move this project forward.

## How are we going to do this?

Stage 1: Dataset Generation & Model Training

- **Seed dataset**: Collect a few hundred images from the target indoor environment.
- **Auto-mask generation (optional)**: If hand-labeled data is not available, run images through a very large plant segmentation model to auto-generate masks.
- **Data augmentation**: Apply common image pre-processing and augmentation techniques (rotation, cutting out parts, scaling) to grow the dataset and cover more edge cases.
- **Model fine-tuning**: Use the resulting image-mask pairs to fine-tune a model to achieve a higher score on the validation set from the unique indoor environment.

### Stage 2: Tracking

- **Leaf tracking**: Use **LeafTrackNet** or similar embedding-based approaches to find similar leaves within a plant and track their growth over time using discontinuous pictures.
- **Database & biomass estimation**: Use the tracking data to build a database of plants and their individual leaves, and estimate biomass.

## Related Works (Previous Research)

It is important to research other papers before getting started on this project. Please take a look at [related_works.md](./related_works.md) for a better context on what has been done before.

## okay, how do i navigate the github?

Take a look at [repo.md](./repo.md) 😄

## Footnote

[^1]: [CUCAI](https://cucai.ca) and internal conferences, as well as some industry people.

[^2]: Inference is when you run an AI model through your input and get some output, so essentially "running" the model
