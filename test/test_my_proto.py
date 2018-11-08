from unittest import TestCase

from apply import PrototypeCreator
from model.my_example import ObjetoSimple


class TestPrototyping(TestCase):

    def test_create_a_prototype(self):
        simple_object = ObjetoSimple()
        mi_prototipo = PrototypeCreator(simple_object).get()
        self.assertTrue(type(simple_object), type(mi_prototipo))
        self.assertTrue(not simple_object == mi_prototipo)
        self.assertEqual(simple_object.my_function_1(), mi_prototipo.my_function_1())
        self.assertEqual(simple_object.my_function_2(), mi_prototipo.my_function_2())

    def test_create_a_prototype_change_func(self):
        simple_object = ObjetoSimple()
        replacer = (lambda: "another response")
        mi_prototipo = PrototypeCreator(simple_object, {"my_function_1": replacer}).get()
        self.assertTrue(type(simple_object), type(mi_prototipo))
        self.assertTrue(not simple_object == mi_prototipo)
        self.assertEqual(simple_object.my_function_1(), "hola mundo 01")
        self.assertEqual(mi_prototipo.my_function_1(), "another response")
        self.assertEqual(simple_object.my_function_2(), mi_prototipo.my_function_2())

    def test_create_a_prototype_remove_func(self):
        simple_object = ObjetoSimple()
        replacer = (lambda: "another response")
        creator = PrototypeCreator(simple_object, {"my_function_1": replacer})
        mi_prototipo = creator.get()
        self.assertEqual(mi_prototipo.my_function_1(), "another response")
        creator.remove_method(mi_prototipo, "my_function_1")
        self.assertEqual(mi_prototipo.my_function_1(), "hola mundo 01")
