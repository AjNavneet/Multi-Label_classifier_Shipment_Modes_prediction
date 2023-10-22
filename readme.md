# Multi-Label Classification for Predicting Shipment Modes

## Project Overview
The transportation industry plays a vital role in the global economy, ensuring the efficient movement of goods. However, choosing the right mode of transport for each shipment can be a complex task, with various factors to consider. Accurate predictions of the appropriate mode of transport can significantly impact delivery time, costs, and safety. This project aims to develop a machine learning model to predict the suitable transport mode for each shipment using different multilabel classification approaches.

---

## Aim
The project's objective is to explore and compare four different multilabel classification approaches, including Naive Independent Models, Classifier Chains, Natively Multilabel Models, and Multilabel to Multiclass Approach. By developing and evaluating these approaches, we aim to improve the decision-making process for selecting transportation modes for shipments.

---

## Data Description
The transport dataset contains 2000 unique products with various features, including product weight, size, value, storage conditions, packaging cost, and more. The dataset also includes binary labels indicating the appropriate transport modes for each product, such as Air, Road, Rail, and Sea.

---

## Tech Stack
- Language: `Python`
- Libraries: `Pandas`, `NumPy`, `Matplotlib`, `Scikit-learn`, `TensorFlow`, `Google BigQuery`

---

## Approach
1. **Exploratory Data Analysis (EDA):**
   - Understand the features.
   - Check data summary.
   - Identify missing or invalid values.
2. **Preprocessing:**
   - Encode categorical features.
   - Split the dataset into training and testing sets.
   - Create cross-validation sets.
3. **Multilabel Classification:**
   - **Approach 0 - Naive Independent Models:**
     - Train separate binary classifiers for each target label (e.g., LightGBM).
     - Predict the labels.
     - Evaluate model performance using the F1 score.
   - **Approach 1 - Classifier Chains:**
     - Train a binary classifier for each target label.
     - Chain the classifiers to consider label dependencies.
     - Predict the labels.
     - Evaluate model performance using the F1 score.
   - **Approach 2 - Natively Multilabel Models:**
     - Train models designed for multilabel classification (e.g., Extra Trees, Neural Networks).
     - Evaluate model performance using the F1 score.
   - **Approach 3 - Multilabel to Multiclass Approach:**
     - Combine different label combinations into a single target label.
     - Train a LightGBM classifier on the combined labels.
     - Evaluate model performance using F1 score, precision, and recall.

---

## Project Structure
- `data`: Contains the dataset used for analysis.
- `lib`: Reference folder with the original Jupyter notebook.
- `ml_pipeline`: Python files with modular functions for data processing.
- `engine.py`: The main execution script.
- `requirements.txt`: List of required libraries and versions.
- `readme.md`: Instructions for running the code.

---

## Concepts Explored
1. Understanding the significance of predicting the appropriate mode of transport in the transportation industry.
2. Exploring multilabel classification and its applications.
3. Utilizing Google BigQuery for dataset exploration and preprocessing.
4. Implementing various multilabel classification approaches and evaluating their performance.
5. Comparing and contrasting the results of different approaches.
6. Understanding the trade-offs and limitations of each approach.

---

## Data Reading with Google Cloud BigQuery

Cloud computing has revolutionized the way we handle and analyze large datasets. Google Cloud Platform (GCP) offers a suite of tools, and one of the most powerful is Google BigQuery. BigQuery is a serverless, highly-scalable, and cost-effective data warehouse designed to process and analyze massive datasets in real-time. This project focuses on leveraging BigQuery to read, preprocess, and prepare data for machine learning.

## Prerequisites

Before running this project, you'll need to create a BigQuery table from a CSV file and authenticate using a Google Cloud Service Account. Here are the necessary steps:

### 1. Creating a Bucket in Google Cloud Storage

- Open the Google Cloud Console and select your project.
- Navigate to "Storage" > "Storage Browser."
- Click "Create Bucket" and specify the name, location, and storage class.
- Once created, select the bucket and click "Upload Files" to upload your CSV file.

### 2. Creating a Dataset in BigQuery with CSV Stored in Cloud Storage

- Open the BigQuery web console in the Google Cloud Console.
- Choose your project and dataset.
- Click "Create Table" and select "Google Cloud Storage" as the source.
- Specify the location of your CSV file and define the table schema.
- Click "Create Table" to load the data from the CSV file.

### 3. Authentication Using a Local System

- Download the `GOOGLE_APPLICATION_CREDENTIALS` JSON file from the Google Cloud Console to authenticate.

## Running the Project

To run the project, follow these steps:

1. Create a BigQuery table from the uploaded CSV file.
2. Download the JSON key for authentication from the Google Cloud Console.
3. Change the project ID in the `read_gbq` function in the code to match your project's name.

---
