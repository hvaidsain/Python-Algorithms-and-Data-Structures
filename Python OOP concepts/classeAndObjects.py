class Computer:

    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu


    def details(self):
        print('Computer configuration is ram:{}gb, cpu:{}'.format(self.ram,self.cpu))

comp1 = Computer(8,"intel")
comp2 = Computer(16,"amd")

comp1.details()
comp2.details()

