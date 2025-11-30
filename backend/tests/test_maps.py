import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_geodata(client):
    """Test the /api/maps/geodata endpoint."""
    locations = ['Eiffel Tower', 'Louvre Museum']
    response = client.post('/api/maps/geodata', json={'locations': locations})

    assert response.status_code == 200
    assert 'coordinates' in response.json
    assert 'travel_times' in response.json
    assert response.json['coordinates']['Eiffel Tower'] == [48.8584, 2.2945]
