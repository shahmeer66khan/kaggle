from google.colab import drive
drive.mount("/content/drive")

import pandas as pd
test = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/test.csv')

test

import random as random
id = test["id"]
Test = pd.DataFrame(id)
arr=[]
for row in id:
  arr.append(random.randint(0,1))
Test["target"] = arr
Test.to_csv('red.csv',index = False)