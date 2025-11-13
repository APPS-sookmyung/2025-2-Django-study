from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse

from flask import Response
from functools import wraps
import json

def as_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        res = json.dumps(res, ensure_ascii=False).encode('utf8')
        return Response(res, content_type='application/json; charset=utf-8')
    return decorated_function

class Minus(Resource):
    @as_json
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('x', required=True, type=int, help='x cannot be blank')
            parser.add_argument('y', required=True, type=int, help='y cannot be blank')
            args = parser.parse_args()
            result = args['x'] - args['y']
            return {'result': f"{str(args['x'])} - {str(args['y'])} = {str(result)} 입니다."}
        except Exception as e:
            return {'error': str(e)}

app = Flask('My First App')
api = Api(app)
api.add_resource(Minus, '/minus')
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000, debug=True)