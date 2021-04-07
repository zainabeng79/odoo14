
from odoo import models, fields, api

class DowntimeTransaction(models.Model):
    _name = 'downtime.transaction'
    _description = 'downtime_transaction_tables'
    _rec_name= 'down_code'

    start_time = fields.Float(string='Start Time',store=True)
    end_time = fields.Float(string='End Time',store=True)
    down_code = fields.Float(string='Downtime Code',store=True)
    tran_date = fields.Float(string='Transaction Date',store=True)
    shift = fields.Float(string='Shift',store=True)
    machine_name = fields.Char(string='Machine Name',store=True)
    status = fields.Selection([
                ('down_continue', 'DownContinue'),
                ('down', 'Down')]
       , string='Status',store=True)
    tran_date_active = fields.Date(string='Transaction Date Active',store=True)
    down_time_desc = fields.Char(string='Down Time Des',store=True)


