from odoo import fields, models


class HelloModel(models.Model):
    _name = "custom.hello"
    _description = "Hello World Model"

    name = fields.Char(string="Message", default="Hello World!")
