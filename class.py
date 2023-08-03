print('Class')
print('='*60)

class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
    
    def getLegs(self):
        return self._legs
    
    def speak(self):
        print(f'{self.name} syas : Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())