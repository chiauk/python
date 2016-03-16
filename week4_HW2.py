#!/user/bin/eve python
#encoding: utf-8

num=input('請輸入任一數字>')

x=1
sum=0

while x<=num:
	if num%x==0:
		sum=sum+1
	x=x+1

if sum==2:
	print '%d為一質數' %num
else:
	print '%d不是質數' %num