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
from ttypes import *
import UserService
import traceback
import logging
import unittest
import HTMLTestRunner
import assertpy  
from config import *
from client_api import client_api_



class test_findXKAccountByProofNum(unittest.TestCase,client_api_):
#findXKAccountByProofNum

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()


	def test_normal_findXKAccountByProofNum(self):

		try:
			assert self.findXKAccountByProofNum(self.identify) is not None
		except BaseException , ex :
			self.error(ex)

		

	def test_long_findXKAccountByProofNum(self):

		try:
			assert self.findXKAccountByProofNum(self.lonidentify) is not None
		except BaseException , ex :
			self.error(ex)


	def test_short_findXKAccountByProofNum(self):

		try:
			assert self.self.findXKAccountByProofNum(self.shoridentify) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_findXKAccountByProofNum(self):

		try:
			assert self.findXKAccountByProofNum(self.mixidentify) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sym_findXKAccountByProofNum(self):

		try:
			assert self.findXKAccountByProofNum(self.symidentify) is not None
		except BaseException , ex :
			self.error(ex)

class test_registerAndBindAccount(unittest.TestCase,client_api_):
#registerAndBindAccount

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_registerAndBindAccount(self):


		try:
			assert self.registerAndBindAccount(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_registerAndBindAccount(self):

		try:
			assert self.registerAndBindAccount(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_short_registerAndBindAccount(self):

		try:
			assert self.registerAndBindAccount(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_registerAndBindAccount(self):

		try:
			assert self.registerAndBindAccount(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_bindDeviceByUserName(unittest.TestCase,client_api_):
#bindDeviceByUserName
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.accountName,self.password,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_allwrong_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.lonaccountName,self.shorpassword,self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.lonaccountName,self.password,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.shoraccountName,self.password,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_mix_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.mixaccountName,self.password,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sym_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.symaccountName,self.password,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)



	def test_longpsd_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.accountName,self.lonpassword,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_shortpsd_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.accountName,self.shorpassword,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mixpsd_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.accountName,self.mixpassword,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sympsd_bindDeviceByUserName(self):

		try:
			assert self.bindDeviceByUserName(self.accountName,self.sympassword,self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_getAccountInfosByDeviceId(unittest.TestCase,conf_param):
#getAccountInfosByDeviceId
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getAccountInfosByDeviceId(self):

		try:	
			assert client_api_().getAccountInfosByDeviceId(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getAccountInfosByDeviceId(self):

		try:
			assert client_api_().getAccountInfosByDeviceId(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getAccountInfosByDeviceId(self):

		try:
			assert client_api_().getAccountInfosByDeviceId(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getAccountInfosByDeviceId(self):
		try:
			assert client_api_().getAccountInfosByDeviceId(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)

class test_getDoctorInfoByDeviceID(unittest.TestCase,conf_param):
#getDoctorInfoByDeviceID
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getDoctorInfoByDeviceID(self):

		try:
			assert client_api_().getDoctorInfoByDeviceID(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_getDoctorInfoByDeviceID(self):

		try:
			assert client_api_().getDoctorInfoByDeviceID(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getDoctorInfoByDeviceID(self):

		try:
			assert client_api_().getDoctorInfoByDeviceID(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getDoctorInfoByDeviceID(self):
		try:
			assert client_api_().getDoctorInfoByDeviceID(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_getRecipeListByDeviceID(unittest.TestCase,conf_param):
#getRecipeListByDeviceID

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getRecipeListByDeviceID(self):

		try:
			assert client_api_().getRecipeListByDeviceID(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getRecipeListByDeviceID(self):

		try:
			assert client_api_().getRecipeListByDeviceID(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getRecipeListByDeviceID(self):

		try:
			assert client_api_().getRecipeListByDeviceID(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getRecipeListByDeviceID(self):
		try:
			assert client_api_().getRecipeListByDeviceID(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_getphotoBydeviceID(unittest.TestCase,conf_param):
#getphotoBydeviceID
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getphotoBydeviceID(self):

		try:
			assert client_api_().getphotoBydeviceID(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getphotoBydeviceID(self):

		try:
			assert client_api_().getphotoBydeviceID(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getphotoBydeviceID(self):

		try:
			assert client_api_().getphotoBydeviceID(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getphotoBydeviceID(self):
		try:
			assert client_api_().getphotoBydeviceID(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_checkBindStateByDeviceID(unittest.TestCase,conf_param):
#checkBindStateByDeviceID
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_checkBindStateByDeviceID(self):

		try:
			assert client_api_().checkBindStateByDeviceID(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_checkBindStateByDeviceID(self):

		try:
			assert client_api_().checkBindStateByDeviceID(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_checkBindStateByDeviceID(self):

		try:
			assert client_api_().checkBindStateByDeviceID(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_checkBindStateByDeviceID(self):
		try:
			assert client_api_().checkBindStateByDeviceID(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_getOutsideListByDeviceId(unittest.TestCase,conf_param):
#getOutsideListByDeviceId
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getOutsideListByDeviceId(self):

		try:
			assert client_api_().getOutsideListByDeviceId(self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getOutsideListByDeviceId(self):

		try:
			assert client_api_().getOutsideListByDeviceId(self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getOutsideListByDeviceId(self):

		try:
			assert client_api_().getOutsideListByDeviceId(self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getOutsideListByDeviceId(self):
		try:
			assert client_api_().getOutsideListByDeviceId(self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)

class test_getNewRecipeListByUserID(unittest.TestCase,conf_param):
#getOutsideListByDeviceId
	
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getNewRecipeListByUserID(self):

		try:
			assert client_api_().getNewRecipeListByUserID(self.accountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getNewRecipeListByUserID(self):

		try:
			assert client_api_().getNewRecipeListByUserID(self.lonaccountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getNewRecipeListByUserID(self):

		try:
			assert client_api_().getNewRecipeListByUserID(self.shoraccountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getNewRecipeListByUserID(self):
		try:
			assert client_api_().getNewRecipeListByUserID(self.mixaccountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sym_getNewRecipeListByUserID(self):
		try:
			assert client_api_().getNewRecipeListByUserID(self.symaccountName) is not None
		except BaseException , ex :
			self.error(ex)

class test_getNewphotoBydeviceID(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getNewphotoBydeviceID(self):

		try:
			assert client_api_().getNewphotoBydeviceID(self.deviceId,self.accountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getNewphotoBydeviceID(self):

		try:
			assert client_api_().getNewphotoBydeviceID(self.deviceId,self.accountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_getNewphotoBydeviceID(self):

		try:
			assert client_api_().getNewphotoBydeviceID(self.deviceId,self.accountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_getNewphotoBydeviceID(self):
		try:
			assert client_api_().getNewphotoBydeviceID(self.deviceId,self.accountName) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sym_getNewphotoBydeviceID(self):
		try:
			assert client_api_().getNewphotoBydeviceID(self.deviceId,self.accountName) is not None
		except BaseException , ex :
			self.error(ex)

class test_serviceCardLoginByCardNum(unittest.TestCase,conf_param):
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_serviceCardLoginByCardNum(self):

		try:
			assert client_api_().serviceCardLoginByCardNum(self.cardid) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_serviceCardLoginByCardNum(self):

		try:
			assert client_api_().serviceCardLoginByCardNum(self.loncardid) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_serviceCardLoginByCardNum(self):

		try:
			assert client_api_().serviceCardLoginByCardNum(self.shorcardid) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_serviceCardLoginByCardNum(self):
		try:
			assert client_api_().serviceCardLoginByCardNum(self.mixcardid) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sym_serviceCardLoginByCardNum(self):
		try:
			assert client_api_().serviceCardLoginByCardNum(self.symcardid) is not None
		except BaseException , ex :
			self.error(ex)

class test_serviceLoginByProofNum(unittest.TestCase,conf_param):
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_serviceLoginByProofNum(self):

		try:
			assert client_api_().serviceLoginByProofNum(self.identify, self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_serviceLoginByProofNum(self):

		try:
			assert client_api_().serviceLoginByProofNum(self.lonidentify, self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_short_serviceLoginByProofNum(self):

		try:
			assert client_api_().serviceLoginByProofNum(self.shoridentify, self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_mix_serviceLoginByProofNum(self):
		try:
			assert client_api_().serviceLoginByProofNum(self.mixidentify, self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_sym_serviceLoginByProofNum(self):
		try:
			assert client_api_().serviceLoginByProofNum(self.symidentify, self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)


class test_editPassword(unittest.TestCase,conf_param):
	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_editPassword(self):

		try:
			assert client_api_().editPassword(self.getPhrcode(self.accountName), self.password, self.password) is None
		except BaseException , ex :
			self.error(ex)

	def test_long_editPassword(self):

		try:
			assert client_api_().editPassword(self.getPhrcode(self.accountName), self.password, self.lonpassword) is None
		except BaseException , ex :
			self.error(ex)


	def test_short_editPassword(self):

		try:
			assert client_api_().editPassword(self.getPhrcode(self.accountName), self.password, self.shorpassword) is None
		except BaseException , ex :
			self.error(ex)


	def test_mix_editPassword(self):

		try:
			assert client_api_().editPassword(self.getPhrcode(self.accountName), self.password, self.mixpassword) is None
		except BaseException , ex :
			self.error(ex)



class test_getCaregiverInfoService(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getCaregiverInfoService(self):

		try:
			assert client_api_().getCaregiverInfoService(self.getPhrcode(self.accountName), self.deviceId) is not None
		except BaseException , ex :
			self.error(ex)

	def test_long_getCaregiverInfoService(self):

		try:
			assert client_api_().getCaregiverInfoService(self.getPhrcode(self.accountName), self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_short_getCaregiverInfoService(self):

		try:
			assert client_api_().getCaregiverInfoService(self.getPhrcode(self.accountName), self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_mix_getCaregiverInfoService(self):

		try:
			assert client_api_().getCaregiverInfoService(self.getPhrcode(self.accountName), self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)

class test_bindDeviceByUserId(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_bindDeviceByUserId(self):

		try:
			assert client_api_().bindDeviceByUserId(self.getPhrcode(self.accountName), self.deviceId) is None
		except BaseException , ex :
			self.error(ex)

	def test_long_bindDeviceByUserId(self):

		try:
			assert client_api_().bindDeviceByUserId(self.getPhrcode(self.accountName), self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_short_bindDeviceByUserId(self):

		try:
			assert client_api_().bindDeviceByUserId(self.getPhrcode(self.accountName), self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_mix_bindDeviceByUserId(self):

		try:
			assert client_api_().bindDeviceByUserId(self.getPhrcode(self.accountName), self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)

class test_deleteAccountsByDeviceId(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_deleteAccountsByDeviceId(self):

		try:
			assert client_api_().deleteAccountsByDeviceId(self.getPhrcode(self.accountName), self.deviceId) is not None
		except BaseException , ex :
			print ex.message
			self.error(ex)

	def test_long_deleteAccountsByDeviceId(self):

		try:
			assert client_api_().deleteAccountsByDeviceId(self.getPhrcode(self.accountName), self.londeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_short_deleteAccountsByDeviceId(self):

		try:
			assert client_api_().deleteAccountsByDeviceId(self.getPhrcode(self.accountName), self.shordeviceId) is not None
		except BaseException , ex :
			self.error(ex)


	def test_mix_deleteAccountsByDeviceId(self):

		try:
			assert client_api_().deleteAccountsByDeviceId(self.getPhrcode(self.accountName), self.mixdeviceId) is not None
		except BaseException , ex :
			self.error(ex)

class test_getFamilyInfosByUserId(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getFamilyInfosByUserId(self):

		try:
			assert [client_api_().getFamilyInfosByUserId(self.getPhrcode(self.accountName))] is not None
			lis = [client_api_().getFamilyInfosByUserId(self.getPhrcode(self.accountName))]
			print lis[0]
		except BaseException , ex :
			print ex.message
			self.error(ex)

class test_getVerifyCodeByDeviceId(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getVerifyCodeByDeviceId(self):

		try:
			assert client_api_().getVerifyCodeByDeviceId(self.getPhrcode(self.accountName)) is not None
			print client_api_().getVerifyCodeByDeviceId(self.getPhrcode(self.accountName))
		except BaseException , ex :
			print ex.message
			self.error(ex)

class test_bindDeviceByFamilyId(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_bindDeviceByFamilyId(slef):
		pass


class test_getDoctorInfoService(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getDoctorInfoService(self):
		try:
			assert client_api_().getDoctorInfoService(self.getPhrcode(self.accountName), self.deviceId) is not None
			print client_api_().getDoctorInfoService(self.getPhrcode(self.accountName), self.deviceId)
		except BaseException , ex :
			print ex.message
			self.error(ex)

class test_getRecipeListByUserID(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getRecipeListByUserID(self):
		try:
			assert client_api_().getRecipeListByUserID(self.getPhrcode(self.accountName)) is not None
		except BaseException , ex :
			print ex.message
			self.error(ex)

class test_getphotoInfoByurl(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getphotoInfoByurl(self):

		a = client_api_().getphotoBydeviceID(self.deviceId)
		b = []
		for i in a:
			print i.photourl
			b.append(i.photourl)

		try:
			assert client_api_().getphotoInfoByurl(b) is not None
		except BaseException , ex :
			print ex.message
			self.error(ex)

class test_getUserNameByUserID(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_getUserNameByUserID(self):

		try:
			# print client_api_().getUserNameByUserID(self.getPhrcode(self.accountName))
			assert client_api_().getUserNameByUserID(self.getPhrcode(self.accountName)) is not None
		except BaseException , ex :
			print ex.message
			self.error(ex)


class test_messageNotify(unittest.TestCase,conf_param):

	def setUp(self):
		transport = conf_sys().transport
		transport.open()

	def teardown(self):
		transport = conf_sys().transport
		transport.close()

	def test_normal_messageNotify(self):

		try:
			# print client_api_().getUserNameByUserID(self.getPhrcode(self.accountName))
			assert client_api_().messageNotify() is not None
		except BaseException , ex :
			print ex.message
			self.error(ex)






if __name__ == "__main__":

	#suite1 = unittest.TestLoader().loadTestsFromTestCase(client_branch)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(test_getUserNameByUserID)
	#unittest.TextTestRunner(verbosity=2).run(suite1)
	unittest.TextTestRunner(verbosity=2).run(suite2)
	#suite = unittest.makeSuite(client_branch_design) #运行类下面的test所有用例
	#suite = unittest.defaultTestLoader.discover('.','unit*.py') #运行当前目录下，以unit开头的所有用例
	#fr = open(localaddr,'wb')
	#runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
	#runner.run(suite2)