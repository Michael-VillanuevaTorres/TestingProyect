import pytest
import app.product.routes as product

def test_get_product(init_database):
    assert product.get_product(1).name == 'default_product'
    assert product.get_product(2) is None  