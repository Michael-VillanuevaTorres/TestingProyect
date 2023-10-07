
from website import create_app
import json

# Fixtures for common configuration
@pytest.fixture
def app_client():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        app.test_client().get('/generate_fake_data')
    client = app.test_client()
    yield client


def test_add_valid_reasignation_petition(client):
    """
    Given: The request with valid data.
    When: The request is sent to add a reassignment request.
    Then: The response is verified to have a 201 status code.
    """
    response = app_client.post('/reasignacion/add/?id_report=1&id_developer=2', json={'motivo': 'Prueba'})
    assert response.status_code == 201

def test_add_invalid_reasignation_petition():
    """
    Given: The request with invalid data.
    When: The request is sent to add a reassignment request.
    Then: The response is verified to have status code 400.
    """
    response = app_client.post('/reasignacion/add/?id_report=1&id_developer=2', json={})
    assert response.status_code == 400

def test_delete_valid_solicitud_reasignacion(app_client):
    """
    Given: A valid reassignment request in the database.
    When: A request for deletion is sent.
    Then: The response is checked for a 201 status code.
    """
    
    response = app_client.delete('/reasignacion/delete/?id_report=1&id_dev=1')
    assert response.status_code == 201

def test_delete_non_existing_solicitud_reasignacion(app_client):
    """
    Given: A request to delete a reassignment request that does not exist.
    When: The request is sent.
    Then: The response is checked for a 404 status code.
    """
    response = app_client.delete('/reasignacion/delete/?id_report=1&id_dev=1')
    assert response.status_code == 404

def test_delete_solicitud_reasignacion_missing_parameters( app_client):
    """
    Given: a request to delete a reasignation petition without all required parameters
    When: the request is sent
    Then: check it returns a 400 status code
    """
    response = app_client.delete('/reasignacion/delete/?id_report=1')
    assert response.status_code == 400

def test_delete_solicitud_reasignacion_db_error( app_client):
    """
    Given: An environment where a delete error occurs.
    When: A request to delete a valid request is sent.
    Then: The response is checked for a status code 500 or an appropriate error code.
    """

    response = app_client.delete('/reasignacion/delete/?id_report=1&id_dev=100')
    assert response.status_code == 500

def test_get_all_reasignation_petitions_from_a_specific_product(app_client):
    """
    Given: A request with a valid 'id_product' parameter.
    When: The function get_all_reasignation_requests_from_a_specific_product is called.
    Then: The response is checked for a status code 200 and an expected format.
    """
    response = app_client.get('/reasignacion/get/all/product/?id_product=1')
    assert response.status_code == 200
    assert 'id_report' in response.json[0]
    assert 'id_developer' in response.json[0]

def test_get_motivo_reasignation_petition_from_a_specific_report( app_client):
    """
    Given: A request with a valid 'id_report' parameter.
    When: The get_get_motivo_reasignation_petition_request_from_a_specific_report function is called.
    Then: The response is verified to have a status code 200 and an expected format.
    """
    response = app_client.get('/reasignacion/get/motivo/report/?id_report=1')
    assert response.status_code == 200
    assert 'motivo' in response.json

def test_get_motivo_reasignation_petition_report_not_found(app_client):
    """
    Given: A request with an 'id_report' that does not exist.
    When: The function get_motif_reasignation_request_request_from_a_specific_report is called.
    Then: The response is checked for a status code 400.
    """
    response = app_client.get('/reasignacion/get/motivo/report/?id_report=999')
    assert response.status_code == 400

def test_get_motivo_reasignation_petition_report_not_in_solicitud_reasignacion( app_client):
    """
    Given: A request with an 'id_report' that is not found in the request_reassignment_request table.
    When: The get_reason_reasignation_request_request_from_a_specific_report function is called.
    Then: Check that the response has status code 400.
    """
    response = app_client.get('/reasignacion/get/motivo/report/?id_report=2')
    assert response.status_code == 400




