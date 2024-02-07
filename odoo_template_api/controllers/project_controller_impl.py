#-*- coding: utf-8 -*-
from . import base_controller
import math
class Index(base_controller.BaseController):
    def get_project_by_id(self, id):
        Project = self.Model('project.task')
        project = Project.search([
            ("id", "=", int(id))
        ])
        if not project or len(project) == 0:
            return False
        return project
    
    def get_all(self, kw):
        Project = self.Model('project.task')
        
        page = kw.get('page', 1)
        limit = kw.get('limit', 10)
        field = kw.get('field', 'id')
        orderBy = kw.get('orderBy', 'asc')
        
        try:
            page = int(page)
            limit = int(limit)
        except ValueError:
            page = 1
            limit = 10

        offset = (page - 1) * limit
        domain = []

        if len(field) == 0:
            field = "id"
        if len(orderBy) == 0:
            orderBy = "asc"

        if 'name' in kw:
            domain.append(('name', 'ilike', kw['name']))

        
        projects = Project.search(
            domain, offset=offset, limit=limit, order=field + ' ' + orderBy)

        response = []
        for project in projects:
            response.append({
                'id': project.id,
                'name': project.name,
            })

        total_count = Project.search_count(domain)
        total_pages = math.ceil(total_count / limit)
        meta = {
            'page': page,
            'limit': limit,
            'total_pages': total_pages,
            'field': field,
            'orderBy': orderBy
        }
        
        return self.res_json_meta(response, True, "Success Get All", meta)

    def create_project(self, kw):
        validation_result = self.validate(kw, ['name'])
        if validation_result:
            return validation_result
        
        name = kw.get('name')
        Project = self.Model('project.task')
        
        new_project = Project.create({
            'name': name
        })
        
        response = {
            'name': new_project.name,
            'id': new_project.id
        }
        
        return self.res_json(response, True, "Success create project")
    
    def get_one(self,  id, kw):
        project = self.get_project_by_id(id)
        if not project:
            return self.res_json({}, False, "Project not found")
        
        response = {
            'id': project.id,
            'name': project.name
        }
        
        return self.res_json(response, True, "Success get project")

    def update_project(self, id, kw):
        validation_result = self.validate(kw, ['name'])
        if validation_result:
            return validation_result
    
        name = kw.get('name')
        project = self.get_project_by_id(id)
        if not project:
            return self.res_json({}, False, "Project not found")
        
        project.write({'name': name})
        
        response = {
            'name': project.name,
            'id': project.id
        }
        
        return self.res_json(response, True, "Success update project")

    def delete_project(self, id, kw):
    
        project = self.get_project_by_id(id)
        if not project:
            return self.res_json({}, False, "Project not found")
        
        project.unlink()
        
        return self.res_json({}, True, "Success delete project")
