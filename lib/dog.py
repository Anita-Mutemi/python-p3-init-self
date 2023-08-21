#!/usr/bin/env python3

class Dog:
    # Remeber that all methods use "self." 
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("Fido")
print(fido.name)
# Fido
print(fido.breed)
#Mutt