# 熙康益体机国际化Thrift
# 用户登录接口定义
# v0.1
# Copyright @ 2013 Neusoft Xikang Healthcare Technology Co.,Ltd
# li.yc@neusoft.com
# 2013/10/25
###############################################################

include "XKCommon.thrift"

// 用户账号信息，客户端登录、注册新用户、编辑用户信息时是该结构定义
struct AccountInfo {
    1: string  userId;               // 用户ID
    2: string  password;             // 登录口令
    3: string  nickName;             // 昵称
    4: string  fullName;						 // 全名
    5: string  registDatetime;       // 注册时间（MM-dd-YYYY），注册处理时，客户端不需要设置该属性值
    6: string  loginDatetime;        // 用户登录时间（MM-dd-YYYY），客户端不需要设置该时间，用户登录成功后，由Service返回
    7: binary  headPortrait;         // 用户头像
    8: string  cardID;               // 身份标识卡ID
    9: string  birthday;             // 出生日期（MM-dd-YYYY）
    10: i32     sex;                  // 性别
    11: string email;                // 电子邮箱
    12: string mobileNum;            // 手机号
    13: string watchId;              // 腕表ID
    14: i32    isEnable              // 账号是否启用
    15:	string deviceId;						 // 益体机唯一ID
    16: i32		 loginStatus;					 // 登录状态标识
    17: string accountName;					 // 登录时账户名
	18: string proofNum;             //身份证号码
	19: string addrDetail;					 // 联系地址:
	20: string login_token;            //登录熙康网的token信息   
	21: string isHost;                 //是否为户主1：户主； 0：非户主
    22: string role;                 //会员角色 1：使用者； 2：反馈者 3：朋友
	23: string usersig;                 //腾讯视频鉴权用的sig，目前户主使用。
	24: string headPictureUrl;                 //用户头像url路径。
	
}

struct PhrHealthClinic{
    1: string id;
    2: string personPhrCode;
    3: string diseaseCode;
    4: string diseaseName;
    5: string icd10Code;
    6: i64 onsetDate;
    7: i64 examineDate;
    8: string orgName;
    9: string doctorName;
    10: string illnessLayerCode;
    11: string illnessLayerName;
    12: string complicationNameStr;
    13: string complicationCodeStr;
    14: string memo;
    15: string prognosisCode;
    16: string prognosisName;
    17: i64 recoveryDate;
    18: i64 optTime;
}


struct YTJ_DiseaseHistory{
    1: string healthCode;
    2: list<PhrHealthClinic> phrDiseaseList;
}


//家族病史
struct YTJ_FamilyDiseaseHistory{
     1: string id;
     2: string personPhrCode;
     3: string relativeCode;
     4: string relativeName;
     5: string diseaseCode;
     6: string diseaseName;
}

//疾病史
struct YTJ_HealthClinicBean{
     1: string id;
     2: string personPhrCode;
     3: string diseaseCode;
     4: string diseaseName;
     5: string icd10Code;
     6: i64 onsetTime;
     7: i64 examineTime;
     8: string orgName;
     9: string doctorName;
     10: string illnessLayerCode;
     11: string illnessLayerName;
     12: string memo;
}


struct YTJ_PhrRiskFactorsBean{
	1: string id;
	2: string personPhrCode;
	3: string riskFactorsFactorCode;
	4: string riskFactorsFactorName;
	5: string riskFactorsName;
	6: string riskFactorsJob;
	7: i32 riskFactorsLength;
}

//用户生活方式
struct YTJ_PhrLifestyle{
    1: string personPhrCode;
    2: string smokingStateCode;
    3: string smokingStateName;
    4: string smokingRateCode;
    5: string smokingRateName;
    6: i32 smokingBeginAge;
    7: string tobaccoTypeCode;
    8: string tobaccoTypeName;
    9: i32 onSmoking;
    10: i32 smokingEndAge;
    11: string drinkingRateCode;
    12: string drinkingRateName;
    13: string drinkingTypeCode;
    14: string drinkingTypeName;
    15: i32 drinkingQuantity;
    16: i32 drinkingStartAge;
    17: string drunkFlag;
    18: string alcoholFlag;
    19: i32 alcoholAge;
    20: string sportsingRateCode;
    21: string sportsingRateName;
    22: i32 sportsingTime;
    23: i32 sportsingYear;
    24: string sportsingType;
    25: string dietingHabitCode;
    26: string dietingHabitName;
    27: string dietingSaltCode;
    28: string dietingSaltName;
    29: string dietingOilCode;
    30: string dietingOilName;
    31: string dietingSugarCode;
    32: string dietingSugarName;
    33: string exposeFlag;
    34: i64 optTime;
    35: list<YTJ_PhrRiskFactorsBean> riskFactorsList;
    36: i32 sportsingNumber;
    37: i64 smokingStartTime;
    38: i64 smokingEndTime;
    39: i64 abstinenceTime;
    40: string drinkingKind;
}

//手术信息
struct YTJ_Anamnesis {
     1: string id;
     2: string personPhrCode;
     3: string anamnesisTypeCode;
     4: string anamnesisTypeName;
     5: string anamnesisName;
     6: string memo;
     7: i64 anamnesisDate;
}

//遗传病史
struct YTJ_PhrHeredopathiaBean {
     1: string id;
     2: string personPhrCode;
     3: string diseaseCode;
     4: string diseaseName;
}

//过敏史
struct YTJ_AllergiesRecordBean {
    1: string allergiesId;
    2: string personPhrCode;
    3: string allergiesCode;
    4: string allergiesName;
    5: string allergiesSymptom;
    6: string allergiesCause;
    7: i64 foundDate;
    8: i64 cureDate;
    9: string notes;
    10: string enabledCode;
    11: string enabledName;
    12: string doctorName;
    13: string sourceTypeCode;
    14: string sourceTypeName;
    15: string orgCode;
    16: string orgName;
    17: string optId;
    18: string optName;
    19: i64 optTime;
    20: string alleriesCategoryCode;
    21: string alleriesCategoryName;
    22: string prognosisCode;
    23: string prognosisName;
    24: string relatedDisease;
}

//用药历史
struct YTJ_MedicationRecordHistoryBean {
	1: string id;
	2: string personPhrCode;
	3: string medicineCode;
	4: string medicineName;
	5: string functionTypeCode;
	6: string funcationTypeName;
	7: string medicineFormulationCode;
	8: string medicineFormulationName;
	9: string medicineRates;
	10: string dosageUnits;
	11: double dose;
	12: double totalDose;
	13: string useMethodCode;
	14: i64 medicineBeginDate;
	15: i64 medicineStopDate;
	16: string doctorName;
	17: string notes;
	18: string sourceTypeCode;
	19: string sourceTypeName;
	20: string orgCode;
	21: string orgName;
	22: string optId;
	23: string optName;
	24: i64 optTime;
	25: string useComplianceName;
	26: string useComplianceCode;
	27: string useMethodName;
}

//个人健康档案信息
struct YTJ_MemberHealthInfo {
    1: string  userId;               // 用户ID
    2: string  nickName;             // 昵称
    3: string  cardID;               // 身份标识卡ID
    4: string  birthday;             // 出生日期（MM-dd-YYYY）
    5: i32     sex;                  // 性别
    6: string  mobileNum;            // 手机号
    7: string  bloodCode;	     // 血型
    8: string  maritalStatus;	     // 婚姻状况
    9: list<YTJ_FamilyDiseaseHistory>  familyDiseaseHistoryList;   //家族病史
    10: YTJ_DiseaseHistory diseaseHistory;	//既往病史
    11: list<YTJ_Anamnesis>  anamnesisInfoList;	//手术史
    12: YTJ_MedicationRecordHistoryBean  medicationRecordHistory;  //用药史
    13: YTJ_PhrLifestyle   phrLifestyle;  	//生活方式
    14: double height;			//身高
    15: double weight;			//体重
    16: list<YTJ_AllergiesRecordBean> AllergiesRecordList;	//过敏史
    17: list<YTJ_PhrHeredopathiaBean>  phrHeredopathiaList;	//遗传病史
}

// 服务卡信息
struct ServiceCardInfo {
    1: string  cardNo;          // 卡号
    2: string  beginTime;       // 开始时间
    3: string  endTime;         // 结束时间
    4: string  status;			// 状态
	5: i32 haveDays;   //剩余天数
}

// 服务卡 登陆返回实体
struct ServiceCardResult{
		1:  AccountInfo accountInfo; //用户信息
		2:  ServiceCardInfo serviceCardInfo; //服务卡信息
		3:  i32 userPoints;//服务评价
		4:  AccountInfo hostAccountInfo; //户主用户信息
}

// 信任关系信息，客户端用于获取被信任用户的相关信息定义
struct MemberInfo{
    1: string  userId;               // 用户ID（Friend ID）
    2: string  nickName;             // 昵称
    3: binary  healdPortrait;        // 用户头像
    4: string  cardID;               // 身份标识卡ID
    5: string  birthday;             // 出生日期（MM-dd-YYYY）
    6: i32     sex;                  // 性别
    7: string  email;                // 电子邮箱
    8: string  mobileNum;            // 手机号
    9: string  watchId;               // 腕表ID
    10: i32    isEnable;             // 账号是否启用
    11: string userSelfId;           // 用户ID（登录用户自己的身份标识）
    12: i32    isAgree;              // 是否允许建立友元关系
    13: string  registDatetime;
    14: string  loginDatetime;
     15: string password;
	 16: string headPictureUrl;                 //用户头像url路径。

}

// 家庭顾问信息结构定义
struct CaregiverInfo {
    1: string  employeeCode;				 // 顾问编码
		2: string  employeeName;				 // 姓名
		3: string  birthday;             // 出生日期
		4: i32     genderCode;					 // 性别代码
		5: string  genderName;					 // 性别
		6: string  nationCode;					 // 民族代码
		7: string  nationName;					 // 民族
		8: string  photoCode;						 // 照片
		9: string  phoneNum;						 // 电话
		10: string mobileNum;						 // 手机号码
		11: string emailNum;						 // 电子邮件
		12: string addrDetail;					 // 联系地址
		13: string postalNum;						 // 邮政编码
		14: string titleCode;						 // 职称代码
		15: string titleName;						 // 职称名称
		16: string graduateSchool;			 // 毕业院校
		17: i32    educationalDegree;    // 学历代码                                                            
		18: string educationalDegreeName;// 学历名称                                                            
		19: i32    maritalStatusCode;		 // 婚姻情况代码                                                          
		20: string maritalStatusName;		 // 婚姻情况名称                                                          
		21: i32    addrCantonalCode;		 // 出生地址：省/直辖市/市/地区/县/区/乡/镇/街道办事处/村/街/路编码                           
		22: string addrCantonalName;		 // 省/直辖市/市/地区/县/区/乡/镇/街道办事处/村/街/路名称                                
		23: i32    proofCode;						 // 证件类型编码                                                          
		24: string proofName;						 // 证件类型名称                                                          
		25: string proofNum;						 // 证件号                                                             
		26: string resume;							 // 简历                                                              
		27: string linkmanName;					 // 紧急联系人
		28: string linkmanPhoneNum;			 // 紧急联系人电话
		29: string preservation;				 // 保留字段
		30: string preservation1;				 // 保留字段
		31: string preservation2;				 // 保留字段
		32: string preservation3;				 // 保留字段
		33: string preservation4				 // 保留字段
		34: binary headPortrait;        // 用户头像
		35: string headPictureUrl;                 //用户头像url路径。
}

struct FamilyInfo {
		1:  string familyId;
		2:  string familyName;
}

struct MemberDoctorRelation {
		1:  string userId; //用户ID
		2:  list<CaregiverInfo> doctors;
}

struct RecipeInfo {
		1:  string setUserId; //设置人用户ID
		2:  string toUserId; //被设置人用户ID
		3:  list<string> times; //设置提醒时间
		4:  string content;    //设置提醒内容
		5:  string crequency;   //提醒频次
		6:  string setPersonName;  //设置人姓名
		7:  string toPersonName;   //被设置人姓名
		8:  string id;           //主键
		9:  string updatetime;    //更新时间
		10: i32 isdel;     //是否删除0 未删除 1 删除
		11: string msg_type;     //1： 文字消息 2：语音消息
		12: string video_url;     //语音消息存储路径
		13: string video_name;     //语音文件名字
		14: string video_length;     //语音文件时长
		15: string startday;     //提醒开始时间，目前单次提醒有效
		
}

struct PhotoInfo {
		1:  string sharePerson; //分享人
		2:  string photourl; //图片路径
		3:  string sharetime; //图片分享时间
		
}

struct MessageInfo {
		1:  string fromPerson; //分享人
		2:  string toPerson; //图片路径
		3:  string messageTime; //图片分享时间
		4:  string messageType; //1 视频不在线通知
		5: string messageContent;
		6: string serviceid; //服务ID
		7: string deviceid; // 设备ID
			
}

struct OutsideInfo {
		1:  string macAddress; //分享人
		2:  string type; //图片路径
		3:  string id;   //数据库id
			
}


struct ServicesInfo {
		1:  string id; //服务ID
		2:  string service_name; //服务名称
		3:  string service_desc;   //服务描述
		4:  string service_type;  //服务类型
		5: string start_service_num; //服务开通电话
		6: string price; //价格
		7: string pattern; // 周期
		8: string yitiji_desc_url; // 服务介绍的url信息		
		9: string service_connect_way; // 联系方式 1.视频 2. 语音 3.电话 4.留言 可多选，逗号分割
		10: string service_connect_tel; // 联系方式为电话时，需拨打的电话
		11: binary banner_yitiji; // 服务的图片 old
		12: string banner_yitiji_not_open; // 服务未开通时益体机显示图片路径
		13: string banner_yitiji_button_color; // 服务的图片周围button颜色
		14: string banner_yitiji_open; //服务的图片 
		15: string preservation;//保留字段
		16: string preservation1; //保留字段
		17: i32 allowManyDoctor; //是否是一服务多个医生 0 一对一服务 1 一对多服务
		18: i32 service_sort;//排序
				
}

struct UsingServices {
		1:  string serviceId; //服务ID
		2:  string service_name; //服务名称
		3:  string familyId;   //家庭ID
		4:  CaregiverInfo caregiver;  //服务医生
		5: string total_price; //总价
		6: string period; // 周期
        7: string startTime;
        8: string endTime; 	
		9: string preservation;//保留字段
		10: string preservation1; //保留字段
		11: string state; 	//服务状态
				
}

struct PurchasedServices {
		1:  string serviceId; //服务ID
		2:  string service_name; //服务名称
		3:  string familyId;   //家庭ID
		4:  list<CaregiverInfo> caregiver;  //服务医生列表
		5: string total_price; //总价
		6: string period; // 周期
        7: string startTime;
        8: string endTime; 	
		9: string preservation;//保留字段
		10: string preservation1; //保留字段
		11: string state; 	//服务状态、
		12:i32 service_sort;//排序
				
}

struct ServiceRecord {
		1:  string familyId; //家庭ID
		2:  string member_code; //服务会员phrcode
		3:  string caregiver_code;   //顾问phrcode
		4:  string start_time;  //服务开始时间
		5: string end_time; //服务结束时间
		6: string total_time; // 服务时长
        7: string service_type; //服务方式
        8: string content; 	//服务内容
		9: i32 user_estimate;//服务评价
		10: string serviceId; //服务ID
		11: string recordId; //服务记录ID
		12: string requirement; //用户诉求
		13: string member_name; //服务会员名字
		14: string caregiver_name; //医生名字
				
}

struct PointRecords {
		1:  string familyId; //家庭ID
		2:  string operate; //获取积分的操作
		3:  string points;   //获得的积分
		4:  i32 types;  //1:加分 2：减分（兑换）
		5:  string from_person; //获取积分的成员
		6:  string person_name; // 成员姓名
		7:  string time; // 获取积分的时间
        8: i32 id; //记录ID 
				
}

struct HealthReport {
		1:  i32 id; //记录ID
		2:  string userId; //用户ID
		3:  string report_title;   //报告名称
		4:  i32 report_type;  //报告类型
		5:  string reporter; //报告人
		6:  string time; // 报告时间
        7:  string report_url; //报告详情路径				
}


struct MessageDetail {
		1:  i32 id; //消息ID
		2:  string msg_type; //消息类型
		3:  string msg_summary;   //标题
		4:  string msg_content;  //消息内容
		5:  string to_person; // 消息接收人ID
        6:  string from_person; //消息发送人ID
        7: 	string to_person_name; //消息接收人姓名
        8:  string from_person_name; //消息发送人姓名	
}

struct HealthControllerPlan {
		1:  i32 id; //消息ID
		2:  string code; //方案唯一标示
		3:  string starttime;   //方案开始时间
		4:  string endtime;  //方案结束时间
		5:  string doctorPhrcode; // 医生ID
        6:  string doctorName; //医生姓名
        7: 	string status; //状态 Yes 正在进行 NO 失效
        8:  string plan_url; //方案详情URL	
}



struct HealthControllerRemind {
		1:  string plancode;   //计划编码
		2:  string schemecode;  //方案编码
		3:  string content; // 计划内容
        4:  string crequeny; //计划频率
        5: 	string exe_time; //执行时间
        6:  string plantype; //计划类型
		7:  string userid; //计划执行人
		8:  string username; //计划执行人姓名
		9:  string doctorid; //医生ID
		10: string doctorname; //医生姓名
}

struct InterfaceLog {
	1: string phrCode;	//会员编码
	2: string ip;	//ip地址
	3: string mac;	//mac地址
	4: string interfaceName;	//接口名称
	5: string lng;	//纬度
	6: string lat;		//经度
	7: string orgId;	//组织机构ID
}

struct PeripheralConfigure{
	1: i32 id;//主键
	2: string peripheralId;//外设id
	3: string peripheralName;//外设名称
	4: string bluetoothId;//蓝牙特征值
	5: string bluetoothName;//蓝牙名称
	6: string peripheralPic;//设备图片
	7: string guidePic;//引导图
	8: string instructionPic;//说明图
	9: string isUse;//0:使用 1:停用
}
service UserService {
    
    //用户登录，客户端需要提供登录用户的账号和密码
    //异常信息：Err0001：登录账号不存在
    //          Err0002：登录密码错误
    //家庭益体机登录除正常验证用户名密码外，区分以下四种情况：
    //1.该用户不属于任何家庭，则创建新家庭F，将此用户加入新家庭F，将益体机绑定此新家庭F，设置loginStatus为0
    //2.该用户属于一个家庭F，且益体机未绑定任何家庭，则将益体机绑定此家庭F，设置loginStatus为0
    //3.该用户属于一个家庭F，且益体机已绑定此家庭F，则无需任何操作，设置loginStatus为0
    //4.该用户属于多个家庭F1、F2、F3，且益体机未绑定任何家庭，设置loginStatus为2，后续需要用户手动选择一个家庭F1或F2或F3与益体机进行绑定，设置loginStatus为2
    //5.该用户属于家庭F1，益体机绑定家庭F2?柚胠oginStatus为1，无论如何也无法登录
    AccountInfo login(1: AccountInfo accountInfo) throws (1: XKCommon.HealthServiceException ex);
    
    //添加新用户,输入长度检查在客户端完成
    //异常信息：Err0003：注册账号重复
    //          Err0014：口令强度不足
    //          Err0007：注册失败#？#
    //          Err0015: 账号格式不正确
    //          Err0004：数据库连接失败
	
	AccountInfo findXKAccountByProofNum(1: string proofNum) throws (1: XKCommon.HealthServiceException ex);
	bool checkBindstate(1: string deviceId, 2: string userId) throws (1: XKCommon.HealthServiceException ex);
	
    AccountInfo registerAccount(1: AccountInfo accountInfo, 2: string deviceId, 3: string verifyCode) throws (1: XKCommon.HealthServiceException ex);

		AccountInfo registerAndBindAccount(1: AccountInfo accountInfo, 2: string deviceId, 3: string verifyCode) throws (1: XKCommon.HealthServiceException ex);
		
    //修改账号信息，账号、密码不能使用该方法来修改
    //异常信息：Err0016：账号信息不能为NULL
    //          Err0004：数据库连接失败
    //          Err0019: 登录过期，请重新登录
    //          Err0020：指定的用户不是当前登录的用户
    AccountInfo updateAccount(1: AccountInfo accountInfo) throws (1: XKCommon.HealthServiceException ex);
    
    //修改登录口令
    //userId: 指定要修改口令的账号
    //oldPassword: 原口令
    //newPassword: 新口令
    //异常信息：Err0017: 原口令错误
    //          Err0014：口令强度不足
    //          Err0004：数据库连接失败
    //          Err0019: 登录过期，请重新登录
    //          Err0020：指定的用户不是当前登录的用户
    void editPassword(1: string userId, 2: string oldPassword, 3: string newPassword) throws (1: XKCommon.HealthServiceException ex);

    //获取信任组成员信息列表
    //userId: 当前登录用户的用户ID
    //异常信息：Err0001：账号不存在
    //          Err0004：数据库连接失败
    //          Err0019: 登录过期，请重新登录
    //          Err0020：指定的用户不是当前登录的用户
    //返回结果：NULL或组成员信息列表
    list<MemberInfo> getMembers(1: string userId) throws (1: XKCommon.HealthServiceException ex);

    //查询账号信息
    //userId: 要查询的账号Id，支持模糊查询，同时查询账号、邮箱、手机号字段
    //nickName:用户账号的昵称，与userId是逻辑或关系，支持模糊查询
    //异常信息：Err0022：未找您要查询的账号
    //          Err0004：数据库连接失败
    //          Err0019: 登录过期，请重新登录
    //返回结果：NULL或查询结果列表

    void addMember(1: string userId, 2: string password, 3: string loginUserId) throws (1: XKCommon.HealthServiceException ex);
    
    //删除信任组成员，本操作只删除组成员信息，并删除登录信息
    //userIds:指定要删除的组成员用户Id（可同时删除多个）
    //userId: 指定当前登录的用户Id
    //异常信息：Err0018：成员账号：#？#不存在
    //          Err0004：数据库连接失败
    //          Err0019: 登录过期，请重新登录
    //          Err0020：指定的用户不是当前登录的用户
    list<MemberInfo> deleteMembers(1: list<string> userIds, 2: string loginUserId) throws (1: XKCommon.HealthServiceException ex);

		//根据userid获取家庭顾问详细信息
    //返回值：家庭顾问详细信息
    //userId: 指定当前登录用户
    //异常信息：Err0019: 登录过期，请重新登录
    //          Err0001：#？#账号不存在
    //          Err0004：数据库连接失败
    //          Err0021：指标代码#？#不存在
    list<CaregiverInfo> getCaregiverInfoService(1: string userId, 2: string deviceId) throws(1: XKCommon.HealthServiceException ex);
    
    void bindDeviceByUserName(1: string userName, 2: string password, 3: string deviceId) throws (1: XKCommon.HealthServiceException ex);
    
    void bindDeviceByUserId(1: string userId, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);
    
    list<AccountInfo> getAccountInfosByDeviceId(1: string deviceId) throws (1: XKCommon.HealthServiceException ex);
    
    list<AccountInfo> deleteAccountsByDeviceId(1: list<string> userIds, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);

		list<FamilyInfo> getFamilyInfosByUserId(1: string userId) throws (1: XKCommon.HealthServiceException ex);
		
		string getVerifyCodeByDeviceId(1: string deviceId) throws (1: XKCommon.HealthServiceException ex);
		
		void sendSmsVerifyCode(1: string phoneNum, 2: string verifyCode, 3: string deviceId) throws (1: XKCommon.HealthServiceException ex);
		
		void validateSmsVerifyCode(1: string phoneNum, 2: string smsVerifyCode, 3: string deviceId) throws (1: XKCommon.HealthServiceException ex);
		
		void resetPassword(1: string phoneNum, 2: string newPassword, 3: string smsVerifyCode, 4: string deviceId) throws (1: XKCommon.HealthServiceException ex);

		void bindDeviceByFamilyId(1: string familyId, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);
		
		void unBindDeviceByFamilyId(1: string familyId, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);
		
		//新加接口，获取当前用户的医生列表。
		 list<CaregiverInfo> getDoctorInfoService(1: string userId, 2: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //新加接口，获取家庭成员的医生列表。
		 list<MemberDoctorRelation> getDoctorInfoByDeviceID(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //新加接口，获取某人的处方列表。
		 list<RecipeInfo> getRecipeListByUserID(1: string userId, 2: string startTime) throws(1: XKCommon.HealthServiceException ex);
		 
		 //新加接口，获取某个设备的处方列表。
		 list<RecipeInfo> getRecipeListByDeviceID(1: string deviceId, 2: string startTime) throws(1: XKCommon.HealthServiceException ex);
		 
		 //新加接口，按时间段获取家庭照片列表。
		 list<PhotoInfo> getphotoBydeviceID(1: string deviceId, 2: string shareTime) throws(1: XKCommon.HealthServiceException ex);
		 
		 list<binary> getphotoInfoByurl(1: list<string> photourls) throws(1: XKCommon.HealthServiceException ex);

                   //根据患者或者医生的phrcode获取姓名
                 string getUserNameByUserID(1: string userId) throws(1: XKCommon.HealthServiceException ex);
		
		 
		  //新加接口，设备是否绑定到家庭，绑定时返回家庭信息。
		 FamilyInfo checkBindStateByDeviceID(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 //视频不在线通知。
		 void messageNotify(1: MessageInfo msgInfo) throws(1: XKCommon.HealthServiceException ex);

                 //获取外设接口。
		 list<OutsideInfo> getOutsideListByDeviceId(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 //获取外设接口。
		 string hostlogin(1: string deviceId, 2:string hostid) throws(1: XKCommon.HealthServiceException ex);
		 
		 //获取全部服务接口。
		 list<ServicesInfo> getAllServices(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //获取已购买的服务接口。
		 list<UsingServices> getUsingServices(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 string addOutside(1: string deviceId, 2:OutsideInfo info) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //获取服务记录。
		 list<ServiceRecord> getServiceRecords(1: string deviceId, 2:string ServiceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //获取服务购买历史接口。
		 list<UsingServices> getServiceHistory(1: string deviceId,2:string serviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 //获取家庭积分接口。
		 i32 getFamilyPoints(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		  
		 //获取积分列表接口。
		 list<PointRecords> getPointsHistory(1: string deviceId,2:i32 num) throws(1: XKCommon.HealthServiceException ex);
		 		 
		 //修改服务评价 1:满意 2：一般 3：差
		 i32 updateServiceRecords(1: i32 recordId, 2:i32 result) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //获取个人月报/周报接口 1： 周报 2： 月报
		 list<HealthReport> getHealthReportLists(1: string userid, 2:i32 type,3: i32 startindex,4:i32 endindex) throws(1: XKCommon.HealthServiceException ex);
		 
		 //根据家庭id 获取个人月报/周报接口 1： 周报 2： 月报
		 list<HealthReport> getHealthReportListsByFamilyId(1: string userid, 2:i32 type,3: i32 startindex,4:i32 endindex,5:string familyId) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //新加接口，获取某人的处方列表。
		 list<RecipeInfo> getNewRecipeListByUserID(1: string userId, 2: string startTime, 3: string endTime) throws(1: XKCommon.HealthServiceException ex);
		 
		 //新加接口，获取某个设备的处方列表。
		 list<RecipeInfo> getNewRecipeListByDeviceID(1: string deviceId, 2: string startTime, 3: string endTime) throws(1: XKCommon.HealthServiceException ex);
		 
		 //新加接口，按时间段获取家庭照片列表。
		 list<PhotoInfo> getNewphotoBydeviceID(1: string deviceId, 2: string starTime,3: string endtime) throws(1: XKCommon.HealthServiceException ex);
		 
		//服务卡先关接口
		//获取个人积分接口
		i32 serviceCardGetUserPoints(1: string userId) throws(1: XKCommon.HealthServiceException ex);

		//获取个人积分列表接口。
		list<PointRecords> serviceCardGetPointsHistory(1: string userId,2:i32 num) throws(1: XKCommon.HealthServiceException ex);

		//按卡号登陆
		ServiceCardResult serviceCardLoginByCardNum(1: AccountInfo accountInfo,2: string cardNo) throws (1: XKCommon.HealthServiceException ex);
			
		//按账户登陆
		ServiceCardResult serviceCardLoginByAccount(1: AccountInfo accountInfo) throws (1: XKCommon.HealthServiceException ex);
		
		
		//绑定熙康关爱卡到指定的人员
		ServiceCardResult BindCardToPerson(1: string deviceid,2: string cardNo,3:string pwd,4:string userid) throws (1: XKCommon.HealthServiceException ex);
		
		//获取已购买的服务接口。
		 list<PurchasedServices> getPurchasedServices(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
			
         //根据消息ID获取推送消息详情接口。
		 MessageDetail getPushMessage(1: string msgid) throws(1: XKCommon.HealthServiceException ex);

        //获取方案列表
		 list<HealthControllerPlan> getHealthControllerPlan(1: string userid) throws(1: XKCommon.HealthServiceException ex);
		 
		 //按人获取健康方案执行计划列表
		 list<HealthControllerRemind> getHealthControllerRemindByMember(1: string userid) throws(1: XKCommon.HealthServiceException ex);
		 
		 //按设备获取健康方案执行计划列表
		 list<HealthControllerRemind> getHealthControllerRemindByDeviceId(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
		 //按设备获取健康方案执行计划列表
		 list<HealthControllerRemind> getHealthControllerRemindByDevice(1: string deviceid) throws(1: XKCommon.HealthServiceException ex);
		 
		 
		 //创建家庭发消息通知运维接口
		void sendMessageToManager(1: AccountInfo accountInfo,2: string deviceid) throws (1: XKCommon.HealthServiceException ex);
		
		
		//按身份证登录接口
		ServiceCardResult serviceLoginByProofNum(1: string proofNum,2:string deviceid) throws (1: XKCommon.HealthServiceException ex);
		
		//获取可呼叫的医生接口
		string getCallDoctor(1:string serviceid);
		
		//埋点接口
		void saveInterfaceLog(1:InterfaceLog interfaceLog);

		//获取设备集合
		list<PeripheralConfigure> getPeripheralConfigureList();
		
		//获取健康档案信息
		YTJ_MemberHealthInfo getMemberHealthInfo(1:string personPHRCode);
		
		//更新健康档案信息
		void updateMemeberHealthInfo(1:string personPHRCode,2:YTJ_MemberHealthInfo healthInfo);
				
}
