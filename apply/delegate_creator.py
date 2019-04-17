class Prototypical(object):

    def __init__(self):
        pass


class DelegateCreator(object):

    def __init__(self, prototype, methods_replace = None):
        self.__prototype = prototype
        self.__methods_replace = methods_replace

    def get(self):
        return self.__create()

    def __create(self):
        result = Prototypical()
        result.__class__ = self.__prototype.__class__
        self.__add_attributes(result)
        if self.__methods_replace:
            for key, value in self.__methods_replace.items():
                result.__dict__[key] = value

        return result

    def __add_attributes(self, result):
        for value in vars(self.__prototype):
            result.__dict__[value] = self.__prototype.__dict__[value]

    def remove_method(self, my_delegate, param, ):
        del my_delegate.__dict__[param]
        if param in my_delegate.__class__.__dict__.keys():
            meth = my_delegate.__class__.__dict__[param]
            my_delegate.__dict__[param] =(lambda: meth(my_delegate))
