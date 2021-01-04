# -*- coding: utf-8 -*-
from odoo import http

# class OdooRoutes(http.Controller):
#     @http.route('/odoo_routes/odoo_routes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_routes/odoo_routes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_routes.listing', {
#             'root': '/odoo_routes/odoo_routes',
#             'objects': http.request.env['odoo_routes.odoo_routes'].search([]),
#         })

#     @http.route('/odoo_routes/odoo_routes/objects/<model("odoo_routes.odoo_routes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_routes.object', {
#             'object': obj
#         })