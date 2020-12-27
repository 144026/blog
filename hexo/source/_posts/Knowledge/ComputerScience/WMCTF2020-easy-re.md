---
title: 一道Perl逆向入门题
date: 2020-08-01 12:57:33
tags:
- CTF
- Reverse
- Perl
categories:
- 知识
- 计算机
---
# 1 Perl与反编译
Perl是解释型语言，要保护其源码，常用的方法有：
- 先将Perl代码转换成C代码，再由C代码得到可执行程序，例如perlcc。反编译的得到的源码不容易看懂。
- 将Perl代码和解释器打包成可执行文件，实际执行时将Perl代码提取出来，交给解释器执行，例如PAR(Perl Archive Toolkit)。可以动态调试得到Perl代码。

<!--more-->



# 2 题目

题目取自WMCTF2020，提示内容如下
 ![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200801160053.png) 

下载程序，运行如下
 <img src="https://raw.githubusercontent.com/144026/rsrc/master/img/20200801160317.png" style="zoom:150%;" />

查看PE信息为64位程序，ida64反编译的C源码效果不佳。使用x64dbg进行断点调试。
1. `F9`执行到出现上述输入提示，`F2`下断点。
2. `Ctrl`+`F2`重新载入，`F9`执行到断点处，`F7`进入。
3. 重复步骤1和2，找到下一层的断点。

很快注意到如下代码段
![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200801160402.png)

内存中跟随rax的值
<img src="https://raw.githubusercontent.com/144026/rsrc/master/img/20200801160418.png" style="zoom:200%;" />

随后的代码段直接通过rax返回了Perl脚本
![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200801160448.png)

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200801160508.png)

得到flag为`WMCTF{I_WAnt_dynam1c_F1ag}`