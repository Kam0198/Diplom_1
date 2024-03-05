from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('Bread',20.7)
        actual_name = bun.get_name()

        assert actual_name == 'Bread'

    def test_get_price(self):
        bun = Bun('Bread', 20.7)
        actual_price = bun.get_price()

        assert actual_price == 20.7