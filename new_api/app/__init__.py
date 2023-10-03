from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.reassignment import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/reassignment')
    
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    from app.developer import bp as developer_bp
    app.register_blueprint(developer_bp, url_prefix='/developer')
    
    from app.product import bp as product_bp
    app.register_blueprint(product_bp, url_prefix='/product')
    
    from app.report import bp as report_bp
    app.register_blueprint(report_bp, url_prefix='/report')
    
    

    return app