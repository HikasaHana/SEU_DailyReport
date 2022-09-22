# SEU_DailyReport  
摸索GitHub Action中......  
每天健康日报的蠢比方法......简单来说就是模拟浏览器健康日报打卡操作。本来以为之前用的那个（ https://github.com/luzy99/SEUAutoLogin ）不能用了，所以自己整了个。


## 配置要求  
·python  
·edgedriver（ https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ ，记得将路径加入环境变量）（如果是ios的话，把代码里Edge相关的换成safari，下载safaridriver。不用chrome是因为有奇怪的版本不适配......）  
## 使用方法  
·pip install requirements  
·根据注释修改dailyreport.py  
·将bat文件设置为windows定时任务（ http://t.zoukankan.com/lishuangyun-p-13072009.html ）
