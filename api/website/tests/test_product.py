import pytest
from flask import jsonify
from website import create_app

# Fixture para configuración común
@pytest.fixture
def app_client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    # Generar datos falsos para pruebas
    response = client.get('/generate_fake_data')
    assert response.status_code == 200
    yield client

def test_get_reports_valid_product(app_client):
    """
    Given: a valid product ID
    When: a request is made to get reports for the product
    Then: it should return a 200 status code and a list of reports
    """
    # Given
    product_id = 1
    
    # When
    response = app_client.get(f'/products/get/reports?id_product={product_id}')
    
    # Then
    assert response.status_code == 200
    data = jsonify(response.get_json())
    assert len(data) == 1
    assert data[0]['id'] == 1
    assert data[0]['title'] == 'Report 1'

def test_get_product(app_client):
    """
    Given: a valid product ID
    When: a request is made to get a product
    Then: it should return a 200 status code and the expected product JSON
    """
    # Given
    product_id = 1
    
    # When
    response = app_client.get(f'/product/get?id_product={product_id}')
    
    # Then
    expected_json = {
        'id': 1,
        'nombre': 'Producto de prueba',
        'id_encargado': 1
    }
    assert response.status_code == 200
    assert response.get_json() == expected_json

def test_get_all_products(app_client):
    """
    Given: the database is populated with fake data
    When: a request is made to get all products
    Then: it should return a 200 status code and the expected product list
    """
    # When
    response = app_client.get("/products/all")
    
    # Then
    assert response.status_code == 200
    
    # Mapear los productos a un formato JSON similar al resultado esperado
    products_json = [
        { "id": 1, "nombre": "Producto 1","id_encargado": None},
        { "id": 2, "nombre": "Producto 2","id_encargado": None},
        { "id": 3, "nombre": "Producto 3","id_encargado": None},
        { "id": 4, "nombre": "Producto 4","id_encargado": None}
    ]

    # Comprobar que la respuesta coincide con la lista esperada de productos
    assert jsonify(products_json).data == response.data