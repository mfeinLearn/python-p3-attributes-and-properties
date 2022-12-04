#!/usr/bin/env python3

class Dog:

    def get_name(self):
        return self._name

    def set_name(self, name):
        if (name == "" or type(name) in (int, float) or len(name) > 25 or len(name) <= 1):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if breed in approved_breeds:
            self._breed = breed
        else: 
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
