from flask import Flask, render_template
from car_inventory.db import db, migrate
from car_inventory.auth.routes import auth_bp
from car_inventory.cars.routes import cars_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('car_inventory.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cars_bp, url_prefix='/cars')

    @app.route('/')
    def home():
        return render_template('home.html')

    return app

from car_inventory.auth import models
