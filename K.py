#!/usr/bin/python
# -*- coding: UTF-8 -*-
#by ZhiQiang Zhao  email:ZhiqiangZhao55@163.com
#KPOINTS for 3D band structure:
#########################################################
import os
import numpy as np
import math
'''
b1 = 2 π ( a2 × a3) /ν
b2 = 2 π ( a3 × a1) /ν
b3 = 2 π ( a1 × a2) /ν
v=a1.a2×a3
'''
##############################

def Vector_fork(a,b):
	a1=a[0];a2=a[1];a3=a[2];
	b1=b[0];b2=b[1];b3=b[2];
	c=[a2*b3-a3*b2,a3*b1-a1*b3,a1*b2-a2*b1] #c=a×b
	return c

###########################

path1="./POSCAR"
f1=open(path1,'r')

a=list()
p=0
while(p<7):
	p+=1
	line=f1.readline()
	arr=line.split()
	if(p in np.arange(3,6,1)):
		a.append(arr[0:3])
		
a1 = [ float(x) for x in a[0] ]
a2 = [ float(x) for x in a[1] ]
a3 = [ float(x) for x in a[2] ]


v0=Vector_fork(a2,a3) 
V=np.inner(np.array(v0),np.array(a1))  
b1=(2*math.pi/V)*np.array(Vector_fork(a2,a3))
b2=(2*math.pi/V)*np.array(Vector_fork(a3,a1))
b3=(2*math.pi/V)*np.array(Vector_fork(a1,a2))
f1.close
#print(b1,b2,b3)
#####################################################

a=input("Please input the precision of the Kpoints:")

xmin=-0.68;xmax=0.68;
zmin=0.3;zmax=1.06;
y=0


h1='k-points along high symmetry lines'
knumber=((xmax-xmin)/a+1)*((zmax-zmin)/a+1)
h2='Reciprocal lattice'

f2=open('./KPOINTS','w')
f2.write(str(h1)+'\n'+'	 '+str(int(knumber))+'\n'+str(h2)+'\n')

for x in np.arange(xmin,(xmax+a), a):

	for z in np.arange(zmin,(zmax+a), a):
	
		num=[x,y,z]
		A=np.mat(num)
		B=np.mat([b1,b2,b3])
		B1=np.linalg.inv(B)#
		C=A*B1
		l=float(C[:,0]);m=float(C[:,1]);n=float(C[:,2])
		f2.writelines('	 {0:.5f} {1:.5f} {2:.5f}   {3:.0f}'.format(l,m,n,1)+'\n')
		
f2.close
