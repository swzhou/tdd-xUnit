from testResult import TestResult

class TestCase:
	def __init__(self, name):
		self.name = name
	def run(self):
		result = TestResult()
		result.testStarted()
		self.setUp()
		method = getattr(self, self.name)
		method()
		self.tearDown()
		return result
	def setUp(self):
		pass
	def tearDown(self):
		pass