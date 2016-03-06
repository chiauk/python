#!user/bin/eve python
#encoding:utf-8

account=raw_input("What's your account?\n")
print "Hello!%s!" %account
print "The balance of your account is $5000."
money=input("How much money do you want to withdraw?\n")

balance=5000-money

f=open("ATM.txt","w")

if balance<0:
	f.write("Balance isn't enough!")
elif balance==0:
	f.write("Balance is 0.")
else:
	f.write("Balance is %d." %balance)

f.close()

