from odoo import models, fields, api

class MaintenanceChecklist(models.Model):
    _name = 'maintenance.checklist'

    name = fields.Char(string="Checklist Name")
    description = fields.Char()

