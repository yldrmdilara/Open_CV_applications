#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle 
image = cv2.imread('/Users/Dilara/Downloads/gökkusagi.jpg')

# Görüntüyü gri tonlamaya çevir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Orijinal Görüntü")

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Gri Tonlamalı Görüntü")

plt.tight_layout()
plt.show()


# In[ ]:




