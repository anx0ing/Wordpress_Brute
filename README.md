# README



### 简介

简单的wordpress xmlrpc.php爆破脚本，可以自动从/wp/v2/users（CVE-2017-5487）接口获取用户名进行爆破，适用于大量的wordpress目标爆破



### 用法

1、自动从/wp/v2/users（CVE-2017-5487）接口获取用户名进行爆破

```
python3 wp_login.py -u https://test.com -pwd password.txt -auto
```

![image-20230320094125477](https://raw.githubusercontent.com/beytagh001/blog-img/main/image-20230320094125477.png)

![image-20230320094203127](https://raw.githubusercontent.com/beytagh001/blog-img/main/image-20230320094203127.png)



2、指定用户名字典爆破

```
python3 wp_login.py -u https://test.com -user username.txt -pwd password.txt
```

![image-20230320093942348](https://raw.githubusercontent.com/beytagh001/blog-img/main/image-20230320093942348.png)


> 注：wordpress默认站点密码需要勾选才能使用弱密码

![image-20230320094756882](https://raw.githubusercontent.com/beytagh001/blog-img/main/image-20230320094756882.png)


### 免责声明

1. 本工具仅面向合法授权的企业安全建设行为与个人学习行为，如您需要测试本工具的可用性，请自行搭建靶机环境。
2. 在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。

如果发现上述禁止行为，我们将保留追究您法律责任的权利。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。

在安装并使用本工具前，请您务必审慎阅读、充分理解各条款内容。

除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。

