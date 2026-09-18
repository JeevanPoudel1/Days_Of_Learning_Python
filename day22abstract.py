class car:
    #abstraction
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print("car started")

car1 =car()
car1.start()


