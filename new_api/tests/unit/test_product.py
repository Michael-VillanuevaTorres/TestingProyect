import pytest

"""def test_status_get_single_product(test_client, init_database):
    assert test_client.get('/product/get?id_product=1').status_code == 200
    
def test_status_error_get_single_product(test_client, init_database):
    assert test_client.get('/product/get?id_product=999').status_code == 400
    
def test_json_get_single_product(test_client, init_database):
    assert test_client.get('/product/get?id_product=1').json['name'] == 'default_product'
    assert test_client.get('/product/get?id_product=1').json['id'] == 1
    
def test_json_error_get_single_product(test_client, init_database):
    assert test_client.get('/product/get?id_product=999').json['message'] == 'el product no existe'
    
    
    """


