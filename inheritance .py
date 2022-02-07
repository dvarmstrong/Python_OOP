

class Person:
    def __init__(self,name, age) -> None:
        self.name = name 
        self.age = age
        self.normal_citizen =True

    def greeting(self):
        print(f"Hi my name is {self.name}")
        return self


person_one = Person("Bob Ross", 60)
person_two = Person("Lucille Ball", 85)
person_two.greeting()



class Superstar(Person):
    def __init__(self, real_name, age, stage_name, catchphrase):
        super().__init__(real_name, age)

        self.stage_name = stage_name
        self.catchphrase = catchphrase
        self.normal_citizen = False


superstar_one = Superstar("Paul David", 61, "Bono", "Its a great day")
superstar_one = Superstar("Gwen Stefani", 25, "Gwen", "Yay")






