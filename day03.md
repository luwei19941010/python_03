day03

##### 今日内容

1.整形

2.布尔类型

3.字符串

##### 内容回顾和补充

###### 1.内容回顾

作业：每周写一个思维导图，罗列本周学习的知识点

- ​		xmind

###### 2.补充：

​		运算符

- in 

  ```
  value='我是中国人'
  #判断‘中国’是否在value所代指的字符串中，‘中国’是否是value所代指的字符串的子序列
  '中国' in value
  ```

  

- not in

### 内容详细

##### 1.整型

```
age=18

```

- py2

  - 在32位主机，整数的位数为32位，取值范围为-2^31至2^31

  - 在64位主机，整数的位数为64位，取值范围为-2^64至2^64

  - 超出长度之后就会变成long类型

  - 整除只能保证整数位

    ```
    from _future_ import division
    v=9/2
    print(v)
    ```

    

- py3

  - 只有int

##### 2.布尔型

- ​	只有两个Ture/False，（0，‘ ’）为F

- 转换

  - 数字转布尔: 0是False，其他都是True

  - 字符串转布尔:“ ”是False，其他都是True

    

##### 3.字符串（str）

###### 	1..lower( ) 

将str转为小写

```
value='LUWEI'
new_value=value.lower()
print(new_value)
---> luwei
```

###### 	2..upper( )

将str转为大写

```
value='luwei'
new_value=value.upper()
print(new_value)
---> LUWEI
```

示例:

```
check_code='KtDp'
code=input('请输入验证码：%s -->'%(check_code,))
if code.upper()==check_code.upper():
    print('输入成功')
```

###### 3..isdigit( )

判断str是否可以转为整数型

```
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
```



###### 4..strip .rstrip .lstrip

去除str中最左边与最右边的空格

```
user=input('plaese input username:')
new_user=user.rstrip().lstrip()
#new_user=user.strip()
print('------>',new_user,'<-----')
```



###### 5.replace( )

替换str中的字符，格式replace(old-str , new-str,count),count为从左往右替换几个，默认全部替换

```
message='替换str中的字符,格式replace(old-str , new-str,count),count为从左往右替换几个,默认全部替换'
message=input('请说话：')
print(message)
data=message.replace('你妹','***',3)
print(data)
--->***1请说话：***1请说话：***1
```



###### 6..split( ) 

将str按一定规则，切割为列表格式，rsplit( ) , lsplit

```
data=message.split(',')     #以‘，’进行切割
#data=message.split(',',1)  #以‘，’进行切割一次
#data=message.rsplit(',',1)  从右开始按‘，’切割，1次。
#data=message.lstrip(',',1)  从左开始按‘，’切割，1次。
print(data)
```



###### 7..startswith()/endswith()

```
name='luwei'
#判断是否已lu开头
flag=name.startswith('lu')
print(flag)
#判断是否已ei结束
flag1=name.endswith('ei')
print(flag1)
```



###### 8..format( )

字符串格式化

```
name='我叫{0}，年龄：{1}'.format('oldboy',73)
print(name)
```



###### 9..encode



```
name='陆威'#解释器读取到内存后，按照unicode编码存储：8个字节
v1=name.encode('utf-8')
print(v1)
v2=name.encode('gbk')
print(v2)
```



###### 10..jion

字符串拼接

```
name='luwei' #l_u_w_e_i
result='_'.join(name)#循环每个元素，并在元素和元素直接加入连接符
print(result)
```



##### 公共

###### 	len（）

 在字符串中，计算字符串中字符的个数。

###### 索引取值

```
v='luwei'
v1=v[1]
print(v1)
--->u
v2=v[-1]
print(v2)
--->i
```

###### 切片 

格式v=val[x:y] 遵循前闭后开原则  -->    x=<索引位置<y

从左往右 索引值 为   0，1，2，3，....

从右往左 索引值为   .....，-3，-2，-1   依然遵循左闭右开的原则。[-3:-1] ，索引范围为 -3=<索引位置<-1

```
val='luwei'
v1=val[2:5]#前闭后开，索引范围为  2=<索引位置<5
-->wei
v2=val[2:-1]
-->we
v3=val[2:]
-->wei
v4=val[:-1]
-->luwe
v5=val[-3:-1]
-->we
```



```
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
```



###### 步长

```
name='luweiluwei'
val=name[0:-1:2]#格式name[x:y:z] z为步长值可以为负，表示从左
val1=name[-1:0:-1]
print(val1)
```



###### for 循环

```
name ='luwei'
for item in name:
	print(item)
	
--->l
--->u
--->w
--->e
--->i
```



range （0，10）

```
for i in range(0,10)
```



### 作业

1.思维导图

2.笔记

3.作业提交

















































































​	



































