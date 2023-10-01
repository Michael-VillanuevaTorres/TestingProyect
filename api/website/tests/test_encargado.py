import pytest
from controllers.refactor_encargado_controller import *
from app import app as flask_app
from unittest.mock import MagicMock

# Fixtures para configuración común
@pytest.fixture
def app_client():
    return flask_app.test_client()

@pytest.fixture
def mock_database():
    return MagicMock()


def test_add_valid_reasignation_petition(self, app_client):
    """
    GIVEN a request with valid data
    WHEN the request is sent to add a reasignation petition
    THEN check it returns a 201 status code
    """
    response = app_client.post('/reasignacion/add/?id_report=1&id_developer=2', json={'motivo': 'Prueba'})
    assert response.status_code == 201

def test_add_invalid_reasignation_petition(self, app_client):
    """
    GIVEN a request with invalid data
    WHEN the request is sent to add a reasignation petition
    THEN check it returns a 400 status code
    """
    response = app_client.post('/reasignacion/add/?id_report=1&id_developer=2', json={})
    assert response.status_code == 400

def test_add_valid_solicitud_reasignacion(self):
    """
    GIVEN valid data
    WHEN add_solicitud_reasignacion is called
    THEN check it returns a successful response
    """
    result = add_solicitud_reasignacion(1, 2, 'Prueba')
    assert result['success'] is True

def test_add_invalid_solicitud_reasignacion(self):
    """
    GIVEN invalid data
    WHEN add_solicitud_reasignacion is called
    THEN check it returns a failed response
    """
    result = add_solicitud_reasignacion(1, 2, '')
    assert result['success'] is False

def test_delete_valid_solicitud_reasignacion(self, app_client):
    """
    GIVEN a valid reasignation petition in the database
    WHEN a request is sent to delete it
    THEN check it returns a 201 status code
    """
    add_test_solicitud_reasignacion()
    response = app_client.delete('/reasignacion/delete/?id_report=1&id_dev=1')
    assert response.status_code == 201

def test_delete_non_existing_solicitud_reasignacion(self, app_client):
    """
    GIVEN a request to delete a non-existing reasignation petition
    WHEN the request is sent
    THEN check it returns a 404 status code
    """
    response = app_client.delete('/reasignacion/delete/?id_report=1&id_dev=1')
    assert response.status_code == 404

def test_delete_solicitud_reasignacion_missing_parameters(self, app_client):
    """
    GIVEN a request to delete a reasignation petition without all required parameters
    WHEN the request is sent
    THEN check it returns a 400 status code
    """
    response = app_client.delete('/reasignacion/delete/?id_report=1')
    assert response.status_code == 400

def test_delete_solicitud_reasignacion_db_error(self, app_client):
    """
    GIVEN an environment where a deletion error occurs
    WHEN a request to delete a valid petition is sent
    THEN check it returns a 500 status code or an appropriate error code
    """
    mock_delete_solicitud_error()
    response = app_client.delete('/reasignacion/delete/?id_report=1&id_dev=1')
    assert response.status_code == 500

def test_get_all_reasignation_petitions_from_a_specific_product(self, app_client):
    """
    GIVEN a request with a valid 'id_product' parameter
    WHEN get_all_reasignation_petitions_from_a_specific_product is called
    THEN check it returns a 200 status code and the expected format
    """
    response = app_client.get('/reasignacion/get/all/product/?id_product=1')
    assert response.status_code == 200
    assert 'id_report' in response.json[0]
    assert 'id_developer' in response.json[0]

def test_get_motivo_reasignation_petition_from_a_specific_report(self, app_client):
    """
    GIVEN a request with a valid 'id_report' parameter
    WHEN get_motivo_reasignation_petition_from_a_specific_report is called
    THEN check it returns a 200 status code and the expected format
    """
    response = app_client.get('/reasignacion/get/motivo/report/?id_report=1')
    assert response.status_code == 200
    assert 'motivo' in response.json

def test_get_motivo_reasignation_petition_report_not_found(self, app_client):
    """
    GIVEN a request with a non-existing 'id_report' parameter
    WHEN get_motivo_reasignation_petition_from_a_specific_report is called
    THEN check it returns a 400 status code
    """
    response = app_client.get('/reasignacion/get/motivo/report/?id_report=999')
    assert response.status_code == 400

def test_get_motivo_reasignation_petition_report_not_in_solicitud_reasignacion(self, app_client):
    """
    GIVEN a request with an 'id_report' not found in the solicitud_reasignacion table
    WHEN get_motivo_reasignation_petition_from_a_specific_report is called
    THEN check it returns a 400 status code
    """
    response = app_client.get('/reasignacion/get/motivo/report/?id_report=2')
    assert response.status_code == 400