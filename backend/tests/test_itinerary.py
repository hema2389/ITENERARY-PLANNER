import pytest
from app import app
import json
from unittest.mock import patch, MagicMock
from langchain_core.messages import AIMessage

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('blueprints.itinerary.get_itinerary_agent')
def test_generate_itinerary(mock_get_agent, client):
    """Test the /api/itinerary/generate endpoint."""
    mock_agent = MagicMock()
    mock_agent.stream.return_value = [
        {'messages': [AIMessage(content='{"days": [{"day_number": 1, "activities": []}]}')]}
    ]
    mock_get_agent.return_value = mock_agent

    response = client.post('/api/itinerary/generate', json={'destination': 'Paris'})

    assert response.status_code == 200
    assert response.json['days'][0]['day_number'] == 1
