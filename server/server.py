from flask import Flask, request
from flask_cors import CORS
from movie import get_model, get_recommendations

import tensorflow as tf
import tensorflow_hub as hub

import matplotlib.pyplot as plt

import os
import re
import numpy as np
import pandas as pd

# sci-kit
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

app = Flask(__name__)
model = get_model()

# Members API route
CORS(app, origins=["http://localhost:5173"], methods=["GET", "POST"], allow_headers=["Content-Type"])

@app.route('/members')
def members():  
  return {
    "members": [
      "Member 1",
      "Member 2",
      "Member 3",
    ]
  }

@app.route('/recommend', methods=["POST"])
def recommend():
  data = request.get_json()
  text = data["text"]
  recommendations = get_recommendations(text, model)
  return recommendations
  

if __name__ == "__main__":
  app.run(debug=True)