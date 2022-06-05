#!/usr/bin/env python
# coding: utf-8

# In[85]:
'''
첫 번째 줄에 집합 A의 원소의 개수 N이 입력된다.( 1≤N≤100 )
두 번째 줄에 집합 A의 원소가 공백으로 분리되어 오름차순으로 입력된다.(각 원소의 값은 1~200 )
첫 번째 줄에 집합 B의 원소의 개수 M이 입력된다.( 1≤M≤100 )
두 번째 줄에 집합 B의 원소가 공백으로 분리되어 오름차순으로 입력된다.(각 원소의 값은 1~200 )

첫째줄에 교집합의 결과를 공백으로 분리하여 오름차순으로 출력한다. 만약 교집합의 결과가 공집합인경우 0을 출력한다. 0 다음에는 공백을 출력하지 않음에 유의한다.
둘째줄에 합집합의 결과를 공백으로 분리하여 오름차순으로 출력한다.

'''
a=input()
b=input().split(" ")
c=input()
d=input().split(" ")

new_list=[]
for v in b:
    if v in d:
        new_list.append(v)
if len(new_list)==0:
    print("0")
else:
    for i in new_list:
        print ("{}".format(int(i)),end=' ')
    print()

k=sorted(list(map(int,list(set(b+d)))))
for j in k:
    print (int(j), end=" ")

