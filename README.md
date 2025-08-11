# Data pipelines

How are data pipelines created ? What happens in each of the steps ? What needs to happen for them to run reliably for production purposes ? 

Allow me to demonstrate with an example. Let's use [data from an Iron Ore flotation plant](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process/) 

## Plan

To do this I'm going to create an **Extract, Transform, Load (ETL)** data pipeline on my local machine. Once the data set is loaded into the data platform we can perform addition transformations on the data store itself.

Once done I'll productionise the pipeline by porting it to a CI/CD system and creating Infrastructure as Code (IaC) to be able to stand up the infrastructure from scratch in a reliable and repeatable way.

### Steps
#### Create the pipeline locally using Python

Pipeline script is [here](https://github.com/nhollingsworth/iron-ore-data-pipeline/blob/main/data-pipeline.py).

|<!-- -->|<!-- -->|
|:-|:-:|
| ~**Extract**~ | ~[this dataset](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process/) from Kaggle using Kaggle API~ |
| ~**Transform**~ |  ~using Python Pandas (set data types, removed duplicates)~|
| **Load** | it into Snowflake|

#### Perform additional transformations on the data set

|<!-- -->|<!-- -->|
|:-|:-:|
| **Transform** | further using SQL run by a Snowflake task |
  
#### Productionise
* Port the Python script + keys to GitHub actions (CI/CD)
* Write a Terraform configuration to automate creation of infrastructure
* Import existing infrastructure into Terraform and/or recreate from scratch using the Terraform configuration
* Lock down the code repository to reduce the chances of accidental pipeline damage
