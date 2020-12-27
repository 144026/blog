---
title: 微机原理课程总结
date: 2020-08-19 02:18:42
tags:
- 微机原理
- 嵌入式
- PIC单片机
categories:
- 知识
- 计算机

mathjax: true
---


# 0 前言
尽量系统地回顾课程内容，巩固相关知识，总结一些用到的方法，揣测这门课培养的思维模式。



<!--more-->



# 1 实验梳理

本课程的实验需要用到：

- hardware: 开发板，包括PIC16F18854芯片x1，LEDx1，4位共阴极数码管，机械按键x11(包括复位键)，触摸按键x3，TMP75芯片x1，micro-USB接口x1，杜邦线若干
- software: MPLAB-ver5.20，mplab-data-visualizer，xc8-ver2.20，putty/org-dian.nbm
- document: 开箱测试、插件安装文档，微机原理课件，PIC16F18854、TMP75AIDGKR数据手册
- management: word，ppt，tx会议，git

## 1.1 闪灯

### 1.1.1 软件延时

发光二极管的阳极 D1 接 RB0， TRISB 设置为输出，ANSELB 设置为数字模式。通过 defsz和 goto语句构成循环，每隔一段时间翻转 PORTB(或LATB)。 

**注意**：写PORTB和LATB是等效的，但是读PORTB是端口实际电平，读LATB是输出锁存。例如仿真翻转LATB时，PORTB窗口监视值不改变。

### 1.1.2 定时器查询

**参数计算**

时钟源$F_{osc}/4=1\ MHz$，$T_{cy}=1\ us$，Timer0(配置参考datasheet 27.0节)选择8位模式，可精确计数499.712ms；选择16 位模式，可精确计数500ms。计算公式为

$$T_{cnt}=N_{pre} \cdot\ N_{cnt} \cdot\ N_{post} \cdot\ T_{cy}$$

为了方便由$N_{cnt}$计算出Timer的置数值，可以使用如下宏定义

```assembly
TMRCNT	EQU 50000
TMRVAL  EQU (.65536−TMRCNT)	;'.'表示十进制
TMRHVAL EQU HIGH(TMRVAL)
TMRLVAL EQU LOW(TMRVAL)
```

**可重定位的汇编代码**

```assembly
RST code        BLOFFSET	;Bootloader Offset
    pagesel     main
    goto        main

    code
main
	goto main
end
```

**程序流程**

计数完成时TMR0IF自动置位，循环查询即可实现定时，如下图

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200824195720.png)

由于PIC16F18854的Timer0具有T0OUT位，可以选择查询T0OUT，或者直接把T0OUT同步到PORTB。采用查询T0OUT方式的流程如下

<img src="https://raw.githubusercontent.com/144026/rsrc/master/img/20200823012617.png" style="zoom: 150%;" />

直接同步T0OUT的流程如下

<img src="https://raw.githubusercontent.com/144026/rsrc/master/img/20200825092318.jpg" style="zoom:80%;" />


**误差控制**

直接置数会造成**漏计**，导致实际计数周期**大于**`TMRCNT`个指令周期，这可以通过调整置数值进行补偿，但并没有从根本上解决问题。

先停止Timer，用置数值加上溢出后的计数，加上Timer停止的时间，再启动Timer就可以**消除**漏计。程序如下

```assembly
banksel T0CON0
label1
    bcf     T0CON0, T0EN	;先停止Timer
    
    movlw   0x0
    addwf   TMR0H, f		;必须先读一次TMR0H来更新它的值?
    
    movlw   TMRLVAL
    addwf   TMR0L, f		;低位预置值+溢出的计数
    btfsc   STATUS, C
    incf    TMR0H			;处理进位
    
    movlw   (label2−label1)
    addwf   TMR0L, f		;再加上Timer停止的时间
    movlw   TMRHVAL
    addfc  TMR0H, f			;高位预置值+溢出的计数+进位
    
    movlw   0x0
    addwf   TMR0L, f		;写TMR0L使TMR0H的更新生效
label2 :
    bsf     T0CON0, T0EN	
```

**注意**：TMR0H实际上是Timer0高8位的一个**缓冲**寄存器，这是为了能同步读写16位的计数值。读TMR0L时，Timer0的高8位才会被缓冲进TMR0H；写TMR0L时，才会把TMR0H的值更新到Timer高8位。(但在仿真中，出现了读TMR0L后，TMR0H并未更新的情况，必须先读一次TMR0H才会更新)

消除漏计后，发现仿真跑表结果在500.000ms左右**周期性抖动**。这是由于计数每$cnt$个$T_{cy}$溢出一次，而主程序每$m$个$T_{cy}$只进行一次查询，这导致检测的溢出会落后$N_{lag}$个$T_{cy}\ \ (0\leq N_{lag}\lt m)$。显然，只有当$cnt$能被$m$整除时，$N_{lag}$才保持不变，跑表结果不发生抖动。进一步考虑到检测到溢出后，从跳出循环执行动作，到跳回到检测语句需要$n$个$T_{cy}$，则当且仅当

$$n=k \cdot\ m +(cnt\mod m)$$

时，跑表结果不变。其中k为非负整数。

### 1.1.3 定时器中断查询

用中断方式控制闪灯，同时使用电平变化中断IOC(Interrupt On Change)改变闪灯速率。

**实验配置**

开启TMR0IE，将控制LED电平和Timer0置位的的部分移入ISR(Interrupt Service Routine)，在主程序循环等待中断，就可以实现中断闪灯。

实现IOC的电路如下，按键K按下后，输入I/O端口的电平出现下降沿。

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200825093032.png)

IOC配置直接参考数据手册即可。

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200825093605.png)

**程序流程**

主程序流程如下，其中RB0用于驱动LED发光，PORTC用于检测按下AN8/AN10产生的IOC。

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200825094745.png)

ISR流程如下，采用软件辅助计数的方式，计数器每溢出$N$次(初始值为10)改变一次LED电平；发生IOC时，改变$N$的值来改变闪烁速率。

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200825095124.png)

然而上述ISR程序存在如下问题：

- 当两个或多个中断同时到来时，只能处理一种中断，并且ISR退出时没有清理其他中断的IF标志位。
- 中断程序没有立刻清理IF标志位。若在ISR执行时发生其他中断，进入中断嵌套(尽管PIC16F18854不支持，但仍应该考虑)，会再次处理没有清理标志位的中断。

更合理的的ISR结构如下

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20200825101348.jpg)

**误差控制**

消除漏计后，同样存在跑表结果周期性抖动的问题。这是由于计数每$cnt$个$T_{cy}$溢出一次，而中断并不能随意打断多周期指令，即计数中断也会落后$N_{lag}$个$T_{cy}\ \ (0\leq N_{lag}\lt 2\sim 4)$。只有$N_{lag}$保持不变时，才不会产生抖动。通过添加nop指令，Timer的中断在单周期指令处发生就可以避免问题。

按键按下一次时往往有几个ms的抖动，多次触发IOC，因此需要**消抖**。可以在每次触发IOC时关闭使能，隔一段时间(例如Timer0中断2次)再打开使能。



## 1.2 数码管显示

## 1.3 按键检测

## 1.4 AD转换

## 1.5 串口通信

### 1.5.1 I2C

### 1.5.1 EUSART

# 2 知识归纳


# 3 方法论和思维模式


# 4 收获与心得


# 5 疑难问题与解决


# 6 对课程的意见和建议
我常常认为，无法提出条理清晰的意见和建议，等同于欠缺理解。我还不够理解这门课程：课程的目的，学生为此需要掌握什么，如何据此设计课程内容，如何教学，如何把握课程进度，如何控制教学质量等等，因此暂不作评价。

# 7 后记