from wasrun import WasRun

test = WasRun("testMethod")
print test.wasRun
test.run()
print test.wasRun

class TestCase:
    def __init__(self, name):
        self.name= name
    def run(self):
        method = getattr(self,self.name)
        method()
