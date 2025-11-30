import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_export_pdf(client):
    """Test the /api/export/pdf endpoint."""
    itinerary_data = {
        'destination': 'Paris',
        'days': [{'day_number': 1, 'activities': [{'name': 'Eiffel Tower'}]}]
    }

    response = client.post('/api/export/pdf', json=itinerary_data)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'
    assert response.headers['Content-Disposition'] == 'attachment; filename=itinerary.pdf'
