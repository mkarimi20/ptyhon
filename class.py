class animals:

    def __init__(self,name, age):
        self.name = name
        self.age = age
    def speak(self,sound):
        print(self.name,sound )
dog = animals('dog', 26)
cat = animals('cat', 11)



print(dog.name, dog.age)
print(dog.name, dog.speak("Waq Waq"))


