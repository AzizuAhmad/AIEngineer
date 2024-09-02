class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    
    def doWork(self):
        if self.occupation == "tennis player":
            print(self.name,"play tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")

    def speaks(self):
        print(self.name,"says how are you ?")

tom = Human("tom cruise","actor")
tom.doWork()
tom.speaks()