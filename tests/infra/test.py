#import configtest # first test
import unittest   # second test

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print ('stp')
        ##set up code

    def runTest(self):
        #runs test
        print ('stp')

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ConfigTestCase))
    return test_suite

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)
