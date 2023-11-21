from flask import Flask, jsonify
import pandas as pd
import redis
import os
app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
data_path = os.path.join(os.getcwd(), 'MovieLens-100K_Recommender-System/data')
movies_df = pd.read_csv(os.path.join(data_path, 'movies.csv'))
ratings_df = pd.read_csv(os.path.join(data_path, 'ratings.csv'))
tags_df = pd.read_csv(os.path.join(data_path, 'tags.csv'))
movies_dict = movies_df.to_dict()
ratings_dict = ratings_df.to_dict()
tags_dict = tags_df.to_dict()
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/api/movies')
def get_movies():
    return jsonify(movies_dict)
@app.route('/api/ratings')
def get_ratings():
    return jsonify(ratings_dict)
@app.route('/api/tags')
def get_tags():
    return jsonify(tags_dict)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
