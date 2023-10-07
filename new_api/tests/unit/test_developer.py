
import json
from controllers.user_controller import *
from app import app as flask_app
from unittest.mock import MagicMock

# Fixtures para configuración común
@pytest.fixture
def app_client():
    return flask_app.test_client()

@pytest.fixture
def mock_database():
    return MagicMock()

def test_get_reportes_from_dev_valid():
    """
    GIVEN a request with valid dev_id
    WHEN the fonction get_reportes_from_dev is called
    THEN check it returns the right json format
    """
    response = app_client.get_reportes_from_dev().get('/dev/reportes/', data=json.dumps({'id_dev' : '1'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200 #checks if all went well
    assert data['id'] == ... #add reels values expected
    assert data['title'] == ...
    assert data['description'] == ...
    assert data['likes'] == ...
    assert data['data'] == ...
    assert data['id_estado'] == ...
    assert data['id_prioridad'] == ...
    assert data['id_producto'] == ...
    assert data['id_developer'] == ...

def test_get_reportes_from_dev_invalid():
    """
    GIVEN a request with an invalid dev_id
    WHEN the fonction get_reportes_from_dev is called
    THEN check it returns te right status code and error message
    """
    response = app_client.get_reportes_from_dev().get('/dev/reportes/', data=json.dumps({'id_dev' : '0'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['error'] == 'No existe el desarollador'


def test_get_likes_from_user_valid():
    """
    GIVEN a request with valid user_id
    WHEN the fonction get_likes_from_user is called
    THEN check it returns the right json format
    """
    response = app_client.get_likes_from_user().get('/user/liked/', data=json.dumps({'id_user' : '1'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200 #checks if all went well
    assert data['id'] == ... #add reels values expected
    assert data['title'] == ...
    assert data['description'] == ...
    assert data['likes'] == ...
    assert data['data'] == ...
    assert data['id_estado'] == ...
    assert data['id_prioridad'] == ...
    assert data['id_producto'] == ...
    assert data['id_developer'] == ...

def test_get_likes_from_user_invalid():
    """
    GIVEN a request with an invalid user_id
    WHEN the fonction get_likes_from_user is called
    THEN check it returns te right status code and error message
    """
    response = app_client.get_likes_from_user().get('/user/liked/', data=json.dumps({'id_user' : '0'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['error'] == 'No existe el usuario'

def test_get_all_reports_and_products_valid():
    """
    GIVEN a request with valid dev_id and product_id
    WHEN the fonction get_all_reports_and_products is called
    THEN check it returns the right json format and status code
    """
    response = app_client.get_all_reportes_and_prodcuts().get('/dev/all/report-product/', data=json.dumps({'id_dev' : '1'}), data=json.dumps({'id_producto' : '2'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200 #checks if all went well
    assert data['total_reports'] == ... #add reels values expected
    assert data['product_reports'] == ...

def test_get_all_reportes_and_prodcuts_invalid():
    """
    GIVEN a request with an invalid dev_id
    WHEN the fonction get_all_reportes_and_prodcuts is called
    THEN check it returns te right status code and error message
    """
    response = app_client.get_all_reportes_and_prodcuts().get('/dev/all/report-product/', data=json.dumps({'id_dev' : '0'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['error'] == 'No existe el desarollador'

def test_get_all_reportes_and_prodcuts_invalid():
    """
    GIVEN a request with an invalid producto_id
    WHEN the fonction get_all_reportes_and_prodcuts is called
    THEN check it returns te right status code and error message
    """
    response = app_client.get_all_reportes_and_prodcuts().get('/dev/all/report-product/', data=json.dumps({'id_producto' : '0'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['error'] == 'No existe el producto'

def test_get_all_reports_related_to_products_valid():
    """
    GIVEN a request with valid dev_id
    WHEN the fonction get_all_reports_related_to_products is called
    THEN check it returns the right json format and status code
    """
    response = app_client.get_all_reports_related_to_products().get('/dev/all-reportes-related-to-products/', data=json.dumps({'id_dev' : '1'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200 #checks if all went well
    assert data['id'] == ... #add reels values expected
    assert data['title'] == ...
    assert data['description'] == ...
    assert data['likes'] == ...
    assert data['data'] == ...
    assert data['id_estado'] == ...
    assert data['id_prioridad'] == ...
    assert data['id_producto'] == ...
    assert data['id_developer'] == ...

def test_get_all_reports_related_to_products_invalid():
    """
    GIVEN a request with an invalid dev_id
    WHEN the fonction get_all_reports_related_to_products is called
    THEN check it returns te right status code and error message
    """
    response = app_client.get_all_reports_related_to_products().get('/dev/all-reportes-related-to-products/', data=json.dumps({'id_dev' : '0'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['message'] == 'el id_dev no se encuentra en la base de datos'

def test_get_dev_info_valid():
    """
    GIVEN a request with valid dev_id
    WHEN the fonction get_dev_info is called
    THEN check it returns the right json format and status code
    """
    response = app_client.get_dev_info().get('/dev/info/', data=json.dumps({'id_dev' : '1'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200 #checks if all went well
    assert data['id'] == ... #add values expected
    assert data['nombre'] == ...
    assert data['email'] == ...
    assert data['id_rol'] == ...

def test_get_dev_info_invalid():
    """
    GIVEN a request with an invalid dev_id
    WHEN the fonction get_dev_info is called
    THEN check it returns te right status code and error message
    """
    response = app_client.get_all_reports_related_to_products().get('/dev/info/', data=json.dumps({'id_dev' : '0'}), content_type='application/json')
	
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['error'] == 'No existe el desarollador'

