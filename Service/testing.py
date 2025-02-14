class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    pass  # Humans work and eat

class Robot(Workable):
    def rotating(self):

        pass  # Robots only work

class sai(Human):
    def work(self):
        print("sai working")
    def eat(self):
        print("sai is eating")

class chitti(Robot):
    def rotating(self):

    def eat (self):
        print("chititi is eating")

y = chitti()
y.eat()
