#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

주민등록번호 입력시 ‘-’ 문자를 입력하여야 하며 숫자와 이어서 입력한다. (예: 781201-1273845)

연도/월/일, 성별을 출력하여야 하며, 연도는 4자리, 월과 일은 2자리로 출력하고, 1개의 빈칸 뒤에 성별을 출력한다.(예 : 1978/12/01 M)
'''

a,b=input().strip().split("-")
a=str(a)
b=str(b)

if b[0]=='1':
    print("19{0}{1}/{2}{3}/{4}{5} M".format(a[0],a[1],a[2],a[3],a[4],a[5]))
elif b[0]=='2':
    print("19{0}{1}/{2}{3}/{4}{5} F".format(a[0],a[1],a[2],a[3],a[4],a[5]))
elif b[0]=='3':
    print("00{0}{1}/{2}{3}/{4}{5} M".format(a[0],a[1],a[2],a[3],a[4],a[5]))
elif b[0]=='4':
    print("00{0}{1}/{2}{3}/{4}{5} F".format(a[0],a[1],a[2],a[3],a[4],a[5]))


# In[ ]:




