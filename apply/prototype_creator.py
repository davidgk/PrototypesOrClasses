class Prototypical(object):

    def __init__(self):
        pass


class PrototypeCreator(object):

    def __init__(self, simple_object, methods_replace = None):
        self.__simple_object = simple_object
        self.__methods_replace = methods_replace

    def __create_prototype(self):
        prototype = Prototypical()
        prototype.__class__ = self.__simple_object.__class__
        if self.__methods_replace:
            for key, value in self.__methods_replace.items():
                prototype.__dict__[key] = value
        return prototype

    def get(self):
        return self.__create_prototype()

    def remove_method(self, mi_prototipo, param, ):
        del mi_prototipo.__dict__[param]
        if param in mi_prototipo.__class__.__dict__.keys():
            meth = mi_prototipo.__class__.__dict__[param]
            mi_prototipo.__dict__[param] =(lambda: meth(mi_prototipo))



