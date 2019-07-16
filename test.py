#!/usr/bin/python
#coding=utf-8

#!/usr/bin/python
# -*- coding: UTF-8 -*-

#cgi
print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello World - 我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>'
print '</body>'
print '</html>'

#import os
#import random
#import sys
#import time
#
#print("你好，世界");
##raw_input("按下 enter 键退出，其他任意键显示...\n");
#
#counter=1000;
#miles=100.0;
#name='John';
#print(name[1:4]);
#print(counter);
#print(miles);
#print(name);
#
#test={};
#test[0]='this is one';
#test['two']='this is two';
#dict={'counter':1000,'miles':100.0,'name':'John'};
#print(test[0]);
#print(test['two']);
#print(dict.keys());
#print(dict.values());
#
#a = 21
#b = 10
#c = 0
# 
#c = a + b;
##print ("1 - c 的值为："),c;
#print "1 - c 的值为：",c;
#
#if a==b :
#    print "1 - a等于b";
#else:
#    print "1 - a不等于b";
#	
#a=1;
#while  a < 7:
#    if a%2 == 0 :
#        print a,'是偶数';
#    else:
#        print a,'是奇数';
#    a +=1;		
#
## 一个简单的条件循环语句实现汉诺塔问题
#
#def my_print(args):
#    print args
#
#def move(n, a, b, c):
#    my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))
#move (3, 'a', 'b', 'c')
#
## 类stwich
#def zero():
#    return 'zero';
#
#def one():
#    return 'one';
#
#def two():
#    return 'two';
#
#def num2str(arg):
#    switcher={0:zero,1:one,2:two,3:lambda:'three'};
#    func=switcher.get(arg,lambda:'nothing');
#    return func();
#if __name__ == '__main__':
#    print num2str(4);
	
#猜大小
#s = int(random.uniform(1,100));
#m = int(input('请输入整数:'));
#
#while m != s:
#    if m > s:
#        print('大了')
#        m = int(input('请输入整数:'))
#    if m < s:
#        print('小了')
#        m = int(input('请输入整数:'))
#    if m == s:
#		print('OK!是否继续:1-是,2-否')
#		n = int(input('请输入:'))
#		if n == 1:
#		    s = int(random.uniform(1,100));
#		    m = int(input('请输入整数:'));
# 	        continue;	

#猜拳
#while 1:
#    s = int(random.uniform(1,4));
#    if s == 1:
#       n = '石头';
#    elif s == 2:
#       n = '剪刀';
#    elif s == 3:
#       n = '布';	
#    m = raw_input('输入 石头、剪子、布,输入"end"结束游戏:');
#    blist = ['石头','剪刀','布'];
#    if m == 'end':
#       break;
#    elif (m not in blist ) and (m !='end'):
#       print '输入错误,请重新输入!';
#    elif (m == n):
#	   print '电脑出了:'+ n +',平局!';
#    elif (m =='石头' and n == '剪刀') or (m =='剪刀' and n == '布') or (m =='布' and n == '石头'):
#       print '电脑出了:'+ n	+',你赢了!';
#    elif (m =='石头' and n == '布') or (m =='剪刀' and n == '石头') or (m =='布' and n == '剪刀'):
#       print '电脑出了:'+ n	+',你输了!';

#摇骰子
#print '摇骰子游戏,开始';
#result = [];
#while True : 
#    result.append(int(random.uniform(1,7)));
#    result.append(int(random.uniform(1,7)));
#    result.append(int(random.uniform(1,7)));
#    count = 0;
#    index = 2;
#    pointstr = '';
#    while index >= 0:
#         count += result[index];
#         pointstr += ' ';
#         pointstr += str(result[index]);
#         index -= 1;
#		 
#    if count <= 11:
#        sys.stdout.write(pointstr + " -> " + str(count) + " -> 小" + "\n");
#    else:
#        sys.stdout.write(pointstr + " -> " + str(count) + " -> 大" + "\n");
#    result = [];
#    clist = ['c','C'];
#    qlist = ['q','Q'];
#    keystr = raw_input('c键继续,q键退出:');
#    while (keystr not in clist) and (keystr not in qlist):
#        keystr = raw_input('按键不对,请重新输入:');		
#    if keystr in qlist :
#	   break;
#    elif keystr in clist :
#	   continue;

#十进制转二进制
#denum = input('输入十进制数:');
#print denum,'(10)',
#blist=[];
#while denum > 0:
#    blist.append(str(denum % 2));
#    denum //= 2;
#print '=',
#while len(blist)>0:
#    sys.stdout.write(blist.pop()) # 无空格输出print '(2)'

#九九乘法表
#i = 0;
#j = 0;
#for i in range(1,10):
#    for j in range(1,10):
#	   print j ,'*', i ,'=', i*j ,
#	   if  i== j:
#	      print '\n'; 
#	      break;		  

#去除字符串首尾的空格
#def trim(s):
#   while s[:1] == ' ':
#      s = s[1:];
#   while s[-1:] == ' ':
#      s = s[:-1];
#   return s;  
#str = '  aaa  ';
#print trim(str);

#1-30质数
#for num in range(1,31):
#   if num==1:
#      print '1既不是质数也不是合数';
#      continue;
#   ilist = [];
#   j=0;
#   for i in range(2,num):
#      if num%i == 0:
#         j=num/i;
#         ilist.append(i);	 
#   if j == 0 :
#      print num, '是一个质数';
#   else :
#	   print num,ilist;

# 打印空心等边三角形 
#rows = int(raw_input('输入行数：'))
#for i in range(0, rows):
#    for k in range(0, 2 * rows - 1):
#        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
#            print " * ",
#        elif i == rows - 1:
#            if k % 2 == 0:
#                print " * ",
#            else:
#                print "   ",
#        else:
#            print "   ",
#    print "\n"