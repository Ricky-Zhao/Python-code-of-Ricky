#!/usr/bin/python
# -*- coding: UTF-8 -*-
#by ZhiQiang Zhao in NUAA  email:ZhiqiangZhao55@163.com
#Kx Ky，energy for 3D band structure:
#the Conversion relationship of Inverted space with Real space
###############################倒格矢计算公式##############################################

import os
import numpy as np
import math
'''
b1 = 2 π ( a2 × a3) /ν
b2 = 2 π ( a3 × a1) /ν
b3 = 2 π ( a1 × a2) /ν
v=a1.a2×a3
'''
##############################定义一个函数计算向量叉乘积######################################

def Vector_fork(a,b):
	a1=a[0];a2=a[1];a3=a[2];
	b1=b[0];b2=b[1];b3=b[2];
	c=[a2*b3-a3*b2,a3*b1-a1*b3,a1*b2-a2*b1] #c=a×b
	return c

#############################读取POSCAR下的晶格基矢a1、a2、a3##################################

f1=open("./POSCAR",'r')
a=list()
p=0
while(p<7):
	p+=1
	line1=f1.readline()
	arr=line1.split()
	if(p in np.arange(3,6,1)):
		a.append(arr[0:3])
f1.close
#a1=a[0];a2=a[1];a3=a[2];
a1 = [ float(x) for x in a[0] ];a2 =[ float(x) for x in a[1] ];a3 = [ float(x) for x in a[2] ];

#############################计算倒格矢：b1，b2,b3#############################################

v0=Vector_fork(a2,a3)
V=np.inner(np.array(v0),np.array(a1))  
b1=(2*math.pi/V)*np.array(Vector_fork(a2,a3))
b2=(2*math.pi/V)*np.array(Vector_fork(a3,a1))
b3=(2*math.pi/V)*np.array(Vector_fork(a1,a2))

##############################从band下的DOSCAR中读取费米能级####################################

f2=open("./DOSCAR",'r')
q=0
while (q<7):
	q+=1
	line2=f2.readline()
	arr=line2.split()
	if(q==6):
		fermi=float(arr[3])
f2.close
print("费米能级为: "+str(fermi))

###################################读取能带数目#################################################

f3=open("./EIGENVAL",'r')
q=0
while (q<7):
	q+=1
	line3=f3.readline()
	arr=line3.split()
	if(q==6):
		global Nbands
		Nbands=int(arr[2])
f3.close
print("能带条数为: "+str(Nbands))

###################################计算文件的总行数#############################################

Nlines = len(f3.readlines())
print("文件总行数为: "+str(Nlines))
f3.close

#########################读取EIGENVAL中每条带的能量值和各个K点笛卡尔坐标########################

i=0
j=0
K=open('./K.txt','w') #'w' means the mode of covering
en=open('./energy.txt','w')
f3=open("./EIGENVAL",'r')

while True:
	i+=1
	if(i!=(Nlines+1)):
		line4=f3.readline()
		arr=line4.split()
			
		if	(i in np.arange(8, (Nlines+1), (Nbands+2))):
			x=float(arr[0]);y=float(arr[1]);z=float(arr[2])
			num=[x,y,z]  #define a list named 'num'
			A=np.mat(num)
			B=np.mat([b1,b2,b3])#倒格子基矢矩阵			
			C=A*B
			l=float(C[:,0]);m=float(C[:,1]);n=float(C[:,2])
			K.writelines('{0:.8f}   {1:.8f}   {2:.8f}'.format(l,m,n)+'\n')
			
		elif(i in np.arange((9+(Nbands+2)*j),((9+Nbands)+(Nbands+2)*j),1)):
			energy=float(arr[1])
			ener=energy-fermi
			en.writelines('{0:.8f}'.format(ener)+'\t')
			
		elif(i==((9+Nbands)+(Nbands+2)*j)):
			j+=1
			en.writelines('\n')
	else:
		break
K.close
en.close
f3.close		

###########################################
	
	
	
	
	