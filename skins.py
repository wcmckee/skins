# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageChops
from PIL import ImageFilter
import random
import os
import sys

# <codecell>

os.chdir('/home/will/Desktop/skins')

# <codecell>

imagRancz = random.choice(os.listdir('/home/will/Desktop/skins'))

# <codecell>


imagRandz = random.choice(os.listdir('/home/will/Desktop/skins'))

# <codecell>

imagRanxz = random.choice(os.listdir('/home/will/Desktop/skins'))

# <codecell>

imagCook = random.choice(os.listdir('/home/will/Desktop/cook'))

# <codecell>


# <codecell>


# <codecell>

print(imagRandz)

# <codecell>

iimg = Image.open(imagRanxz)

# <codecell>

iimg2 = Image.open(imagRandz)

# <codecell>

iimg5 = Image.open(imagRancz)

# <codecell>


# <codecell>

iimg5.show()

# <codecell>

iimg3 = ImageChops.difference(iimg, iimg2)

# <codecell>

iimg8 = ImageChops.difference(iimg3, iimg2)

# <codecell>

iimg8.show()

# <codecell>

print iimg8.size

# <codecell>

iimg9swap = iimg8.rotate(180)

# <codecell>

iimg9swap.show()

# <codecell>

iimg3.show()

# <codecell>

iimg5 = ImageChops.darker(iimg5, iimg3)

# <codecell>

img6 = ImageChops.blend(iimg5, iimg, .5)

# <codecell>

img6.show()

# <codecell>

iimg5.show()

# <codecell>


# <codecell>

randNumz = random.randint(1,10)

# <codecell>

os.chdir('/home/will/Desktop/cook')

# <codecell>

showCook = Image.open(imagCook)

# <codecell>


# <codecell>

import sys

# <codecell>

os.chdir('/home/will/Desktop/output')

# <codecell>

iimg3.save('image3.jpg')
img6.save('image6.jpg')
iimg5.save(imagRanxz)

# <codecell>

ls

# <codecell>


# <codecell>

img3blur = iimg3.filter(ImageFilter.BLUR)

# <codecell>

img3blur.show()

# <codecell>

img3other = iimg3.filter(ImageFilter.GaussianBlur)
img3other.show()

# <codecell>

print img3other.format, img3other.size, img3other.mode

# <codecell>

resize = (1920, 1080)

# <codecell>

img3other.resize(resize)
img3other.save('large.jpg')
img3other.show()

# <codecell>

ls

# <codecell>

largeImg3 = Image.open('large.jpg')

# <codecell>

largeImg3.format, img3other.size, img3other.mode

# <headingcell level=1>

# hello there 

# <markdowncell>

# this is a test 

# <codecell>

img7 = ImageChops.invert(img6)
img7.show()

# <codecell>

img7.save(imagRandz)

# <codecell>

enchane = ImageEnhance.Brightness(iimg)
blendz = enchane.enhance(3)
blendz.show()

# <codecell>

print randNumz

# <headingcell level=5>

# Create ward room numbers

# <codecell>

wardRooms = range(1,11)

# <codecell>

print wardRooms

# <codecell>

wardRooms.append('b')

# <codecell>

print wardRooms

# <codecell>

for data in enumerate(wardRooms):
    print data

# <codecell>

for info in wardRooms:
    print info

# <codecell>

wardRooms * 4

# <codecell>

startWard = range(1,13)

# <codecell>

print startWard

# <codecell>

startWard.extend('a')

# <codecell>

print startWard

# <codecell>

startWard * 4

# <codecell>

roomLet = ['a','b','c','d']

# <codecell>

print 'a' * 12

# <codecell>

print roomLet

# <codecell>

roomLet * 12

# <codecell>

startWard.append(roomLet)

# <codecell>

print startWard

# <codecell>

roomZero =  startWard[0]

# <codecell>

myStr = str(roomZero)

# <codecell>

roomLetter = printroom[0]

# <codecell>

roomStr = str(roomLetter)

# <codecell>

finalNum = myStr + roomStr

# <codecell>


# <codecell>

SatBreak = ['wheetbix', 'cornflakes', 'porridge']
MilkType = ['blue', 'light', 'soy']
BreadType = ['wholemeal', 'white']
BreadToast = [True, False]
HaveButter = [True, False]
SpreadType  = ['peanut butter', 'jam', 'honey']
NumToast = [0,1,2,3]

# <codecell>

print NumToast

# <codecell>

import random

# <codecell>

dry = random.choice(SatBreak)

# <codecell>

dry

# <codecell>

milk = random.choice(MilkType)

# <codecell>

print milk

# <codecell>

bType = random.choice(BreadType)

# <codecell>

print bType

# <codecell>

NumbToas = random.randint(1,3)

# <codecell>

print NumbToas

# <codecell>

class MenuItems():
    def sayHello():
        print ('hello')

# <codecell>

MenuItems.sayHello()

# <headingcell level=1>

#  I HATE SPORT

# <codecell>

spread = random.choice(SpreadType)

# <codecell>

spread

# <codecell>

BreakLast = []

# <codecell>

BreakLast.append(dry)

# <codecell>

BreakLast.append(milk)

# <codecell>

BreakLast.append(bType)

# <codecell>

BreakLast.append(spread)

# <codecell>

print BreakLast

# <codecell>

for data in BreakLast:
    BreakLast.append('test')

# <codecell>

print BreakLast

# <codecell>

ls

# <codecell>

cassie = random.choice(os.listdir('/home/will/Desktop/output'))

# <codecell>

print cassie

# <codecell>

mixCas = Image.open(cassie)

# <codecell>

mixCas.show()

# <codecell>

mixCok = ImageChops.blend(iimg, mixCas, .5)

# <codecell>

mixCok.show()

# <codecell>

os.chdir('/home/will/Desktop/wirepil')

# <codecell>

ls

# <codecell>

import json

# <codecell>

wirePil = open('wirePIL.ipynb')

# <codecell>

import PIL

# <markdowncell>

# How can I read a ipynb as a JSON object like I do normal JSON objects?

# <codecell>

wirePil(0,80)

# <codecell>

PIL.ImageFilter.FIND_EDGES()

# <codecell>

PIL.ImageFilter.BLUR()

# <codecell>

MenuSize = ['small', 'med', 'large']

# <codecell>

optionOne = ['chicken stir-fry', 'beef lasagne', 'vegetable lasagne']

# <codecell>

mainMeal = random.choice(optionOne)

# <codecell>

mashedPotato = [True, False]

# <codecell>

seasonVege = [True, False]

# <codecell>

salt = [True, False]

# <codecell>

saltChoice = random.choice(salt)

# <codecell>

print saltChoice

# <codecell>

random.choice(salt)

# <codecell>

peper = [True, False]

# <codecell>

pepChoice = random.choice(peper)

# <codecell>

puding = ['Fruit ShortCake', 'Melrose Cream', 'Stewed Fruit', 'Jelly & Ice Cream']

# <codecell>

pudChoice = random.choice(puding)

# <codecell>

print pudChoice

# <codecell>

dinerList = []

# <codecell>

dinerList.append('salt: ')

# <codecell>

dinerList.append(saltChoice)

# <codecell>

dinerList

# <codecell>

dinerList.append('pepper: ')

# <codecell>

dinerList.append(pepChoice)

# <codecell>

dinerList

# <codecell>


# <codecell>

dinerList.append('Pudding: ')

# <codecell>

dinerList.append(pudChoice)

# <codecell>

dinerList

# <codecell>

dinerList.append('Dinner: ')

# <codecell>

dinerList.append(mainMeal)

# <codecell>

dinerList

# <codecell>


# <codecell>

dinerList[0]

# <codecell>

patDetail = []

# <codecell>

LastName = ['Mckee', 'Harrison', 'Boyld']

# <codecell>

ward = ['er', 'burns', 'plastic', 'child', 'medical']

# <codecell>

print ward

# <codecell>

ranWard = random.choice(ward)

# <codecell>

print ranWard

# <codecell>

cubeNum = random.randint(1,11)

# <codecell>

cubeNum

# <codecell>

cubeLet = ['a','b','c','d']

# <codecell>

ranCube = random.choice(cubeLet)

# <codecell>

print ranCube

# <codecell>

cubeNum 

# <codecell>

x = str(cubeNum)

# <codecell>

y = str(ranCube)

# <codecell>

roomNumb = x + y

# <codecell>

print roomNumb

# <codecell>


# <codecell>

patDetail.append

# <codecell>


