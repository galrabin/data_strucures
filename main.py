#! /usr/bin/env python3




class Animal:
    def get_noise(self):
        return self.noise

    def get_color(self):
        return self.color


class Dog(Animal):
    def __init__(self):
        self.noise = 'Haaa'
        self.color = 'Red'

    def get_color(self):
        return "3"

an = Dog()
print(an.get_color())
