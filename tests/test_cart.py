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

    # --- BÀI TEST MỚI THÊM ---
    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        
        # 100$ giảm 20% phải trả về 80.0$
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        
        # Kiểm tra bắt lỗi: percent > 100 phải văng lỗi ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    # tests/test_cart.py (thêm test)
    def test_sort_by_title(self):
        ...
    def test_sort_by_cost(self):
        ...