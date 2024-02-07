#-*- coding: utf-8 -*-
from . import base_controller
from odoo import http
from odoo.http import request

class Index(base_controller.BaseController):
    def login(self, kw):
        self.logger.info(kw)
        login = kw.get('login')
        password = kw.get('password')
        db = kw.get('db')
        User = self.Model('res.users')
        
        user = User.search([
            ('login', '=', login)
        ], limit=1)
        http.request.session.authenticate(db, login, password)
        return self.res_json(request.env['ir.http'].session_info(), True, "Success login")
