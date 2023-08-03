print('inheritance')
print('='*60)

class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
    
    def getLegs(self):
        return self._legs
    
    def speak(self):
        print(f'{self.name} syas : Bark!')

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')
    
    def wagTail(self):
        print('Vigorous wagging!!')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()