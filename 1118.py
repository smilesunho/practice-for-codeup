# -*- coding: utf-8 -*-
"""1118.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fjt7r2vyemt0m_vfTRPh7XSVYpAEvjdf
"""

'''
삼각형의 넓이를 구하는 프로그램을 작성한다.

삼각형의 넓이 = 밑변 * 높이 / 2

삼각형의 넓이를 소수 첫째자리까지 출력한다..
'''
import numpy as np
a,b=input().split(" ")
a=int(a)
b=int(b)
print('{}'.format(np.round(a*b/2,1)))