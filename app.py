
import json
with open('100tweets.json', 'r', encoding='utf-8', errors='replace') as f:
    data = json.load(f)
    

import json
with open('100tweets.json', encoding='latin-1') as f:
    data = json.load(f)


from flask import Flask
app = Flask(__name__)

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


@app.errorhandler(404)
def not_found(e):
    return '', 404

# Test endpoints
#curl http://localhost:5000/
#curl http://localhost:5000/tweets 
#curl http://localhost:5000/tweets/100

# Invalid cases 
#curl http://localhost:5000/missing
#curl http://localhost:5000/tweets/99999

if __name__ == '__main__':
   app.run()