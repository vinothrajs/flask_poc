
# generated code
from flask import render_template, Blueprint

product_bp = Blueprint('product', __name__)

@product_bp.route('/product')
def products():
    return render_template('product.html')