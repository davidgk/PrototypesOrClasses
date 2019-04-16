from unittest import TestCase

from apply import PrototypeCreator
from model.car import Car


class TestPrototyping(TestCase):

    def test_when_create_a_car_then_prototype_it_should_be_pretty_similar(self):
        my_car_prototype = Car("super_movil", "blue")
        creator = PrototypeCreator(my_car_prototype)
        my_car_delegate = creator.get()
        self.assertEquals(type(my_car_prototype), type(my_car_delegate))
        self.assertTrue(not my_car_prototype == my_car_delegate)
        self.assertEqual(my_car_prototype.brand(), my_car_delegate.brand())
        self.assertEqual(my_car_prototype.color(), my_car_delegate.color())

    def test_create_a_prototype_from_car_and_replace_color(self):
        my_car_prototype = Car("super_movil", "blue")
        replacer = (lambda: "red")
        creator = PrototypeCreator(my_car_prototype, {"color": replacer})
        my_car_delegate = creator.get()
        self.assertTrue(type(my_car_prototype), type(my_car_delegate))
        self.assertTrue(not my_car_prototype == my_car_delegate)
        self.assertEqual(my_car_prototype.color(), "blue")
        self.assertEqual(my_car_delegate.color(), "red")
        self.assertEqual(my_car_prototype.brand(), my_car_delegate.brand())

    def test_create_a_prototype_remove_func(self):
        my_car_prototype = Car("super_movil", "blue")
        replacer = (lambda: "green")
        creator = PrototypeCreator(my_car_prototype, {"color": replacer})
        my_car_delegate = creator.get()
        self.assertEqual(my_car_delegate.color(), "green")
        creator.remove_method(my_car_delegate, "color")
        self.assertEqual(my_car_delegate.color(), "blue")
