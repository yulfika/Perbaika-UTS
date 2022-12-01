#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
email = input('Masukan Email anda : ')
pos_at = 0
pos_titik = 0
pos_at = email.find('@')
pos_titik = email.find('.')
print(pos_at < pos_titik)


# In[2]:


#2
kalimat = input('Masukan Kalimat : ')
i = 0
kata = ''
for i in range (len(kalimat)):
    if kalimat[i] == 'a' or kalimat [i] == 'A':
        kata = kata + '4'
    elif kalimat [i] == 'e' or kalimat [i] == 'E':
        kata = kata + '3'
    elif kalimat [i] == 'L':
        kata = kata + '7'
    elif kalimat [i] == 'S':
        kata = kata + '5'
    else:
        kata = kata + kalimat [i]
print(kata)

