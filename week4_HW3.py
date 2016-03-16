#!/user/bin/eve python
#encoding: utf-8

f=open('input.txt')

cont=f.readline()

print '此文件裡共有',cont.count(' '),'個空白鍵'
print '此文件裡共有',cont.count('e'),'個字母 e'
print '此文件裡共有',len(cont),'個字元'

a=float(cont.count(' '))/float(len(cont))
b=float(cont.count('e'))/float(len(cont))

print '空白鍵佔總文件%f' %a
print '字母 e佔總文件%f' %b