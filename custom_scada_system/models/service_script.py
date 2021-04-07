import json
import requests
import werkzeug
headers = {'Content-Type': 'application/json'}
# target server authenticate url
url_connect = "http://localhost:8069/web/session/authenticate"
data_connect = {
    "params": {
        "db": "odoo142",
        "login": "zeinabeng900@gmail.com",
        "password": "admin",
    }
}
# create new session
session = requests.Session()
connect_session = session.post(url=url_connect, data=json.dumps(data_connect), headers=headers)
if connect_session.ok:
    result = connect_session.json()['result']
    if result.get('ocn_token_key'):
        session.cookies['session_id'] = result.get('ocn_token_key')
# ----------------------------

# url to create data coming form skada
url ='http://localhost:8069/api/json_post_srequest'
# please send data like this format
data = [
    ({
        'shift': 'Day',
        'operator_Id': '4516',
        'machine_code': 'NL-20',
        'status': '',
        'nail_dia': 3.05,
        'nail_length':54,
        'nail_speed':0,
        'nail_produced':0,
        # 't_date': '12-19-2020',
        'hours': 0,
        'minute': 13,
        'input_code': '0',
        'input_coiltag': '0',
        'output_code': '0',
        'inupt_coil_weight': 0,
        'machine_code': '',
        'shift_ope_code': '',
        'crane_ope_code': '',
        'forklift_ope_code': '',
        'ope_code1': '',
        'ope_code2': '',
        # 'starttime': '1-1-1900  4:30:00',
        # 'endtime': '1-1-1900   3:00:00',
        'input_dia': '',
        'output_dia': '',
        'output_length': '',
        'scrap': 0,
        # 't_time': '1-1-1900  8:38:17',
        'coil_status': '',
        # 'tab_date': '',
        'tab_actual_weight': '',
        'tab_scrap_weight': '',
        'tab_mac_id': '',
        'tab_mcn_code': '',
        'tab_user_id': '',
        'tab_scrap_type': '',
        'tab_in_barcode': '',
        'tab_out_barcode': '',
        'tab_scrap_powder_kg': '',
        'tab_scrap_coil_kg': '',
        # 't_date':'12/1/2020  06:55:15',
    }),
]
# post data from skada to odoo to create it
response = session.post(url=url, data=json.dumps({'data': data}), headers=headers)
# response.json()  = {'jsonrpc': '2.0', 'id': None, 'result': '{"success": [29, 30]}'}
data = data=json.dumps({'data': data})
# print(data)
print(response.json())
