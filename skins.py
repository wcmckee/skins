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

effectList = ['difference', 'darker', 'lighter', 'multiply', 'screen']

# <codecell>

lenEff = len(effectList)

# <codecell>

print lenEff

# <codecell>

daChoice = random.choice(effectList)

# <codecell>

print daChoice

# <codecell>

mergeChop = 'ImageChops.' + daChoice

# <codecell>

print mergeChop

# <markdowncell>

# apply this effect to the files

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

iimgz7 = ImageChops.darker(iimg5, iimg9swap)

# <codecell>

iimgz7.show()

# <codecell>

iimgz8 = iimgz7.filter(ImageFilter.DETAIL)

# <codecell>

iimgz8.show()

# <codecell>

iimgz2 = ImageChops.blend(iimg5, iimg3, .2)

# <codecell>

iimgz2.show()

# <codecell>

imgz10 = iimgz2.filter(ImageFilter.CONTOUR)

# <codecell>

imgz10.show()

# <codecell>

InImgz10 = ImageChops.invert(imgz10)

# <codecell>

InImgz10.show()

# <codecell>

fixImg = ImageEnhance.Color(InImgz10)
DieImage = ImageEnhance.Contrast(InImgz10)

# <codecell>

newFix = fixImg.enhance(50)

# <codecell>

dieFix = DieImage.enhance(10)

# <codecell>

blenzImg = ImageChops.difference(dieFix, iimg8)

# <codecell>

blenzImg.show()

# <codecell>

randNumz = random.randint(1,10)

# <codecell>


# <codecell>

os.chdir('/home/will/Desktop/cook')

# <codecell>

showCook = Image.open(imagCook)

# <codecell>

from PIL import ImageFont

# <codecell>


# <codecell>

import sys

# <codecell>

os.chdir('/home/will/Desktop/output')

# <codecell>

iimg3.save(imagRancz)
img6.save(imagCook)
iimg5.save(imagRanxz)

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>

resize = (1920, 1080)

# <codecell>


# <codecell>


# <codecell>


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
blendz = enchane.enhance(2)
blendz.show()

# <codecell>

bluzImage = ImageChops.blend(iimgz2, iimg5, .3)

# <codecell>

bluzImage.show()

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


# <codecell>


# <codecell>


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

os.chdir('/home/will/Desktop/arcticMonkeys/')

# <codecell>

cassie = random.choice(os.listdir('/home/will/Desktop/arcticMonkeys'))

# <codecell>

cassie2 = random.choice(os.listdir('/home/will/Desktop/arcticMonkeys'))

# <codecell>

arcImage = Image.open(cassie)

# <codecell>

arcImage2 = Image.open(cassie2)

# <codecell>

arcSwap = ImageChops.blend(arcImage, arcImage2, .5)

# <codecell>

arcSwap.show()

# <codecell>

arcBlend = ImageChops.darker(arcSwap, arcImage2)
arcBlend.show()

# <codecell>

arcBlur = arcBlend.filter(ImageFilter.BLUR)
arcBlur.show()

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


# <codecell>


# <codecell>


# <codecell>


