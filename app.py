from flask import Flask, render_template , Blueprint
import json

import importlib

app = Flask(__name__)

blueprint_modules = ["about", "home", "employee", "generate", "product"]
# Dynamic import and registration of blueprints
# Dynamic import and registration of blueprints with error handling
for blueprint_module in blueprint_modules:
    module_path = f"pages.{blueprint_module}"
    try:
        module = importlib.import_module(module_path)
        blueprint = getattr(module, f"{blueprint_module}_bp")
        app.register_blueprint(blueprint)
    except ImportError as e:
        print(f"Error importing {module_path}: {e}")

## static Import & Registertaion 
# from pages import about , home ,employee , generate , product
# app.register_blueprint(about.about_bp)
# app.register_blueprint(home.home_bp)
# app.register_blueprint(employee.employee_bp)
# app.register_blueprint(generate.generate_bp)
# app.register_blueprint(product.product_bp)



