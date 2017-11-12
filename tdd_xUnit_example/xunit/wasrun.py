from testcase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun= 1
        self.log= self.log + "testMethod"

    def run(self):
        method = getattr(self, self.name)
        method()

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= 1
        self.log= "setUp"
