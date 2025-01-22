from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from pydantic import BaseModel
import io

app = FastAPI()

data=None
model=None

    # For Uploding


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global data
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")

    try:
        contents =await file.read()
        data = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        return{"message":"File Uploaded successfully,","columns":list(data.columns)}
    except Exception as e:
        raise HTTPException(status_code=500,detail= str(e))

    #  For Train

@app.post("/train")
async def train_model():
    global data , model
    if data is None:
        raise HTTPException(status_code=400, detail="No dataset Uploded,")

    try:
        if 'DownTime_Flag' not in data.columns:
            raise HTTPException(status_code=400,detail="Data must contain 'DownTime_Flag' column.")
        
        x = data.drop(columns=['DownTime_Flag','Machine_ID'])
        y = data['DownTime_Flag']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        model=DecisionTreeClassifier()
        model.fit(x_train, y_train)

        y_pred=model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')

        with open("model.pk1","wb")as f:
            pickle.dump(model,f)

            return{"message":"Model trained Successfully.", "accuracy":accuracy,"f1_score":f1}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # For Predict

class PredictRequest(BaseModel):
    Temperature: float
    Run_Time: float

@app.post("/predict")
async def predict(request: PredictRequest):
    global model
    if model is None:
        raise HTTPException(status_code=400, detail="Model Not Trained.")
    
    try:
        input_data = pd.DataFrame([request.dict()])
        prediction = model.predict(input_data)[0]
        confidence = max(model.predict_proba(input_data)[0])
        return{"DownTime":"Yes" if prediction else "No","Confidence": confidence}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))