#-*- coding: utf-8 -*-
from . import base_controller
from odoo import http
from odoo.http import request

class Index(base_controller.BaseController):
    
    def login_impl(self, kw):
        validate_result = self.validate(kw, ['login', 'password', 'db'])
        if validate_result:
            return validate_result
        
        login = kw.get('login')
        password = kw.get('password')
        db = kw.get('db')
        
        http.request.session.authenticate(db, login, password)
        return self.res_json(request.env['ir.http'].session_info(), True, "Success login")

    def register_impl(self, kw):
        validate_result = self.validate(kw, ['name', 'email', 'password'])
        if validate_result:
            return validate_result
        
        name = kw.get('name')
        email = kw.get('email')
        password = kw.get('password')
        user = self.User().search([
            ('login', '=', email)
        ])
        
        if len(user) > 0:
            return self.res_json(None, False, "Email already registered")

        self.User().create({
            'name': name,
            'login': email,
            'email': email,
            'password': password,
        })
        
        return self.res_json(None, True, "Success registered user.")