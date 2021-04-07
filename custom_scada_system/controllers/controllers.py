# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
import odoo.http as http
from odoo.http import request
import requests
import json
# create service
# live data  controller
class MachineScadaInfo(http.Controller):
    @http.route('/api/json_post_srequest', type='json', methods=['POST'], auth="user")
    def machine_info(self, **kw):
        try:
            data = request.jsonrequest.get('data')
        except Exception as e:
            return e
        try:
            res_machine_obj = request.env['scada.livedata']
            smachine_ids = res_machine_obj.sudo().create(data)
        except Exception as e:
            return e
        try:
            return json.dumps({"Success": "Records partner created with ids {}".format(smachine_ids.ids)})
        except Exception as e:
            return e
# start stop  machine
class MachineInfo(http.Controller):
    @http.route('/machine_start_and_stop/info/', type='json', methods=['POST'], auth="user")
    def machine_info(self, **kw):
        try:
            data = request.jsonrequest.get('data')
        except Exception as e:
            return e
        try:
            machine_info_obj = request.env['machine.start.stop']
            ifo_ids = machine_info_obj.sudo().create(data)
        except Exception as e:
            return e
        try:
            return json.dumps({"success": "Records created with ids {}".format(ifo_ids.ids)})
        except Exception as e:
            return e

# downtime transaction
class ScadaTables(http.Controller):
    @http.route('/scada_tables/', type='json', methods=['POST'], auth="user")
    def scada_system(self, **kw):
        try:
            data = request.jsonrequest.get('data')
        except Exception as e:
            return e
        try:
            res_partner = request.env['downtime.transaction']
            if_ids = res_partner.sudo().create(data)
        except Exception as e:
            return e
        try:
            return json.dumps({"success": "Records created with ids {}".format(if_ids.ids)})
        except Exception as e:
            return e
# speed
class ScadaSpeed(http.Controller):
    @http.route('/scada_table/', type='json', methods=['POST'], auth="user")
    def scada_system(self, **kw):
        try:
            data = request.jsonrequest.get('data')
        except Exception as e:
            return e
        try:
            res_partner = request.env['production.speed']
            if_ids = res_partner.sudo().create(data)
        except Exception as e:
            return e
        try:
            return json.dumps({"success": "Records created with ids {}".format(if_ids.ids)})
        except Exception as e:
            return e
# machine capacity
class ScadaCap(http.Controller):
    @http.route('/scada_cap', type='json', methods=['POST'], auth="user")
    def scada_cap_system(self, **kw):
        try:
            data = request.jsonrequest.get('data')
        except Exception as e:
            return e
        try:
            res_partner = request.env['machine.capacity']
            if_ids = res_partner.sudo().create(data)
        except Exception as e:
            return e
        try:
            return json.dumps({"success": "Records  capacity created with ids {}".format(if_ids.ids)})
        except Exception as e:
            return e