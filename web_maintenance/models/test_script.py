import requests
import json
# url_connect = "http://localhost:8014/web/session/authenticate"
# url = "http://localhost:8014/machine/info/"
# data_connect = {
#     "params": {
#         "db": "fields2",
#         "login": "admin",
#         "password": "1",
#     }
# }

# target server authenticate url

url_connect = "http://75.119.131.24/web/session/authenticate"

# url to create data coming form skada

url = "http://75.119.131.24/machine/info/"

headers = {'Content-Type': 'application/json'}
# data to connect with database

data_connect = {
    "params": {
        "db": "ps_group",
        "login": "admin",
        "password": "admin",
    }
}

# please send data like this format

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
# create new session
session = requests.Session()
connect_session = session.post(url=url_connect, data=json.dumps(data_connect), headers=headers)
if connect_session.ok:
    result = connect_session.json()['result']
    if result.get('session_id'):
        session.cookies['session_id'] = result.get('session_id')

# ----------------------------

# post data from skada to odoo to create it

response = session.post(url=url, data=json.dumps({'data': data}), headers=headers)
print(response)

# response.json()  = {'jsonrpc': '2.0', 'id': None, 'result': '{"success": [29, 30]}'}
print(response.json())
