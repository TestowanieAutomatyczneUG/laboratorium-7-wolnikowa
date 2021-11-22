import unittest
import requests


class FoodApi:
    def get_meals_by_name(self, name):
        if type(name) != str:
            raise TypeError('Name must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+name)
        return meals.json()

    def get_meal_by_id(self, id):
        if type(id) != str and type(id) != int:
            raise TypeError('Id must be a string or an integer')
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i='+str(id))
        return meal.json()

    def get_random_meal(self):
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        return meal.json()

    def get_meal_categories(self):
        categories = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
        return categories.json()

    def get_categories_list(self):
        categories = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
        return categories.json()

    def get_areas_list(self):
        areas = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
        return areas.json()

    def get_ingredients_list(self):
        ingredients = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
        return ingredients.json()

    def get_filter_meals_by_ingredient(self, ingredient):
        if type(ingredient) != str:
            raise TypeError('Ingredient must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?i='+ingredient)
        return meals.json()

    def get_filter_meals_by_category(self, category):
        if type(category) != str:
            raise TypeError('Category must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+category)
        return meals.json()

    def get_filter_meals_by_area(self, area):
        if type(area) != str:
            raise TypeError('Area must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?a='+area)
        return meals.json()


class FoodApiTest(unittest.TestCase):
    def setUp(self):
        self.api = FoodApi()

    def test_get_meals_by_name(self):
        response = self.api.get_meals_by_name('Arrabiata')
        self.assertEqual(response['meals'][0]['idMeal'], '52771')

    def test_get_meals_by_name_wrong_type(self):
        with self.assertRaises(TypeError):
            self.api.get_meals_by_name(5435)

    def test_get_meals_by_name_none(self):
        response = self.api.get_meals_by_name('fefewfwff')
        self.assertEqual(response['meals'], None)

    def test_get_meals_by_first_letter_wrong_type(self):
        with self.assertRaises(TypeError):
            self.api.get_meals_by_first_letter(678)

    def test_get_meals_by_first_letter_none(self):
        response = self.api.get_meals_by_first_letter('9')
        self.assertEqual(response['meals'], None)

    def test_get_meal_by_id(self):
        response = self.api.get_meal_by_id(52772)
        self.assertEqual(response['meals'][0]['strMeal'], 'Teriyaki Chicken Casserole')

    def test_get_meal_by_id_wrong_type(self):
        with self.assertRaises(TypeError):
            self.api.get_meal_by_id([])

    def test_get_meal_by_id_none(self):
        response = self.api.get_meal_by_id('9999999')
        self.assertEqual(response['meals'], None)

    def test_get_random_meal(self):
        response = self.api.get_random_meal()
        self.assertEqual(len(response['meals']), 1)

    def test_get_meal_categories(self):
        response = self.api.get_meal_categories()
        categories = []
        for meal in response['categories']:
            categories.append(meal['strCategory'])
        self.assertCountEqual(categories, [
            'Beef',
            'Chicken',
            'Dessert',
            'Lamb',
            'Miscellaneous',
            'Pasta',
            'Pork',
            'Seafood',
            'Side',
            'Starter',
            'Vegan',
            'Vegetarian',
            'Breakfast',
            'Goat'
        ])

    def test_get_categories_list(self):
        response = self.api.get_categories_list()
        self.assertEqual(len(response['meals']), 14)

    def test_get_areas_list(self):
        response = self.api.get_areas_list()
        self.assertEqual(len(response['meals']), 27)

    def test_get_ingredients_list(self):
        response = self.api.get_ingredients_list()
        ingredient_name = ''
        for ingredient in response['meals']:
            if ingredient['idIngredient'] == '370':
                ingredient_name = ingredient['strIngredient']
                break
        self.assertEqual(ingredient_name, 'Paccheri Pasta')

    def test_get_filter_meals_by_ingredient(self):
        response = self.api.get_filter_meals_by_ingredient('chicken_breast')
        meals = []
        for meal in response['meals']:
            meals.append(meal['idMeal'])
        self.assertCountEqual(meals, [
            '53016',
            '52850',
            '52818',
            '52875',
            '53011',
            '52951',
            '52993',
            '52820',
            '52933'
        ])

    def test_get_filter_meals_by_ingredient_wrong_type(self):
        with self.assertRaises(TypeError):
            self.api.get_filter_meals_by_ingredient(-65)

    def test_get_filter_meals_by_ingredient_none(self):
        response = self.api.get_filter_meals_by_ingredient('bing')
        self.assertEqual(response['meals'], None)

    def test_get_filter_meals_by_category(self):
        response = self.api.get_filter_meals_by_category('Seafood')
        meal_id = ''
        for meal in response['meals']:
            if meal['strMeal'] == 'Seafood fideuà':
                meal_id = meal['idMeal']
                break
        self.assertEqual(meal_id, '52836')

    def test_get_filter_meals_by_category_wrong_type(self):
        with self.assertRaises(TypeError):
            self.api.get_filter_meals_by_category(-65)

    def test_get_filter_meals_by_category_none(self):
        response = self.api.get_filter_meals_by_category('test')
        self.assertEqual(response['meals'], None)

    def test_get_filter_meals_by_area(self):
        response = self.api.get_filter_meals_by_area('Canadian')
        self.assertEqual(len(response['meals']), 13)

    def test_get_filter_meals_by_area_wrong_type(self):
        with self.assertRaises(TypeError):
            self.api.get_filter_meals_by_area(-65)

    def test_get_filter_meals_by_area_none(self):
        response = self.api.get_filter_meals_by_area('pong')
        self.assertEqual(response['meals'], None)

    def tearDown(self):
        self.api = None


if __name__ == '__main__':
    unittest.main()