
# generated code
from flask import render_template, Blueprint

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders')
def orders():
    return render_template('order.html')


@order_bp.route('/neworders')
def neworders():
    return render_template('neworders.html')
