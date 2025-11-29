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

@patch('blueprints.crowd.get_crowd_density_agent')
def test_get_crowd_score(mock_get_agent, client):
    """Test the /api/crowd/score endpoint."""
    # Create a mock agent executor
    mock_agent_executor = MagicMock()
    mock_agent_executor.stream.return_value = [
        {'messages': [AIMessage(content='Thinking...')]},
        {'messages': [AIMessage(content='75')]}
    ]
    mock_get_agent.return_value = mock_agent_executor

    # Make the request
    response = client.post('/api/crowd/score', data=json.dumps({'location': 'test_location'}), content_type='application/json')

    # Assertions
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['location'] == 'test_location'
    assert data['score'] == 75

    # Verify that the agent was created and called correctly
    mock_get_agent.assert_called_once()
    mock_agent_executor.stream.assert_called_once()
    call_args, call_kwargs = mock_agent_executor.stream.call_args
    assert call_args[0] == {"messages": [{"role": "user", "content": "what is the crowd score for test_location"}]}
    assert call_kwargs['stream_mode'] == "values"

def test_get_crowd_forecast(client):
    """Test the /api/crowd/forecast endpoint."""
    response = client.get('/api/crowd/forecast?location=test_location')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['location'] == 'test_location'
    assert 'forecast' in data
    assert len(data['forecast']) == 7
