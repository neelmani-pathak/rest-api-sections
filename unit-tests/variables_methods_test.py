
import unittest
import sys
import os

import section2.newfile as nf

# sys.path.append('/root/section2')
# from newfile import my_multiplication_method

# sys.path.append(os.path.abspath("../section2"))
# import newfile


class TestVariables(unittest.TestCase):

    def test_my_multiplication_method(self):
        self.assertEqual(nf.my_multiplication_method(5, 4), 20)
