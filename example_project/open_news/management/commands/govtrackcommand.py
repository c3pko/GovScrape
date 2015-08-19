from django.core.management.base import BaseCommand, CommandError
import json
import urllib2

class Command(BaseCommand):
	
	def __init__(self, query_params = 'congress=114&current_status=enacted_signed&q=Office+of+Science+and+Technology+Policy'):
		# 'congress=114&current_status=enacted_signed&q=Office+of+Science+and+Technology+Policy'
		x = urllib2.urlopen('https://www.govtrack.us/api/v2/bill?'+query_params).read()
		resp = json.loads(x)
		self.bills = resp[u'objects']
		'''self.meta = resp[u'meta']
		'''
	
	def get_bill_fields(self):
		key_dict = self.bills[0].keys()
		return key_dict

