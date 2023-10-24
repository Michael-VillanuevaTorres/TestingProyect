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
    from app.models.role import Role
    from app.models.developer import Developer
    from app.models.product import Product
<<<<<<< HEAD
    from app.models.report import Report

    from app.models.user import User
    from app.models.state import State
    from app.models.priority import Priority

    from app.models.relationship_developer_product import RelationshipDeveloperProduct
    from app.models.user import User
    
    tester_role = Role(name='testero')
    default_product = Product(name='default_product')
    default_product2 = Product(name='default_product2')
    
    default_developer = Developer(name="default_developer", email='default@email.com', id_role=1)
    default_developer2 = Developer(name="default_developer2", email='default2@email.com', id_role=1)
    
    default_user = User(name='default_user', email='default@email.com')
=======
#
    
    tester_role = Role(name='testero')
    default_product = Product(name='default_product')
    default_developer = Developer(name="default_developer", email='defaul@email.com', id_role=0)
>>>>>>> parent of 47d285ae (test(reports): Create tests for report paths and fix associated bugs)


    db.session.add(tester_role)    
    
    db.session.add(default_product)
<<<<<<< HEAD

=======
    db.session.add(default_developer)
>>>>>>> parent of 47d285ae (test(reports): Create tests for report paths and fix associated bugs)
    db.session.commit()
    




    db.session.add(default_product2)
    
    db.session.add(default_developer)
    db.session.add(default_developer2)
    
    db.session.add(default_user)
    
    db.session.commit()
    
    #default_relationship = RelationshipDeveloperProduct(id_product=1, id_developer=1)
    
    default_report = Report(title='default', description='default description', id_product=1, id_user=1)
    
    #db.session.add(default_relationship)
    db.session.add(default_report)
    
    db.session.commit()
    
    

    yield 
    
<<<<<<< HEAD
   
=======
>>>>>>> parent of 47d285ae (test(reports): Create tests for report paths and fix associated bugs)
    db.drop_all()
    