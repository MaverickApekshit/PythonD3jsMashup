import webapp2
from google.appengine.ext.webapp import template

class ShowHome(webapp2.RequestHandler):
	def get(self):
		temp_data = {}
		temp_path = 'Templates/index.html'
		self.response.out.write(template.render(temp_path,temp_data))

class ShowChartPage(webapp2.RequestHandler):
	def get(self):
		temp_data = {}
		temp_path = 'Templates/chart.html'
		self.response.out.write(template.render(temp_path,temp_data))
		
application = webapp2.WSGIApplication([
	('/chart', ShowChartPage),
	('/', ShowHome),
], debug=True)