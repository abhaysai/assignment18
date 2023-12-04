import json
import pytest
from app import app, data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_tweet_success(client):
    tweet_data = {
        'username': 'test_user',
        'content': 'This is a test tweet.'
    }
    response = client.post('/tweets', json=tweet_data)
    assert response.status_code == 201
    assert 'message' in response.json
    assert 'tweet' in response.json

def test_create_tweet_failure_incomplete_request(client):
    incomplete_tweet_data = {
        'username': 'test_user'
    }
    response = client.post('/tweets', json=incomplete_tweet_data)
    assert response.status_code == 400
    assert 'error' in response.json
