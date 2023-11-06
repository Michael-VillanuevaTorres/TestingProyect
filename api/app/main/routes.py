from app.product import bp as app
from app.extensions import db

from app.models.product import Product
from app.models.report import Report
from app.models.user import User
from app.models.developer import Developer
from app.models.like import Like
from app.models.priority import Priority
from app.models.comment import Comment
from app.models.reassignment import Reassignment
from app.models.relationship_developer_product import RelationshipDeveloperProduct
from app.models.relationship_user_product import RelationshipUserProduct
from app.models.state import State
from app.models.role import Role


@app.route('/')
def index():
    pass

@app.route('/report/<int:id>')
def reporte(id):
    pass

@app.route('/product/<int:id>')
def producto(id):
    pass


