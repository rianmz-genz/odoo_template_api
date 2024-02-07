#-*- coding: utf-8 -*-
from odoo import http
from . import project_controller_impl
class ProjectController(project_controller_impl.Index):
    @http.route('/api/projects', auth='public', methods=["GET"],cors="*")
    def index(self, **kw):
        return self.get_all(kw)

    @http.route('/api/projects/create', auth='public', methods=["POST"], cors="*", csrf=False)
    def create_project_controller(self, **kw):
        return self.create_project(kw)
    
    @http.route('/api/projects/<int:id>', auth='public', methods=["PUT"], cors="*", csrf=False)
    def update_project_controller(self, id, **kw):
        return self.update_project(id, kw)
    
    @http.route('/api/projects/<int:id>', auth='public', methods=["DELETE"], cors="*", csrf=False)
    def delete_project_controller(self, id, **kw):
        return self.delete_project(id, kw)
    
    @http.route('/api/projects/<int:id>', auth='public', methods=["GET"], cors="*", csrf=False)
    def get_one_project_controller(self, id, **kw):
        return self.get_one(id, kw)