import pytest
from website import create_app

@pytest.fixture()
def app():
    from website import db
    
    app = create_app()
    app.config.update({
        "TESTING": True,
    })  

    with app.app_context():
        db.create_all()    

    ctx = app.app_context()
    ctx.push()
    
    yield app
    
    with app.app_context():
        db.session.remove()
        db.drop_all()
        
    ctx.pop()

    
    
@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()