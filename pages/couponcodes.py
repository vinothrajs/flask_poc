# pages/home.py

from flask import redirect, render_template, Blueprint, url_for , flash , jsonify
from pages.TaskForms import TaskForm
import requests
from collections import namedtuple

couponcodes_bp = Blueprint('couponcodes', __name__)

# Define a named tuple for the API response data
Coupon = namedtuple('Coupon', ['id', 'CouponCode', 'EffectiveFrom', 'EffectiveTill', 'DiscountPercentage', 'createdAt', 'updatedAt', 'publishedAt'])

# Define your API URL
api_url = 'http://174.129.234.82:1337/api/coupon-codes'

# Example of token generation (replace with your actual authentication logic)
AUTH_TOKEN =  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzAwMTkzMTcxLCJleHAiOjE3MDI3ODUxNzF9.EYFneh0Lbf8qIoHU4kpvI6ft0q3Stbn7iqOq4Q62f84'


@couponcodes_bp.route('/couponcodes_form_withdata')
def couponcodes_form_withdata():
    try:

        # Set up headers with bearer token
        headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}

        # Make a request to the API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and create a list of named tuples
            api_data = response.json()['data']
            coupons = [Coupon(**coupon['attributes'], id=coupon['id']) for coupon in api_data]

            # Render the HTML template with the data
            return render_template('couponcode_jinja.html', coupons=coupons)
        else:
            # If the request was not successful, return an error message
            return jsonify({'error': f'Request failed with status code {response.status_code}'})

    except Exception as e:
        # Handle any exceptions that might occur during the request
        return jsonify({'error': f'An error occurred: {str(e)}'})



@couponcodes_bp.route('/couponcodes_form')
def couponcodes_form():
    try:

        return render_template('couponcodes.html')

    except Exception as e:
        # Handle any exceptions that might occur during the request
        return jsonify({'error': f'An error occurred: {str(e)}'})


@couponcodes_bp.route('/get_couponcodes_json')
def get_couponcodes_json():
    try:

        # Set up headers with bearer token
        headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}

        # Make a request to the API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and create a list of named tuples
            api_data = response.json()['data']
            coupons = [Coupon(**coupon['attributes'], id=coupon['id']) for coupon in api_data]

            # Convert named tuples to a list of dictionaries
            coupons_data = [coupon._asdict() for coupon in coupons]
            return jsonify({'coupons': coupons_data})
        else:
            # If the request was not successful, return an error message
            return jsonify({'error': f'Request failed with status code {response.status_code}'})

    except Exception as e:
        # Handle any exceptions that might occur during the request
        return jsonify({'error': f'An error occurred: {str(e)}'})