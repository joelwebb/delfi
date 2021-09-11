from flask import request, g, Blueprint, json, Response
from .all_models import site_model, site_schema
from .all_models import instrument_model, instrument_schema
from .all_models import container_model, container_schema
from . import db

# schema
site_api = Blueprint('site_api', __name__)
site_schema = site_schema()
container_api = Blueprint('container_api', __name__)
container_schema = container_schema()
instrument_api = Blueprint('instrument_api', __name__)
instrument_schema = instrument_schema()


# routes
@site_api.route('/<int:site_id>', methods=['POST'])
def create(site_id):
    """ create new site"""
    req1 = site_model.get_one_site(site_id)
    if req1:
      return custom_response({'error': 'site alread exists'}, 404)
    req_data = request.get_json()

    data = site_schema.load(req_data)
    req1 = site_model(data)
    req1.id = site_id
    req1.save()
    data = site_schema.dump(req1)
    return custom_response(data, 201)


@site_api.route('/', methods=['GET'])
def get_all():
    """ Return all of the sites"""
    req1s = site_model.get_all_sites()
    data = site_schema.dump(req1s, many=True)
    return custom_response(data, 200)


@site_api.route('/<int:site_id>', methods=['GET'])
def get_one(site_id):
    """Get one site by ID"""
    req1 = site_model.get_one_site(site_id)
    if not req1:
      return custom_response({'error': 'site not found'}, 404)
    data = site_schema.dump(req1)
    return custom_response(data, 200)



@site_api.route('/<int:site_id>', methods=['PUT'])
def update(site_id):
    """Update """
    req_data = request.get_json()
    req1 = site_model.get_one_site(site_id)
    if not req1:
      return custom_response({'error': 'site not found'}, 404)

    data = site_schema.load(req_data)
    
    req1.update(data)
    
    data = site_schema.dump(req1)
    return custom_response(data, 200)


@site_api.route('/<int:site_id>', methods=['DELETE'])
def delete(site_id):
  """Delete"""
  req1 = site_model.get_one_site(site_id)
  if not req1:
    return custom_response({'error': 'site not found'}, 404)
  data = site_schema.dump(req1)
  req1.delete()
  return custom_response({'message': 'deleted'}, 204)
  

# containers
@container_api.route('/<int:container_id>', methods=['POST'])
def create(container_id):
    """ create new container"""
    req1 = container_model.get_one_container(container_id)
    if req1:
      return custom_response({'error': 'container alread exists'}, 404)

    req_data = request.get_json()
    data = container_schema.load(req_data)
    req1 = container_model(data)
    req1.id = container_id
    req1.save()
    data = container_schema.dump(req1)
    return custom_response(data, 201)



@container_api.route('/', methods=['GET'])
def get_all():
    """ Return all of the containers"""
    req1s = container_model.get_all_containers()
    data = container_schema.dump(req1s, many=True)
    return custom_response(data, 200)


@container_api.route('/<int:container_id>', methods=['POST'])
def post_one(container_id):
    """Get one site by ID"""

    #check if record exists, send error if it does
    req1 = container_model.get_one_container(container_id)
    if not req1:
      req_data = request.get_json()
      req1 = container_schema.load(req_data)
      req1['container_id'] = container_id
      container_model_object = container_model(req1)
      container_model_object.save()
      data = container_schema.dump(req1)
      return custom_response(data, 200)

    else:
      return custom_response({'error': 'container already exists'}, 404)


@container_api.route('/<int:container_id>', methods=['GET'])
def get_one(container_id):
    """Get one container by ID"""
    req1 = container_model.get_one_container(container_id)
    if not req1:
      return custom_response({'error': 'container not found'}, 404)
    data = container_schema.dump(req1)
    return custom_response(data, 200)


@container_api.route('/<int:container_id>', methods=['PUT'])
def update(container_id):
    """ Update by id"""

    req_data = request.get_json()
    req1 = container_model.get_one_container(container_id)
    if not req1:
      return custom_response({'error': 'container_id not found'}, 404)

    data = container_schema.load(req_data)
    
    req1.update(data)
    
    data = container_schema.dump(req1)
    return custom_response(data, 200)


@container_api.route('/<int:container_id>', methods=['DELETE'])
def delete(container_id):
  """Delete A Blogreq1"""
  req1 = container_model.get_one_container(container_id)
  if not req1:
    return custom_response({'error': 'req1 not found'}, 404)
  data = container_schema.dump(req1)
  req1.delete()
  return custom_response({'message': 'deleted'}, 204)






@instrument_api.route('/<int:instrument_id>', methods=['POST'])
def create(instrument_id):
    """ create new instrument"""
    req1 = instrument_model.get_one_instrument(instrument_id)
    if req1:
      return custom_response({'error': 'instrument alread exists'}, 404)

    req_data = request.get_json()
    data = instrument_schema.load(req_data)
    req1 = instrument_model(data)
    req1.id = instrument_id
    req1.save()
    data = instrument_schema.dump(req1)
    return custom_response(data, 201)


@instrument_api.route('/', methods=['GET'])
def get_all():
    """ Return all of the instruments"""
    req1s = instrument_model.get_all_instruments()
    data = instrument_schema.dump(req1s, many=True)
    return custom_response(data, 200)

@instrument_api.route('/<int:instrument_id>', methods=['POST'])
def post_one(instrument_id):
    """create one site by ID"""

    #check if record exists, send error if it does
    req1 = container_model.get_one_container(instrument_id)
    if not req1:
      req_data = request.get_json()
      req1 = instrument_schema.load(req_data)
      req1['instrument_id'] = instrument_id
      instrument_model_object = instrument_id(req1)
      instrument_model_object.save()
      data = instrument_schema.dump(req1)
      return custom_response(data, 200)

    else:
      return custom_response({'error': 'container already exists'}, 404)


@instrument_api.route('/<int:instrument_id>', methods=['GET'])
def get_one(instrument_id):
    """Get one instrument by ID"""
    req1 = instrument_model.get_one_instrument(instrument_id)
    if not req1:
      return custom_response({'error': 'instrument not found'}, 404)
    data = instrument_schema.dump(req1)
    return custom_response(data, 200)


@instrument_api.route('/<int:instrument_id>', methods=['PUT'])
def update(instrument_id):
    """Update """
    req_data = request.get_json()
    req1 = instrument_model.get_one_instrument(instrument_id)
    if not req1:
      return custom_response({'error': 'instrument not found'}, 404)

    data = instrument_schema.load(req_data)
    
    req1.update(data)
    
    data = instrument_schema.dump(req1)
    return custom_response(data, 200)


@instrument_api.route('/<int:instrument_id>', methods=['DELETE'])
def delete(instrument_id):
  """Delete"""
  req1 = instrument_model.get_one_instrument(instrument_id)
  if not req1:
    return custom_response({'error': 'instrument not found'}, 404)
  data = instrument_schema.dump(req1)
  req1.delete()
  return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
  """ Custom Response """
  return Response( mimetype="application/json", response=json.dumps(res), status=status_code)

