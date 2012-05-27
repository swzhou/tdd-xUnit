import sys
sys.path.insert(0, 'src')
from testCase import TestCase
from wasRun import WasRun

class TestCaseFacts(TestCase):
	def testRunning(self):
		test = WasRun("testMethod")
		assert(not test.wasRun)
		test.run()
		assert(test.wasRun)
TestCaseFacts("testRunning").run()