#namespace is a memory block where name are mapped to object


class Mobile:
    fp="working"

    @classmethod
    def cls_method(cls):
        print("access by class method ",cls.fp)


redmi=Mobile()
lava=Mobile()
realme=Mobile()

print("Mobile.fp ",Mobile.fp)
print("redmi.fp ",redmi.fp)
print("lava.fp ",lava.fp)
print("realme.fp ",realme.fp)
print()

print("Mobile.fp ",id(Mobile.fp))
print("redmi.fp ",id(redmi.fp))
print("lava.fp ",id(lava.fp))
print("realme.fp ",id(realme.fp))

print("modifying by object name like redmi ")
redmi.fp="not working"

print()
print("Mobile.fp ",Mobile.fp)
print("redmi.fp ",redmi.fp)
print("lava.fp ",lava.fp)
print("realme.fp ",realme.fp)

print("modifying by class name like Mobile ")
Mobile.fp="Y"
print()
print("Mobile.fp ",Mobile.fp)
print("redmi.fp ",redmi.fp)
print("lava.fp ",lava.fp)
print("realme.fp ",realme.fp)

print()
print("Mobile.fp ",id(Mobile.fp))
print("redmi.fp ",id(redmi.fp))
print("lava.fp ",id(lava.fp))
print("realme.fp ",id(realme.fp))




