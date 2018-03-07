# -*- coding: utf-8 -*-

from thrift import Thrift	
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient      #开发使用的thrift框架http请求，需要进入python在thrift包里找到合适的对应方法
import time
import sys	
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('D:/thrift/gen-py')  
from ttypes import *
from config import *
import UserService
import traceback
import unittest
import assertpy
import HTMLTestRunner                         #报表
import logging                                #日志

class client(unittest.TestCase,conf_sys):


	def setUp(self):
		transport = self.transport
		transport.open()

	def teardown(self):
		transport = self.transport
		transport.close()


	def test_login(self):
		#main

		client = self.client
		a = self.a
		
		try:
			assert client.login(a).login_token is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



	def test_registerAndBindAccount(self):
		#main
		
		client = self.client
		mif = self.mif
		
		try:
			assert client.registerAndBindAccount(mif,"awifidc:44:27:96:e9:ea","") is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_updateAccount(self):
		#main

		client = self.client
		mif = self.mif
		
		try:
			assert client.updateAccount(mif) is not None
		except BaseException , ex :
			print ex
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


	def test_getAccountInfosByDeviceId(self):
		#main
		client = self.client
		
		try:
			assert client.getAccountInfosByDeviceId('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getDoctorInfoByDeviceID(self):
		#main
		mdr = self.mdr
		
		try:
			assert self.client.getDoctorInfoByDeviceID('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



	def test_getRecipeListByDeviceID(self):
		#main
		rif = self. rif
		
		try:
			assert [self.client.getRecipeListByDeviceID('awifidc:44:27:96:e9:ea','0')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getphotoBydeviceID(self):
		#main
		
		pif = self.pif
		try:
			assert [self.client.getphotoBydeviceID('awifidc:44:27:96:e9:ea','0')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



	def test_getUserNameByUserID(self):
		#branch
		
		try:
			assert self.client.getUserNameByUserID('M5A1CFEDBE4B09F03008C774D') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_checkBindStateByDeviceID(self):
		#main
		
		try:
			assert self.client.checkBindStateByDeviceID('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_messageNotify(self):
		#main
		time1 = int(time.time())
		msgtime = str(time1)
		msg = MessageInfo(
			fromPerson = 'M5A1CFEDBE4B09F03008C774D',
			toPerson = 'M55FA54FBE4B0BB9D487A7D17',
			messageTime = msgtime,
			messageType = '1',
			messageContent = '123sgfdg',
			serviceid = '',
			deviceid = ''
			)
		# msg = {
		# 	'fromPerson' : 'M5A1CFEDBE4B09F03008C774D',
		# 	'toPerson' : 'M55FA54FBE4B0BB9D487A7D17',
		# 	'messageTime' : msgtime,
		# 	'messageType' : '1',
		# 	'messageContent' : '123sgfdg',
		# 	'serviceid' : '',
		# 	'deviceid' : '',
		# }

		try:
			print msg
			assert self.client.messageNotify(msg) is None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					print ex
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getOutsideListByDeviceId(self):
		#main
		
		try:
			assert self.client.getOutsideListByDeviceId('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getAllServices(self):
		#main
		
		try:
			assert self.client.getAllServices('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



	def test_getUsingServices(self):
		#main
		
		try:
			assert self.client.getUsingServices('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



	def test_getFamilyPoints(self):
		#main
		
		try:
			assert self.client.getFamilyPoints('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getPointsHistory(self):
		#main
		
		try:
			assert self.client.getPointsHistory('awifidc:44:27:96:e9:ea',50) is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_serviceCardLoginByAccount(self):
		#main
		a = self.a
		
		try:
			assert self.client.serviceCardLoginByAccount(a) is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



	def test_getPurchasedServices(self):
		#main
		try:
			assert self.client.getPurchasedServices('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getHealthControllerRemindByDeviceId(self):
		#main
		
		try:
			assert self.client.getHealthControllerRemindByDeviceId('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_getHealthControllerRemindByDevice(self):
		#main
		
		try:
			assert self.client.getHealthControllerRemindByDevice('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)


	def test_sendMessageToManager(self):
		#main
		a = self.a
		
		try:
			assert self.client.sendMessageToManager(a,'awifidc:44:27:96:e9:ea') is None
		except BaseException , ex :
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


	def test_getPeripheralConfigureList(self):
		#main
		
		try:
			assert self.client.getPeripheralConfigureList() is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				try:
					assertpy.assert_that(e).contains('HTTP')
				except:
					raise TypeError('ICE Error')
				else:
					print ex.message
					raise TypeError('HTTP ERROR')
			else:
				print(e)



if __name__ == "__main__":
	#21testcase

	suite = unittest.makeSuite(client) #运行类下面的test所有用例
	fr = open(localaddr,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
	runner.run(suite)
	
	# # 构造测试集
 #    suite = unittest.TestSuite()
 #    suite.addTest(client("test_messageNotify"))
 #    # 执行测试
 #    runner = unittest.TextTestRunner()
 #    runner.run(suite)