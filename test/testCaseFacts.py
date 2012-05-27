import sys
sys.path.insert(0, 'src')
from testCase import TestCase
from wasRun import WasRun

class TestCaseFacts(TestCase):
	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)
TestCaseFacts("testTemplateMethod").run()