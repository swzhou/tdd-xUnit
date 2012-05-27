class TestCase:
	def __init__(self, name):
		self.name = name
	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()
	def setUp(self):
		pass