
# FastAPI Model Training and Prediction API

This project provides a RESTful API built with FastAPI for uploading a dataset, training a decision tree model, and making predictions. The model predicts whether a downtime event will occur based on certain input features.

## Endpoints

### 1. `/upload` (POST)

This endpoint allows you to upload a CSV file containing the dataset. The dataset should include a column named `DownTime_Flag`, which is used as the target variable for model training.

#### Request:
- **File**: A CSV file containing the dataset. The file must have a `DownTime_Flag` column.

#### Response:
- **message**: A success message indicating the file has been uploaded.
- **columns**: A list of column names in the uploaded CSV file.

#### Example in Postman:
1. Select **POST** method.
2. Set the URL to `http://127.0.0.1:8000/upload`.
3. Under the **Body** tab, select **form-data**.
4. Add a field with key `file`, and upload the CSV file.
5. Hit **Send**.

### 2. `/train` (POST)

This endpoint trains a decision tree model using the uploaded dataset. The model is trained to predict the `DownTime_Flag` based on the features in the dataset.

#### Request:
- **None** (uses the uploaded CSV for training).

#### Response:
- **message**: A success message indicating the model has been trained.
- **accuracy**: The accuracy of the model on the test set.
- **f1_score**: The F1 score (weighted) of the model.

#### Example in Postman:
1. Select **POST** method.
2. Set the URL to `http://127.0.0.1:8000/train`.
3. Hit **Send**.

### 3. `/predict` (POST)

This endpoint allows you to make predictions using the trained model. You need to provide the input features (e.g., `Temperature`, `Run_Time`) in the request body.

#### Request:
- **Temperature**: A float representing the temperature.
- **Run_Time**: A float representing the run time.

#### Response:
- **Downtime**: A prediction of whether downtime will occur ("Yes" or "No").
- **Confidence**: The confidence score of the prediction.

#### Example in Postman:
1. Select **POST** method.
2. Set the URL to `http://127.0.0.1:8000/predict`.
3. Under the **Body** tab, select **raw** and set the type to **JSON**.
4. Add the following JSON body:
    ```json
    {
      "Temperature": 75.5,
      "Run_Time": 120.0
    }
    ```
5. Hit **Send**.

## Project Setup

### 1. Clone the repository:
```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 2. Install dependencies:
Make sure you have Python 3.7+ installed. Install the required libraries by running:
```bash
pip install -r requirements.txt
```

### 3. Run the application:
To start the FastAPI application, run:
```bash
uvicorn main:app --reload
```
This will start the server locally at `http://127.0.0.1:8000`.

### 4. Interact with the API:
- Use Postman or any other API client to interact with the API.
- Access the automatic API documentation at `http://127.0.0.1:8000/docs`.

## Model Details

- **Model Type**: Decision Tree Classifier
- **Training Method**: A decision tree is trained on the uploaded dataset. It uses the `DownTime_Flag` as the target variable.
- **Evaluation Metrics**: The model is evaluated based on accuracy and F1 score.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- scikit-learn
- pandas
