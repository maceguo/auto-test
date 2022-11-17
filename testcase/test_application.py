import requests,json,sys,pytest,allure
sys.path.append('.')
from utils.logger import logger
from Lib.mortgage_application import Application

class Test_Application_pipe(Application):

    def test_start(self):
        #开始申请
        self.start_application()
        # 标的房
        self.varibles_purposre()
        #产权
        self.varibles_property()
        # 更新开始变量
        self.varibles_staring()
        # 保存开始申请
        self.starting_save()

    def test_personal_information(self):
        # 更新变量，开始更新个人信息
        self.varibles_cri()
        # 准备填写个人信息
        self.varibles_creditscore()
        # 填写个人信息
        self.varibles_myself()
        # 查询征信
        self.credit_check()

    def test_personal_income(self):
        # 更新变量，准别填写收入
        self.varibles_cedit()
        # 即将填写收入
        self.varibles_selfincome()
        # 填写收入
        self.varibles_incomeconfirm()
        # 保存收入
        self.selfincome_confirm()

    def test_personal_property(self):
        # 更新变量，准备填写个人房产信息
        self.varibles_startprd()
        # 是否有共借人
        self.varibles_isOnTheTitle()
        # 共借人信息确认
        self.notitle_confirm()
        # 其他信息确认
        self.other_confirm()

    def test_property(self):
        # 更新变量，曾经房产信息
        self.varibles_assets()
        # 其他房产信息
        self.varibles_ownCurrentEstate()
        # 更新当前流程
        self.varibles_processtag()
        # 即将确认房产
        self.varibles_ownpro()
        # 拥有房产确认
        self.ownpro_confirm()

    def test_personal_situation(self):
        # 更新变量，即将填写situation
        self.varibles_situation()
        # 填写situation
        self.varibles_situationsave()
        # 提交situation
        self.situation_confirm()

    def test_purchase_price(self):
        # 更新主流程，即将填写贷款金额
        self.process_situation()
        # 填写贷款金额
        self.varibles_price()
        # 确认贷款金额
        self.price_confirm()
        # 保存所有信息
        self.all_confirm()

    def test_all_varibles(self):
        # 更新所有变量
        self.varibles_all()