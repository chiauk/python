#!/usr/bin/eve python
#encoding: utf-8

import random

count=1
first=random.randint(1,100)

num=input('1~100 請輸入你猜的數字>>')

front=1
behind=100

while num!=first:
	if num>first:
		behind=num
		print '現在的範圍是 %d~%d' %(front,behind)
		
	if num<first:
		front=num
		print '現在的範圍是 %d~%d' %(front,behind)

	num=input('請輸入你猜的數字>>')	
	count=count+1

print '恭喜你猜中了!終極密碼是%d，你花了%d次猜對' %(first,count)
	