# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

import odoo.http as http
from odoo.http import request
import requests
import json


class MaintenanceRequest(http.Controller):

    @http.route('/maintenance/ticket/create/', type="http", auth="public", website=True)
    def maintenance_ticket_create(self, **kw):
        """  Create maintenance ticket"""
        values = kw
        try:
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
        except:
            print("Please refresh the page")

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


class MachineInfo(http.Controller):
    @http.route('/machine/info/', type='json', methods=['POST'], auth="user")
    def machine_info(self, **kw):
        try:
            data = request.jsonrequest.get('data')
        except Exception as e:
            return e
        try:
            machine_info_obj = request.env['machine.info']
            ifo_ids = machine_info_obj.sudo().create(data)
        except Exception as e:
            return e
        try:
            return json.dumps({"success": "Records created with ids {}".format(ifo_ids.ids)})
        except Exception as e:
            return e

    # res partner controller
    class PartnerInfo(http.Controller):
        @http.route('/api/json_post_request', type='json', methods=['POST'], auth="user")
        def partner_info(self, **kw):
            try:
                data = request.jsonrequest.get('data')
            except Exception as e:
                return e
            try:
                res_partner_obj = request.env['res.partner']
                partner_ids = res_partner_obj.sudo().create(data)
            except Exception as e:
                return e
            try:
                return json.dumps({"Success": "Records partner created with ids {}".format(partner_ids.ids)})
            except Exception as e:
                return e
