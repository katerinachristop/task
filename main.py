from fastapi import FastAPI
import h5py
from pydantic import BaseModel
import json

import mxnet as mx
from mxnet.gluon.model_zoo import vision
import numpy as np

"""
Create the class for loading the pre-trained model
"""

class Image(BaseModel):
    image_str: str


class ModelPrediction(BaseModel):
    ctx = mx.cpu()
    densenet121 = vision.densenet121(pretrained=True, ctx=ctx)

    # Loading the data
    filename = "densenet121_weights_tf_dim_ordering_tf_kernels.h5"

    with h5py.File(filename, "r") as f:
         data = list(f.keys())
         labels = np.array(data)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from root"}

@app.post("/predict")
async def predict(image_str, densenet121):
    filename = "densenet121_weights_tf_dim_ordering_tf_kernels.h5"

    with h5py.File(filename, "r") as f:
         data = list(f.keys())
    # Get a test image
    
    predictions = densenet121(image_str).softmax()
    # print(predictions.shape)
    
    return {"image": predictions}


