class Student:
    #class variable
    location = "Mumbai"
    def __init__(self,name,roll):
        #instance variables
        self.name = name
        self.roll = roll

    # objectMethod
    def getName(self):
        return self.name

    @classmethod
    #class method...use of decorator @classmethod
    def getLocation(cls):
        return cls.location

    #static method
    @staticmethod

    def printStaticMessage():
        print("This is a static message")


if __name__ == "__main__":
    #all fn works
    
    s1 = Student("harsh",20)
    s2 = Student("nemoy",22)

    print(s1.getName())
    print(s1.getLocation())

    print(Student.getLocation())
    Student.printStaticMessage()
    s1.printStaticMessage()

