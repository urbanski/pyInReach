# MIT License

# Copyright (c) 2017 Will Urbanski

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests

def SendMessageToDevices(mapshare_url, message):
	h = {}
	h['X-Requested-With'] = 'XMLHttpRequest'
	h['Accept'] = 'application/json, text/javascript, */*;'
	h['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

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