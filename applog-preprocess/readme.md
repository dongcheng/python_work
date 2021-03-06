#日志分析项目
> 日志分析项目涉及到如下环节：

- 数据采集 (ios/andriod/server)
- 数据传输 (php)
- 实时处理
	- 读取 logstash
	- 存储 elasticsearch
	- 统计展示 kibana
	- `输出到预处理 redis`
- `离线处理`
	- 离线预处理
		- 通用处理
		- 分类处理
		- 输出到上传odps 文件/flume
	- 上传odps
		- 数据转换
		- 当日数据计算
		- 历史数据计算
		- 结果数据输出mysql
- 数据查询
	- 查询
	- 定时邮件

>**本文侧重于描述离线预处理环节**

##一. 数据采集
###1.1 客户端
####1.1.1 自定义埋点
[接口文档](http://appapi.people.com.cn:100/total/index1.php) 和 [埋点事件](http://appapi.people.com.cn:100/static/click_v1.htm)
####1.1.2 `通用页面拦截日志`

##二. 数据传输
###2.1 数据格式化
###2.2 `服务器数据加入`

##三. 实时处理
###3.1 logstash处理入库
通过配置logstash读取redis中的实时数据，然后进行处理后存储到elasticsearch中，目前进行了以下处理：

- 时间转换
- ios手机型号转换
- 根据ip地址获取通过geoip获取更多信息

##四. `离线处理`
###4.1 `离线预处理`
>说明：用于读取客户端传回来的日志，进行处理之后输入给分析系统，以保证日志的正确性和格式统一，加入通用处理与分类处理环节来进行一些初步加工，满足一些简单的数据需求

####4.1.1 日志读取
> 说明：从redis中读取日志数据

####4.1.2 通用处理
> 说明：进行一些ip，手机型号，时间修正的处理

####4.1.3 分类处理
> 说明：根据不同的日志类型进行个性化的处理，如用文章详情页的日志来统计文章的点击量

- type为news的日志是新闻点击日志，通过news_id来进行点击量的统计，以news_id为key使用redis计数器进行点击数量的统计，同时将news_id放到list，后台根据list更新文章点击量

####4.1.4 日志输出
> 说明：将日志输出到redis、文件、flume等

输出文件字段的顺序：

```js
	"app_key", "channel_id", "channel_num", "channel_title", "client_code", 
	"client_ver", "ctime", "destation", "device_model", "device_os", 
	"device_product", "device_size", "endtime", "event_name", 
	"geoip_area_code", "geoip_city_name", "geoip_continent_code", 
	"geoip_country_code2", "geoip_country_code3", "geoip_country_name", 
	"geoip_dma_code", "geoip_ip", "geoip_latitude", "geoip_location", 
	"geoip_longitude", "geoip_postal_code", "geoip_real_region_name", 
	"geoip_region_name", "geoip_timezone", "identifier", "ip",
	"isoCC", "isoCe", "latitude", "longitude", "MCC", "message", "MNC", 
	"network_state", "news_id", "news_title", "platform", "source", "sp", 
	"startup", "state", "tags", "type", "udid", "user_id", "user_name", 
	"user_type", "visit_id", "visit_start_time", "deal_date"
```

###4.2 上传odps
###4.3 当日数据计算
###4.4 历史数据计算
###4.5 结果输出到mysql

##五. 报表系统
###5.1 查询
###5.2 邮件发送