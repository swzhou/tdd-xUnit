import sys
sys.path.insert(0, 'src')
from testCase import TestCase
from wasRun import WasRun

class TestCaseFacts(TestCase):
	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)
	def testResult(self):
		test = WasRun("testMethod")
		result = test.run()
		assert("1 run, 0 failed" == result.summary())
TestCaseFacts("testTemplateMethod").run()
TestCaseFacts("testResult").run()