import pytest

from app import create_app
from app.extensions import db
from config import TestingConfig

@pytest.fixture(scope='module')
def test_client():
    app = create_app(TestingConfig)

    # other setup can go here

    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!
    
@pytest.fixture(scope='module')
def init_database(test_client):
    
    tester_role = Role(name='tester')
    default_developer = Developer(name='default_developer',email='defaul@email.com', id_role=tester_role.id)
    default_product = Product(name ='default_product')
    
    db.session.add(tester_role)
    db.session.add(default_developer)
    db.session.add(default_product)
    
    db.session.commit()
    
    yield 
    
    db.drop_all()
    