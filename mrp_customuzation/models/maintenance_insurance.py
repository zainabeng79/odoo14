from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'maintenance.insurance'
    _description = 'Description'

    name = fields.Char("insurance name:")
    description = fields.Text("Description insurance")
