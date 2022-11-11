'''
Singleton pattern exercise
1. Using __new__ to implement singleton pattern
2. Using __init__ to implement singleton pattern
'''

# Using __new__

# class ParkingLot:
    # singleton ParkingLot to ensure only one object of ParkingLot in the system,
    # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
    # similarly exit panels will also use this object to close parking tickets
    # instance = None
    # class __Onlyone:
    #     def __init__(self, id, loc, type) -> None:
    #         self.id = id
    #         self.loc = loc
    #         self.type = type
        
    # def __new__(cls, id, loc, type) -> None:
    #     # if ParkingLot.instance == None:
    #     if not ParkingLot.instance:
    #         print("Create Singleton obj")
    #         ParkingLot.instance = ParkingLot.__Onlyone(id, loc, type)
    #     else:
    #         ParkingLot.instance.id = id
    #         ParkingLot.instance.loc = loc
    #         ParkingLot.instance.type = type
    #     return ParkingLot.instance
    
    # def __getattr__(self, name):
    #     return getattr(self.instance, name)




# Using __init__

from typing import Any


class ParkingLot:
    instance = None
    class __OnlyOne:
        def __init__(self, name, address):
            self.__name = name
            self.__address = address
    
        

    def __init__(self, name, address):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        else:
            ParkingLot.instance.__name = name
            ParkingLot.instance.__address = address

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def get_name(self):
        return self.instance.__name
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        setattr(self.instance, __name, __value)

    def set_name(self, n ,v):
        self.instance.__name = v
        


x = ParkingLot('west', 'Large')
print(x)
y = ParkingLot('East', 'Compact')
print(y)
print(x)
print(x.instance == y.instance)
print(x.get_name())
# x.set_name()
x.set_name("__name", "North")
x.instance.__name = "Norch"
print(x.get_name())



'''
Example from: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

Thread safe: https://refactoring.guru/design-patterns/singleton/python/example#example-1
'''

# class OnlyOne(object):
#     class __OnlyOne:
#         def __init__(self):
#             self.val = None
#         def __str__(self):
#             return repr(self) + self.val
#     instance = None
#     def __new__(cls): # __new__ always a classmethod
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__OnlyOne()
#         return OnlyOne.instance
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#     def __setattr__(self, name):
#         return setattr(self.instance, name)

# x = OnlyOne()
# x.val = 'sausage'
# print(x)
# y = OnlyOne()
# y.val = 'eggs'
# print(y)
# z = OnlyOne()
# z.val = 'spam'
# print(z)
# print(x)
# print(y)
# print(x == y)