#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
로또 순위 매기는 방법)

등수	방법
1등	당첨번호 6개 일치
2등	당첨번호 5개 일치 + 보너스번호 일치
3등	5개 번호 일치
4등	4개 번호 일치
5등	3개 번호 일치
꽝	2개 이하 일치
 
첫 줄에 로또 당첨번호 6개와 보너스 번호 1개가 주어진다.
둘째 줄에 지혜가 가지고 있는 로또 번호 6개가 주어진다. 

'''
a=list(map(int,input().strip().split(" ")))
b=list(map(int,input().strip().split(" ")))
c=a.pop()
d=0
for i in range(0,6):
    if b[i] in a:
        d=d+1
if d==6:
    print("1")
elif d==5:
    for i in range(0,6):
        if b[i] not in a:
            if b[i]==c:
                print("2")
            else:
                print("3")
elif d==4:
    print("4")
elif d==3:
    print("5")
else:
    print("0")
        


# In[ ]:





# In[ ]:




