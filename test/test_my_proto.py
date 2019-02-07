from unittest import TestCase

from apply import PrototypeCreator
from model.car import Car


class TestPrototyping(TestCase):

    def test_when_create_a_car_then_prototype_it_should_be_pretty_similar(self):
        my_car = Car("super_movil", "blue")
        creator = PrototypeCreator(my_car)
        my_prototype = creator.get()
        self.assertEquals(type(my_car), type(my_prototype))
        self.assertTrue(not my_car == my_prototype)
        self.assertEqual(my_car.brand(), my_prototype.brand())
        self.assertEqual(my_car.color(), my_prototype.color())

    def test_create_a_prototype_from_car_and_replace_color(self):
        original_car = Car("super_movil", "blue")
        replacer = (lambda: "red")
        creator = PrototypeCreator(original_car, {"color": replacer})
        my_prototype = creator.get()
        self.assertTrue(type(original_car), type(my_prototype))
        self.assertTrue(not original_car == my_prototype)
        self.assertEqual(original_car.color(), "blue")
        self.assertEqual(my_prototype.color(), "red")
        self.assertEqual(original_car.brand(), my_prototype.brand())

    def test_create_a_prototype_remove_func(self):
        original_car = Car("super_movil", "blue")
        replacer = (lambda: "verde")
        creator = PrototypeCreator(original_car, {"color": replacer})
        my_prototype = creator.get()
        self.assertEqual(my_prototype.color(), "verde")
        creator.remove_method(my_prototype, "color")
        self.assertEqual(my_prototype.color(), "blue")
