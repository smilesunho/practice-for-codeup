# -*- coding: utf-8 -*-
"""2008.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fjt7r2vyemt0m_vfTRPh7XSVYpAEvjdf
"""

'''
첫째 줄에 데이터의 개수 n이 주어진다. (2≤n≤100)
둘째 줄에 n개의 수가 공백으로 분리되어 입력된다.(각각의 수는 1~200인 정수)

수의 순서가 오름차순인 경우 '오름차순', 내림차순인 경우 '내림차순', 둘 다 아닐 경우 '섞임'을 출력한다.
'''
a=input()
a=int(a)
b=list(map(int,input().strip().split(" ")))
c=b.copy()
c.sort(reverse=True)
d=sorted(b)

if c==b and b==d:
  print("섞임")
elif c==b:
  print("내림차순")
elif d==b:
  print("오름차순")
else:
  print("섞임")