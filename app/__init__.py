from flask import Flask
from .models import db
from routes import main_bp
from sqlalchemy import text

def create_app(config_class='config.config'):
    """Initializes the Flask application, configures extensions and registers blueprints."""
    app = Flask(__main__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.register_blueprint(main_bp)

  @app.before_request
  def create_tables():
      """Ensures the books table exists before handling any requests.psql -U postgres"""
      with app.app_context():
          try:
              # Check if tables are present by attempting a simple query
              db.session.execute(text("SELECT 1 FROM books LIMIT 1"))
          except Except:
              # If query fails, create all tables defined in models.py
              print("Database structure not found. Creating taables now...")
              db.create_all()
              db.session.commit()
  return app
