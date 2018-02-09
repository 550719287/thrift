# -*- coding: utf-8 -*-

from thrift import Thrift	
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
import logging
import assertpy
from config import conf_sys

#main 主功能不需要参数设计 见client文件
#needd device 需要各种参数变量设计 见client_branch_design文件
#branch 分支结构需要其它接口返回值作为中间参数  见client_branch_design文件

class client_api_(conf_sys):

#log = open(time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt",'wb')

	def login(self):
		#main

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


	def findXKAccountByProofNum(self,idfy):
		#need device
		client = self.client
		return client.findXKAccountByProofNum(idfy)
		

	def checkBindstate(self,mac,phr):
		#branchmac
		client = self.client
		return client.checkBindstate(mac,phr)

	def registerAccount(self):
		#main

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


	def registerAndBindAccount(self,mac):
		#need device

		client = self.client
		return client.registerAndBindAccount(self.mif,mac,"")

	def updateAccount(self):
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
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def editPassword(self,phr,psd1,psd2):
		#branch and need device

		client = self.client
		return client.editPassword(phr,psd1,psd2)
		

	def getMembers(self):
		#branch
		#error
		#没有参数
		pass

	def addMember(self):
		#branch
		#error
		#没有参数
		pass

	def deleteMembers(self):
		#branch
		#error
		#没有参数
		pass

	def getCaregiverInfoService(self,phr,mac):
		#branch
		#error
		#没有接口

		client = self.client
		return client.getCaregiverInfoService(phr,mac)

	def bindDeviceByUserName(self,accountName,password,deviceId):
		#need device

		client = self.client
		return client.bindDeviceByUserName(accountName,password,deviceId)

	def bindDeviceByUserId(self,phr,mac):
		#branch

		client = self.client
		return client.bindDeviceByUserId(phr,mac)
		

	def getAccountInfosByDeviceId(self,mac):
		#main or need device
		client = self.client
		return client.getAccountInfosByDeviceId(mac)

	def deleteAccountsByDeviceId(self,phr,mac):
		#branch
		return self.client.deleteAccountsByDeviceId(phr,mac)
		

	def getFamilyInfosByUserId(self,phr):
		#branch
		return self.client.getFamilyInfosByUserId(phr)
		


	def getVerifyCodeByDeviceId(self,phr):
		#branch
		return self.client.getVerifyCodeByDeviceId(phr)
		

	def sendSmsVerifyCode(self,username):
		#branch
		return self.client.sendSmsVerifyCode()

	def validateSmsVerifyCode(self):
		#branch
		pass

	def resetPassword(self):
		#branch
		pass

	def bindDeviceByFamilyId(self,familyid,mac):
		#branch
		return self.client.bindDeviceByFamilyId(familyid,mac)
		

	def unBindDeviceByFamilyId(self,familyid,mac):
		#branch
		return self.client.unBindDeviceByFamilyId(familyid,mac)


	def getDoctorInfoService(self,phr,mac):
		#branchmac
		cgi = self.cii
		return self.client.getDoctorInfoService(phr,mac)


	def getDoctorInfoByDeviceID(self,mac):
		#need device
		mdr = self.mdr
		return self.client.getDoctorInfoByDeviceID(mac)


	def getRecipeListByUserID(self,phr):
		#branch
		rif = self.rif
		return [self.client.getRecipeListByUserID(phr,'0')]

	def getRecipeListByDeviceID(self,mac):
		#need device
		rif = self. rif
		return self.client.getRecipeListByDeviceID(mac,'0')


	def getphotoBydeviceID(self,mac):
		#need device
		
		pif = self.pif
		return self.client.getphotoBydeviceID(mac,'0')


	def getphotoInfoByurl(self,photourl):
		#branch
		return self.client.getphotoInfoByurl(photourl)

	def getUserNameByUserID(self,phr):
		#branch
		return self.client.getUserNameByUserID(phr)

	def checkBindStateByDeviceID(self,mac):
		#need device
		return self.client.checkBindStateByDeviceID(mac)


	def messageNotify(self,msginfo):
		#branch
		return self.client.messageNotify(msginfo)

	def getOutsideListByDeviceId(self,mac):
		#need device
		return self.client.getOutsideListByDeviceId(mac)


	def hostlogin(self):
		#branch
		#hostID没用过
		pass

	def getAllServices(self,mac):
		#main
		return self.client.getAllServices(mac)


	def getUsingServices(self):
		#main
		
		try:
			assert self.client.getUsingServices('awifidc:44:27:96:e9:ea') is not None
		except BaseException , ex :
			print ex
			e = str(ex)
			try:
				assertpy.assert_that(e).contains('HealthServiceException')
			except:
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def addOutside(self):
		#branch
		#益体机绑定外设业务更改
		pass

	def getServiceRecords(self,mac,serviceid):
		#branch
		return self.client.getServiceRecords(mac,serviceid)

	def getServiceHistory(self,mac,serviceid):
		#branch
		return self.client.getServiceHistory(mac,serviceid)

	def getFamilyPoints(self):
		#main
		
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

	def getPointsHistory(self):
		#main
		
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

	def updateServiceRecords(self,recordid):
		#branch
		return self.client.updateServiceRecords(1,recordid)

	def getHealthReportLists(self,phr):
		#branch
		return self.client.getHealthReportLists(phr,1,0,100)


	def getHealthReportListsByFamilyId(self,phr,familyid):
		#branch

		return self.client.getHealthReportListsByFamilyId(phr,3,0,5000,familyid)

	def getNewRecipeListByUserID(self,username):
		#need device
		return [self.client.getNewRecipeListByUserID('awifidc:44:27:96:e9:ea','0',username)]
		

	def getNewphotoBydeviceID(self,mac,username):
		#need device
		return [self.client.getNewphotoBydeviceID(mac,'0',username)]

	def serviceCardGetUserPoints(self,phr):
		#branch
		return self.client.serviceCardGetUserPoints(phr)


	def serviceCardGetPointsHistory(self,phr):
		#branch
		#num参数不知道
		return self.client.serviceCardGetPointsHistory(phr,50)


	def serviceCardLoginByCardNum(self,cardid):
		#need device
		a = self.a
		return self.client.serviceCardLoginByCardNum(a,cardid)

	def serviceCardLoginByAccount(self):
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
				raise TypeError('Network Error')
			else:
				raise TypeError('HealthServiceException')

	def BindCardToPerson(self,mac,cardid,psd,phr):
		#branch and need device
		return self.client.BindCardToPerson(mac,cardid,psd,phr)

	def getPurchasedServices(self):
		#main
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

	def getPushMessage(self):
		#branch
		pass

	def getHealthControllerPlan(self):
		#branch
		
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

	def getHealthControllerRemindByMember(self):
		#branch
		
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

	def getHealthControllerRemindByDeviceId(self):
		#main
		
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

	def getHealthControllerRemindByDevice(self):
		#main
		
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

	def sendMessageToManager(self):
		#main
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

	def serviceLoginByProofNum(self,mac,ide):
		#need device
		return self.client.serviceLoginByProofNum(ide,mac)
		

	def getCallDoctor(self,serviceid):
		#branch
		return self.client.getCallDoctor(serviceid)

	def saveInterfaceLog(self):
		#branch
		#南京益体机专用需要提供经纬度
		pass

	def getPeripheralConfigureList(self):
		#main
		
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

	def getMemberHealthInfo(self,phr):
		#branch
		return self.client.getMemberHealthInfo(phr)

	def updateMemeberHealthInfo(self,phr,get):
		#branch
		return self.client.updateMemeberHealthInfo(phr,get)

if __name__ == "__main__":
	a = client_api_()
	print a.findXKAccountByProofNum('210103199007141514')