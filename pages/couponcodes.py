# pages/home.py

from flask import redirect, render_template, Blueprint, request, url_for , flash , jsonify
from pages.TaskForms import TaskForm
import requests
from collections import namedtuple

couponcodes_bp = Blueprint('couponcodes', __name__)

# Define a named tuple for the API response data
Coupon = namedtuple('Coupon', ['id', 'CouponCode', 'EffectiveFrom', 'EffectiveTill', 'DiscountPercentage', 'createdAt', 'updatedAt', 'publishedAt'])
# Define a namedtuple for the pagination metadata
Pagination = namedtuple('Pagination', ['start', 'limit', 'total'])
Pagination_size = namedtuple('Pagination', ['page', 'pageSize', 'pageCount','total'])
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
        ## form default configure
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

# ?skip=0&take=2
@couponcodes_bp.route('/get_couponcodes_json_paging')
def get_couponcodes_json_paging():
    try:

        # Set up headers with bearer token
        headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
        api_url = 'http://174.129.234.82:1337/api/coupon-codes'

        # Get skip and take parameters from the request
        skip = int(request.args.get('skip', 0))
        take = int(request.args.get('take', 2))
        # Make a request to the API
        url_with_pagination = f'{api_url}?pagination[start]={skip}&pagination[limit]={take}'
        print(url_with_pagination)
        response = requests.get(url_with_pagination, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and create a list of named tuples
            api_data = response.json()['data']
            coupons = [Coupon(**coupon['attributes'], id=coupon['id']) for coupon in api_data]

            # Convert named tuples to a list of dictionaries
            coupons_data = [coupon._asdict() for coupon in coupons]

            api_data_meta = response.json()['meta']
            print(api_data_meta)
            # Extract values using the namedtuple
            pagination_meta = api_data_meta['pagination']
            print(pagination_meta)
            Pagination_size_value = Pagination(pagination_meta['start'], pagination_meta['limit'], pagination_meta['total'])

            # Create the response JSON
            response_data = {
                "totalCount": Pagination_size_value.total,
                "coupons": coupons_data
            }
            return jsonify(response_data)
        else:
            # If the request was not successful, return an error message
            return jsonify({'error': f'Request failed with status code {response.status_code}'})

    except Exception as e:
        # Handle any exceptions that might occur during the request
        return jsonify({'error': f'An error occurred: {str(e)}'})