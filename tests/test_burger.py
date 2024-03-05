from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns_successful(self):
        mock_bun = Mock()
        mock_bun.bun = Bun('Булка', 30)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        assert burger.bun.get_name() == ('Булка')

    def test_add_ingredient_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('SAUCE', "Соус", 20)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.ingredients != [['SAUCE', "Соус", 20]]

    def test_remove_ingredient_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('SAUCE', "hot sauce", 10)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredients_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients_1 = Ingredient('SAUCE', "Соус", 90)
        mock_ingredient.ingredients_2 = Ingredient('FILLING', "Горчица", 80)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients_1)
        burger.add_ingredient(mock_ingredient.ingredients_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients.index(mock_ingredient.ingredients_1) == 1

    @patch('praktikum.bun.Bun.get_price', return_value=30)
    @patch('praktikum.ingredient.Ingredient.get_price', return_value=40)
    def test_get_price_burger_successful(self, mock_bun_get_price, mock_ingredient_get_price):
        mock_bun = Mock()
        mock_bun.bun = Bun('Булка', 100)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('SAUCE', "Соус", 135)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.get_price() == 100

    @patch('praktikum.bun.Bun.get_name', return_value='Булка')
    @patch('praktikum.ingredient.Ingredient.get_type', return_value='FILLING')
    @patch('praktikum.ingredient.Ingredient.get_name', return_value='Горчица')
    def test_get_receipt_successful(self, mock_bun_get_name, mock_ingredient_get_type, mock_ingredient_get_name):
        mock_bun = Mock()
        mock_bun.bun = Bun('Булка с маком', 300)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('FILLING', "Горчица", 250)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.get_receipt() == '(==== Булка ====)\n''= filling Горчица =\n''(==== Булка ====)\n''\n''Price: 850'