#!/usr/bin/python
# -*- coding: UTF-8 -*-
#by ZhiQiang Zhao  email:ZhiqiangZhao55@163.com
import os

file=open("./bandstructure.txt",'r')
K=open('./out.txt','w') 
a=0	
b=input("interval:")  #以多少为间隔提取数据

while True:
	a+=1
	line=file.readline()
	arr=line.split()
	if(line!=''):

		if(a==1):
			x=float(arr[0])
			K.writelines('{0:.8f}'.format(x)+'\n')
		elif(a % b == 0):
			y=float(arr[0])
			K.writelines('{0:.8f}'.format(y)+'\n')
		else:
			continue
			
	else:
		break
		

file.close