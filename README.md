# SEU_DailyReport  
每天健康日报的蠢比方法......简单来说就是模拟浏览器健康日报打卡操作。本来以为之前用的那个（ https://github.com/luzy99/SEUAutoLogin ）不能用了，所以自己整了个。  
只有在自己整了之后才能知道别人写得多好😭  
## 使用方法  
### GitHub Action  
1.fork的仓库无法修改可见性，所以先fork，然后新建一个私密的repository，选择import code，把fork的仓库链接复制粘贴进去就行。  
2.修改代码中的配置信息，然后action里配置一下。   
  
默认每天早上八点填报，可自行修改.github/workflows/dailyreport.yml中第五行代码调整时间。  
### 本地部署  
1.安装python 和 pip模块  
2.pip install -r requirements.txt  
3.按照提示填写一卡通号和密码  
4.将dailyreport.bat添加到windows定时任务（ http://t.zoukankan.com/lishuangyun-p-13072009.html ）。  
配置的常规选择Win10操作的“起始于（可选）栏”填写bat文件所在文件夹。  
  
由于默认是windows系统，所以如果是ios系统，需要把Edgedriver相关改成safaridriver，并修改useragent，记得将safaridriver的路径添加到环境变量。  
## 注意  
体温默认填写36.3，其余数据按照前一天数据不做改动。有信息变动的需要注意在自动日报之前手动日报一次覆盖信息。  
有其他自动日报（上面的链接）的使用者反映系统检测出“非人工打卡”而提示“健康状态异常”，导致入校申请不通过。  
