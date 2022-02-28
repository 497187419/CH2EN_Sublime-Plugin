from urllib import request, parse
import sublime_plugin
import threading
import hashlib
import sublime
import random
import json

appid = '20220226001099253'
secretKey = '1URTROOigZpjihLcNRHo'
targetUrl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

def getTranslationFromBaidu(src):
	q = src
	salt = random.randint(32768, 65536)
	sign = appid + q + str(salt) + secretKey
	md5Value = hashlib.md5()
	md5Value.update(sign.encode('utf-8'))
	sign = md5Value.hexdigest()
	postData = {
		'appid': appid,
		'q': q,
		'sign': sign,
		'salt': salt,
		'from': 'auto',
		'to': 'en'
	}
	postDataEncode = parse.urlencode(postData)
	f = request.urlopen(targetUrl, data=postDataEncode.encode())
	data = f.read()
	return json.loads(data.decode('utf-8'))['trans_result'][0]['dst']

class translateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty() or s.size() <= 1:
				break
			t = NewThread(getTranslationFromBaidu, (self.view.substr(s),))
			t.start()
			t.join()
			self.view.replace(edit, sublime.Region(s.begin(), s.end()), t.getResult())
			break

class NewThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args
	def getResult(self):
		return self.res
	def run(self):
		self.res = self.func(*self.args)