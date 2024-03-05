from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Cheese', 100)
        actual_name = ingredient.get_name()

        assert actual_name == 'Cheese'

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'Cheese', 100)
        actual_price = ingredient.get_price()

        assert actual_price == 100

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Cheese', 100)
        actual_type = ingredient.get_type()

        assert actual_type == 'SAUCE'