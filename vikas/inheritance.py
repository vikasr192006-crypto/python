class animal:
    def speak(self):
        print("this animal make a sound")
class dog(animal):
    def speak(self):
        print("the dog barks")

dog = dog()
dog.speak()

