#!/usr/bin/env python
# coding: utf-8

# In[1]:


file_name = "words_alpha.txt"

with open(file_name, encoding="utf-8") as f:
    data_lines = f.read()
data_lines = data_lines.split('\n')

namelist = list(set(data_lines))

password = input("パスワードを英字で入力してください")
import string
#アルファベットの大文字のみの出力
abc = list(string.ascii_uppercase)
df = list(password)
a = []
for x in range(len(list(password))):
    for y in range(len(list(string.ascii_uppercase))):
        if df[x].find(abc[y]) == 0:
            a.append(y)
            break

answer = []
for z in range(26):
    
    lists = []
    b = []
    aps = ""
    for i in range(len(a)):
        b.append((a[i]+z)%26)
    for x in range(len(list(password))):
        aps += abc[b[x]]
    for x in range(len(namelist)):   
        if aps.lower().find(namelist[x]) != -1:
            lists.append(namelist[x])
    answer.append(len(lists))
    
aps = ""
b = []
ans = answer.index((max(answer)))
for i in range(len(a)):
    b.append((a[i]+ans)%26)
for x in range(len(list(password))):
        aps += abc[b[x]]
        
print("The result is n=",26-ans,"The sentence is",aps)


# In[ ]:




