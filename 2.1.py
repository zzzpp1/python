#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a=input("a:")
a=int(a)
#q=[]
if a==1:
    q=[1]
elif a==2:
    q=[1,1]
elif a>=3 :
    q=[1,1]
    for i in range(3,a+1):
        q.append(q[-1]+q[-2])
print(q)
