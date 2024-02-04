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


def get_model():
    model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model = hub.load(model_url)
    print("module %s loaded" % model_url)
    return model


def embed(texts, model):
    return model(texts)

def get_recommendations(text, model, no_of_recommendations=10):
    df = pd.read_csv("Top_10000_Movies.csv", engine="python")
    df = df[["original_title", "overview"]]
    df = df.dropna()
    df = df.reset_index()
    df = df[:5500]

    titles = list(df["overview"])
    embeddings = embed(titles, model)
    nn = NearestNeighbors(n_neighbors=no_of_recommendations)
    nn.fit(embeddings)
    emb = embed([text], model)
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    return df["original_title"].iloc[neighbors].tolist()


# model(["This movie was great!"])


# df = pd.read_csv("Top_10000_Movies.csv", engine="python")
# df.head()


# df = df[["original_title", "overview"]]
# df.head()


# df = df.dropna()
# df = df.reset_index()
# df = df[:5500]


# titles = list(df["overview"])


# titles[:10]


# embeddings = embed(titles)
# print("The embedding shape is: ", embeddings.shape)




# pca = PCA(n_components=2)
# emb_2d = pca.fit_transform(embeddings)



# plt.figure(figsize=(11, 6))
# plt.title("Embedding Space")
# plt.scatter(emb_2d[:, 0], emb_2d[:, 1])
# plt.show()



# nn = NearestNeighbors(n_neighbors=15)
# nn.fit(embeddings)


# def recommend(text):
#     emb = embed([text])
#     neighbors = nn.kneighbors(emb, return_distance=False)[0]
#     return df["original_title"].iloc[neighbors].tolist()



# print("Recommend Movies: ")
# recommend("Baseball")