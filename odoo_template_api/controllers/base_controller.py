from odoo import api, http
from base64 import b64encode, b64decode
from odoo.http import request
import json
import logging
class BaseController(http.Controller):
    _name = 'basecontroller'
    logger = logging.getLogger(__name__)
    @api.model
    def validate(self, kw, required_fields):
        for field_name in required_fields:
            if field_name not in kw or not kw[field_name]:
                return self.res_json(f'`{field_name}` is required.', False, 'Validation Error', 400)
        return None
    
    @api.model
    def Model(self, model):
        return request.env[model].sudo()
    
    @api.model
    def res_json(self, result, status, message, code = 200):
        return request.make_response(
                json.dumps(
                    {
                        'message': message,
                        'status': status,
                        'data': result,
                    }
                ), 
                headers={'Content-Type': 'application/json'},
                status=code
            )
        
    @api.model
    def res_json_meta(self, result, status, message, meta):
        return request.make_response(
                json.dumps(
                    {
                        'message': message,
                        'status': status,
                        'data': result,
                        'meta': meta
                    }
                ), 
                headers={'Content-Type': 'application/json'}
            )