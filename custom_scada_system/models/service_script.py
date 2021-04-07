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
        # 't_date':'12/1/2020  06:55:15',
    }),
]
# post data from skada to odoo to create it
response = session.post(url=url, data=json.dumps({'data': data}), headers=headers)
# response.json()  = {'jsonrpc': '2.0', 'id': None, 'result': '{"success": [29, 30]}'}
data = data=json.dumps({'data': data})
# print(data)
print(response.json())
