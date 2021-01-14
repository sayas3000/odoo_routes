# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RutaRecord(models.Model):
    _name = "odoo_route.cod_route"

    _order = 'sequence'
    sequence = fields.Integer(string='Sequencia')

    # _rec_name permite mostrar el código
    _rec_name = 'code'
    code = fields.Char(string='Código Rutas')
    description = fields.Char(string='Descripción Rutas', required=True)

    #devuelve las rutas
    codes = fields.Many2one('odoo_route.cod_route', string='Lista Rutas', ondelete='cascade')


    #controla que no se repitan rutas
    _sql_constraints = [
        ('code', 'UNIQUE (code)', 'Ya existe la ruta con ese nombre')
    ]

    #oculta filtros innecesarios
    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(RutaRecord, self).fields_get(allfields, attributes)
        fields_to_hide = ['codes',
                          'sequence',
                          'id']
        for field in fields_to_hide:
            res[field]['selectable'] = False  # disable field visible in filter
            res[field]['sortable'] = False  # disable field visible in grouping
        return res

class ClientRoutesRecord(models.Model):
    _inherit = 'res.partner'
    _order = 'sequence,id'
    sequence = fields.Integer(string='Orden')

    #devueve la lista con las rutas de ese cliente
    list_routes = fields.Many2many('odoo_route.cod_route', 'codes')

class RouteClients(models.Model):
    _inherit = 'odoo_route.cod_route'

    #devuelve la lista de clientes que pertenecen a estas rutas, por eso se pone codes
    list_clients = fields.Many2many('res.partner', 'codes')




