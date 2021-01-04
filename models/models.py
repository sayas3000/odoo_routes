# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RutaRecord(models.Model):
    _name = "odoo_route.cod_route"
    #_order = 'sequence'

    #_rec_name permite mostrar el código
    _rec_name = 'code'
  #  sequence = fields.Integer(string='Sequencia')
    code = fields.Char(string='Código Rutas')
    description = fields.Char(string='Descripción Rutas', required=True)

    codes = fields.Many2one('odoo_route.cod_route', string='Lista Rutas')

    #controla que no se repitan rutas
    _sql_constraints = [
        ('code', 'UNIQUE (code)', 'Ya existe la ruta con ese nombre'),
        ('codes', 'UNIQUE (codes)', 'Ruta repetida')
    ]

    #oculta filtros innecesarios
    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(RutaRecord, self).fields_get(allfields, attributes)
        fields_to_hide = ['codes',
                          #'sequence',
                          'id']
        for field in fields_to_hide:
            res[field]['selectable'] = False  # disable field visible in filter
            res[field]['sortable'] = False  # disable field visible in grouping
        return res


'''
    @api.multi
    def ruta_record(self):
        vals = {
            'code': self.code,
            'description': self.description,
            'codes': self.codes,
        }
        self.env['odoo_route.cod_route'].create(vals)
'''

class ClientRoutesRecord(models.Model):
    _inherit = 'res.partner'
   # codes = fields.Many2one('odoo_route.cod_route', string='Lista Rutas')
    #@api.multi
    #def compute_field(self):
    #    self.list_routes = self.codes
    #list_routes = fields.One2many('odoo_route.cod_route', 'code', compute=compute_field)
    #list_routes = fields.One2many('odoo_route.cod_route', 'code', 'description', copy=True)
    list_routes = fields.One2many('odoo_route.cod_route', 'code')
    
   # list_routes = fields.One2many('res.partner', 'codes')
    @api.onchange('list_routes')
    def _onchange_list_routes(self):
        for rec in self:
            print('listas', self.list_routes[0].id)





