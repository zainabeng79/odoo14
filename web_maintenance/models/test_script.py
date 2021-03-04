import requests
import json

# url_connect = "http://75.119.131.24/web/session/authenticate"
url_connect = "http://localhost:8014/web/session/authenticate"
# url = "http://75.119.131.24/machine/info/"
url = "http://localhost:8014/machine/info/"

headers = {'Content-Type': 'application/json'}

data_connect = {
    "params": {
        "db": "fields2",
        "login": "admin",
        "password": "1",
    }
}
#
# data_connect = {
#     "params": {
#         "db": "ps_group",
#         "login": "admin",
#         "password": "admin",
#     }
# }

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

session = requests.Session()

r = session.post(url=url_connect, data=json.dumps(data_connect), headers=headers)

if r.ok:
    result = r.json()['result']

    if result.get('session_id'):
        session.cookies['session_id'] = result.get('session_id')

r = session.post(url=url, data=json.dumps({'data': data}), headers=headers)
print(r)
print(r.json())
