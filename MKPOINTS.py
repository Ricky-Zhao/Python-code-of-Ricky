#!/usr/bin/python
# -*- coding: UTF-8 -*-
#by ZhiQiang Zhao  email:ZhiqiangZhao55@163.com
#a simple code is used to get the KPOINTS file for energy band calculation

import os
import numpy as np

f1=open("./HPoints",'r')
Nlines = len(open("./HPoints",'r').readlines())
f1.close

f2=open("./HPoints",'r')
K=open('./KPOINTS','w')


h1='k-points along high symmetry lines'
h2=input("numbers of points:")  
h3='Line-Mode \nReciprocal'
K.write(str(h1)+'\n'+'	 '+str(int(h2))+'\n'+str(h3)+'\n')

a=0
while True:
	a+=1
	line=f2.readline() 
	if(line!=''):

		if(a in np.arange(2, Nlines,1)):
			K.writelines(' '+str(line)+'\n'+' '+str(line))
		
		else:
			K.writelines(' '+str(line))
	else:
		break
f2.close