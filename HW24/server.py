from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn

app = FastAPI()

model = mlflow.sklearn.load_model("models:/diabets/1")

class PatientData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

@app.post("/api/v1/predict")
def predict(data: PatientData):
    features = [[data.age, data.sex, data.bmi, data.bp, 
                 data.s1, data.s2, data.s3, data.s4, data.s5, data.s6]]
    result = model.predict(features)[0]
    return {"predict": float(result)}
