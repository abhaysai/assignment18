import json
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('100tweets.json', encoding='latin-1') as f:
    data = json.load(f)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/tweets')
def get_tweets():
    return json.dumps(data)

@app.route('/100tweets/<keyword>')
def get_filtered_tweets(keyword):
    filtered = [t for t in data if keyword in t['text']]
    return json.dumps(filtered)

@app.route('/tweets/<int:id>')
def get_tweet(id):
    try:
        tweet = next(t for t in data if t['id'] == id)
        return json.dumps(tweet)
    except:
        return 'Tweet not found', 404

# New POST endpoint for creating a new tweet
@app.route('/tweets', methods=['POST'])
def create_tweet():
    try:
        tweet_data = request.get_json()

        if 'username' not in tweet_data or 'content' not in tweet_data:
            return jsonify({"error": "Incomplete request. Please provide username and content"}), 400

        new_tweet = {
            'id': len(data) + 1,
            'username': tweet_data['username'],
            'content': tweet_data['content']
        }
        data.append(new_tweet)

        return jsonify({"message": "Tweet created successfully", "tweet": new_tweet}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
