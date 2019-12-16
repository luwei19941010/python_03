#-*-coding:utf-8-*-
# Author:Lu Wei


"""
#################lower() and upper()##############
value='luwei'
new_value=value.upper()
print(new_value)

value='LUWEI'
new_value=value.upper()
print(new_value)


check_code='KtDp'
code=input('请输入验证码：%s -->'%(check_code,))
if code.upper()==check_code.upper():
    print('输入成功')

################isdigit###############

print('''欢迎选择服务：
1.马杀鸡
2.SPA
3.足疗
''')

while True:
    num=input('请输入--->')
    if num.isdigit():
        num=int(num)
        print(num)
    else:
        print('输入有误')



###########strip/rstrip/lstrip###########

user=input('plaese input username:')
new_user=user.rstrip().lstrip()
#new_user=user.strip()
print('------>',new_user,'<-----')



###########replace(替换)###########

message=input('请说话：')
print(message)
data=message.replace('你妹','***',3)
print(data)


########### split 切割###########
message='替换str中的字符,格式replace(old-str , new-str,count),count为从左往右替换几个,默认全部替换'
data=message.split(',')
#data=message.split(',',1)
#data=message.rsplit(',',1)
#data=message.lstrip(',',1)
print(data)

index=0
count=0
data=input('请输入内容：')
data_len=len(data)

while True:
    val=data[index]
    if val.isdigit():
        count+=1
    if index ==data_len-1:
        print(count)
        break
    else:
        index+=1

#############索引##############
val='luwei'
v1=val[1]
print(v1)
v2=val[-1]
print(v2)
"""
#############切片##############
val='luwei'
v1=val[2:5]#前闭后开，索引范围为  2=<索引位置<5
v2=val[2:-1]
v3=val[2:]
v4=val[-3:-1]
print(v4)












