from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

def main():
    cart = Cart()

    # Test trường hợp giỏ hàng trống (theo yêu cầu code review)
    cart.print_cart()

    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=18.99))

    # In giỏ hàng sau khi thêm đĩa
    cart.print_cart()

if __name__ == "__main__":
    main()