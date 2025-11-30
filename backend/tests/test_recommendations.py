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

@patch('blueprints.recommendations.get_recommendation_agent')
def test_get_alternatives(mock_get_agent, client):
    """Test the /api/recommendations/alternatives endpoint."""
    mock_agent = MagicMock()
    mock_agent.stream.return_value = [
        {'messages': [AIMessage(content='{"name": "Colmar, France"}')]}
    ]
    mock_get_agent.return_value = mock_agent

    response = client.post('/api/recommendations/alternatives', json={'original_poi': {'name': 'Eiffel Tower'}})

    assert response.status_code == 200
    assert response.json['name'] == 'Colmar, France'
