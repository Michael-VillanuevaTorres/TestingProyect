import pytest

from app import create_app
from app.extensions import db
from config import TestingConfig
import app.report.routes as report 

@pytest.fixture(scope='function')
def test_client():
    app = create_app(TestingConfig)

    # other setup can go here

    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!
    
@pytest.fixture(scope='function')
def init_database(test_client):
    from app.models.role import Role
    from app.models.developer import Developer
    from app.models.product import Product
    from app.models.report import Report
    from app.models.user import User
    from app.models.state import State
    from app.models.priority import Priority
    from app.models.relationship_developer_product import RelationshipDeveloperProduct
    
    # Roles
    tester_role = Role(name='testero')
    db.session.add(tester_role)
    
    # Products
    default_product = Product(name='default_product')
    default_product2 = Product(name='default_product2')
    db.session.add(default_product)
    db.session.add(default_product2)
    
    # Developers
    default_developer = Developer(name="default_developer", email='default@email.com', id_role=1)
    default_developer2 = Developer(name="default_developer2", email='default2@email.com', id_role=1)
    db.session.add(default_developer)
    db.session.add(default_developer2)
    
    # Users
    default_user = User(name='default_user', email='default@email.com')
    db.session.add(default_user)
    
    # Commit changes
    db.session.commit()
    
    # RelationshipDeveloperProduct
    default_relationship = RelationshipDeveloperProduct(id_product=1, id_developer=1)
    db.session.add(default_relationship)
    
    # Reports
    default_report = Report(title='default_report', description='default description', id_product=1, id_user=1)
    db.session.add(default_report)
    
    # Commit changes
    db.session.commit()
    
    yield
    
    # Cleanup
    db.drop_all()
    