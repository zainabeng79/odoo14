from odoo import models, fields, api


class MaintenanceReq(models.Model):
    _inherit = 'maintenance.request'
    requester_id = fields.Many2one('res.partner','created By')
    des_loc = fields.Many2one('res.partner','Destination Location')
    matrial_req_emp = fields.Many2one('res.partner','Matrial Requisition Employee')
    # name = fields.Char('Name', required=True)

