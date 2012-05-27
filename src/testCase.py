class TestCase:
	def __init__(self, name):
		self.name = name
	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()
		self.tearDown()
	def setUp(self):
		pass
	def tearDown(self):
		pass