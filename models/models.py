# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RouteRecord(models.Model):
    _name = "odoo_routes.route"

    _order = 'sequence'
    sequence = fields.Integer(string='Sequencia')

    # _rec_name permite mostrar el código
    _rec_name = 'code'
    code = fields.Char(string='Código Rutas')
    description = fields.Char(string='Descripción Rutas', required=True)
    
    route_lines = fields.One2many('odoo_routes.route_line', 'route', string="Orden de Clientes")

    #codes = fields.Many2one('odoo_routes.route', 'Lista Rutas')

    #controla que no se repitan rutas
    _sql_constraints = [
        ('code', 'UNIQUE (code)', 'Ya existe la ruta con ese nombre')
    ]

    #oculta filtros innecesarios
    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(RouteRecord, self).fields_get(allfields, attributes)
        fields_to_hide = ['code',
                          'sequence',
                          'id']
        for field in fields_to_hide:
            res[field]['selectable'] = False  # disable field visible in filter
            res[field]['sortable'] = False  # disable field visible in grouping
        return res

    
class RouteLineRecord(models.Model):
    _name = 'odoo_routes.route_line'

    client_id = fields.Many2one('res.partner', string='Cliente')

    _rec_name = 'orders'
    orders = fields.Integer(string='Orden')

    route = fields.Many2one('odoo_routes.route', string="Ruta")



class ClientRoutesRecord(models.Model):
    _inherit = 'res.partner'

#    _order = 'sequence'
 #   sequence = fields.Integer(string='Sequence')

    # devueve la lista con las rutas de ese cliente

    list_routes = fields.Many2many('odoo_routes.route_line', 'route')
    #list_routes = fields.Many2many('odoo_routes.route', 'codes')


