import pytest
from app import app
import json
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('blueprints.chat.get_conversational_agent')
@patch('blueprints.chat.get_session')
def test_post_message(mock_get_session, mock_get_agent, client):
    """Test the /api/chat/message endpoint."""
    mock_get_session.return_value = {'session_id': 'test_session'}

    mock_agent = MagicMock()
    mock_agent.predict.return_value = "Hello!"

    mock_get_agent.return_value = mock_agent

    response = client.post('/api/chat/message', json={'message': 'Hi', 'session_id': 'test_session'})

    assert response.status_code == 200
    assert response.json['response'] == 'Hello!'
