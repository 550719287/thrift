# -*- coding: utf-8 -*-

from thrift import Thrift	
#from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient 
import time
import sys	
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('D:/thrift/gen-py')  
import ttypes
import UserService
import traceback
import logging
import unittest
import HTMLTestRunner
import assertpy



class client(unittest.TestCase):
	transport = THttpClient.THttpClient('10.32.173.200', 8085, '/XK_Phr_Proxy/UserServlet')  # ip  port projectname
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = UserService.Client(protocol)

	a = ttypes.AccountInfo()
	a.userId = 'M5A1CFEDBE4B09F03008C774D'
	a.accountName = '15040344536'
	a.password = '123456'
	a.deviceId = 'awifidc:44:27:96:e9:ea'

	mif = ttypes.MemberInfo()
	cii = ttypes.CaregiverInfo()
	mdr = ttypes.MemberDoctorRelation()
	rif = ttypes.RecipeInfo()
	pif = ttypes.PhotoInfo()
	fif = ttypes.FamilyInfo()


	#log = open(time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt",'wb')


	def setUp(self):
		transport = self.transport
		transport.open()

	def teardown(self):
		transport = self.transport
		transport.close()


	def test_001_login(self):

		transport = self.transport
		client = self.client
		mif = self.mif
		
		try:
			assert client.login(mif).login_token is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')


	def test_002_findXKAccountByProofNum(self):
		transport = self.transport
		client = self.client
		try:
			assert client.findXKAccountByProofNum("210103199007141514").userId is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_003_checkBindstate(self):
		transport = self.transport
		client = self.client
		
		try:
			assert client.checkBindstate("awifidc:44:27:96:e9:ea","M5A1CFEDBE4B09F03008C774D") is False or True
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_004_registerAccount(self):
		transport = self.transport
		client = self.client
		mif = self.mif
		
		try:
			assert client.registerAccount(mif,"awifidc:44:27:96:e9:ea","") is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')


	def test_005_registerAndBindAccount(self):
		transport = self.transport
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
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_006_updateAccount(self):
		transport = self.transport
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
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_007_editPassword(self):
		transport = self.transport
		client = self.client
		
		try:
			assert client.editPassword('M5A1CFEDBE4B09F03008C774D','123456','123456') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_008_getMembers(self):
		pass

	def test_009_addMember(self):
		pass

	def test_010_deleteMembers(self):
		pass

	def test_011_getCaregiverInfoService(self):
		transport = self.transport
		client = self.client
		
		try:
			assert client.getCaregiverInfoService('M5A1CFEDBE4B09F03008C774D','awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_012_bindDeviceByUserName(self):
		transport = self.transport
		client = self.client
		
		try:
			assert client.bindDeviceByUserName('15040344536','123456','awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_013_bindDeviceByUserId(self):
		transport = self.transport
		client = self.client
		
		try:
			assert client.bindDeviceByUserId('M5A1CFEDBE4B09F03008C774D','awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_014_getAccountInfosByDeviceId(self):
		client = self.client
		
		try:
			assert client.getAccountInfosByDeviceId('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_015_deleteAccountsByDeviceId(self):
		
		try:
			assert self.client.deleteAccountsByDeviceId('M5A1CFEDBE4B09F03008C774D','awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')	
	
	def test_016_getFamilyInfosByUserId(self):

		try:
			assert self.client.getFamilyInfosByUserId('M5A1CFEDBE4B09F03008C774D') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')


	def test_017_getVerifyCodeByDeviceId(self):
		
		try:
			assert self.client.getVerifyCodeByDeviceId('M5A1CFEDBE4B09F03008C774D') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_018_sendSmsVerifyCode(self):
		pass

	def test_019_validateSmsVerifyCode(self):
		pass

	def test_020_resetPassword(self):
		pass

	def test_021_bindDeviceByFamilyId(self):
		pass
		

	def test_022_unBindDeviceByFamilyId(self):
		pass


	def test_023_getDoctorInfoService(self):
		cgi = self.cii
		
		try:
			assert [self.client.getDoctorInfoService('M5A1CFEDBE4B09F03008C774D','awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')


	def test_024_getDoctorInfoByDeviceID(self):
		mdr = self.mdr
		
		try:
			assert [self.client.getDoctorInfoByDeviceID('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_025_getRecipeListByUserID(self):
		rif = self.rif
		
		try:
			assert [self.client.getRecipeListByUserID('M5A1CFEDBE4B09F03008C774D','0')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_026_getRecipeListByDeviceID(self):
		rif = self. rif
		
		try:
			assert [self.client.getRecipeListByDeviceID('awifidc:44:27:96:e9:ea','0')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_027_getphotoBydeviceID(self):
		pif = self.pif
		
		try:
			assert [self.client.getphotoBydeviceID('awifidc:44:27:96:e9:ea','0')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_028_getphotoInfoByurl(self):
		pass

	def test_029_getUserNameByUserID(self):
		
		try:
			assert [self.client.getUserNameByUserID('M5A1CFEDBE4B09F03008C774D')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_030_checkBindStateByDeviceID(self):
		
		try:
			assert [self.client.checkBindStateByDeviceID('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_031_messageNotify(self):
		pass

	def test_032_getOutsideListByDeviceId(self):
		
		try:
			assert [self.client.getOutsideListByDeviceId('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_033_hostlogin(self):
		pass

	def test_034_getAllServices(self):
		
		try:
			assert [self.client.getAllServices('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')


	def test_035_getUsingServices(self):
		
		try:
			assert [self.client.getUsingServices('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_036_addOutside(self):
		pass

	def test_037_getServiceRecords(self):
		pass

	def test_038_getServiceHistory(self):
		pass

	def test_039_getFamilyPoints(self):
		
		try:
			assert [self.client.getFamilyPoints('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_040_getPointsHistory(self):
		
		try:
			assert [self.client.getPointsHistory('awifidc:44:27:96:e9:ea',50)] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_041_updateServiceRecords(self):
		pass

	def test_042_getHealthReportLists(self):
		
		try:
			assert [self.client.getHealthReportLists('M5A1CFEDBE4B09F03008C774D',1,0,100)] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_043_getHealthReportListsByFamilyId(self):
		pass

	def test_044_getNewRecipeListByUserID(self):
		
		try:
			assert [self.client.getNewRecipeListByUserID('awifidc:44:27:96:e9:ea','0','1516090125')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_045_getNewphotoBydeviceID(self):
		
		try:
			assert [self.client.getNewphotoBydeviceID('awifidc:44:27:96:e9:ea','0','1516090125')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_046_serviceCardGetUserPoints(self):
		
		try:
			assert self.client.serviceCardGetUserPoints('M5A1CFEDBE4B09F03008C774D') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_047_serviceCardGetPointsHistory(self):
		
		try:
			assert self.client.serviceCardGetPointsHistory('M5A1CFEDBE4B09F03008C774D',50) is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_048_serviceCardLoginByCardNum(self):
		a = self.a
		
		try:
			assert self.client.serviceCardLoginByCardNum(a,'66660024900193') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_49_serviceCardLoginByAccount(self):
		a = self.a
		
		try:
			assert self.client.serviceCardLoginByAccount(a) is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_050_BindCardToPerson(self):
		
		try:
			assert self.client.BindCardToPerson('awifidc:44:27:96:e9:ea','66660024900193','111111','M5A1CFEDBE4B09F03008C774D') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_051_getPurchasedServices(self):
		
		try:
			assert [self.client.getPurchasedServices('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_052_getPushMessage(self):
		pass

	def test_053_getHealthControllerPlan(self):
		
		try:
			assert [self.client.getHealthControllerPlan('M5A1CFEDBE4B09F03008C774D')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_054_getHealthControllerRemindByMember(self):
		
		try:
			assert [self.client.getHealthControllerRemindByMember('M5A1CFEDBE4B09F03008C774D')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_055_getHealthControllerRemindByDeviceId(self):
		
		try:
			assert [self.client.getHealthControllerRemindByDeviceId('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_056_getHealthControllerRemindByDevice(self):
		
		try:
			assert [self.client.getHealthControllerRemindByDevice('awifidc:44:27:96:e9:ea')] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_057_sendMessageToManager(self):
		a = self.a
		
		try:
			assert self.client.sendMessageToManager(a,'awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_058_serviceLoginByProofNum(self):
		
		try:
			assert self.client.serviceLoginByProofNum('210103199007141514','awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_059_getCallDoctor(self):
		pass

	def test_060_saveInterfaceLog(self):
		pass

	def test_061_getPeripheralConfigureList(self):
		
		try:
			assert [self.client.getPeripheralConfigureList()] is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_062_getMemberHealthInfo(self):
		
		try:
			assert self.client.getMemberHealthInfo('M5A1CFEDBE4B09F03008C774D') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def test_063_updateMemeberHealthInfo(self):
		pass


if __name__ == "__main__":

	#suite = unittest.TestLoader().loadTestsFromTestCase(client)
	#unittest.TextTestRunner(verbosity=2).run(suite)
	suite = unittest.makeSuite(client) #运行类下面的test所有用例
	#suite = unittest.defaultTestLoader.discover('.','unit*.py') #运行当前目录下，以unit开头的所有用例
	fr = open('D:\\Report_ikeepertest.html','wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
	runner.run(suite)