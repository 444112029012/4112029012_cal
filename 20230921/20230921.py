# -*- coding: utf-8 -*-
"""20230921.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jp47QFw6k1Fq_0WngSliwFxEgccn1t_Q
"""

import os
import shutil
import time
def inf():
    a = os.path.getsize("CS/homework.txt")
    b = os.path.getmtime("CS/homework.txt")
    b = time.ctime(b)
    print(a, b)
if os.path.exists("CS"):
    shutil.rmtree("CS")
os.mkdir("CS")
file_1 = open("homework.txt", "w")
with open("homework.txt", "w") as file_1:
    file_1.write("4112029012, 王昱殊")
shutil.move("homework.txt", "CS")
file_1 = open("CS/homework.txt", "r")
content = file_1.read()
print(content)
inf()
shutil.rmtree("CS")