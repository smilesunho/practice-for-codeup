# -*- coding: utf-8 -*-
"""2411.ipynb

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

첫 번째 줄에 남학생의 수
두 번째 줄에 여학생의 수
'''
a=input()
a=int(a)
b=0
c=0
d=0
while b<a:
  k1=input().strip().split(",")
  if k1[1]=="F":
    c=c+1
  elif k1[1]=="M":
    d=d+1
  b=b+1
print(d)
print(c)