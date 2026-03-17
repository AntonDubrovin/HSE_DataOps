from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
    result = data.age * 2.5 + data.bmi * 3.2
    return {"predict": result}
