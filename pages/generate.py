# pages/home.py

from flask import render_template, Blueprint
import os
from jinja2 import Template

generate_bp = Blueprint('generate', __name__)

@generate_bp.route('/generate')
def generate():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(script_dir)
        file_path = os.path.join(script_dir, 'controller_template.j2')

        # Read the Jinja2 template from a file
        with open(file_path, 'r') as template_file:
            template_content = template_file.read()
        
        # Create a Jinja2 template object
        template = Template(template_content)

        # Define variables for template rendering
        variables = {
                'table_name':'',
                'route_nmae':'order',
                'html_file_name':'order',
                'fun_name' : 'orders',
                'user_custom_code_loigic_before_save' :'fecth()=>()nind',
                'user_custom_code_loigic_after_save' :''
        }

        # Render the template with variables
        rendered_code = template.render(variables)

        # Specify the file path to save the generated Python code
        new_file_path = os.path.join(script_dir, 'order.py')

        # Write the rendered code to a Python file
        with open(new_file_path, 'w') as python_file:
            python_file.write(rendered_code)

        return {"message": "Generated Python code saved to prodyct.py"}