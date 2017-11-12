import unittest
from wasrun import WasRun

class TestCaseTest(unittest.TestCase):
    # def setUp(self):
    #     self.test= WasRun("testMethod")
    #
    # def testRunning(self):
    #     self.test.run()
    #     assert(self.test.wasRun)

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod" == self.test.log)

TestCaseTest("testRunning").run()


if __name__ == "__main__":
    unittest.main()
