import sys
sys.path.insert(0, 'src')
from testCase import TestCase
from wasRun import WasRun

class TestCaseFacts(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")
	def testRunning(self):
		self.test.run()
		assert(self.test.wasRun)
	def testSetUp(self):
		self.test.run()
		assert(self.test.wasSetUp)
TestCaseFacts("testRunning").run()
TestCaseFacts("testSetUp").run()