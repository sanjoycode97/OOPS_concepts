class Mobile:
    fp="working"

    @classmethod
    def cls_method(cls,r):
        cls.r=r
        print(f"access by class method var1 {cls.fp} and {cls.r} ")


redmi=Mobile()
redmi.cls_method(10)