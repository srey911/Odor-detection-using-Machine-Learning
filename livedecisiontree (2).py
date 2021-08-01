#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


# In[54]:


data = pd.read_csv("ODORDATASETCORRECT.csv")
data = data.rename(columns={'Unnamed: 0': "Target"})


# In[55]:


data


# In[56]:


feature_cols = ['MQ2','MQ3','MQ9','MQ135']
x = data[feature_cols]
y = data.Target


# In[57]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3, random_state = 20)

x_test


# In[58]:


clf = DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)


# In[59]:


print("Accuracy",metrics.accuracy_score(y_test,y_pred))

y_pred,y_test


# In[60]:



import os
try:
  import serial
except ImportError:
  print ("Trying to Install required module: pyserial\n")
  os.system('pip install pyserial')
  import serial
  
import time
#while True:
with serial.Serial('COM3', 9600, timeout=1) as ser:
    time.sleep(2)  
    ser.write(b'A')
    line = str(ser.readline())
    data = line.split(',')
    MQ2 = data[1]
    MQ3 = data[2]
    MQ9 = data[3]
    MQ135 = data[4]
    print(MQ2 + "," + MQ3 + "," + MQ9 + "," + MQ135)
    z = (MQ2 + " " + MQ3 + " " + MQ9 + " " + MQ135)


# In[61]:


z1 = z.split(" ")


z_test = pd.DataFrame(columns = ['MQ2','MQ3','MQ9','MQ135'])
z_test.loc[0] = z1
z_test


# In[62]:


z_pred = clf.predict(z_test)

z_pred[0]


# In[32]:


get_ipython().system('pip install gtts')
get_ipython().system('pip install pyttsx3')
import pyttsx3
from gtts import gTTS
import os
mytext = z_pred[0]
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("result.mp3")
  
# Playing the converted file
os.system("start result.mp3")


# In[ ]:




