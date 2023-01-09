import requests, allure, sys,pprint
sys.path.append('.')
from Lib.login import Signin, Verifycode


class Test_brokerinfo():
    def test_register_account(self):
        signup_url = 'http://test-pos-api.youland.com/usercenter/api/user/sign_up?role=broker'
        header = {
            'accept': 'application/json',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        payload = {
            "appkey": "jjHggHfNVaGvkabpQXfs",
            "emailParam": {
                "email": "920217@qq.com",
                "name": "macewf",
                "password": "QWExMjM0NTY=",
                "userType": "BROKER"
            }
        }
        resp = requests.post(signup_url, headers=header, json=payload)
        code_result = Verifycode().verifycode('REGISTER', (payload['emailParam']['email'],))
        assert resp.status_code == 200 and code_result == True
