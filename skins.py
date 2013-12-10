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
import glob

# <codecell>

devInput = ('/home/will/Desktop/video/street')

# <codecell>

os.chdir('/home/will/Desktop/video/street')

# <codecell>

imagRancz = random.choice(os.listdir(devInput))

# <codecell>


imagRandz = random.choice(os.listdir(devInput))

# <codecell>

imagRanxz = random.choice(os.listdir(devInput))

# <codecell>

imagCook = random.choice(os.listdir(devInput))

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


# <codecell>

iimg3 = ImageChops.difference(iimg, iimg2)

# <codecell>

iimg8 = ImageChops.difference(iimg3, iimg2)

# <codecell>


# <codecell>

print iimg8.size

# <codecell>

iimg9swap = iimg8.rotate(180)

# <codecell>


# <codecell>


# <codecell>

iimg5 = ImageChops.darker(iimg5, iimg3)

# <codecell>

img6 = ImageChops.blend(iimg5, iimg, .5)

# <codecell>


# <codecell>


# <codecell>

iimgz7 = ImageChops.darker(iimg5, iimg9swap)

# <codecell>


# <codecell>

iimgz8 = iimgz7.filter(ImageFilter.DETAIL)

# <codecell>


# <codecell>

iimgz2 = ImageChops.blend(iimg5, iimg3, .2)

# <codecell>

imgz10 = iimgz2.filter(ImageFilter.CONTOUR)

# <codecell>

InImgz10 = ImageChops.invert(imgz10)

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

randNumz = random.randint(1,10)

# <codecell>

os.chdir('/home/will/Desktop/output')

# <codecell>

iimg3.save(imagRancz)
img6.save(imagCook)
iimg5.save(imagRanxz)

# <codecell>

img7 = ImageChops.invert(img6)

# <codecell>

img7.save(imagRandz)

# <codecell>

enchane = ImageEnhance.Brightness(iimg)
blendz = enchane.enhance(2)

# <codecell>

bluzImage = ImageChops.blend(iimgz2, iimg5, .3)

# <codecell>

print randNumz

# <codecell>

cassie = random.choice(os.listdir('/home/will/Desktop/output'))

# <codecell>

print cassie

# <codecell>

mixCas = Image.open(cassie)

# <codecell>

mixCok = ImageChops.blend(iimg, mixCas, .5)

# <codecell>

os.chdir('/home/will/Desktop/arcticMonkeys/')

# <codecell>

cassie = random.choice(os.listdir('/home/will/Desktop/arcticMonkeys'))

# <codecell>

cassie2 = random.choice(os.listdir('/home/will/Desktop/arcticMonkeys'))

# <codecell>

cassie3 = random.choice(os.listdir('/home/will/Desktop/arcticMonkeys'))

# <codecell>

arcImage = Image.open(cassie)

# <codecell>

arcImage2 = Image.open(cassie2)

# <codecell>

arcImage3 = Image.open(cassie3)

# <codecell>

os.chdir('/home/will/Desktop/arcOut/')

# <codecell>

arcSwap = ImageChops.blend(arcImage, arcImage2, .5)

# <codecell>


arcSwap.save(cassie)

# <codecell>

arcBlend = ImageChops.darker(arcSwap, arcImage2)
arcBlend.save(cassie2)

# <codecell>

arcCompo = ImageChops.blend(arcImage2, arcImage3, .8)

# <codecell>


arcCompo.save(cassie3)

# <codecell>


