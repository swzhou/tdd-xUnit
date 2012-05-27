import sys
sys.path.insert(0, 'src')
from testCase import TestCase
from testResult import TestResult
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
	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		result = test.run()
		assert("1 run, 1 failed" == result.summary())
	def testFailedResultFormatting(self):
		result = TestResult()
		result.testStarted()
		result.testFailed()
		assert("1 run, 1 failed" == result.summary())
print TestCaseFacts("testTemplateMethod").run().summary()
print TestCaseFacts("testResult").run().summary()
print TestCaseFacts("testFailedResult").run().summary()
print TestCaseFacts("testFailedResultFormatting").run().summary()