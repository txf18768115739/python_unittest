# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':#执行测试套程序
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('UnittestTextReport.txt', 'a') as f:#打印出报告
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
