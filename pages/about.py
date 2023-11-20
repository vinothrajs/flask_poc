# pages/about.py

from flask import jsonify, render_template, Blueprint, request

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return render_template('about.html')

# Mock data for demonstration purposes
orders_data = [
    {"id": 1, "product": "Product A"},
    {"id": 2, "product": "Product B"},
    {"id": 3, "product": "Product C"},
    {"id": 4, "product": "Product D"},
    {"id": 5, "product": "Product E"},
    {"id": 6, "product": "Product F"},
    {"id": 7, "product": "Product G"},
    {"id": 8, "product": "Product H"},
    {"id": 9, "product": "Product I"},
    {"id": 10, "product": "Product J"},
    {"id": 11, "product": "Product A"},
    {"id": 12, "product": "Product B"},
    {"id": 13, "product": "Product C"},
    {"id": 14, "product": "Product D"},
    {"id": 15, "product": "Product E"},
    {"id": 16, "product": "Product F"},
    {"id": 17, "product": "Product G"},
    {"id": 18, "product": "Product H"},
    {"id": 19, "product": "Product I"},
    {"id": 20, "product": "Product J"},
]


@about_bp.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        # Get skip and take parameters from the request
        skip = int(request.args.get('skip', 0))
        take = int(request.args.get('take', 10))

        # Filter records based on skip and take parameters
        filtered_orders = orders_data[skip: skip + take]

        # Create the response JSON
        response_data = {
            "totalCount": len(orders_data),
            "data": filtered_orders
        }

        return jsonify(response_data)

    except Exception as e:
        # Handle exceptions, log errors, etc.
        return jsonify({"error": str(e)}), 500