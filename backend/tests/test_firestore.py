import pytest
from unittest.mock import patch, MagicMock
from utils import firestore

@pytest.fixture(autouse=True)
def mock_firestore():
    """Mock the Firestore client."""
    with patch('utils.firestore.db', new_callable=MagicMock) as mock_db:
        yield mock_db

def test_add_document(mock_firestore):
    """Test the add_document function."""
    mock_doc_ref = MagicMock()
    mock_doc_ref.id = 'test_id'
    mock_firestore.collection.return_value.document.return_value = mock_doc_ref

    doc_id = firestore.add_document('test_collection', {'key': 'value'})

    mock_firestore.collection.assert_called_with('test_collection')
    mock_firestore.collection.return_value.document.assert_called_once()
    mock_doc_ref.set.assert_called_with({'key': 'value'})
    assert doc_id == 'test_id'

def test_get_document(mock_firestore):
    """Test the get_document function."""
    mock_doc = MagicMock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {'key': 'value'}
    mock_firestore.collection.return_value.document.return_value.get.return_value = mock_doc

    doc = firestore.get_document('test_collection', 'test_id')

    mock_firestore.collection.assert_called_with('test_collection')
    mock_firestore.collection.return_value.document.assert_called_with('test_id')
    assert doc == {'key': 'value'}

def test_update_document(mock_firestore):
    """Test the update_document function."""
    firestore.update_document('test_collection', 'test_id', {'key': 'new_value'})

    mock_firestore.collection.assert_called_with('test_collection')
    mock_firestore.collection.return_value.document.assert_called_with('test_id')
    mock_firestore.collection.return_value.document.return_value.update.assert_called_with({'key': 'new_value'})

def test_delete_document(mock_firestore):
    """Test the delete_document function."""
    firestore.delete_document('test_collection', 'test_id')

    mock_firestore.collection.assert_called_with('test_collection')
    mock_firestore.collection.return_value.document.assert_called_with('test_id')
    mock_firestore.collection.return_value.document.return_value.delete.assert_called_once()
