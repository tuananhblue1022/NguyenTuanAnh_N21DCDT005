from collections import deque
import time

class AnimalShelter:
    def __init__(self):
        self.dog_queue = deque()
        self.cat_queue = deque()
        self.timestamp = 0  
    class Animal:
        def __init__(self, species):
            self.species = species
            self.timestamp = None

    def enqueue(self, species):
        animal = self.Animal(species)
        animal.timestamp = self.timestamp
        self.timestamp += 1
        if species == 'dog':
            self.dog_queue.append(animal)
        elif species == 'cat':
            self.cat_queue.append(animal)

    def dequeueAny(self):
        if not self.dog_queue:
            return self.dequeueCat()
        elif not self.cat_queue:
            return self.dequeueDog()
        else:
            if self.dog_queue[0].timestamp < self.cat_queue[0].timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()

    def dequeueDog(self):
        if self.dog_queue:
            return self.dog_queue.popleft().species
        else:
            return None

    def dequeueCat(self):
        if self.cat_queue:
            return self.cat_queue.popleft().species
        else:
            return None

# Example usage:
shelter = AnimalShelter()
shelter.enqueue('cat')
shelter.enqueue('dog')
shelter.enqueue('cat')
shelter.enqueue('dog')

print(shelter.dequeueAny()) 
print(shelter.dequeueDog())  
print(shelter.dequeueAny())  
print(shelter.dequeueCat()) 
