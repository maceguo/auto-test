import pprint,pytest,sys
from Lib.login import Signin
sys.path.append('.')
from config.config import host
from utils.logger import logger
import requests,allure
from utils.excel_handle import get_excel_data
from utils.util import listapplication



@allure.feature('Dashboard')
class Test_Dashboard:
    def setup_class(self,username='mace@126.com',password='QWExMjM0NTY='):
        #登录获取token
        self.token=Signin().signin(username,password)
        #获取通过的申请编号（取第一个）
        self.pre_application =listapplication(self.token)

    @allure.story('申请列表')
    def test_listapplication(self):
        login_url = f'{host}processes/user/application'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        paylod = {"page": 1, "size": 50, "loanId": "", "loanType": [], "stage": [], "beginTime": "", "endTime": ""}
        resp = requests.post(login_url, headers=header, json=paylod)
        # print(resp.text)
        assert resp.status_code == 200

    @allure.story('单独申请记录')
    def test_processesinfo(self):
        login_url = f'{host}processes/{self.pre_application}'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        # pprint.pprint(resp.text)
        #比对响应码
        assert resp.status_code == 200

    @allure.story('个人设置信息')
    def test_sttingsinfo(self):
        login_url = f'{host}dashboard/user/settings/info'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        # pprint.pprint(resp.text)
        # 比对响应码
        assert resp.status_code == 200
        
    @allure.story('预批准信')
    def test_letter(self):
        login_url = f'{host}dashboard/letter/{self.pre_application}'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

    @allure.story('申请summary')
    def test_summary(self):
        login_url = f'{host}dashboard/overview/summary/{self.pre_application}'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

    @allure.story('申请状态')
    def test_taskstatus(self):
        login_url = f'{host}dashboard/user/tasks/status/{self.pre_application}'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200

    @allure.story('查看所有产品信息')
    def test_rateall(self):
        login_url = f'{host}dashboard/rate/{self.pre_application}/all'
        header = {
            'authorization': self.token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
        resp = requests.get(login_url, headers=header)
        assert resp.status_code == 200