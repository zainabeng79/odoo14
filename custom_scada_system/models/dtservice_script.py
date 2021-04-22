import json
import requests
import werkzeug


headers = {'Content-Type': 'application/json'}

# target server authenticate url
url_connect = "http://75.119.131.24/web/session/authenticate"
# data to connect with database
data_connect = {
    "params": {
        "db": "ps_group",
        "login": "admin",
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
url = "http://75.119.131.24/scada_tables/"
# please send data like this formathttp://75.119.131.24/web/session/authenticate
data = [
    ({'start_time':'20.30'}),

]
# post data from skada to odoo to create it
response = session.post(url=url, data=json.dumps({'data': data}), headers=headers)

# response.json()  = {'jsonrpc': '2.0', 'id': None, 'result': '{"success": [29, 30]}'}
print(response.json())
