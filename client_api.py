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
		return client.findXKAccountByProofNum(idfy).userId
		

	def checkBindstate(self):
		#branchmac
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
		pass

	def addMember(self):
		#branch
		#error
		pass

	def deleteMembers(self):
		#branch
		#error
		pass

	def getCaregiverInfoService(self,phr,mac):
		#branch
		#error

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
		return client.bindDeviceByFamilyId(familyid,mac)
		

	def unBindDeviceByFamilyId(self,familyid,mac):
		#branch
		return client.unbindDeviceByFamilyId(familyid,mac)


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

	def checkBindStateByDeviceID(self):
		#need device
		return self.client.checkBindStateByDeviceID('awifidc:44:27:96:e9:ea')


	def messageNotify(self):
		#branch
		pass

	def getOutsideListByDeviceId(self):
		#need device
		return self.client.getOutsideListByDeviceId('awifidc:44:27:96:e9:ea')


	def hostlogin(self):
		#branch
		pass

	def getAllServices(self):
		#main or need device
		
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


	def getUsingServices(self):
		#main or need device
		
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

	def addOutside(self):
		#branch
		pass

	def getServiceRecords(self):
		#branch
		pass

	def getServiceHistory(self):
		#branch
		pass

	def getFamilyPoints(self):
		#main or need device
		
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
		#main or need device
		
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

	def updateServiceRecords(self):
		#branch
		pass

	def getHealthReportLists(self):
		#branch
		
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

	def getHealthReportListsByFamilyId(self):
		#branch
		pass

	def getNewRecipeListByUserID(self,userid):
		#need device
		return [self.client.getNewRecipeListByUserID('awifidc:44:27:96:e9:ea','0',userid)]
		

	def getNewphotoBydeviceID(self,mac,username):
		#need device
		return [self.client.getNewphotoBydeviceID(mac,'0',username)]

	def serviceCardGetUserPoints(self):
		#branch
		
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

	def serviceCardGetPointsHistory(self):
		#branch
		
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

	def BindCardToPerson(self):
		#branch and need device
		
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
		

	def getCallDoctor(self):
		#branch
		pass

	def saveInterfaceLog(self):
		#branch
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

	def getMemberHealthInfo(self):
		#branch
		
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

	def updateMemeberHealthInfo(self):
		#branch
		pass

if __name__ == "__main__":
	a = client_api_()
	print a.findXKAccountByProofNum('210103199007141514')