# -*- coding: utf-8 -*-
"""2416.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fjt7r2vyemt0m_vfTRPh7XSVYpAEvjdf
"""

'''
첫번째 줄에 SNS를 이용하는 학생수 n(2 <= n <= 150)이 입력된다.
n 줄에 걸쳐서 각 학생들의 정보가 다음과 같이 쉼표(,)로 구분되어 입력된다.
이름,성별,나이,친구1,친구2,친구3,...친구10
*학생들의 이름은 모두 다르다.
*친구의 수는 최소 1명에서 최대 10명이다.
마지막 줄에 A학생의 이름이 입력된다.


첫 줄에 A학생의 남자 친구들의 수
두번째 줄에 A학생의 여자 친구들의 수.
'''

a=input()
a=int(a)
b=0
d={}
while b<a:
  k1=[]
  k1=input().strip().split(",")
  j=len(k1)
  f=[]
  for i in range(1,j):
    f.append(k1[i])
  d[k1[0]]=f
  b=b+1

e=input()
t=d[e]
M=0
F=0
for i in range(2,len(t)):
  k=t[i]
  if d[k][0]=="M":
    M=M+1
  elif d[k][0]=="F":
    F=F+1
print(M)
print(F)