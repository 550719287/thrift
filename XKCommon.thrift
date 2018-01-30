# 熙康益体机国际化Thrift
# 数据传输协议接口中使用的共通部分定义
# v0.1
# Copyright © 2013 Neusoft Xikang Healthcare Technology Co.,Ltd
# li.yc@neusoft.com
# 2013/10/25
###############################################################



###############################################################
# 服务处理异常
# Err0001：#？#账号不存在
# Err0002：登录密码错误
# Err0003：注册账号重复
# Err0004：数据库连接失败
# Err0005：添加账号失败
# Err0006：指标数据类型错误#？#
# Err0007：注册失败#？#
# Err0008：指标数据保存失败#？#
# Err0009：获取指标数据失败#？#
# Err0010：获取信任列表失败#？#
# Err0011：添加信任关系失败#？#
# Err0012：获取指标字典数据失败#？#
# Err0013: 修改口令错误#?#
# Err0014：口令强度不足
# Err0015: 账号格式不正确
# Err0016：账号信息不能为NULL
# Err0017: 原口令错误
# Err0018: 成员账号：#？#不存在
# Err0019: 登录过期，请重新登录
# Err0020：指定的用户不是当前登录的用户
# Err0021：指标代码#？#不存在
# Err0022：未找您要查询的账号
# Err9999：系统异常，请联系系统管理员
###############################################################
exception HealthServiceException {
  1: string code,           // 异常编码
  2: string message      // 异常消息消息
}