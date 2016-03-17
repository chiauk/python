#!/usr/bin/eve python
#encoding: utf-8

def isPrime(N):
	x=1
	sum=0

	while x<=N:
		if N%x==0:
			sum=sum+1
		x=x+1

	global a
	a=1

	if sum==2:
		return a
	else:
		a=0
		return a

total=0

for x in range(2,1000):	
	if isPrime(x)==1:
		total=total+x

print total