#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy


# In[ ]:


a= cv2.imread("C:/Users/Ritesh/Downloads/bright.jpg")


# In[ ]:


a.shape


# In[ ]:


cv2.imshow("pixel",a)
a1=cv2.resize("pixel",400,300)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:


cv2.imshow("pixel",a)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:


gray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)


# In[ ]:


cv2.imshow("pixel",gray)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:


Sum = []


# In[ ]:


(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
#image=cv2.rectangle(a,maxLoc,[0,255,0],2)
image = cv2.circle(a, maxLoc, 20, (0, 0, 255), 2)
#cv2.imshow("Naive",a )
#cv2.waitKey()
#cv2.destroyAllWindows()


# In[ ]:


temp2 = a[2000:,1300:]


# In[ ]:



cv2.imshow("Naive",temp2 )
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import cv2
import numpy


# In[2]:


a= cv2.imread("C:/Users/Ritesh/Downloads/bright.jpg")
a.shape


# In[3]:


gray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)


# In[4]:


(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)


# In[11]:


image = cv2.circle(a, maxLoc, 20, (0, 0,255), 2)


# In[12]:


temp2 = a[2000:,1300:]


# In[13]:


cv2.imshow("Brigtest spot",temp2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




