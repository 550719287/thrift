# ������������ʻ�Thrift
# �û���¼�ӿڶ���
# v0.1
# Copyright @ 2013 Neusoft Xikang Healthcare Technology Co.,Ltd
# li.yc@neusoft.com
# 2013/10/25
###############################################################

include "XKCommon.thrift"



// �û��˺���Ϣ���ͻ��˵�¼��ע�����û����༭�û���Ϣʱ�Ǹýṹ����
struct AccountInfo {
    1: string  userId;               // �û�ID
    2: string  password;             // ��¼����
    3: string  nickName;             // �ǳ�
    4: string  fullName;			 // ȫ��
    5: string  registDatetime;       // ע��ʱ�䣨MM-dd-YYYY����ע�ᴦ��ʱ���ͻ��˲���Ҫ���ø�����ֵ
    6: string  loginDatetime;        // �û���¼ʱ�䣨MM-dd-YYYY�����ͻ��˲���Ҫ���ø�ʱ�䣬�û���¼�ɹ�����Service����
    7: binary  headPortrait;         // �û�ͷ��
    8: string  cardID;               // ��ݱ�ʶ��ID
    9: string  birthday;             // �������ڣ�MM-dd-YYYY��
    10: i32     sex;                 // �Ա�
    11: string email;                // ��������
    12: string mobileNum;            // �ֻ���
    13: string watchId;              // ���ID
    14: i32    isEnable              // �˺��Ƿ�����
    15:	string deviceId;			 // �����ΨһID
    16: i32		 loginStatus;		 // ��¼״̬��ʶ
    17: string accountName;			 // ��¼ʱ�˻���
	18: string proofNum;             //���֤����
	19: string addrDetail;			 // ��ϵ��ַ
	20: string login_token;          //��¼��������token��Ϣ   
	21: string isHost;               //�Ƿ�Ϊ����1�������� 0���ǻ���
    22: string role;                 //��Ա��ɫ 1��ʹ���ߣ� 2�������� 3������
	23: string usersig;              //��Ѷ��Ƶ��Ȩ�õ�sig��Ŀǰ����ʹ�á�
	24: string headPictureUrl;       //�û�ͷ��url·����
	
}

// �û��˺���Ϣ���ͻ��˵�¼��ע�����û����༭�û���Ϣʱ�Ǹýṹ����
struct AccountInfo_new {
    1: string  userId;               // �û�ID
    2: string  password;             // ��¼����
    3: string  nickName;             // �ǳ�
    4: string  fullName;			 // ȫ��
    5: string  registDatetime;       // ע��ʱ�䣨MM-dd-YYYY����ע�ᴦ��ʱ���ͻ��˲���Ҫ���ø�����ֵ
    6: string  loginDatetime;        // �û���¼ʱ�䣨MM-dd-YYYY�����ͻ��˲���Ҫ���ø�ʱ�䣬�û���¼�ɹ�����Service����
    7: binary  headPortrait;         // �û�ͷ��
    8: string  cardID;               // ��ݱ�ʶ��ID
    9: string  birthday;             // �������ڣ�MM-dd-YYYY��
    10: i32     sex;                 // �Ա�
    11: string email;                // ��������
    12: string mobileNum;            // �ֻ���
    13: string watchId;              // ���ID
    14: i32    isEnable              // �˺��Ƿ�����
    15:	string deviceId;			 // �����ΨһID
    16: i32		 loginStatus;		 // ��¼״̬��ʶ
    17: string accountName;		     // ��¼ʱ�˻���
	18: string proofNum;             //���֤����
	19: string addrDetail;			 // ��ϵ��ַ:
	20: string login_token;          //��¼��������token��Ϣ   
	21: string isHost;               //�Ƿ�Ϊ����1�������� 0���ǻ���
    22: string role;                 //��Ա��ɫ 1��ʹ���ߣ� 2�������� 3������
	23: string usersig;              //��Ѷ��Ƶ��Ȩ�õ�sig��Ŀǰ����ʹ�á�
	24: string headPictureUrl;       //�û�ͷ��url·����
	25: double height;               //�û�ͷ��url·����
}

//����ʷ����
struct PhrHealthClinic{
    1: string id;                    //��������
    2: string personPhrCode;         //���˽���������ʶ��
    3: string diseaseCode;           //��������
    4: string diseaseName;           //��������
    5: string icd10Code;             //��������
    6: i64 onsetDate;                //�������ڣ�����1970��1��1�տ�ʼ�����ĺ�����
    7: i64 examineDate;              //ȷ�����ڣ�����1970��1��1�տ�ʼ�����ĺ�����
    8: string orgName;               //��������
    9: string doctorName;            //���ҽʦ����
    10: string illnessLayerCode;     //�����ּ�Code
    11: string illnessLayerName;     //�����ּ�Name
    12: string complicationNameStr;  //����֢Name������ԡ�&������
    13: string complicationCodeStr;  //����֢Code������ԡ�&������
    14: string memo;                 //��ע
    15: string prognosisCode;        //Ԥ��״̬��
    16: string prognosisName;        //Ԥ��״̬����
    17: i64 recoveryDate;            //�ָ����ڣ�����1970��1��1�տ�ʼ�����ĺ�����
    18: i64 optTime;                 //����ʱ�䣬����1970��1��1�տ�ʼ�����ĺ�����
}

//�����������ʷ
struct YTJ_DiseaseHistory{
    1: string healthCode;            //��������
    2: list<PhrHealthClinic> phrDiseaseList;//��������
}


//���岡ʷ
struct YTJ_FamilyDiseaseHistory{
     1: string id;                  //��������
     2: string personPhrCode;	    //���˽���������ʶ��
     3: string relativeCode;		//��ر���
     4: string relativeName;		//�������
     5: string diseaseCode;			//��������
     6: string diseaseName;			//��������
}

//����ʷ
struct YTJ_HealthClinicBean{
     1: string id;					//��������
     2: string personPhrCode;		//���˽���������ʶ��
     3: string diseaseCode;			//��������
     4: string diseaseName;			//��������
     5: string icd10Code;			//��������
     6: i64 onsetTime;				//�������ڣ�����1970��1��1�տ�ʼ�����ĺ�����
     7: i64 examineTime;			//ȷ�����ڣ�����1970��1��1�տ�ʼ�����ĺ�����
     8: string orgName;				//��������
     9: string doctorName;			//���ҽʦ����
     10: string illnessLayerCode;	//�����ּ�Code
     11: string illnessLayerName;	//�����ּ�Name
     12: string memo;				//��ע
}

//����
struct YTJ_PhrRiskFactorsBean{
	1: string id;							//����
	2: string personPhrCode;				//���˽���������ʶ��
	3: string riskFactorsFactorCode;		//�������ش���
	4: string riskFactorsFactorName;		//������������
	5: string riskFactorsName;				//��������
	6: string riskFactorsJob;				//����ְҵ
	7: i32 riskFactorsLength;				//���ճ̶�
}

//�û����ʽ
struct YTJ_PhrLifestyle{
    1: string personPhrCode;				//���˽���������ʶ��
    2: string smokingStateCode;				//����״������
    3: string smokingStateName;				//����״������
    4: string smokingRateCode;				//����Ƶ�ʱ���
    5: string smokingRateName;				//����Ƶ������
    6: i32 smokingBeginAge;					//��ʼ���̵�����
    7: string tobaccoTypeCode;				//��ʳ�̲��������
    8: string tobaccoTypeName;				//��ʳ�̲���������
    9: i32 onSmoking;						//��������
    10: i32 smokingEndAge;					//ֹͣ���̵�����
    11: string drinkingRateCode;			//����Ƶ�ʱ���
    12: string drinkingRateName;			//����Ƶ������
    13: string drinkingTypeCode;			//�����������
    14: string drinkingTypeName;			//������������
    15: i32 drinkingQuantity;				//��������(��)
    16: i32 drinkingStartAge;				//��ʼ��������(��)
    17: string drunkFlag;					//��һ����Ʊ�־
    18: string alcoholFlag;					//��Ʊ�־
    19: i32 alcoholAge;						//�������(��)
    20: string sportsingRateCode;			//����Ƶ�ʱ���
    21: string sportsingRateName;			//����Ƶ������
    22: i32 sportsingTime;					//ÿ�����ٶ���ʱ��
    23: i32 sportsingYear;					//��ֶ���ʱ��
    24: string sportsingType;				//�ճ��˶���ʽ
    25: string dietingHabitCode;			//��ʳϰ�ߴ���
    26: string dietingHabitName;			//��ʳϰ������
    27: string dietingSaltCode;				//����������
    28: string dietingSaltName;				//����������
    29: string dietingOilCode;				//����������
    30: string dietingOilName;				//����������
    31: string dietingSugarCode;			//����������
    32: string dietingSugarName;			//����������
    33: string exposeFlag;					//ְҵ��¶��־
    34: i64 optTime;						//����ʱ��
    35: list<YTJ_PhrRiskFactorsBean> riskFactorsList;//ְҵ��¶��Ϣ��
    36: i32 sportsingNumber;				//ÿ�������˶�����
    37: i64 smokingStartTime;				//��ʼ����ʱ��
    38: i64 smokingEndTime;					//����ʱ��
    39: i64 abstinenceTime;					//���ʱ��	
    40: string drinkingKind;				//��������
}

//������Ϣ
struct YTJ_Anamnesis {
     1: string id;							//����
     2: string personPhrCode;				//��Ա����������ʶ��
     3: string anamnesisTypeCode;			//���ͱ���
     4: string anamnesisTypeName;			//��������
     5: string anamnesisName;				//��������
     6: string memo;						//��ע
     7: i64 anamnesisDate;					//��ʱ��¼��ʱ��
}

//�Ŵ���ʷ
struct YTJ_PhrHeredopathiaBean {
     1: string id;							//����
     2: string personPhrCode;				//���˽���������ʶ��
     3: string diseaseCode;					//�Ŵ�������
     4: string diseaseName;					//�Ŵ�������
}

//����ʷ
struct YTJ_AllergiesRecordBean {
    1: string allergiesId;					//����
    2: string personPhrCode;				//���˽���������ʶ��
    3: string allergiesCode;				//��������
    4: string allergiesName;				//��������
    5: string allergiesSymptom;				//����֢״
    6: string allergiesCause;				//����Դ
    7: i64 foundDate;						//��������
    8: i64 cureDate;						//��������
    9: string notes;						//��ע
    10: string enabledCode;					//�Ƿ�����
    11: string enabledName;					//�Ƿ���������
    12: string doctorName;					//����ҽʦ���� 
    13: string sourceTypeCode;				//��¼��Դ��ʽ 0:�ֹ����ݣ�1:ҽԺ���ݣ�2:�����ɼ����ݣ�3:�����ֹ�����
    14: string sourceTypeName;				//��¼��Դ��ʽ 0:�ֹ����ݣ�1:ҽԺ���ݣ�2:�����ɼ����ݣ�3:�����ֹ�����
    15: string orgCode;						//��������
    16: string orgName;						//ҽԺ(����)���� 
    17: string optId;						//�����˱���
    18: string optName;						//������
    19: i64 optTime;						//����ʱ��
    20: string alleriesCategoryCode;		//���������
    21: string alleriesCategoryName;		//���������
    22: string prognosisCode;				//Ԥ��״̬��
    23: string prognosisName;				//Ԥ��״̬����
    24: string relatedDisease;				//��������
}

//��ҩ��ʷ
struct YTJ_MedicationRecordHistoryBean {
	1: string id;							//����
	2: string personPhrCode;				//���˽���������ʶ��
	3: string medicineCode;					//ҩƷ����
	4: string medicineName;					//ҩƷ����
	5: string functionTypeCode;				//�������ͱ���
	6: string funcationTypeName;			//������������
	7: string medicineFormulationCode;		//ҩ����ʹ���
	8: string medicineFormulationName;		//ҩ���������
	9: string medicineRates;				//ҩ��ʹ��Ƶ��
	10: string dosageUnits;					//ҩ��ʹ�ü�����λ
	11: double dose;						//ҩ��ʹ�ôμ�����������
	12: double totalDose;					//ҩ��ʹ���ܼ���
	13: string useMethodCode;				//ҩ��ʹ��;�����루�÷����룩
	14: i64 medicineBeginDate;				//��ҩ��ʼ����ʱ��
	15: i64 medicineStopDate;				//��ҩֹͣ����ʱ��
	16: string doctorName;					//ҽ������
	17: string notes;						//��ע
	18: string sourceTypeCode;				//��¼��Դ��ʽ 0:�ֹ����ݣ�1:ҽԺ���ݣ�2:�����ɼ����ݣ�3:�����ֹ�����	
	19: string sourceTypeName;				//��¼��Դ��ʽ 0:�ֹ����ݣ�1:ҽԺ���ݣ�2:�����ɼ����ݣ�3:�����ֹ�����
	20: string orgCode;						//��������
	21: string orgName;						//ҽԺ(����)����
	22: string optId;						//������id
	23: string optName;						//����������
	24: i64 optTime;						//����ʱ��
	25: string useComplianceName;			//��ҩ����������
	26: string useComplianceCode;			//��ҩ�����Դ���
	27: string useMethodName;				//ҩ��ʹ��;������
}

//���˽���������Ϣ
struct YTJ_MemberHealthInfo {
    1: string  userId;               // �û�ID
    2: string  nickName;             // �ǳ�
    3: string  cardID;               // ��ݱ�ʶ��ID
    4: string  birthday;             // �������ڣ�MM-dd-YYYY��
    5: i32     sex;                  // �Ա�
    6: string  mobileNum;            // �ֻ���
    7: string  bloodCode;	     	 // Ѫ��
    8: string  maritalStatus;	     // ����״��
    9: list<YTJ_FamilyDiseaseHistory>  familyDiseaseHistoryList;   //���岡ʷ
    10: YTJ_DiseaseHistory diseaseHistory;						   //������ʷ
    11: list<YTJ_Anamnesis>  anamnesisInfoList;				   	   //����ʷ
    12: YTJ_MedicationRecordHistoryBean  medicationRecordHistory;  //��ҩʷ
    13: YTJ_PhrLifestyle   phrLifestyle;  						   //���ʽ
    14: double height;			  //���
    15: double weight;			  //����
    16: list<YTJ_AllergiesRecordBean> AllergiesRecordList;		   //����ʷ
    17: list<YTJ_PhrHeredopathiaBean>  phrHeredopathiaList;	       //�Ŵ���ʷ
}

// ������Ϣ
struct ServiceCardInfo {
    1: string  cardNo;          // ����
    2: string  beginTime;       // ��ʼʱ��
    3: string  endTime;         // ����ʱ��
    4: string  status;			// ״̬
	5: i32 haveDays;   			//ʣ������
}

// ���� ��½����ʵ��
struct ServiceCardResult{
	1:  AccountInfo accountInfo; 				//�û���Ϣ
	2:  ServiceCardInfo serviceCardInfo; 		//������Ϣ
	3:  i32 userPoints;							//��������
	4:  AccountInfo hostAccountInfo; 			//�����û���Ϣ
}

// ���ι�ϵ��Ϣ���ͻ������ڻ�ȡ�������û��������Ϣ����
struct MemberInfo{
    1: string  userId;               // �û�ID��Friend ID��
    2: string  nickName;             // �ǳ�
    3: binary  healdPortrait;        // �û�ͷ��
    4: string  cardID;               // ��ݱ�ʶ��ID
    5: string  birthday;             // �������ڣ�MM-dd-YYYY��
    6: i32     sex;                  // �Ա�
    7: string  email;                // ��������
    8: string  mobileNum;            // �ֻ���
    9: string  watchId;              // ���ID
    10: i32    isEnable;             // �˺��Ƿ�����
    11: string userSelfId;           // �û�ID����¼�û��Լ�����ݱ�ʶ��
    12: i32    isAgree;              // �Ƿ���������Ԫ��ϵ
    13: string  registDatetime;      //ע��ʱ��
    14: string  loginDatetime;		 //��¼ʱ��
    15: string password;			 //����
	16: string headPictureUrl;       //�û�ͷ��url·����

}

// ��ͥ������Ϣ�ṹ����
struct CaregiverInfo {
    1: string  employeeCode;			// ���ʱ���
	2: string  employeeName;			// ����
	3: string  birthday;           	 	// ��������
	4: i32     genderCode;				// �Ա����
	5: string  genderName;				// �Ա�
	6: string  nationCode;				// �������
	7: string  nationName;				// ����
	8: string  photoCode;				// ��Ƭ
	9: string  phoneNum;				// �绰
	10: string mobileNum;				// �ֻ�����
	11: string emailNum;				// �����ʼ�
	12: string addrDetail;				// ��ϵ��ַ
	13: string postalNum;				// ��������
	14: string titleCode;				// ְ�ƴ���
	15: string titleName;				// ְ������
	16: string graduateSchool;			// ��ҵԺУ
	17: i32    educationalDegree;       // ѧ������                                                            
	18: string educationalDegreeName;   // ѧ������                                                            
	19: i32    maritalStatusCode;		// �����������                                                          
	20: string maritalStatusName;		// �����������                                                          
	21: i32    addrCantonalCode;		// ������ַ��ʡ/ֱϽ��/��/����/��/��/��/��/�ֵ����´�/��/��/·����                           
	22: string addrCantonalName;		// ʡ/ֱϽ��/��/����/��/��/��/��/�ֵ����´�/��/��/·����                                
	23: i32    proofCode;				// ֤�����ͱ���                                                          
	24: string proofName;				// ֤����������                                                          
	25: string proofNum;				// ֤����                                                             
	26: string resume;					// ����                                                              
	27: string linkmanName;				// ������ϵ��
	28: string linkmanPhoneNum;			// ������ϵ�˵绰
	29: string preservation;			// �����ֶ�
	30: string preservation1;			// �����ֶ�
	31: string preservation2;			// �����ֶ�
	32: string preservation3;			// �����ֶ�
	33: string preservation4			// �����ֶ�
	34: binary headPortrait;       		// �û�ͷ��
	35: string headPictureUrl;          //�û�ͷ��url·����
}

//��ͥ��Ϣ
struct FamilyInfo {
	1:  string familyId;			//��ͥ����			
	2:  string familyName;			//��ͥ����
}

//�û�ҽ��
struct MemberDoctorRelation {
	1:  string userId; 				//�û�ID
	2:  list<CaregiverInfo> doctors;//��ͥ������Ϣ�ṹ����
}

//����
struct RecipeInfo {
	1:  string setUserId;		 	//�������û�ID
	2:  string toUserId; 			//���������û�ID
	3:  list<string> times; 		//��������ʱ��
	4:  string content;    			//������������
	5:  string crequency;   		//����Ƶ��
	6:  string setPersonName;  		//����������
	7:  string toPersonName;   		//������������
	8:  string id;           		//����
	9:  string updatetime;    		//����ʱ��
	10: i32 isdel;     				//�Ƿ�ɾ��0 δɾ�� 1 ɾ��
	11: string msg_type;     		//1�� ������Ϣ 2��������Ϣ
	12: string video_url;     		//������Ϣ�洢·��
	13: string video_name;     		//�����ļ�����
	14: string video_length;     	//�����ļ�ʱ��
	15: string startday;     		//���ѿ�ʼʱ�䣬Ŀǰ����������Ч
		
}

//ͼƬ��Ϣ
struct PhotoInfo {
	1:  string sharePerson; 		//������
	2:  string photourl;			//ͼƬ·��
	3:  string sharetime; 			//ͼƬ����ʱ��
		
}

//��Ϣ��Ϣ
struct MessageInfo {
	1:  string fromPerson; 			//������
	2:  string toPerson; 			//ͼƬ·��
	3:  string messageTime; 		//ͼƬ����ʱ��
	4:  string messageType; 		//1 ��Ƶ������֪ͨ
	5: string messageContent;		//����
	6: string serviceid;			//����ID
	7: string deviceid;				// �豸ID
			
}

//����
struct OutsideInfo {
	1:  string macAddress;		//������
	2:  string type; 			//ͼƬ·��
	3:  string id;   			//���ݿ�id
			
}

//������Ϣ
struct ServicesInfo {
	1:  string id; 							//����ID
	2:  string service_name; 				//��������
	3:  string service_desc;    			//��������
	4:  string service_type;    			//��������
	5: string start_service_num; 			//����ͨ�绰
	6: string price; 						//�۸�
	7: string pattern; 						// ����
	8: string yitiji_desc_url; 				// ������ܵ�url��Ϣ		
	9: string service_connect_way;  		// ��ϵ��ʽ 1.��Ƶ 2. ���� 3.�绰 4.���� �ɶ�ѡ�����ŷָ�
	10: string service_connect_tel; 		// ��ϵ��ʽΪ�绰ʱ���貦��ĵ绰
	11: binary banner_yitiji; 				// �����ͼƬ old
	12: string banner_yitiji_not_open; 		// ����δ��ͨʱ�������ʾͼƬ·��
	13: string banner_yitiji_button_color;  // �����ͼƬ��Χbutton��ɫ
	14: string banner_yitiji_open; 			//�����ͼƬ 
	15: string preservation;				//�����ֶ�
	16: string preservation1;				//�����ֶ�
	17: i32 allowManyDoctor; 				//�Ƿ���һ������ҽ�� 0 һ��һ���� 1 һ�Զ����
	18: i32 service_sort;					//����
				
}

//����ʹ����Ϣ
struct UsingServices {
	1:  string serviceId; 			//����ID
	2:  string service_name; 		//��������
	3:  string familyId;  			//��ͥID
	4:  CaregiverInfo caregiver; 	//����ҽ��
	5: string total_price; 			//�ܼ�
	6: string period; 				// ����
    7: string startTime;			//��ʼʱ��
    8: string endTime; 				//����ʱ��
	9: string preservation;			//�����ֶ�
	10: string preservation1; 		//�����ֶ�
	11: string state; 				//����״̬
				
}

//������Ϣ
struct PurchasedServices {
	1:  string serviceId; 				//����ID
	2:  string service_name; 			//��������
	3:  string familyId;   				//��ͥID
	4:  list<CaregiverInfo> caregiver;  //����ҽ���б�
	5: string total_price;				//�ܼ�
	6: string period; 					// ����
    7: string startTime;				//��ʼʱ��
    8: string endTime; 					//����ʱ��
	9: string preservation;				//�����ֶ�
	10: string preservation1;			//�����ֶ�
	11: string state; 					//����״̬
	12:i32 service_sort;				//����
				
}

//�����¼
struct ServiceRecord {
	1:  string familyId; 				//��ͥID
	2:  string member_code; 			//�����Աphrcode
	3:  string caregiver_code;   		//����phrcode
	4:  string start_time;  			//����ʼʱ��
	5: string end_time; 				//�������ʱ��
	6: string total_time; 				//����ʱ��
    7: string service_type; 			//����ʽ
    8: string content; 					//��������
	9: i32 user_estimate;				//��������
	10: string serviceId; 				//����ID
	11: string recordId; 				//�����¼ID
	12: string requirement; 			//�û�����
	13: string member_name; 			//�����Ա����
	14: string caregiver_name; 			//ҽ������
				
}

//���ּ�¼
struct PointRecords {
	1:  string familyId; 		//��ͥID
	2:  string operate; 		//��ȡ���ֵĲ���
	3:  string points;   		//��õĻ���
	4:  i32 types;  			//1:�ӷ� 2�����֣��һ���
	5:  string from_person; 	//��ȡ���ֵĳ�Ա
	6:  string person_name; 	// ��Ա����
	7:  string time; 			// ��ȡ���ֵ�ʱ��
    8:  i32 id; 				//��¼ID 
				
}

//��������
struct HealthReport {
	1:  i32 id; 				//��¼ID
	2:  string userId; 			//�û�ID
	3:  string report_title;    //��������
	4:  i32 report_type;  		//��������
	5:  string reporter; 		//������
	6:  string time; 			// ����ʱ��
    7:  string report_url; 		//��������·��				
}

//��Ϣ����
struct MessageDetail {
	1:  i32 id; 				//��ϢID
	2:  string msg_type; 		//��Ϣ����
	3:  string msg_summary;   	//����
	4:  string msg_content;  	//��Ϣ����
	5:  string to_person; 		//��Ϣ������ID
    6:  string from_person; 	//��Ϣ������ID
    7: 	string to_person_name;  //��Ϣ����������
    8:  string from_person_name;//��Ϣ����������	
}

//�ƻ� 
struct HealthControllerPlan {
	1:  i32 id; 				//��ϢID
	2:  string code; 			//����Ψһ��ʾ
	3:  string starttime;   	//������ʼʱ��
	4:  string endtime;  		//��������ʱ��
	5:  string doctorPhrcode; 	//ҽ��ID
    6:  string doctorName; 		//ҽ������
    7: 	string status; 			//״̬ Yes ���ڽ��� NO ʧЧ
    8:  string plan_url; 		//��������URL	
}

//�ƻ�����
struct HealthControllerRemind {
	1:  string plancode;   					//�ƻ�����
	2:  string schemecode;  				//��������
	3:  string content; 					// �ƻ�����
    4:  string crequeny; 					//�ƻ�Ƶ��
    5: 	string exe_time; 					//ִ��ʱ��
    6:  string plantype; 					//�ƻ�����
	7:  string userid; 						//�ƻ�ִ����
	8:  string username; 					//�ƻ�ִ��������
	9:  string doctorid; 					//ҽ��ID
	10: string doctorname; 					//ҽ������
}

//�ӿ���־
struct InterfaceLog {
	1: string phrCode;			//��Ա����
	2: string ip;				//ip��ַ
	3: string mac;				//mac��ַ
	4: string interfaceName;	//�ӿ�����
	5: string lng;				//γ��
	6: string lat;				//����
	7: string orgId;			//��֯����ID
}

//������Ϣ
struct PeripheralConfigure{
	1: i32 id;					//����
	2: string peripheralId;		//����id
	3: string peripheralName;	//��������
	4: string bluetoothId;		//��������ֵ
	5: string bluetoothName;	//��������
	6: string peripheralPic;	//�豸ͼƬ
	7: string guidePic;			//����ͼ
	8: string instructionPic;	//˵��ͼ
	9: string isUse;			//0:ʹ�� 1:ͣ��
}
service UserService {
    
    //�û���¼���ͻ�����Ҫ�ṩ��¼�û����˺ź�����
    //�쳣��Ϣ��Err0001����¼�˺Ų�����
    //          Err0002����¼�������
    //��ͥ�������¼��������֤�û��������⣬�����������������
    //1.���û��������κμ�ͥ���򴴽��¼�ͥF�������û������¼�ͥF����������󶨴��¼�ͥF������loginStatusΪ0
    //2.���û�����һ����ͥF���������δ���κμ�ͥ����������󶨴˼�ͥF������loginStatusΪ0
    //3.���û�����һ����ͥF����������Ѱ󶨴˼�ͥF���������κβ���������loginStatusΪ0
    //4.���û����ڶ����ͥF1��F2��F3���������δ���κμ�ͥ������loginStatusΪ2��������Ҫ�û��ֶ�ѡ��һ����ͥF1��F2��F3����������а󶨣�����loginStatusΪ2
    //5.���û����ڼ�ͥF1��������󶨼�ͥF2?�����loginStatusΪ1���������Ҳ�޷���¼
    AccountInfo login(1: AccountInfo accountInfo) throws (1: XKCommon.HealthServiceException ex);
    
    //������û�,���볤�ȼ���ڿͻ������
    //�쳣��Ϣ��Err0003��ע���˺��ظ�
    //          Err0014������ǿ�Ȳ���
    //          Err0007��ע��ʧ��#��#
    //          Err0015: �˺Ÿ�ʽ����ȷ
    //          Err0004�����ݿ�����ʧ��
	AccountInfo findXKAccountByProofNum(1: string proofNum) throws (1: XKCommon.HealthServiceException ex);
	
	//�鿴����userId�Ƿ�󶨵�ĳ�������  
	//1.�豸id 2.�û�id
	bool checkBindstate(1: string deviceId, 2: string userId) throws (1: XKCommon.HealthServiceException ex);
	
	//ע���˻�      
	//1.accountInfo���˻��ࣻ2.deviceId���豸id��3.verifyCode:��֤�롣
    AccountInfo registerAccount(1: AccountInfo accountInfo, 2: string deviceId, 3: string verifyCode) throws (1: XKCommon.HealthServiceException ex);

	//ע���ͥ��Ա����   
	//1.�˻���     2.�豸id     3.��֤��
	AccountInfo registerAndBindAccount(1: AccountInfo accountInfo, 2: string deviceId, 3: string verifyCode) throws (1: XKCommon.HealthServiceException ex);
		
    //�޸��˺���Ϣ���˺š����벻��ʹ�ø÷������޸�
    //�쳣��Ϣ��Err0016���˺���Ϣ����ΪNULL
    //          Err0004�����ݿ�����ʧ��
    //          Err0019: ��¼���ڣ������µ�¼
    //          Err0020��ָ�����û����ǵ�ǰ��¼���û�
    AccountInfo updateAccount(1: AccountInfo accountInfo) throws (1: XKCommon.HealthServiceException ex);
	
	//�޸��˺���Ϣ���˺š����벻��ʹ�ø÷������޸�
    //�쳣��Ϣ��Err0016���˺���Ϣ����ΪNULL
    //          Err0004�����ݿ�����ʧ��
    //          Err0019: ��¼���ڣ������µ�¼
    //          Err0020��ָ�����û����ǵ�ǰ��¼���û�
	AccountInfo_new updateAccount_new(1: AccountInfo_new accountInfo) throws (1: XKCommon.HealthServiceException ex);
    
    //�޸ĵ�¼����
    //userId: ָ��Ҫ�޸Ŀ�����˺�
    //oldPassword: ԭ����
    //newPassword: �¿���
    //�쳣��Ϣ��Err0017: ԭ�������
    //          Err0014������ǿ�Ȳ���
    //          Err0004�����ݿ�����ʧ��
    //          Err0019: ��¼���ڣ������µ�¼
    //          Err0020��ָ�����û����ǵ�ǰ��¼���û�
    void editPassword(1: string userId, 2: string oldPassword, 3: string newPassword) throws (1: XKCommon.HealthServiceException ex);

    //��ȡ�������Ա��Ϣ�б�
    //userId: ��ǰ��¼�û����û�ID
    //�쳣��Ϣ��Err0001���˺Ų�����
    //          Err0004�����ݿ�����ʧ��
    //          Err0019: ��¼���ڣ������µ�¼
    //          Err0020��ָ�����û����ǵ�ǰ��¼���û�
    //���ؽ����NULL�����Ա��Ϣ�б�
    list<MemberInfo> getMembers(1: string userId) throws (1: XKCommon.HealthServiceException ex);

    //��ѯ�˺���Ϣ
    //userId: Ҫ��ѯ���˺�Id��֧��ģ����ѯ��ͬʱ��ѯ�˺š����䡢�ֻ����ֶ�
    //nickName:�û��˺ŵ��ǳƣ���userId���߼����ϵ��֧��ģ����ѯ
    //�쳣��Ϣ��Err0022��δ����Ҫ��ѯ���˺�
    //          Err0004�����ݿ�����ʧ��
    //          Err0019: ��¼���ڣ������µ�¼
    //���ؽ����NULL���ѯ����б�
    void addMember(1: string userId, 2: string password, 3: string loginUserId) throws (1: XKCommon.HealthServiceException ex);
    
    //ɾ���������Ա��������ֻɾ�����Ա��Ϣ����ɾ����¼��Ϣ
    //userIds:ָ��Ҫɾ�������Ա�û�Id����ͬʱɾ�������
    //userId: ָ����ǰ��¼���û�Id
    //�쳣��Ϣ��Err0018����Ա�˺ţ�#��#������
    //          Err0004�����ݿ�����ʧ��
    //          Err0019: ��¼���ڣ������µ�¼
    //          Err0020��ָ�����û����ǵ�ǰ��¼���û�
    list<MemberInfo> deleteMembers(1: list<string> userIds, 2: string loginUserId) throws (1: XKCommon.HealthServiceException ex);

		//����userid��ȡ��ͥ������ϸ��Ϣ
    //����ֵ����ͥ������ϸ��Ϣ
    //userId: ָ����ǰ��¼�û�
    //�쳣��Ϣ��Err0019: ��¼���ڣ������µ�¼
    //          Err0001��#��#�˺Ų�����
    //          Err0004�����ݿ�����ʧ��
    //          Err0021��ָ�����#��#������
    list<CaregiverInfo> getCaregiverInfoService(1: string userId, 2: string deviceId) throws(1: XKCommon.HealthServiceException ex);
    
	//ͨ���û��������롢�豸ID��Ӽ�ͥ��Ա
	//1.�û�����   2.����   3.�豸id
    void bindDeviceByUserName(1: string userName, 2: string password, 3: string deviceId) throws (1: XKCommon.HealthServiceException ex);
    
	//ͨ���û�personPhrCode���豸ID��Ӽ�ͥ��Ա
	//1.�û�id     2.�豸id
    void bindDeviceByUserId(1: string userId, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);
    
	//ͨ���豸ID ��ȡ�û���Ϣ
	//1.�豸id
    list<AccountInfo> getAccountInfosByDeviceId(1: string deviceId) throws (1: XKCommon.HealthServiceException ex);
	
	//ͨ���豸ID ��ȡ�û���Ϣ
	//1.�豸id
	list<AccountInfo_new> getAccountInfosByDeviceId_new(1: string deviceId) throws (1: XKCommon.HealthServiceException ex);
    
	//ͨ���豸ID  ɾ����Ա
	//1.id����   2.�豸id
    list<AccountInfo> deleteAccountsByDeviceId(1: list<string> userIds, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);

	//ͨ���û�personPhrCode ��ȡ��ͥ��Ϣ
	//1.personPhrCode
	list<FamilyInfo> getFamilyInfosByUserId(1: string userId) throws (1: XKCommon.HealthServiceException ex);
	
	//��ȡ ������֤�� ͨ��deviceId
	//1.�豸id
	string getVerifyCodeByDeviceId(1: string deviceId) throws (1: XKCommon.HealthServiceException ex);
	
	//���� ��֤��   ��ȷ���·�����
	//1.�ֻ���  2.��֤��  3.�豸id
	void sendSmsVerifyCode(1: string phoneNum, 2: string verifyCode, 3: string deviceId) throws (1: XKCommon.HealthServiceException ex);
	
	//��֤�ֻ�����
	//1.�ֻ���   2.��֤��
	void validateSmsVerifyCode(1: string phoneNum, 2: string smsVerifyCode) throws (1: XKCommon.HealthServiceException ex);
	
	//��������
	//1.�ֻ���  2.������   3.��֤��    4.�豸id
	void resetPassword(1: string phoneNum, 2: string newPassword, 3: string smsVerifyCode, 4: string deviceId) throws (1: XKCommon.HealthServiceException ex);

	//�豸�󶨼�ͥ
	//1.��ͥid   2.�豸id
	void bindDeviceByFamilyId(1: string familyId, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);
	
	//�豸����ͥ
	//1.��ͥid   2.�豸id
	void unBindDeviceByFamilyId(1: string familyId, 2: string deviceId) throws (1: XKCommon.HealthServiceException ex);
		
	//�¼ӽӿڣ���ȡ��ǰ�û���ҽ���б�
	//1.�û�id  2.�豸id
	list<CaregiverInfo> getDoctorInfoService(1: string userId, 2: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ȡ��ͥ��Ա��ҽ���б�
	//1.�豸id
	list<MemberDoctorRelation> getDoctorInfoByDeviceID(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ȡĳ�˵Ĵ����б�
	//1.�û�id  2.��ʼʱ��
	list<RecipeInfo> getRecipeListByUserID(1: string userId, 2: string startTime) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ȡĳ���豸�Ĵ����б�
	//1.�豸id   2.��ʼʱ��
	list<RecipeInfo> getRecipeListByDeviceID(1: string deviceId, 2: string startTime) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ʱ��λ�ȡ��ͥ��Ƭ�б�
	//1.�豸id  2.����ʱ��
	list<PhotoInfo> getphotoBydeviceID(1: string deviceId, 2: string shareTime) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡͼƬ
	//1.ͼƬ·��
	list<binary> getphotoInfoByurl(1: list<string> photourls) throws(1: XKCommon.HealthServiceException ex);

    //���ݻ��߻���ҽ����phrcode��ȡ����
	//1.�û�id
    string getUserNameByUserID(1: string userId) throws(1: XKCommon.HealthServiceException ex);
		
	//�¼ӽӿڣ��豸�Ƿ�󶨵���ͥ����ʱ���ؼ�ͥ��Ϣ��
	//1.�豸id
	FamilyInfo checkBindStateByDeviceID(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//��Ƶ������֪ͨ��
	//1.��Ϣ��Ϣ��
	void messageNotify(1: MessageInfo msgInfo) throws(1: XKCommon.HealthServiceException ex);

    //��ȡ����ӿڡ�
	//1.�豸id
	list<OutsideInfo> getOutsideListByDeviceId(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡ����ӿڡ�
	//1.�豸id  2.��id
	string hostlogin(1: string deviceId, 2:string hostid) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡȫ������ӿڡ�
	//1.�豸id
	list<ServicesInfo> getAllServices(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡ�ѹ���ķ���ӿڡ�
	//1.�豸id
	list<UsingServices> getUsingServices(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
	
	//��������
	//1.�豸id   2.�豸��
	string addOutside(1: string deviceId, 2:OutsideInfo info) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡ�����¼��
	//1.�豸id  2.����id
	list<ServiceRecord> getServiceRecords(1: string deviceId, 2:string ServiceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡ��������ʷ�ӿڡ�
	//1.�豸id  2.����id
	list<UsingServices> getServiceHistory(1: string deviceId,2:string serviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡ��ͥ���ֽӿڡ�
	//1.�豸id
	i32 getFamilyPoints(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		  
	//��ȡ�����б�ӿڡ�
	//1.�豸id   2.����
	list<PointRecords> getPointsHistory(1: string deviceId,2:i32 num) throws(1: XKCommon.HealthServiceException ex);
		 		 
	//�޸ķ������� 1:���� 2��һ�� 3����
	//1.��¼id    2.���
	i32 updateServiceRecords(1: i32 recordId, 2:i32 result) throws(1: XKCommon.HealthServiceException ex);
		 
	//��ȡ�����±�/�ܱ��ӿ� 1�� �ܱ� 2�� �±�
	//1.�û�id   2.����   3.��ʼλ��   4.����λ��
	list<HealthReport> getHealthReportLists(1: string userid, 2:i32 type,3: i32 startindex,4:i32 endindex) throws(1: XKCommon.HealthServiceException ex);
		 
	//���ݼ�ͥid ��ȡ�����±�/�ܱ��ӿ� 1�� �ܱ� 2�� �±�
	//1.�û�id   2.����   3.��ʼλ��   4.����λ��   5.��ͥid
	list<HealthReport> getHealthReportListsByFamilyId(1: string userid, 2:i32 type,3: i32 startindex,4:i32 endindex,5:string familyId) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ȡĳ�˵Ĵ����б�
	//1.�û�id   2.��ʼʱ��   3.����ʱ��
	list<RecipeInfo> getNewRecipeListByUserID(1: string userId, 2: string startTime, 3: string endTime) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ȡĳ���豸�Ĵ����б�
	//1.�豸id  2.��ʼʱ��   3.����ʱ��
	list<RecipeInfo> getNewRecipeListByDeviceID(1: string deviceId, 2: string startTime, 3: string endTime) throws(1: XKCommon.HealthServiceException ex);
		 
	//�¼ӽӿڣ���ʱ��λ�ȡ��ͥ��Ƭ�б�
	//1.�豸id   2.��ʼʱ��   3.����ʱ��
	list<PhotoInfo> getNewphotoBydeviceID(1: string deviceId, 2: string starTime,3: string endtime) throws(1: XKCommon.HealthServiceException ex);

	//��ȡ���˻��ֽӿ�
	//1.�û�id
	i32 serviceCardGetUserPoints(1: string userId) throws(1: XKCommon.HealthServiceException ex);

	//��ȡ���˻����б�ӿڡ�
	//1.�û�id  2.����
	list<PointRecords> serviceCardGetPointsHistory(1: string userId,2:i32 num) throws(1: XKCommon.HealthServiceException ex);

	//�����ŵ�½
	//1.�ʺ���   2.����
	ServiceCardResult serviceCardLoginByCardNum(1: AccountInfo accountInfo,2: string cardNo) throws (1: XKCommon.HealthServiceException ex);
			
	//���˻���½
	//1.�ʺ���   
	ServiceCardResult serviceCardLoginByAccount(1: AccountInfo accountInfo) throws (1: XKCommon.HealthServiceException ex);
		
	//�������ذ�����ָ������Ա
	//1.�豸id   2.����   3.����   4.�û�id
	ServiceCardResult BindCardToPerson(1: string deviceid,2: string cardNo,3:string pwd,4:string userid) throws (1: XKCommon.HealthServiceException ex);
		
	//��ȡ�ѹ���ķ���ӿ�
	//1.�豸id
	list<PurchasedServices> getPurchasedServices(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
			
    //������ϢID��ȡ������Ϣ����ӿڡ�
	//1.��Ϣid
	MessageDetail getPushMessage(1: string msgid) throws(1: XKCommon.HealthServiceException ex);

    //��ȡ�����б�
	//1.�û�id
	list<HealthControllerPlan> getHealthControllerPlan(1: string userid) throws(1: XKCommon.HealthServiceException ex);
		 
	//���˻�ȡ��������ִ�мƻ��б�
	//1.�û�id
	list<HealthControllerRemind> getHealthControllerRemindByMember(1: string userid) throws(1: XKCommon.HealthServiceException ex);
		 
	//���豸��ȡ��������ִ�мƻ��б�
	//1.�豸id
	list<HealthControllerRemind> getHealthControllerRemindByDeviceId(1: string deviceId) throws(1: XKCommon.HealthServiceException ex);
		 
	//���豸��ȡ��������ִ�мƻ��б�
	//1.�豸id
	list<HealthControllerRemind> getHealthControllerRemindByDevice(1: string deviceid) throws(1: XKCommon.HealthServiceException ex);
		 
		 
	//������ͥ����Ϣ֪ͨ��ά�ӿ�
	//1.�˻���   2.�豸id
	void sendMessageToManager(1: AccountInfo accountInfo,2: string deviceid) throws (1: XKCommon.HealthServiceException ex);
		
	//�����֤��¼�ӿ�
	//1.���֤   2.�豸��
	ServiceCardResult serviceLoginByProofNum(1: string proofNum,2:string deviceid) throws (1: XKCommon.HealthServiceException ex);
		
	//��ȡ�ɺ��е�ҽ���ӿ�
	//1.����id
	string getCallDoctor(1:string serviceid);
		
	//���ӿ�
	//1.��־��
	void saveInterfaceLog(1:InterfaceLog interfaceLog);

	//��ȡ�豸����
	list<PeripheralConfigure> getPeripheralConfigureList();
		
	//��ȡ����������Ϣ
	//1.�û�id
	YTJ_MemberHealthInfo getMemberHealthInfo(1:string personPHRCode);
		
	//���½���������Ϣ
	//1.�û�id    2.������Ϣ��
	void updateMemeberHealthInfo(1:string personPHRCode,2:YTJ_MemberHealthInfo healthInfo);
		
	//������֤��
	//1.�ֻ���
	void ytj_public_sendVerifyCode(1:string phoneNum);
		
	//��ѯ�ֻ����Ƿ�ע��
	//1.�ֻ���
	void isEffectiveMobileNumber(1:string phoneNum);
		
	//ע��ӿ�
	//1.����  2.������   3.����   4.���֤   5.�ֻ���   6.��֤��
	void ytj_public_register(1:string cardNum,2:string cardPW,3:string name,4:string ProofNum,5:string phoneNum,6:string verifyCode) throws (1: XKCommon.HealthServiceException ex);
	
	//��ע�Ტ��¼
	//1.���֤��   2.����   3.�Ա�
	ServiceCardResult serviceCardLoginByProofNumAndRegister(1:string proofNum,2:string birthday,3:i32 sex, 4:string macAddress,5:string name) throws (1: XKCommon.HealthServiceException ex);
	
	//����������������ֻ��Ż������֤�Ű󶨿�
	//1.����   2.����   3.����
	void ytj_public_BindCard(1:string cardNum,2:string id,3:i32 type) throws (1: XKCommon.HealthServiceException ex);
		
	//����(����/�ֻ�����/���֤��/�ǳ�/��Ա����)Ψһ��ѯ��Ա
	//1.����   2.����
	string findPersonPhrCodeByUniquerHealthInfo(1:string id,2:i32 type) throws (1: XKCommon.HealthServiceException ex);
		
	//ͨ��phrcode��ȡ�û���Ϣ
	//1.�û�id
	AccountInfo getAccountInfosByPhrCode(1:string phrcode) throws (1: XKCommon.HealthServiceException ex);
		
				
}
