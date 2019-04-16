from unittest import TestCase

from apply import PrototypeCreator
from model.car import Car


class TestPrototyping(TestCase):

    def test_when_create_a_delegate_from_prototype_then_both_should_behave_same_way(self):
        my_car_prototype = Car("super_movil", "blue")
        creator = PrototypeCreator(my_car_prototype)
        my_car_delegate = creator.get()
        self.assertEquals(type(my_car_prototype), type(my_car_delegate))
        self.assertTrue(not my_car_prototype == my_car_delegate)
        self.assertEqual(my_car_prototype.brand(), my_car_delegate.brand())
        self.assertEqual(my_car_prototype.color(), my_car_delegate.color())

    def test_when_delegate_change_some_behave_then_prototype_should_not(self):
        my_car_prototype = Car("super_movil", "blue")
        replacer = (lambda: "red")
        creator = PrototypeCreator(my_car_prototype, {"color": replacer})
        my_car_delegate = creator.get()
        self.assertTrue(type(my_car_prototype), type(my_car_delegate))
        self.assertTrue(not my_car_prototype == my_car_delegate)
        self.assertEqual(my_car_prototype.color(), "blue")
        self.assertEqual(my_car_delegate.color(), "red")
        self.assertEqual(my_car_prototype.brand(), my_car_delegate.brand())

    def test_when_delegate_remove_some_behave_should_answer_with_prototype_behave(self):
        my_car_prototype = Car("super_movil", "blue")
        replacer = (lambda: "green")
        creator = PrototypeCreator(my_car_prototype, {"color": replacer})
        my_car_delegate = creator.get()
        self.assertEqual(my_car_delegate.color(), "green")
        creator.remove_method(my_car_delegate, "color")
        self.assertEqual(my_car_delegate.color(), "blue")
