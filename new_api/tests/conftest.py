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



    # Cometer los cambios en la base de datos
    db.session.commit()
    
    tester_role = Role(name='testero')
    default_product = Product(name='default_product')

    db.session.add(tester_role)
    db.session.commit()
    
    db.session.add(default_product)
    db.session.commit()
    
    
    developer = Developer(
        name="Developers 1",
        email="Developers1@example.com",
        id_role=0
    )
    db.session.add(developer)
    db.session.commit()

    developer2 = Developer(
        name="Developers 2",
        email="Developers2@example.com",
        id_role=1
    )
    db.session.add(developer)
    db.session.commit()

    # Crear Clients (2 en total)
    
    client = User(
        name="Client 1",
        email="email1@example.com"
    )
    db.session.add(client)
    db.session.commit()

    client2 = User(
        name="Client 2",
        email="email1@example.com"
    )
    db.session.add(client)
    db.session.commit()



    # Crear Reports (2 por cada Product)
      
    report = Report(
        title="Report 1",
        description="Description Report 1",
        id_product=default_product.id,
        id_user=1, 
    )
    db.session.add(report)
    Report.add_developer(report, 1)
    db.session.commit()

    report2 = Report(
        title="Report 2",
        description="Description Report 2",
        id_product=default_product.id,
        id_user=1, 
    )
    db.session.add(report)
    Report.add_developer(report, 1)
    db.session.commit()

    state=State(
        name="state 1"
    )
    db.session.add(state)

    state2=State(
        name="state 2"
    )
    db.session.add(state2)

    
    priority = Priority(
        name="priority 1"
    )
    db.session.add(priority)
    db.session.commit()

    priority2 = Priority(
        name="priority 1"
    )
    db.session.add(priority2)
    db.session.commit()
    




    yield 
    
    db.session.rollback()
    db.drop_all()
    