from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    tweets = data.get('tweets')
    if not tweets or not isinstance(tweets, list):
        return jsonify({"error": "Entrée invalide, une liste de tweets est attendue."}), 400

    results = {}
    for tweet in tweets:
        score = predict_sentiment(tweet)
        results[tweet] = score
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
