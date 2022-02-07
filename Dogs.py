


class Dog :
    species = "Cannis familiaris" #Class attribute 

    def __init__(self, name, age) :
        self.name  = name               #Instance attributes 
        self.age = age                  #Instance attributes 


    #Instance method
    def _str_(self):
        print (f"{self.name} is {self.age} years old")
        
        
        


    # Instance method to speak 
    def speak(self, sound):
        print( f"{self.name} says {sound}")
        return self
        



buddy = Dog("Buddy", 3)
tiger = Dog("tiger", 9)


tiger.speak("roar")
buddy.speak("meaow")

print(tiger.name)
print(tiger._str_())
