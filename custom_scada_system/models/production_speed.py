# -*- coding: utf-8 -*-

from odoo import models, fields, api

class production_speed(models.Model):
    _name = 'production.speed'
    _description = 'scada_tables.scada_tables'
    _rec_name= 'machine_code'

    machine_code = fields.Char(string='Machine Code',store=True)
    speed = fields.Float(string='Machine Speed',store=True)
    tran_date = fields.Date(string='Transaction Date', store=True)
    tran_time = fields.Float(string=' Transaction Time',store=True)
    nail_dai = fields.Float(string='Product Diameter', store=True)
    nail_length = fields.Float(string='Product Length', store=True)
    nail_produced = fields.Integer(string='Number Of Nail Produced', store=True)
    in_item = fields.Integer(string='Input Product Code', store=True)
    nail_hour = fields.Integer(string='Production Hour', store=True)
    nail_min = fields.Integer(string='Production Minute', store=True)
    out_item = fields.Integer(string=' Output Product code', store=True)
    in_weight = fields.Integer(string=' Production Input Material Weight', store=True)
    tag = fields.Char(string='Tag Number', store=True)
    operator = fields.Integer(string='Operator Code', store=True)
    status = fields.Boolean(string='Status', store=True)


# class DowntimeTransaction(models.Model):
#     _name = 'downtime.transaction'
#     _description = 'scada_tables.scada_tables'
#     _rec_name = 'machine_code'
