import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên (phải thành công)
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}")))

        # Thêm đĩa thứ 21 (phải thất bại và trả về False)
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))