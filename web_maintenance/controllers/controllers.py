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

    @http.route('/web/machine/info/', csrf=False, type='json', methods=['POST'], auth="user")
    def machine_info(self, **kw):
        data = [
            {
                'Machine_Code': '232100',
                'Machine_Name': 'NAIL # 1 Wafios N-41',
                'Machine_ShortName': 'NL-01',
                'BAMS_Mac_Code': '201101',
                'BAMS_Mac_Desc': 'Nail Machine #1',
            },
            {
                'Machine_Code': '232101',
                'Machine_Name': 'NAIL # 1 Wafios N-41',
                'Machine_ShortName': 'NL-02',
                'BAMS_Mac_Code': '201102',
                'BAMS_Mac_Desc': 'Nail Machine #2',
            }]
        url = 'http://75.119.131.24/'
        url_connect = "{}/user/login".format(url)
        url_info = "{}/user/getInfo".format(url)
        headers = {'Content-Type': 'application/json'}
        data_connect = {
            "params": {
                "db": "ps_group",
                "email": "admin",
                "password": "admin",
            }
        }
        data = { "params": {"token": "< my test account id >" }}
        data_json = json.dumps(data)
        r = requests.get(url=url_connect, data=json.dumps(data_connect), headers=headers)
        print(r)
        print(r.json())
        r = requests.get(url=url_info, data=data_json, headers=headers)
        print(r)
        print(r.json())
        try:
            machine_info_obj = request.env['machine.info']
            ifo_ids = machine_info_obj.create(data)
        except Exception as e:
            return 'error'

        return json.dumps({"success": ifo_ids.ids})
