import psycopg2
import requests
from config.config import host


def search_code(action,email):
    '''
    连接数据库，查询发送的验证码
    :param action: 注册，重置密码，修改邮箱。。。
    :param email: 邮箱
    :return:查找到的验证码
    '''
    # 建立连接
    conn = psycopg2.connect(
            "dbname=test-common-user-center user=ulandmaster password=k2G9!Qpr host=youland-test-db-instance-1.cjurcg0zx8s1.us-west-1.rds.amazonaws.com port=5432")
    # 获取游标
    cur = conn.cursor()
    # 查询数据库获取tenant_id
    sql1 = "SELECT tenant_id FROM public.yl_oss_institution_app where appkey = 'jcDlAFZpmslrRYwUzfpP'"
    try:
        cur.execute(sql1)
        tenant_ids = cur.fetchone()
        #数据库查询code
        sql = f"SELECT code FROM public.yl_oss_verify_code where inbox_email = '{email}' and tenant_id = '{tenant_ids[0]}' and biz_type = '{action}' and validate = '1' ORDER BY expired_time DESC"
        cur.execute(sql)
        rows2 = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return rows2[0][0]

def del_user(email):
    '''
    连接数据库，删除用户
    :param email: 传入需要删除的用户email
    :return: 无
    '''
    conn = psycopg2.connect(
        "dbname=test-common-user-center user=ulandmaster password=k2G9!Qpr host=youland-test-db-instance-1.cjurcg0zx8s1.us-west-1.rds.amazonaws.com port=5432")
    # 获取游标
    cur = conn.cursor()
    try:
        sql = f"select id from yl_oss_user where email = '{email}'" #通过email查找到用户id
        cur.execute(sql)
        id = cur.fetchall()[0][0]
        if id:
            sql1 = f"delete from yl_oss_user where id = '{id}'" #用户表删除用户
            cur.execute(sql1)
            sql2 = f"delete from yl_oss_account where user_id = '{id}'"#账户表删除账户
            cur.execute(sql2)
            conn.commit()
    finally:
        cur.close()
        conn.close()

def listapplication(token):
    login_url = f'{host}processes/user/application'
    header = {
            'authorization': token,
            'accept': 'application/json,text/plain,',
            'user-agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }
    paylod = {"page": 1, "size": 50, "loanId": "", "loanType": [], "stage": [], "beginTime": "", "endTime": ""}
    resp = requests.post(login_url, headers=header, json=paylod)
        # print(resp.text)
    assert resp.status_code == 200
    dict = resp.json()
        # print(dict)
    application_list = dict['content']
        # print(application_list)
    pre_list = []
    for i in application_list:
        if i['loanStage'] == 'Pre Approved':
            pre_list.append(i['youlandId'])
                # print(pre_list)
    return pre_list[0]
