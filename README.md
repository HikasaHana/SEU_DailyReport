# SEU_DailyReport  
每天健康日报的蠢比方法......简单来说就是模拟浏览器健康日报打卡操作。本来以为之前用的那个（ https://github.com/luzy99/SEUAutoLogin ）不能用了，所以自己整了个。  
只有在自己整了之后才能知道别人写得多好😭  
## 使用方法  
### GitHub Action  
1.由于fork的仓库无法修改可见性，默认公开（你的一卡通号和密码），所以要新建一个private的repository，选择import code，把本仓库的链接复制粘贴进去就行。  
2.修改代码中的配置信息，然后检查一下action是否正常。   
  
默认每天早上八点填报，可自行修改.github/workflows/dailyreport.yml中第五行代码调整时间。  
### 本地部署  
1.安装python 和 pip模块。  
2.运行requirements.bat，检查所有模块是否成功安装。  
3.修改代码中的配置信息。   
4.将dailyreport.bat添加到windows定时任务（ http://t.zoukankan.com/lishuangyun-p-13072009.html ）。  
常规中的配置选择Win10，操作中的“起始于（可选）”栏填写bat文件所在文件夹。  
  
由于默认是windows系统，所以如果是ios系统，需要把Edgedriver相关改成safaridriver，并修改useragent，记得将safaridriver的路径添加到环境变量。  
## 注意  
体温默认填写36.3，其余数据按照前一天数据不做改动。有信息变动的需要注意在自动日报之前手动日报一次覆盖信息。  
有其他自动日报（上面的链接）的使用者反映系统检测出“非人工打卡”而提示“健康状态异常”，导致入校申请不通过。  
## 附录：webhook部署（服务器端）  
1.下载go-cqhttp（https://github.com/Mrs4s/go-cqhttp/releases）  
2.初次运行时，选择HTTP通信，然后按照提示修改配置文件。记得添加机器人为QQ好友。  
3.服务器端下载宝塔面板（https://www.bt.cn/new/product.html），下载完成后，根据所给链接、账号、密码从控制端登录。  
4.选择网站→添加站点→创建站点，域名填写服务器公网IP。  
5.点击网站名，选择反向代理→添加反向代理，目标URL填写go-cqhttp配置文件中HTTP代理（默认为127.0.0.1:5700）。  
6.运行go-cqhttp。  
7.浏览器访问http://服务器公网ip/send_private_msg?user_id=你的QQ&message=123，测试消息是否成功发送。  
