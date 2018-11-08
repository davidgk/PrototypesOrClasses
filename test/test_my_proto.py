from unittest import TestCase

from apply import PrototypeCreator
from model.automovil import Automovil


class TestPrototyping(TestCase):

    def test_when_create_a_car_then_prototype_it_should_be_pretty_similar(self):
        my_car = Automovil("poncho", "azul")
        creator = PrototypeCreator(my_car)
        mi_prototipo = creator.get()
        self.assertEquals(type(my_car), type(mi_prototipo))
        self.assertTrue(not my_car == mi_prototipo)
        self.assertEqual(my_car.marca(), mi_prototipo.marca())
        self.assertEqual(my_car.color(), mi_prototipo.color())

    def test_create_a_prototype_from_car_and_replace_color(self):
        auto_original = Automovil("poncho", "azul")
        replacer = (lambda: "rojo")
        creator = PrototypeCreator(auto_original, {"color": replacer})
        mi_prototipo = creator.get()
        self.assertTrue(type(auto_original), type(mi_prototipo))
        self.assertTrue(not auto_original == mi_prototipo)
        self.assertEqual(auto_original.color(), "azul")
        self.assertEqual(mi_prototipo.color(), "rojo")
        self.assertEqual(auto_original.marca(), mi_prototipo.marca())

    def test_create_a_prototype_remove_func(self):
        auto_original = Automovil("poncho", "azul")
        replacer = (lambda: "verde")
        creator = PrototypeCreator(auto_original, {"color": replacer})
        mi_prototipo = creator.get()
        self.assertEqual(mi_prototipo.color(), "verde")
        creator.remove_method(mi_prototipo, "color")
        self.assertEqual(mi_prototipo.color(), "azul")
