from odoo import models, fields, api


class MachineStartStopAction(models.Model):
    _name = 'machine.start.stop'

    MCN_CODE = fields.Char('Machine Code')
    T_Date = fields.Datetime('Transaction Date')
    MST_Time = fields.Datetime('Machine Start Time')
    MET_Time = fields.Datetime('Machine Stop Time')
    Status = fields.Char('Machine Running Status')

