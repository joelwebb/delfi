from marshmallow import fields, Schema
import datetime
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import scoped_session, sessionmaker, Query
from . import db

class container_model(db.Model):
    """model for our containers"""
    __tablename__ =  'containers'
    id = db.Column(db.Integer, primary_key=True)
    container = db.Column(db.String(128))
    uuid_barcode = db.Column(db.String(128))
    description = db.Column(db.String(128), nullable=True)
    instruments_id = db.Column(db.Integer, db.ForeignKey('instruments.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
      """Class constructor"""
      self.container = data.get('container')
      self.uuid_barcode = data.get('uuid_barcode')
      self.description = data.get('description')
      self.instruments_id = data.get('instruments_id')  
      self.created_at = datetime.datetime.utcnow()
      self.modified_at = datetime.datetime.utcnow()

    def save(self):
      db.session.add(self)
      db.session.commit()

    def update(self, data):
      for key, item in data.items():
        setattr(self, key, item)
      self.modified_at = datetime.datetime.utcnow()
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()

    @staticmethod
    def get_all_containers():
      return container_model.query.all()

    @staticmethod
    def get_one_container(id):
      return container_model.query.get(id)
    
    def __repr(self):
      return '<id {}>'.format(self.id)


class container_schema(Schema):
    """ container_schema"""
    id = fields.Int(dump_only=True)
    container = fields.Str(required=True)
    uuid_barcode = fields.Str(required=True)
    description = fields.Str(required=True)
    instruments_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)




class instrument_model(db.Model):
  """instrument Model"""
  __tablename__ = 'instruments'

  id = db.Column(db.Integer, primary_key=True)
  computer = db.Column(db.String(128),)
  mac_address = db.Column(db.String(128))
  freezer = db.Column(db.String(128))
  site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
  containers = db.Column(db.String(128))
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.computer = data.get('computer')
    self.mac_address = data.get('mac_address')
    self.freezer = data.get('freezer')
    self.containers = data.get('containers')
    self.site_id = data.get('site_id')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_instruments():
    return instrument_model.query.all()
  
  @staticmethod
  def get_one_instrument(id):
    return instrument_model.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class instrument_schema(Schema):
  """instrument Schema"""
  id = fields.Int(dump_only=True)
  computer = fields.Str(required=True)
  mac_address = fields.Str(required=True)
  freezer = fields.Str(required=True)
  site_id = fields.Int(required=True)
  containers = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)


class site_model(db.Model):
    """model for our sites"""
    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    instruments = db.Column(db.String(128))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        """Class constructor"""
        self.name = data.get('name')
        self.address = data.get('address')
        self.instruments = data.get('instruments')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_sites():
        return site_model.query.all()

    @staticmethod
    def get_one_site(id):
        return site_model.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class site_schema(Schema):
    """site_schema"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    instruments = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

