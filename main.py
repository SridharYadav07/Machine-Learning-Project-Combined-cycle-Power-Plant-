import fastapi
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np

app = FastAPI()
model = pickle.load(open('rfr_model.pkl','rb'))

class UserInput(BaseModel):
    temperature: float
    exhaust_vacuum: float
    amb_pressure: float
    r_humidity: float


@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.post('/predict')
async def predict(UserInput: UserInput):
    prediction = model.predict(np.array([UserInput.temperature,
                                         UserInput.exhaust_vacuum,
                                         UserInput.amb_pressure,
                                         UserInput.r_humidity]).reshape(1, -1))
    return{'prediction': prediction.tolist()}
