import unittest

class TestCaseTest(unittest.TestCase):
    def testSetUp(self):
        test= WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

    def testRunning(self):
        test= WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("testRunning").run()


if __name__ == "__main__":
    unittest.main()
