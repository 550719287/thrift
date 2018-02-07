# -*- coding: utf-8 -*-
# 
from thrift import Thrift	 
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient 
import sys	
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('D:/thrift/gen-py')  
import ttypes
import UserService 
import assertpy
import unittest

#报告路径
localaddr = 'D:\\Report_ikeepertest.html'

# testcase



#接口地址配置
ipaddr = '10.32.173.200'
	#服务器地址
port = 8085
	#端口号
projectname = '/XK_Phr_Proxy/UserServlet'
	#工程路径

#log = open(time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt",'wb')



class conf_sys(object):
	#server
	
	transport = THttpClient.THttpClient(ipaddr ,port ,projectname)  # ip  port projectname
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = UserService.Client(protocol)

	#class
	
	a = ttypes.AccountInfo()
	a.accountName = 'M5A1CFEDBE4B09F03008C774D'
	a.accountName = '15040344536'
	a.password = '123456'
	a.deviceId = 'awifidc:44:27:96:e9:ea'

	mif = ttypes.MemberInfo()
	cii = ttypes.CaregiverInfo()
	mdr = ttypes.MemberDoctorRelation()
	rif = ttypes.RecipeInfo()
	pif = ttypes.PhotoInfo()
	fif = ttypes.FamilyInfo()

class conf_param(object):
	#param
	
	identify = '210103199007141514'
	lonidentify = '2101031990071415145'
	shoridentify = '21010319900714151'
	mixidentify = '000103199007141d14'
	symidentify = '210103199007141,.;（）'
	#身份证

	password = '1q![];'
	lonpassword = '12345678901234567890[]qwerty'
	shorpassword = '12345'
	mixpassword = '1q[ ]#；（）'

	deviceId = 'awifi44:2c:05:4a:72:5d'
	londeviceId = 'awifidc:44:27:96:e9:ea:12'
	shordeviceId = 'awifidc:44:27:96:e9'
	mixdeviceId = 'awifidc:44:27:96:e9:[]'

	cardid = '66660024900193'
	loncardid = '666600249001931'
	shorcardid = '6666002490019'
	mixcardid = '666600249001sql'
	symcardid = '66660024900[ ]（）'
	#健康卡号

	accountName = '13500009876'
	lonaccountName = '1516090125123'
	shoraccountName = '1516090125'
	mixaccountName = '15160901qs你好'
	symaccountName = '15160901[ ]（）'



	def error(self,ex):
		e = str(ex)
		try:
			assertpy.assert_that(e).contains('HealthServiceException')
		except:
			try:
				assertpy.assert_that(e).contains('HTTP')
			except:
				print ex.message
				raise TypeError('ICE Error')
			else:
				print ex.message
				raise TypeError('HTTP ERROR')
		else:
			print(e)

	def getPhrcode(self,accountName):
		phr = conf_sys().client.findPersonPhrCodeByUniquerHealthInfo(accountName,0)
		return phr

	def getfamilyid(self,phr):
		familyid = conf_sys().client.getFamilyInfosByUserId(phr)
		return familyid

