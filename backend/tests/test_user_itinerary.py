import pytest
from app import app
import json
from unittest.mock import patch, MagicMock
import warnings
from pydantic import PydanticDeprecatedSince20

warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('middleware.auth.auth.verify_id_token')
@patch('blueprints.user_itinerary.add_document')
def test_save_itinerary(mock_add, mock_verify, client):
    """Test the /api/itinerary/user/save endpoint."""
    mock_verify.return_value = {'uid': 'test_uid'}

    response = client.post('/api/itinerary/user/save', json={'destination': 'Paris', 'days': []}, headers={'Authorization': 'Bearer test_token'})

    assert response.status_code == 200
    mock_add.assert_called_once()

@patch('middleware.auth.auth.verify_id_token')
def test_get_saved_itineraries(mock_verify, client):
    """Test the /api/itinerary/user/saved endpoint."""
    mock_verify.return_value = {'uid': 'test_uid'}

    response = client.get('/api/itinerary/user/saved', headers={'Authorization': 'Bearer test_token'})

    assert response.status_code == 200
    assert response.json == []

@patch('middleware.auth.auth.verify_id_token')
@patch('blueprints.user_itinerary.add_document')
def test_submit_feedback(mock_add, mock_verify, client):
    """Test the /api/itinerary/user/feedback endpoint."""
    mock_verify.return_value = {'uid': 'test_uid'}
    response = client.post('/api/itinerary/user/feedback', json={'itinerary_id': '123', 'crowd_averse_satisfaction': 5, 'experience_quality': 5, 'comments': 'Great!'}, headers={'Authorization': 'Bearer test_token'})

    assert response.status_code == 200
    mock_add.assert_called_once()
