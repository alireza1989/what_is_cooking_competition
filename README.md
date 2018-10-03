# what_is_cooking_competition
Kaggle Competition: [What's cooking?!](https://www.kaggle.com/c/whats-cooking-kernels-only)  

## Problem:

**The competitions** asks to predict the category of a dish's cuisine given a list of its ingredients.

In the dataset, we include the **recipe id**, **the type of cuisine**, and **the list of ingredients of each recipe** (of variable length). The data is stored in JSON format. 

#### An example of a recipe node in train.json:

```json
 {
 "id": 24717,
 "cuisine": "indian",
 "ingredients": [
     "tumeric",
     "vegetable stock",
     "tomatoes",
     "garam masala",
     "naan",
     "red lentils",
     "red chili peppers",
     "onions",
     "spinach",
     "sweet potatoes"
 ]
 },
 ```
 
In the test file **test.json**, the format of a recipe is the same as **train.json**, only *the cuisine type* is removed, <font color=red>as it is the target variable you are going to predict.</font>

#### File descriptions:

**train.json -** the training set containing recipes id, type of cuisine, and list of ingredients

**test.json -** the test set containing recipes id, and list of ingredients

**sample_submission.csv -** a sample submission file in the correct format
In the dataset, we include the recipe id, the type of cuisine, and the list of ingredients of each recipe (of variable length). The data is stored in JSON format.


----

## Environment Setup: 

### Use my basic DeepLearning machine automated setup here to setup your environment on public cloud providers:

[Basic_Deeplearning_Machine](https://github.com/alireza1989/basic_deeplearning_machine)

* Clone the project on your vm instance (compute engine for Google Cloud Platform or EC2 for AWS).
* Use the instruction the ReadMe file and run this bash script "cuda_with_compiled_tensorflow.sh".
* Now you should have a working deeplearning instance.
* clone "What's cooking project" in your remote instance and should be able to run the Jupyter Notebook in this project. 

---

## I am still working on the project to traing a model that predicts with the highest accuracy.  The highest accuracy on Kaggle is 82.X % 

---
