#-*-coding:utf-8-*-
# Author:Lu Wei
'''
#有变量name = " aleX leNb " 完成如下操作：
name='aleX leNb '
#1.移除 name 变量对应的值两边的空格,并输出处理结果
name1=name.strip()
print('---->',name1,'<----')
#2.判断 name 变量是否以 "al" 开头,并输出结果（用切片）
name2=name.strip()
if name2[0:2]=='al':
    print('yes,{0}'.format(name2))
else:
    print('NO')
#3.判断name变量是否以"Nb"结尾,并输出结果（用切片）
name3=name
val=len(name3.strip())
if name3[val-2:-1]=='Nb':
    print('yes,{0}'.format(name3))
else:
    print('NO')
#4.将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结
name4=name
print(name4.replace('l','p'))
#5.将name变量对应的值中的第一个"l"替换成"p",并输出结果
name5=name
print(name5.replace('l','p',1))
#6.将 name 变量对应的值根据 所有的"l" 分割,并输出结果
name6=name
print(name6.split('l'))
#7.将name变量对应的值根据第一个"l"分割,并输出结果
name7=name
print(name7.split('l',1))
#8.将 name 变量对应的值变大写,并输出结果
name8=name
print(name8.upper())
#9.将 name 变量对应的值变小写,并输出结果
name9=name
print(name9.lower())
#10.请输出 name 变量对应的值的第 2 个字符?
name10=name
print(name10[1])
#11.请输出 name 变量对应的值的前 3 个字符?
name11=name
print(name11[0:3])
#12.请输出 name 变量对应的值的后 2 个字符?
name12=name
print(name12[-2:])


###有字符串s = "123a4b5c"
s='123a4b5c'
#1.通过对s切片形成新的字符串 "123"
s1=s
print(s1[:3])
#2.通过对s切片形成新的字符串 "a4b"
s2=s
print(s2[3:6])
#3.通过对s切片形成字符串s5,s5 = "c"
s3=s
print(s3[-1])
#4.通过对s切片形成字符串s6,s6 = "ba2"
s4=s
print(s4[-3::-2])


###使用while循环字符串 s="asdfer" 中每个元素。
s="asdfer"
len_new=len(s)
index=0
while index<=len_new-1:
    print(s[index])
    index+=1


#使用while循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s='321'
len_new=len(s)
index=0
while index<=len_new-1:
    print('倒计时%s秒'%(s[index]))
    index+=1
print('go go go')


#实现一个整数加法计算器(两个数相加)：
content = input("请输入内容:").strip()
len_new=len(content)
index=b=0
while index<=len_new-1:
    if content[index].isdigit():
        a=int(content[index])
        index+=1
        b=b+a
    else:
        index += 1
print(b)


#计算用户输入的内容中有几个 h 字符？
content=input('请输入：')
len_new=len(content)
index=count=0
while index<=len_new-1:
    if content[index]=='h':
        count+=1
        index+=1
    else:
        index += 1
print(count)


#计算用户输入的内容中有几个 h 或 H 字符？
content=input('请输入：').lower()
len_new=len(content)
index=count=0
while index<=len_new-1:
    if content[index]=='h':
        count+=1
        index+=1
    else:
        index += 1
print(count)
#-------2------------------
content=input('请输入：')
len_new=len(content)
index=count1=count=0
while index<=len_new-1:
    if content[index]=='h':
        count+=1
        index+=1
    elif content[index]=='H':
        count1+=1
        index+=1
    else:
        index += 1
print(count,count1)

#使用while循环分别正向和反向对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言。" 进行打印。

message = "伤情最是晚凉天，憔悴厮人不堪言。"
len_new=len(message)
index=0
index1=-1
while index<=len_new-1:
        print(message[index])
        index+=1
print(-len_new)
while index1>=-len_new:
    print(message[index1])
    index1-=1


#获取用户输入的内容中 前4个字符中 有几个 A ？
content=input('请输入：')[0:4]
index=count=0
while True:
    if content[index]=='A':
        count+=1
    index+=1
    if index ==4:
        break
print(count)
'''


#获取用户输入的内容，并计算前四位"l"出现几次,并输出结果。













