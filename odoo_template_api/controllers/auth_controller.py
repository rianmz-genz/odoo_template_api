#-*- coding: utf-8 -*-

from odoo import http
from . import auth_controller_impl
class AuthController(auth_controller_impl.Index):
    
    @http.route('/api/auth/login', auth='public', methods=["POST"], csrf=False, cors="*")
    def login_controller(self, **kw):
        return self.login_impl(kw)
    
    @http.route('/api/auth/register', auth='public', methods=["POST"], csrf=False, cors="*")
    def register_controller(self, **kw):
        return self.register_impl(kw)