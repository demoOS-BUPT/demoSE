# 分布式空调系统

## 文件目录：

- AirClient.py 客户端空调类
- AirServer.py 服务端空调类
- Client.py 客户端demo
- Server.py 服务端demo

- Database.py 数据库操作【待完善】
- air.db sqlite数据库文件
- air.conf 配置文件，代码中还没有加入，用ConfigParser解析

## 空调基本属性

- room 房间id
- mode 制冷制热['cold', 'hot']
- tempFrom 工作温度范围[int]
- tempTo 工作温度范围[int]
- tempWidth 温度波动范围[int]
- totalMoney 累计计费[%.2 float]
- time 服务端时间[年/月/日/时/分/秒]
- tempChange 温度变化、指三秒的温度变化量[float]
- perMoney 单价、指三秒的消费价格[$.2 float]
- totalElec 总计电量[%.2 float]
- currentTemp 当前温度[%.2 float]
- finalTemp 目标温度[%.2 float]
- wind 风速大小[1,2,3]
- startTime 开房时间、socket连接时间
- openTime 本次开空调时间
- sleep 是否睡眠状态[True, False]


## 配置信息

- 三种风速下的单位时间耗电量
- 每度电的价格
