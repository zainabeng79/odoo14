# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

import odoo.http as http
from odoo.http import request


class Academy(http.Controller):

    @http.route('/maintenance/ticket/create/', type="http", auth="public", website=True)
    def maintenance_ticket_create(self, **kw):
        """  Create maintenance ticket"""
        values = kw
        new_user = request.env['maintenance.request'].sudo().create(
            {'name': values['name'], 'equipment_id': int(values['equipment_id']),
             'maintenance_team_id': int(values['maintenance_team_id']),
             'maintenance_type': values['maintenance_type'],
             'schedule_date': values['schedule_date'],
             'description': "Request Details: {}.\nCustomer: {}\nPhone: {}\nEmail: {}".format(values['description'],
                                                                                              values['user_name'],
                                                                                              values['phone'],
                                                                                              values['email'])})
        return http.request.render('web_maintenance.ticket_create_done',
                                   {'title': str(new_user.name)})

    @http.route('/web_maintenance/ticket_create_form/', auth='public', website=True, type="http")
    def index(self, **kw):
        equipment_ids = request.env['maintenance.equipment'].sudo().search([])
        maintenance_team_ids = request.env['maintenance.team'].sudo().search([])
        return http.request.render('web_maintenance.index',
                                   {'equipment_ids': equipment_ids,
                                    'maintenance_team_ids': maintenance_team_ids})

    @http.route('/web_maintenance/ticket_create/', auth='public', website=True, type='http', multilang=True,
                sitemap=True)
    def list(self, **kw):
        return http.request.render('web_maintenance.listing', {})
