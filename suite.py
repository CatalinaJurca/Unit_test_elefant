import unittest

import HtmlTestRunner

from test_search import Test_Search
from test_contact_form import Test_Contact_Form

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_list = unittest.TestSuite()
        test_list.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test_Search),
                            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Contact_Form)])

        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Test execution report",
                                               report_name="Test results")
        runner.run(test_list)
