# -*- coding: utf-8 -*-
"""1158.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fjt7r2vyemt0m_vfTRPh7XSVYpAEvjdf
"""

'''

공의 위치 n이 정수로 입력됨.(이번에는 정수로 입력됨)
공이 떨어지는 위치 n이 30≤n≤40 이거나 60≤n≤70 이면, win을 출력, 그외에는 lose를 출력한다.
'''
n=input()
n=int(n)
if 30<=n and n<=40:
  print("win")
elif 60<=n and n<=70:
  print("win")
else:
  print("lose")