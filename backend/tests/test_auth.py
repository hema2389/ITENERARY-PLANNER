import pytest
from app import app
import json
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('blueprints.auth.auth.verify_id_token')
@patch('blueprints.auth.get_document')
@patch('blueprints.auth.add_document')
@patch('blueprints.auth.update_document')
def test_verify_token_new_user(mock_update, mock_add, mock_get, mock_verify, client):
    """Test token verification for a new user."""
    mock_verify.return_value = {'uid': 'test_uid', 'email': 'test@example.com'}
    mock_get.return_value = None

    response = client.post('/api/auth/verify', json={'token': 'test_token'})

    assert response.status_code == 200
    mock_add.assert_called_once()
    mock_update.assert_not_called()

@patch('blueprints.auth.auth.verify_id_token')
@patch('blueprints.auth.get_document')
@patch('blueprints.auth.add_document')
@patch('blueprints.auth.update_document')
def test_verify_token_existing_user(mock_update, mock_add, mock_get, mock_verify, client):
    """Test token verification for an existing user."""
    mock_verify.return_value = {'uid': 'test_uid', 'email': 'test@example.com'}
    mock_get.return_value = {'uid': 'test_uid', 'email': 'test@example.com'}

    response = client.post('/api/auth/verify', json={'token': 'test_token'})

    assert response.status_code == 200
    mock_add.assert_not_called()
    mock_update.assert_called_once()

@patch('middleware.auth.auth.verify_id_token')
@patch('blueprints.auth.get_document')
def test_get_user(mock_get, mock_verify, client):
    """Test the GET /api/auth/user endpoint."""
    mock_verify.return_value = {'uid': 'test_uid'}
    mock_get.return_value = {'uid': 'test_uid', 'email': 'test@example.com'}

    response = client.get('/api/auth/user', headers={'Authorization': 'Bearer test_token'})

    assert response.status_code == 200
    assert response.json['email'] == 'test@example.com'

@patch('middleware.auth.auth.verify_id_token')
@patch('blueprints.auth.get_document')
@patch('blueprints.auth.update_document')
def test_update_user(mock_update, mock_get, mock_verify, client):
    """Test the PUT /api/auth/user endpoint."""
    mock_verify.return_value = {'uid': 'test_uid'}
    mock_get.return_value = {'uid': 'test_uid', 'email': 'test@example.com'}

    response = client.put('/api/auth/user', json={'budget': 1000}, headers={'Authorization': 'Bearer test_token'})

    assert response.status_code == 200
    mock_update.assert_called_once()
