#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
10의 자릿수와 1의 자릿수를 서로 바꾸고, 거기에 2를 곱한다.
예) 70일 경우 14가 된다.( 70 -> 07 -> 14 )
이 알고리즘은 때로는 부작용을 일으켜 휴지통의 내용이 더 많아 질지도 모른다.
만약 이 알고리즘의 심각한 부작용으로 수치가 100이 넘는다면 100의 자릿수는 무시된다.

첫째 줄에 휴지통을 압축했을 때 양을 출력한다.
둘째 줄에 그 양이 50이하이면 GOOD 을 출력하고, 
50을 넘으면 OH MY GOD 을 출력한다.
'''
a=input()
a=str(a)
if len(a)==2:
    a1=a[0]
    a2=a[1]
    a3=a2+a1
    a3=int(a3)
    if a3*2<100:
        if int(a3)*2<=50:
            print(int(a3)*2)
            print('GOOD')
        else:
            print(int(a3)*2)
            print('OH MY GOD')
    else: 
        if int(a3)*2-100<=50:
            print(int(a3)*2-100)
            print('GOOD')
        else:
            print(int(a3)*2-100)
            print('OH MY GOD')
else:
    if int(a)*20<100:
        if int(a)*20<=50:
            print(int(a)*20)
            print('GOOD')
        else:
            print(int(a)*20)
            print('OH MY GOD')
    else:
        if int(a)*20-100<=50:
            print(int(a)*20-100)
            print('GOOD')
        else:
            print(int(a)*20-100)
            print('OH MY GOD')
        

    


# In[ ]:





# In[ ]:




