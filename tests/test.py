import sys
import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('tests')
    ret = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)
