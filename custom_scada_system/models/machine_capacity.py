from odoo import models, fields, api

class MachineCapacity(models.Model):
    _name = 'machine.capacity'


    machine_name = fields.Char(string='Machine Name')
    length = fields.Char(string='Length')
    dia = fields.Char(string='Dia')
    Producedperhour = fields.Float(string='Produced per hour')
    producedpershift = fields.Float(string='Produced per shift')
    Nailpermin = fields.Float(string='Nailpermin')
