from flask import Flask
from .config import app_config
from .all_views import container_api
from .all_views import instrument_api 
from .all_views import site_api 
from flask_swagger_ui import get_swaggerui_blueprint
from . import db
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker
from .all_models import *
def create_app(env_name):
  """Creates an API for hosting the laboratory app for Delfi"""
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

  # initialize our db
  
  db.init_app(app)
  with app.app_context():
      db.create_all()
   # Swagger
  SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint('/docs', '/static/swagger.json',config={'app_name': "My Rest App"})

  app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix='/docs')
  #register blueprints for our other apps
  app.register_blueprint(site_api, url_prefix='/site')
  app.register_blueprint(instrument_api, url_prefix='/instrument')
  app.register_blueprint(container_api, url_prefix='/container')

  @app.route('/health', methods=['GET'])
  def index():
    """example endpoint"""
    return 'endpoint is healthy'

  @app.route('/seed', methods=['GET'])
  def seed():
    """example endpoint to seed the database"""
    try:
      engine = create_engine('sqlite:///test.db' , echo=False)
      sites = pd.read_csv("src/static/sites.csv")
      instruments = pd.read_csv("src/static/instruments.csv")
      containers = pd.read_csv("src/static/containers.csv")
      # Create a Session
      Session = sessionmaker(bind=engine)

      for site in sites.iterrows():
        new_site = site_model( data={
            "name": str(site[1].name),
            "address": str(site[1].address),
            "instruments": str(site[1].instruments)
          } )
        try:
          print(new_site.address)
          db.session.add(new_site)
          db.session.commit()

        except:
          pass

      for instrument in instruments.iterrows():
        new_instrument = instrument_model(data={
          "computer": instrument[1].computer,
          "mac_address": str(instrument[1].mac_address),
          "freezer" : instrument[1].freezer,
          "site_id": instrument[1].site_id,
          "containers": str(instrument[1].containers)
          })
        try:
          db.session.add(new_instrument)
          db.session.commit()
        except:
          pass

      for container in containers.iterrows():
          new_container = container_model(data={
            "container": str(container[1].container),
            "uuid_barcode": str(container[1].uuid_barcode),
            "description" : str(container[1].description),
            "instruments_id": str(container[1].instruments_id)
            })
          try:
            db.session.add(new_container)
            db.session.commit()

          except:
            pass
          
        # Add the record to the session object

      return 'seeded examples in the database'
    except Exception as e:
      return "{}: unable to seed database".format(e)

  return app


if __name__ == '__main__':
  app = create_app()
  