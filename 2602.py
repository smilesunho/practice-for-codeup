#!/usr/bin/env python
# coding: utf-8

# In[16]:


'''
입력예시
93 94 87 
82 75 91 
78 89 92 
- 첫째 줄에는 1번 학생의 세 과목 점수와 총점
- 둘째 줄에는 2번 학생의 세 과목 점수와 총점
- 셋째 줄에는 3번 학생의 세 과목 점수와 총점
- 넷째 줄에는 각 과목의 합이 출력된다.
'''
a,b,c=map(int,input().strip().split(" "))
a1,b1,c1=map(int,input().strip().split(" "))
a2,b2,c2=map(int,input().strip().split(" "))
print(a, b, c, a+b+c, )
print(a1, b1, c1, a1+b1+c1, )
print(a2, b2, c2, a2+b2+c2, )
print(a+a1+a2, b+b1+b2, c+c1+c2, a+b+c+a1+b1+c1+a2+b2+c2, )

