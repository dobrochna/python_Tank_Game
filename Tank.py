class Tank(object):
    def __init__(self,name):
        self.name = name
        self.alive = True
        self.amo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %ishells)" % (self.name, self.armor, self.amo)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        if self.amo >=1:
            self.amo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit!")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")
