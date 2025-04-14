from odoo import models, fields

class HelloModel(models.Model):
    _name = 'custom.hello'
    _description = 'Hello World Model'

    name = fields.Char(string='Message', default='Hello World!')
