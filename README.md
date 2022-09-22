# SEU_DailyReport  
每天健康日报的蠢比方法......简单来说就是模拟浏览器健康日报打卡操作。本来以为之前用的那个（ https://github.com/luzy99/SEUAutoLogin ）不能用了，所以自己整了个。  
只有在自己整了之后才能知道别人写得多好😭  
## 使用方法  
### GitHub Action  
fork一份到自己的仓库，设置为private，改一下一卡通号和密码，设置一下workflow，大概就能用了（？）  
### 本地部署  
安装python 和 pip模块  
pip install -r requirements.txt  
按照提示填写一卡通号和密码  
将dailyreport.bat添加到windows定时任务（ http://t.zoukankan.com/lishuangyun-p-13072009.html ）  
由于默认是windows系统，所以如果是ios系统，需要把Edgedriver相关改成safaridriver，并修改useragent，记得将safaridriver的路径添加到环境变量。  
## 注意  
体温默认填写36.3，其余数据按照前一天数据不做改动。有信息变动的需要注意手动日报一次。（自动运行时间为每日八点）  
有其他自动日报的使用者反映系统检测出“非人工打卡”而提示“健康状态异常”，导致入校申请不通过。如果是本地部署，应该不会有这问题（？）  
