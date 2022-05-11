import unittest
from unittest.mock import MagicMock
import calc
class TestCalc(unittest.TestCase):

    def test_clear(self):
        self.assertEqual(calc.expression,'')

    def test_notclear(self):
        self.assertNotEqual(calc.expression,'string')



    def test_btn_clck(self,item='6'):
        calc.btn_click = MagicMock(return_value=item)
        self.assertEqual(calc.btn_click(item),'6')

    def test_btn_clcknoteql(self,item='6'):
        calc.btn_click = MagicMock(return_value=item)
        self.assertNotEqual(calc.btn_click(item),'66')



    def test_btnoteql(self,expression='6+6'):
        #expression = '6+6'
        calc.bt_equal= MagicMock(return_value = eval(expression))
        self.assertNotEqual(calc.bt_equal(expression),11)

    def test_bteql(self,expression='6+6'):
        #expression = '6+6'
        calc.bt_equal= MagicMock(return_value = eval(expression))
        self.assertEqual(calc.bt_equal(expression),12)


