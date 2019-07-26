class Vehicle:
    def __init__(self, wheels, vtype):
        self._wheels = wheels
        self._vehtype = vtype
        self._fuel = ''
        
    @property
    def _fuel(self):
        return self.__fuel
        
    @_fuel.setter
    def _fuel(self, fuel):
        self.__fuel = fuel

class Car(Vehicle):
    def __init__(self, wheels, fuel, brand, model):
        Vehicle.__init__(self, wheels, 'Car')
        Vehicle._fuel = fuel
        self._brand = brand
        self._model = model
        
    @property
    def _brand(self):
        return self.__brand
        
    @_brand.setter
    def _brand(self, brand):
        self.__brand = brand
        
    @property
    def _model(self):
        return self.__model;
        
    @_model.setter
    def _model(self, model):
        self.__model = model
        
        
car = Car(4, 'Petrol', 'Audi', 'A6')
print(car._wheels)
print(car._fuel)
print(car._model)