import pytest

from app.models.product import Product
from app.models.report import Report
from app.models.developer import Developer
from app.models.relationship_developer_product import RelationshipDeveloperProduct

from app.extensions import db

def test_status_get_single_product(test_client, init_database):
    """
    GIVEN a valid product ID
    WHEN a GET request is made to retrieve a single product
    THEN the response status code should be 200 (OK)
    """
    assert test_client.get('/product/get?id_product=1').status_code == 200
    
def test_status_error_get_single_product(test_client, init_database):
    """
    GIVEN an invalid/non-existent product ID
    WHEN a GET request is made to retrieve a single product
    THEN the response status code should be 400 (Bad Request)
    """
    assert test_client.get('/product/get?id_product=999').status_code == 400
    
def test_json_get_single_product(test_client, init_database):
    """
    GIVEN a valid product ID
    WHEN a GET request is made to retrieve a single product
    THEN the JSON response should contain the product name and ID
    """
    response = test_client.get('/product/get?id_product=1').json
    assert response['name'] == 'default_product'
    assert response['id'] == 1
    
def test_json_error_get_single_product(test_client, init_database):
    """
    GIVEN an invalid/non-existent product ID
    WHEN a GET request is made to retrieve a single product
    THEN the JSON response should contain an error message
    """
    response = test_client.get('/product/get?id_product=999').json
    assert response['message'] == 'el producto no existe'
    
def test_status_get_all_products(test_client, init_database):
    """
    GIVEN the existence of one or more products
    WHEN a GET request is made to retrieve all products
    THEN the response status code should be 200 (OK)
    """
    assert test_client.get('/product/get/all').status_code == 200
    
def test_status_error_get_all_products(test_client, init_database):
    """
    GIVEN no products exist in the database
    WHEN a GET request is made to retrieve all products
    THEN the response status code should be 400 (Bad Request)
    """
    db.session.query(Product).delete()
    db.session.commit()
  
    assert test_client.get('/product/get/all').status_code == 400

def test_json_get_all_products(test_client, init_database):
    """
    GIVEN the existence of one or more products
    WHEN a GET request is made to retrieve all products
    THEN the JSON response should contain information about each product
    """
    response = test_client.get('/product/get/all').json
    
    assert response[0]['name'] == 'default_product'
    assert response[0]['id'] == 1
    
    assert response[1]['name'] == 'default_product2'
    assert response[1]['id'] == 2
    
def test_json_error_get_all_products(test_client, init_database):
    """
    GIVEN no products exist in the database
    WHEN a GET request is made to retrieve all products
    THEN the JSON response should contain an error message
    """
    db.session.query(Product).delete()
    db.session.commit()
  
    response = test_client.get('/product/get/all').json
    assert response['message'] == 'no hay productos'
    
def test_status_get_pending_reports(test_client, init_database):
    """
    GIVEN the existence of pending reports for a product
    WHEN a GET request is made to retrieve pending reports for that product
    THEN the response status code should be 200 (OK)
    """
    assert test_client.get('/product/get/pending_reports?id_product=1').status_code == 200
    
def test_status_error_get_pending_reports(test_client, init_database):
    """
    GIVEN no product with the specified id exists
    WHEN a GET request is made to retrieve pending reports
    THEN the response status code should be 400 (Bad Request)
    """
    assert test_client.get('/product/get/pending_reports?id_product=999').status_code == 400
    
def test_json_get_pending_reports(test_client, init_database):
    """
    GIVEN the existence of pending reports for a product
    WHEN a GET request is made to retrieve pending reports for that product
    THEN the JSON response should contain information about each pending report
    """
    report = test_client.get('/product/get/pending_reports?id_product=1').json[0]
    
    assert report['title'] == 'default_report'
    assert report['description'] == 'default description'
    assert report['id_product'] == 1
    assert report['id_user'] == 1
    assert report['id_state'] == 0
    
def test_json_no_product_error_get_pending_reports(test_client, init_database):
    """
    GIVEN no product with the specified id exists
    WHEN a GET request is made to retrieve pending reports
    THEN the JSON response should contain an error message
    """
    assert test_client.get('/product/get/pending_reports?id_product=999').json['message'] == 'el producto no existe'
    
def test_json_error_report__get_pending_reports(test_client, init_database):
    """
    GIVEN there are no pending reports for a product
    WHEN a GET request is made to retrieve pending reports for that product
    THEN the JSON response should contain an error message
    """
    db.session.query(Report).delete()
    db.session.commit()
    
    assert test_client.get('/product/get/pending_reports?id_product=1').json['message'] == 'el producto no tiene reportes pendientes'
    
def test_status_get_all_reports_from_product(test_client, init_database):
    """
    GIVEN the existence of reports for a product
    WHEN a GET request is made to retrieve all reports for that product
    THEN the response status code should be 200 (OK)
    """
    assert test_client.get('/product/get/reports/all?id_product=1').status_code == 200
    
def test_status_get_all_error_reports_from_product(test_client, init_database):
    """
    GIVEN no product with the specified id exists
    WHEN a GET request is made to retrieve all reports
    THEN the response status code should be 400 (Bad Request)
    """
    assert test_client.get('/product/get/reports/all?id_product=999').status_code == 400
    
def test_status_no_report_error_get_all_reports_from_product(test_client, init_database):
    """
    GIVEN there are no reports for a product
    WHEN a GET request is made to retrieve all reports for that product
    THEN the response status code should be 400 (Bad Request)
    """
    db.session.query(Report).delete()
    db.session.commit()
    
    assert test_client.get('/product/get/reports/all?id_product=1').status_code == 400

def test_json_get_all_reports_from_product(test_client, init_database):
    """
    GIVEN the existence of reports for a product
    WHEN a GET request is made to retrieve all reports for that product
    THEN the JSON response should contain information about each report
    """
    report1 = test_client.get('/product/get/reports/all?id_product=1').json[0]
    
    assert report1['title'] == 'default_report'
    assert report1['description'] == 'default description'
    assert report1['id_product'] == 1
    assert report1['id_user'] == 1
    assert report1['id_state'] == 0

def test_json_no_product_error_get_all_reports_from_product(test_client, init_database):
    """
    GIVEN no product with the specified id exists
    WHEN a GET request is made to retrieve all reports
    THEN the JSON response should contain an error message
    """
    assert test_client.get('/product/get/reports/all?id_product=999').json['message'] == 'el producto no existe'

def test_json_no_report_error_get_all_reports_from_product(test_client, init_database):
    """
    GIVEN there are no reports for a product
    WHEN a GET request is made to retrieve all reports for that product
    THEN the JSON response should contain an error message
    """
    db.session.query(Report).delete()
    db.session.commit()
    
    assert test_client.get('/product/get/reports/all?id_product=1').json['message'] == 'el producto no tiene reportes asignados'
    
def test_status_get_developers_from_product(test_client, init_database):
    """
    GIVEN the existence of developers assigned to a product
    WHEN a GET request is made to retrieve all developers for that product
    THEN the response status code should be 200 (OK)
    """
    assert test_client.get('/product/get/developers/all?id_product=1').status_code == 200
    
def test_status_error_get_developers_from_product(test_client, init_database):
    """
    GIVEN no product with the specified id exists
    WHEN a GET request is made to retrieve all developers
    THEN the response status code should be 400 (Bad Request)
    """
    assert test_client.get('/product/get/developers/all?id_product=999').status_code == 400
    
def test_status_no_developers_error_get_developers_from_product(test_client, init_database):
    """
    GIVEN there are no developers assigned to a product
    WHEN a GET request is made to retrieve all developers for that product
    THEN the response status code should be 400 (Bad Request)
    """
    db.session.query(Product).delete()
    db.session.commit()
    
    assert test_client.get('/product/get/developers/all?id_product=1').status_code == 400
    
def test_json_get_developers_from_product(test_client, init_database):
    """
    GIVEN the existence of developers assigned to a product
    WHEN a GET request is made to retrieve all developers for that product
    THEN the JSON response should contain information about each developer
    """
    developer = test_client.get('/product/get/developers/all?id_product=1').json[0]
    
    assert developer['name'] == 'default_developer'
    assert developer['email'] == 'default@email.com'
    
def test_json_error_no_product_get_developers_from_product(test_client, init_database):
    """
    GIVEN no product with the specified id exists
    WHEN a GET request is made to retrieve all developers
    THEN the JSON response should contain an error message
    """
    assert test_client.get('/product/get/developers/all?id_product=999').json['message'] == 'el producto no existe'
    
def test_json_no_developers_error_get_developers_from_product(test_client, init_database):
    """
    GIVEN there are no developers assigned to a product
    WHEN a GET request is made to retrieve all developers for that product
    THEN the JSON response should contain an error message
    """
    db.session.query(Developer).delete()
    db.session.query(RelationshipDeveloperProduct).delete()
    db.session.commit()
    
    assert test_client.get('/product/get/developers/all?id_product=1').json['message'] == 'el producto no tiene desarrolladores asignados'
