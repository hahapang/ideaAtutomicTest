import unittest
from os import listdir
from os.path import isfile, join
from importlib.machinery import SourceFileLoader
from HtmlTestRunner import HTMLTestRunner

my_path = 'TestCase'

onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f)) and f != '__init__.py' and not f.startswith('.')]
suites = unittest.TestSuite()
for f in onlyfiles:
    test = SourceFileLoader(f,join(my_path,f)).load_module()
    suite = unittest.TestLoader().loadTestsFromModule(test)
    suites.addTest(suite)

runner = HTMLTestRunner(output='output')

if __name__ == "__main__":
    runner.run(suites)
