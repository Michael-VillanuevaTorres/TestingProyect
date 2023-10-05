import pytest
from flask import jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from app import app

# Fixture para configuración común
@pytest.fixture
def app_client():
    with app.test_client() as client:
    # Generar datos falsos para pruebas
        response = client.get('/generate_fake_data')
        yield client


def test_get_all_products(app_client):
    """
    Given: the database is populated with fake data
    When: a request is made to get all products
    Then: it should return a 200 status code and the expected product list
    """
    # When
    response = app_client.get('/products/all')
    
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