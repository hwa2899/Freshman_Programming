# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:37:07 2018

@author: Ching
"""

class animal():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def sit(self):
        print(self.name+" sit...")
    def walk(self):
        print(self.name+" walk...")
class dog(animal):
    def __init__(self, name,color):
        super().__init__(name,color)
    def bite(self):
        print(self.name+" bite...")
class bird(animal):
    def __init__(self,name,color):
        super().__init__(name,color)
    def fly(self):
        print(self.name+" fly...")
mydog=dog("dog","yellow")
mydog.sit()
mydog.walk()
mydog.bite()

mybird=bird("bird","white")
mybird.sit()
mybird.walk()
mybird.fly()