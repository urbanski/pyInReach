import requests

#todo-- discover deviceids

def SendMessageToDevices(mapshare_url, message):
	h = {}
	h['X-Requested-With'] = 'XMLHttpRequest'
	h['Accept'] = 'application/json, text/javascript, */*;'
	h['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
	h['User-Agent'] = 'Mozilla/5.0'

	req = requests.post('%s/Map/SendMessageToDevices' % mapshare_url, headers=h, allow_redirects=False, data = message.to_dict())

	return req

class Message:
	fromAddr = None
	messageText = None
	deviceIds = []

	def __init__(self, deviceIds = [], messageText = None, fromAddr = None):
		self.fromAddr = fromAddr
		self.deviceIds = deviceIds
		self.messageText = messageText

	def to_dict(self):
		return {'fromAddr': self.fromAddr, 'messageText': self.messageText, 'deviceIds': self.deviceIds}