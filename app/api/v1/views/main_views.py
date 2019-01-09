from flask import Blueprint, jsonify, request, make_response
from flask import Blueprint

version1 = Blueprint('apiv1',
                     __name__,
                     url_prefix='/api/v1')


@version1.route('/', methods=['GET'])
@version1.route('/home', methods=['GET'])
def home():
    result = jsonify({'status':200,'data':[]})
    return make_response(result,200)
