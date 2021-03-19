---
title: 日志
date: 2020-09-20 23:30:37
tags:
- 时间管理
- 计划
- 反思
categories:
- 其他

mathjax: true
---

9.20, 2020 $\sim$

<!--more-->

# 2020

## 2020-9

学习NSA著名工具Fuzzbunch，学习入侵检测。主要分析EternalRomance，同时整体调研NSA的全部泄漏工具，以便进一步学习。

### 2020-9-20

1. 记录romance前75个包的关键字段。确定romance如何发包实现heap spray，和spray之后多个transaction之间的排布。
2. spray之后直到第一次越界读，存在多次越界修改相邻transaction的操作。但是不清楚transaction结构体的定义，不知道改了哪些字段。


### 2020-9-21

1. 记录romance第二次越界读之前的流量，猜测`pTransaction+168`为InSetup缓冲区起始，`pTransaction+80`为`OutData`指针地址起始。
2. 考虑到romance越界写操作的核心部分为靶机内存偏移，因此只要保证偏移不变，写操作流量包的字段可以有较大变化，不便于匹配，搁置romance详细过程的分析。


### 2020-9-22

1. 分析romance的主要流量特征，学习ET/OPEN规则，发现需要改动，才能匹配TID和control_transaction。


### 2020-9-23
反思：
1. 电脑崩了之后，恢复困难。软件、数据、文档、资源的存储缺乏管理，取舍起来困难而低效。需要考虑重点存放文档、资源、路径明确的重要数据，其他的丢了就丢了。
2. 需要考虑对硬盘关键数据进行备份，以免出现硬盘烧毁的情况。


### 2020-9-25
1. 调研NSA泄露工具库的其他工具。许多工具的目标软件非常古老，有些甚至必须运行在古老的RHL系统(2003)上，学习价值比较低。

总结：
1. RHL和RHEL的区别。
2. 检索漏洞利用相关工具的相关信息时，找到其CVE编号很重要。


### 2020-9-27
1. 继续调研了另外几种NSA工具：都是针对服务和守护进程的漏洞，只调研到系统版本信息。
2. NSA的部分工具，如SNEER，没找到CVE编号；有些工具甚至连用法、作用都不明确。


### 2020-9-30
1. 调研虚拟机平台：VMware、qemu/kvm、Xen、VirtualBox


## 2020-10
- 继续学习Fuzzbunch，主要是Eternalchampion。
- 学习linux初步，学习qemu等工具
- 学习通信相关课程

### 2020-10-02
1. virt-manager解决qemu虚拟机的device型号指定问题。


### 2020-10-3
1. 复习部分MS17-010 Bug.txt

反思：
- 软件工程：用户需求和系统设计的冲突?
    写story$\longrightarrow$story依赖和分类$\longrightarrow$模块化？


### 2020-10-7
1. 4天软件工程课程。敏捷开发，自动化测试，多人协作
2. Clion，Git，Svn，Shell脚本
3. 一次linux课程，initrd

反思：
1. shell的语法设计思想？
    - 关键字、变量、基本运算
    - 流程控制：逻辑表达式、逻辑判断语句
    - 模块化：函数
    - 其他特性

### 2020-10-10
1. linux initrd文件系统,只包含bash。依赖打包的自动化脚本。
2. os
3. sw2020


### 2020-10-14
1. 通信电子线路：电路理论review：串并联谐振（品质因数/失谐系数）
2. 计算机网络：分层协议对比
3. linux文件系统：挂载硬盘，0.55手动，0.6自动加载驱动（mods和udev）

misc:
1. n维bfs的一种实现，树的层序遍历。
    - 不能斜着走：以起点为根的$2n$叉树
    - 可以斜着走：以起点为根的$3^n-1$叉树

2. start organizational management:
    - task manager: `MS todo`
    - calendar: ?
    - note-taking system: `vim-markdown + hexo + xmind`
    - storages and sync: ?

### 2020-10-15
1. DSP 频率取样
2. 计网：SMTP。HTTP，cookies，Web代理计算


### 2020-10-16
1. linux笔记
2. 配置wine环境
3. linux下重新picgo + github图床，发现api.github.com的DNS污染问题


### 2020-10-29
1. linux小系统v0.7
2. centos6.9配网络启动服务 + 半自动脚本部署


### 2020-10-20
2. 体育课
3. 使用POC脚本成功复现CVE-2017-0146，但fuzzbunch.champion无法成功

### 2020-10-22
1. DSP课程
    - FFT计算线性卷积：3点和1000点，分段计算
        - $L(3*3) = 5$，重叠部分：相加/丢弃
    - 数字滤波器
        - IIR滤波器基本结构
            1. $Y = (1+ \Sigma b_n z^{-n}) \cdot W \ ;\ W =  \cfrac{1}{1-\Sigma a_n z^{-n}} \cdot X$
            2. $Y = \cfrac{1}{1-\Sigma a_n z^{-n}} \cdot W\ \ ;\ W = ( 1+ \Sigma b_n z^{-n}) \cdot X$

2. 计算机网络
    - 回顾：系统方法、网络设计需求
    - 开始连接
        - 介质类型？
        - 发送
            - Non-Return Zero
                - 全1 基线偏移
                - 全0 空闲误判
            - 边沿脉冲表示0、1：$\eta =  50\%$
            - 4B/5B：$\eta = 80\%$
        - 纠错
            - 奇偶校验：1维/2维/2维plus（hamming code）
            - **CRC校验**
            - checksum
                - 反码加法    
        - 接入控制：冲突检测，随机调度？
3. 选频网络知识地图
4. 逛博客（看热闹）
    - dx: ldd、tikz、图床
    - qy: linux简介、几个RE:
    - lu: 学习方法论x3、逆向工具表、dos启动简介、shellcode简介
5. 复习习CVE-2017-0146(Eternalchampion)攻击过程
    - **to the stack** is_name_valid(6): indata -> stack.unicode_str
    - **race!** trans2_2nd: DataDisp at [e|r]ip
    - **lose** invalid_dev: 2nd to slow~ (7_sp0_x64,s2008_sp0_x86
    - **win** u r the champ (xp_sp3_x86
    - **the nsa tricks** q_ea_size(2) + name_valid(6) + 2nd $\times$ 8
        - **no use?** :/

### 2020-10-23

1. 编译内核
    - `make localmodconfig`, `make tinyconfig`, `make menuconfig`,`make -j8`
    - host编译-> guest, make版本问题？(did you mean TAB instead of 8 spaces)
    - scl.gcc9直接`make menuconfig`出错
    - `tar -z|j|J` :  `gz|bzip2|xz`
2. 操作系统
    - PV原语：两种模型
        - 互斥：资源有限
        - 同步：资源不断产生?
    - 其他同步/互斥机制
        - mutex、flock
        - spinlock(seen in kernel)
    - 存储器管理
        - 内存模型
            - 分段(data share) + 分页(内存碎片) = 段页式（现代os）
        - 运行管理
            - 内存/磁盘置换、缺页中断
        - 存储共享
            - IPC
            - 代码段重用，数据段Copy-on-Write

3. 了解earlyshovel github py脚本
    - `t(arget)[ip|port], c(allback)[ip|port|l(ocal)port]`
    - 文件包含关系复杂，vscode尚需grep，vim怎么搞定？

4. 种子讲坛black story
    - 事件1 -> 事件2，如何2分找到逻辑通路？

5. champion笔记整理
    - 复现总结 + 原理总结


### 2020-10-24
1. bili-ctf ($\times$) 679($\surd$)
    - `<script> $ajax`: url + method + function(data) ?
2. linux命令总结
    - `echo`
        - `echo $str`将去除换行、tab、多个空格，`echo "$str"`保留
    - `sed`
        - `&`表示已匹配的串
        - `sed '/^$//g`无法删除空行，`\n`仍会保留
        - `sed '/^\s*$/d'`删除空白字符行, `sed '/^$/d'`删除空行(一行只含一个`\n`)
    - `curl`
        - `-H` (header，`-L`重定向时不变)
            - add: `-H "a: aa" -H "b: bb" ...`
            - rm: `-H "a:"`
            - empty: `-H "a;"`
        - `-A $agent` (User-Agent)
        - `-b|--cookie "name1=value1; name2=value2"`
        - `-c|--cookie-jar $file`
        - `-o $file` (`file=-` for stdout)
            - `-O`
        - `-i`(inlude header); `-I`(header only)
4. 分析champion 检测策略
5. hexo博客: heso mathjax`$inline math$`中，`$`内侧有空格时无法渲染


### 2020-10-25
1. 高频谐振小放
    - 模型、参数（A、B、Q）
    - 单级、多级
2. DSP
    - 几种离散Fourier    
        - DTFT: $X(e^{j\omega})= \sum x(n)\cdot e^{-j\omega n}$
        - DFS: $\tilde{X}(k)= \sum x((n))_{_N}\cdot e^{-j\frac{2\pi}{N} kn}$
        - DFT: $X(k) =\tilde X(k) \cdot R_{_N}(k)$
    - 频率取样: 任意周期/非周期$x(n)$
        - z平面单位圆取样：$X(k) = X(z)|_{ z= exp\{j\frac{2k\pi}{N}\} } \Longleftrightarrow x((n))_{_N} = \sum_r x(n+rN)$
        - 数字频域在$[0,2\pi)$内等间隔抽样：$X(k)= X(e^{j\omega})|_{\omega = \frac{2k\pi}{N}}$
    - 线性卷积/循环卷积？
    

### 2020-10-26
1. DSP
    - 几种卷积
        - 线性：$x_1(n) * x_2(n) = \sum\limits_{m=-\infty}^{+\infty} x_1(m) x_2(n-m)$
        - 周期：$x_1((n))_N * x_2((n))_N = \sum\limits_{m=0}^{N-1} x_1(m) x_2((n-m))_N$
        - 循环：$x_1(n) \textcircled{1} x_2(n) = [x_1((n))_N * x_2((n))_N ] \cdot R_N(n)$
    - FFT
        - 时基

2. 计网
    - Access Control
        - Multiplex，集中管理：无冲突、利用率低
            - TDMA, **CDMA**, FDMA, OFDMA
        - Random Access分布式
            - Aloha net: $\eta_{_{Time Divsion}} \le \frac{1}{e}$
            - CSMA(Carrier Sense Multiple Access): $\eta = f(a,x)$
                - backoff strategy: 概率重传/等待窗口

3. ADI
    - 跳频？
        - 跳频序列
            - 有限/无限长
        - 跳频同步
            - 阻塞试同步？
            - 定时器
            - 外时钟
            - ...


### 2020-10-27

![20201028012621](https://raw.githubusercontent.com/144026/rsrc/master/img/20201028012621.png)

- NT trans response有data/parameter count字段

### 2020-10-29

![20201030210305](https://raw.githubusercontent.com/144026/rsrc/master/img/20201030210305.png)

**总结**

- 火灾消防演练：
    - 灭火器材：楼道消防栓、灭火器(干粉/泡沫/$CO_2$)(点射)
    - 自救器材：防毒面具、逃生绳
    - 需要警惕的常识
        - 火灾中的爆燃
        - 电器遇水爆炸
        - ......


## 2020-11

Elastic Stack.

### 2020-11-1

![20201102021309](https://raw.githubusercontent.com/144026/rsrc/master/img/20201102021309.png)


### 2020-11-2

![20201103023343](https://raw.githubusercontent.com/144026/rsrc/master/img/20201103023343.png)


### 2020-11-3

![20201104010611](https://raw.githubusercontent.com/144026/rsrc/master/img/20201104010611.png)


### 2020-11-4

![20201105002213](https://raw.githubusercontent.com/144026/rsrc/master/img/20201105002213.png)


### 2020-11-7

![20201110014653](https://raw.githubusercontent.com/144026/rsrc/master/img/20201110014653.png)


### 2020-11-9

1. $\LaTeX$
    - `titlesec`
        - `\titleformat*{\section}{}`
    - `zhnum`/`\chinese`
        - `\renewcommand`
        - `\thesection`?
    - `\setlength{\baselineskip}{22pt}`
    - `\fontsize{12pt}{\baselineskip}`

2. 本机DNS被污染，修复时浪费大量时间，其中有两个问题。
    1. 改`hosts`不起效：域名打错字了
        - 根据`nsswitch.conf`，`hosts`名称解析是`files`最优先，修改不起效应该立刻怀疑打错字。
    2. 尝试网络上的各种dns刷新方法，wireshark抓包都没显示刷新成功。
        - 本机使用的哪种DNS服务？
            - 查看`nsswitch.conf`, `locate mdns4_mininal`, `dpkg -S`, `dpkg -L`
            - `mdns4_minimal`怎样刷新缓存?


### 2020-11-10

1. $\LaTeX$
    - **`ctexart`类型数字、字母比中文小**，ctex宏包手册没有提到这件事。
        - `article`类型显示正常
    - `\renewcommand + thesection`的问题：`subsection`显示不正常
    - `ctexart`设置标题格式：`\ctexset`
        - `ctexart`不修复，宁愿用Word
    - `\pagestyle{plain}`
    - `\algorithm`, `\algorithmicx`, `\algpseudocode`
        - `\Require`, `\Ensure`
        - `\If`/`\EndIf`, `\For`/`\EndFor`, ...

2. grafana搭建
    - `wget .tar.gz` + `tar -xzf`
    - `bin/grafana-server`
    - `supervisorctl`管理


### 2020-11-11

1. ADI
    - matlab数据类型、转换
    - 基本流程控制

2. `fontspec`宏包手册
    - `\setmainfont{}[UprightFeatures = {Scale=x,WordSpace{x,x,x},OpticalSize=x}]`调整英文字体大小
    - `ctexart`中`\ref`，`\eqref`的大小正常，但也会被上述命令缩放
    - 别用`ctexart`


### 2020-11-15

1. ADI
    - bpsk_demo收发联调不通，怀疑是同步问题

2. 通电ch3作业
3. 网络拓扑展示方式？
    - 手绘拓扑: Visio, drawio
    - 自动探测、绘制: the Dude? 查不到权威/广泛使用的解决方案


### 2020-11-16

1. DSP
    - ch4作业30%
    - 安装Octave
2. 通电
    - ch4知识地图
    - ch5xmind笔记(部分)

ToDo:

1. DSP
    - ch4 作业
    - DSP实验环境准备: Octave可用性测试
2. 通电
    - 实验环境准备：安装multisim
3. 计网
    - ADI调试TCP-pluto示例
4. 网络拓扑展示
    - 自动网络拓扑是否广泛使用？
    - 自动网络拓扑能做到什么地步？
    - 有无开源解决方案？
    - 手画试试看


### 2020-11-20

1. 形势与政策

2. git
    - switch` [-c] <branch> [<start-point>]`
    - checkout`[-b] <branch>`
    - branch
        - `-vva`
        - `<newbranch> [<start-point>]`
        - `-cCmMdD <branch>`
        - `-u <upstream_branch> [<branch>]`
    - remote
        - `add|rm|rename <remote> [<url>]`
        - `prune <branch>`
    - fetch
        - `<remote> [-t <branch>] [-m <master> (set up default branch refs/remote/HEAD)]`
    - push
        - `--all`
        - `[-u] <remote> [<src>[:<dst>]]`
        - `-d <remote> <ref_spec>]`

3. MLX90614 ?


### 2020-11-22

1. 输入法
    - 百度输入法
        - `dpkg`安装，缺少依赖: `apt --fix-broken install` (原理？)
        - `dpkg`卸载，`~/{.config, .cache}`仍然存在相关文件
        - 之后使用`dpkg`/`apt`时，出现`ERR: xxxbaiduxxx.desktop: No such file or directory`
            - 尝试`touch`产生该文件，同样提示`No such file or directory`
            - 发现该文件是损坏的软链接
    - libPinyin
        - 出现不常用词时，用空格选中的词汇，**不加入user dictionary**
            - 需要用数字依次选中
        - 单字的更新权重比词汇低
        - 出现在首页的5个词汇不更新
            
2. vivaldi
    - `apt update`报错，发现添加了vivaldi源
        - `sudo rm /etc/apt/source.list.d/vivaldi*`
            
3. gitee
    - C语言拆分大文件，分批推送
        - gitee告警，仓库最大为1G

4. zathura
    - zathura预览tex编译结果时出现问题
        - `cp xxx.tex new.tex`，重新编译，显示正常。`tex`文件没有问题。
        - `cp xxx.pdf new.pdf && zathura new.pdf`发现显示正常。问题出在zathura配置。
        - `locate zathura`
        - 配置文件`/home/drh/.local/share/zathura/history`，找到`xxx.pdf`，ColumnPerPage改为1，恢复正常。


### 2020-11-23

1. 计网
    - ch3作业
    - 可靠传输：重传
        - 单分组：等待重传，效率低下
        - 多分组同时发送。**注意：**此时$ACK_n$表示已连续成功接收了$n$帧数据。
            - 后退N帧(Go-Back-N)重传。
            - 选择重传。
    - pluto
        - 等待重传demo
2. 通电实验
    - R、L、C对Q的影响：$A = \dfrac{xxx}{g_\Sigma}$
        - R越大，增益越大，通频带越窄
        - L越小，C越大，通频带越窄

TODO:
- 计网作业$\times$3
- 通电实验报告


### 2020-11-24

1. 电磁场课程
    - beamforming视频

2. supervisor查错失败
    - `systemd`执行`supervisor -n -c $conf`后，supervisor下进程无法正常启动
        - `ss-local`被SIGSEGV(segment violation)终止
    - 怀疑是`ss-local`的程序问题，添加grafana，无法正常启动
        - grafana无法进入`directory`
        - 去掉`directory`并改为绝对目录，被SIGSEGV终止
    - 怀疑是`-n`的问题，去掉`-n`手动执行，成功(grafana可以进入目录)
        - **加上`-n`手动执行，成功**
        - **注意：为控制变量，正确的做法应该是先手动执行相同指令，再去掉`-n`**
    - `systemd`去掉`-n`，supervisor.service启动后直接退出
    - 放弃查错，直接用`systemd`启动`ss-local`

3. chrome instance
    - 第二次启动chrome，命令行proxy参数不生效
    - 查看手册
        - `--user-data-dir=xxx`指定config目录
        - 相同config目录时，多次启动chrome，会复用已有的进程，新参数传不进去
    - xfce keyboard添加快捷键，无法展开参数`~`等
        - 快捷命令`CWD`为当前用户home

4. `curl -fsSL`
    - **`curl` shows HTML reponses on STDOUT, and its progresses and errors on STDERR.**
    - `-f, --fail`, suppress HTML failure docs(http error code, etc.) delivered by server. That is, suppress stdout, useful for scripts.
    - `-s, --silent`, no progress, no error message. That is, suppress stderr.
    - `-S, --show-error`, with `-s`, show error when fails. That is on sstderr, suppress progress, but not errors.
    - `-L, --location`, follow redirection

5. `ffmpeg`
    - `sudo apt-get install ffmpeg && man ffmpeg`
    - `ffmpeg -i music.m4a music-out.mp3`

6. 计网作业
    - ch5
        - UDP使用stand-and-wait ARQ
            - 可以传输文件，例如T(rivial)FTP
            - 使用固定端口，重启后出现混淆
        - TCP握手和挥手的ACK递增
            - FIN的ACK必须递增，否则混淆
            - SYN的ACK可以不递增：SYN前不会有TCP形式的ACK？

### 2020-11-26

1. DSP答疑+计网课程
2. 计网ch6作业
3. Grafana前端


### 2020-11-27

1. matlab
    - 文件、函数名中的`-`被解析成减号
    - `global`变量必须先声明再赋值
    - `timer('TimerFcn',@your_func,'StartDelay',5)`时，`your_func()`函数应该接收2个参数，即`function your_func(obj,rhs) xxx; xxx; end`

2. git
    - `git push`失败：`\xxx\xxxgit: permission denied`，添加远程仓库时，使用了全角字符。`git remote set-url <remote> <new_url>`改为半角字符`url`


### 2020-11-28

1. `git`
    - `git branch -d $local_branch`, `git branch -r -d $remote_ref_branch`
    - `git push -d $repo $refspec [--force]` / `git push $repo [+]<src>:<dst>`
    - `git remote prune`

2. optofluidic, flow cytometry
3. 年鉴安排
4. pluto
    - `hopsend_saw`第一个包始终ACKed，存在逻辑漏洞。


## 2020-12

### 2020-12-6

1. DSP
    1. $x(n) = w(n) + v(n)$，那么$S_{xx}(z)$和$S_{ww}(z),\ S_{vv}(n)$的关系？
        - $R_{xx}(m) = R_{ww}(m) + R_{vv}(m) + R_{wv}(m) + R_{vw}(m) =R_{ww}(m) + R_{vv}(m) + R_{wv}(m) + R_{wv}(-m)$
        - 则：$S_{xx}(z) = S_{ww}(z) + S_{vv}(z) + S_{wv}(z) + S_{wv}(z^{-1})$
        - 问题在于两个随机信号，没有表达式，$R_{wv}(m)$怎么求？
    2. DFT的一些变换问题
        - 时域抽选和频域抽选 $x(2n) \leftrightarrow ?\ |\ ? \leftrightarrow X(2k), \ (0,\dots,\frac{N}{2}-1)$
        - 时域分段和频域分段 $x(n)+x(n+\frac{N}{2}) \leftrightarrow ?\ |\ ? \leftrightarrow X(k)+X(k+\frac{N}{2}),\ (0,\dots,\frac{N}{2}-1)$
        - 时域延拓和频域延拓 $x(n)+x(n-N) \leftrightarrow ?\ |\ ? \leftrightarrow X(k)+X(k-N),\ (0,\dots,2N-1)$

2. ip route
    - show | list | add | del
    - change : can't change `metrics` due to `rtnetlink` protocol limitations(use `metrics` to separate routing records)

总结：别用`ip route change`


### 2020-12-7

1. `iptables -t nat -A POSTROUTING -s 192.168.x.x/24 -j SNAT --to-source 192.168.y.y`不起效果(ubuntu2004/1804)？
2. jumpserver: `p` print hosts, select its number to ssh to a host.
3. zsh `$PROMPT` format
    - `%B{}|%b`/`%F{}|%f`/`%K{}|%k`: define|undefine bold,foreground,background
    - `%(#.root_str.nonroot_str)` expands according to root privilege
4. `__git_ps1 [formatted_str]`, e.g.`. /usr/lib/git-core/git-sh-prompt && __git_ps1 "%%B%%F{cyan}%%K{blue}%s%%b%%f%%k"`
    - output a formatted string if in git repo; if not, output nothing
    - `%s` turns into `branch_name`, `%%` turns into `%`
    - `vim /usr/lib/git-core/git-sh-prompt` to see some options
        - `GIT_PS1_STATESEPARATOR`,`GIT_PS1_SHOWDIRSTATE`,etc.


### 2020-12-8

**内容**
1. mysql数据库迁移
    - export: `mysqldump -u <user> -p --all-databases > sqldump.sql`
    - import: `mysql -u <user> -p; source /path/to/tosqldump.sql`
2. ubuntu2004安装mysql后无法进入
    - 报错`Access denied for user 'root'@'localhost'`：使用`/etc/mysql/debian.cnf`中的`debian-sys-maint`账户登陆
3. ubuntu2004，sql8.0，无法修改密码
    - 5.7版本：`use mysql; update user set authentication_string=password("newpass") where user="root"; [flush privileges;]`，已经没有password函数，不能使用
    - 8.0版本`alter user 'root'@'localhost' identified by 'newpass'`，使用后`select * from user where user="root"`，没有变化，仍然不能`mysql -u`登陆。
4. 使用`debian-sys-maint`账户，在8.0版本中`source sqldump.sql`(来自5.0版本)后，使用`alter user`报错`ERROR 1726 (HY000): Storage engine 'MyISAM' does not support system tables. [mysql.user]`
5. ssh端口转发(参数指定有顺序)
    - local to remote: `ssh -L local_addr:remote_addr`
    - remote to local: `ssh -R remote_addr:local_addr`
    - global port access: `-g`, same as `0.0.0.0:<port>`
    - background and detach: `-f`, implies `-n`, so a command must be specified
        - `-n`: redirect stdin from `/dev/null`
        - `-N`: no commands, use for forwarding only, override `-f`'s compulsory command specifying.
    - e.g. `ssh -gfNL 3000:localhost:3000 <usr>@<host> [ -p <port> ]`(can be used with `systemd`)

**总结**
1. 搜索报错没有问题，但是对于报错的解决方案，应该考虑软件版本的影响
2. 搜索软件使用方式时，一定要带上版本，如"mysql8.0修改密码"


### 2020-12-9
1. awk
    - `awk <commands_string> <file1> <file2> ...`, **NOTE** that `<command_str>` should be a single argument, if not, subsequent commands will be treated as filenames.
    - `awk '{gsub(<rexp>,<str>);print}`中，`gsub`的参数应该是`""`包括起来的字符串

2. bash参数展开: word splitting按空格分词，例如`awk BEGIN{RS=EOF} 'command1;command2;...'`中`command1;command2;...`不会执行。
    - 改用`awk BEGIN{RS=EOF}\ 'commands...'`, `awk 'BEGIN{RS=EOF} commands...'`, `awk BEGIN{RS=EOF}'commands...'`


### 2020-12-10
1. linux修改用户名，组名
    - [-] `useradd <newname> && userdel <oldname>`/`groupadd <newname> && group <oldname>`：可能无法继承原有用户/组的权限等信息(`uid`和`gid`可能不同，待验证)
    - [+] 替换文件
        - 换组名：替换`/etc/group`,`/etc/gshadow`中所有`<oldgrpname>`
        - 换用户名：替换`/etc/passwd`,`/etc/shadow`,`/etc/group`,`/etc/gshadow`中的所有`<oldusrname>`。注意：不换`shadow`则无法使用密码;不换`group`则无法使用各种组，例如`sudo`组的权限。

2. linux误删`/etc/group,passwd,gshadow,shadow`：使用系统自带备份文件`/etc/{group,passwd,gshadow,shadow}-`恢复

3. `zsh`与`bash`的区别：`echo \\\n`的执行结果
    - `bash`的`echo`为`/usr/bin/echo`，`zsh`的`echo`为内建命令， 类似于`/usr/bin/echo -e`

### 2020-12-15
1. `sudoers.d/xxx-grant-root.conf`不生效
    - `sudoers.d/README`: **... file that do not end in '~' or contain a '.' character.**

### 2020-12-20
**操作过程回忆**(大概)
1. add a i386 arch, install the deepin*wine*.debs, got deps error
2. apt-get install xxx:i386, still got 1 dep can't installed(libjpeg-turbo8?)
3. apt remove deepin*, apt remove wine*, (some kali-linux-* gone too)
4. apt autoremove
5. (perhaps 3?) install another deepin*wine* debs, got warning, packing old packges
6. reboot, lightdm failed.

**尝试解决**
1. apt-get upgrade, over 180 packages too old and got upgraded???
2. see `/var/log/lightdm/{lightdm.log,x-0.log}`，error is `The name org.freedesktop.Accounts was not provided by any .service`
    - `sudo apt-get install accountsservice`
3. still failure, see `/var/log/Xorg/xxx.log`, find `key->initialized` assertion failure)
4. google, gstreamer-vaahi package problem? no such package installed.


### 2020-12-21
**重装系统**
1. tar包备份`home`，`dd if=xxx.iso of=/dev/sdb`制作启动盘，重装系统
2. 参照`kali`和`usr-soft-list`重新配置基本功能

**Usb2Vga驱动**(DisplayLink)
1. 安装DL ubuntu驱动(5.3.1)失败，查看`/var/lib/dkms/evdi/1.7.0/build/make.log`，提示`include/generated/autoconf.h`, `include/config/auto.conf`缺失，需在内核源码位置执行`make oldconfig && make prepare`
    - 进入`/usr/src/linux-headers-5.9.0-kali-amd64`执行，报错`Can't open scripts/mkmakefile`。进一步查看，发现文件已存在，且内容有效。
    - 解压内核源码到新目录，`make oldconfig && make prepare`成功，替换为headers目录，驱动仍然安装失败
    - 恢复headers目录，仅替换'缺失'的文件，仍然失败
    - **问题等待进一步解决**
2. 使用`AdnanHodzic/displaylink-debian`安装(支持kali-rolling)
    - 安装时必须`cd`进入目录，必须`sudo ./displaylink-debian.sh`
    - 安装时无法解析`www.displaylink.com`
        - `vim /etc/proxychains4.conf && proxychains4 sudo ./xxx`
    - 驱动安装成功，**使用了同样的官方驱动，这个脚本如何做到成功安装?**（待研究）
3. post-install
    - `sudo ./displaylink-debian.sh --debug`，up and running
    - `xrandr --listproviders`只有一个输出
        - 根据文档(脚本github)修改`/etc/X11/xorg.conf.d/20-displaylink.conf`，重启出现多个输出
    - `xrandr --setprovideroutputsource`修改1-4，仍然没有输出可用
        - _重启，`xrandr --setprovideroutputsource 4 0`，出现显示画面_
    - **画面卡顿、撕裂问题**

**主控文档**
1. wps没有主控文档，ms-office2007没有主控文档
2. 分工：避免分配不熟悉的部分

### 2020-12-22
1. 自动答题脚本
    - 从html提取文字+题库搜索+根据返回答案触发网页操作?
    - 脚本(只剩下壳子和付费题库)、网课小工具(chrome插件)无法正常使用
    - 需要使用特殊浏览器，反制检测：原理？

### 2020-12-24

1. linux声卡配置(Advanced Linux Sound Architecture)
    - 查看声卡信息
        - `cat /proc/asound/card`
        - `aplay -l`(needs `alsa-utils`)
    - 修改默认声卡
        - alsa( or pulseaudio?) 默认使用card/device number最小的设备作为默认声卡
        - 修改默认声卡对应的设备：`vim /etc/asound`(system-wide) or `vim ~/.asoundrc`(user-specific)
        ```bash
        defaults.pcm.card $card_num
        defaults.pcm.device $device_num
        ```
        - 修改声卡设备的设备号？(需要修改modprobe相关配置)


### 2020-12-27
1. vim solarized 配色
    1. `vim-colors-solarized`插件：对tui vim支持较差
        - 使用terminal的palette，因此必须把terminal改成solarized配色：非常别扭，并且在`qterminal`和`gnome-terminal`下使用自带solarized配色时，`ls`的结果配色错误。
        - terminal支持256(8-bit)模式时，使用标准的256种颜色近似：`let g:solarized_termcolors=256`，近似效果很差，甚至可以称为诡异。
    2. 使用`set termguicolors`(编译时`+termguicolors`)，而`base16-vim`配色时利用这一特性直接指定24-bit颜色（vim似乎直接取代terminal来渲染编辑区域的画面？）
        - `colorscheme base16-solarized-dark`效果较好
            - **编辑很大的markdown文档(比如这个日志)，`G`跳到底部时高亮渲染失败，必须连续地滑动到底部一次**
            - `base16`系列主题的C语法高亮似乎不够丰富？
2. vimrc整理
    - `set showcmd`在右下脚显示没输入完的命令
    - `set showmatch`显示成对的括号
    - `set termguicolors` vim使用24-bit颜色，而不依赖terminal的调色板
3. 博客source dir push到仓库新分支
    - 更新next theme，merge合并冲突：删除windows系统引入的`\r`(`^M`)，`awk 'BEGIN{RS=EOF} gsub(/\r/,"") file'`
    - 打包theme文件夹到xz tarball，配置`.gitignore`：`themes/*<CR>!themes/*.tar.xz`
        - **注意**：使用`theme/`会ignore文件夹本身，再用`!themes/xxx`reinclude文件夹内部的文件，**不会生效**
4. `git merge`冲突
    - resolve: `git diff`, `git mergetool`，这时冲突的文件内容被修改为：
    ```txt
    <<<<<<your changes below
    you your yours
    ====== delimiter
    they their theirs
    >>>>>>their changes above
    ```
    - `git merge --continue`
        - 完成后，上述过渡文件变为`xxxx.orig`
    - `git merge --abort`
5. tips
    - `curl -fsS`的隐患
        - `-f`阻止显示HTTP错误码，`404`、`503`等错误发生时，`curl`不会给出任何提示
        - `-sS`虽然能显示错误码，但不会显示warning信息。例如下载二进制文件时，`curl`不会警告'binary files may mess up your terminal'就直接退出，给定位错误造成困难


### 2020-12-28
1. **Optimal Structure**: A problem's solution can be constructed (in certain way) from solutions of its subproblems.
    - **overlapping**: A subproblem $V_i$ is contained in all 'upper' subproblems $V_{j},j>i$, meaning that solving any $V_j$ solves $V_i$ as well (e.g. fibonacci). A `DP` solution can then be applied in either:
        1. _top-down approach_.
        2. _bottom-up approach_.
    - **non-eoverlapping**: $V_i\dots V_j$ are similar but separate problems, their solutions are independent from each other (e.g. quik sort, merge sort). `Divide and conquer` is applied.
    - **greedy**: if simply adding all $V_i\dots V_j$ yields the whole solution, then `greedy` solution can be applied.

2. leetcode: buy and sell stocks
    - done 120,121
        - 待总结
    - 看答案122,188: **做不出来原因待总结**
        - 按120、121的思路: 设法找$maxP_i$和$maxP_{i+1}$之间的关系，即已知$maxP_i$和`price[i+1]`，还需要知道$i$时刻的哪些变量？得到$max_P_{i+1}$之后如何更新这些变量？
            - 120题：`min_price[i]`
            - 121题：当前买入的`valley[i]`，从`valley[i]`之后上涨到的`peak[i]`
                - 或者只需要`price[i]`来确认是否上涨

3. `gs`: ghostscript, `man gs` to see more
    - downgrade pdf quality and size:
    ```bash
    gs -sDEVICE=pdfwrite \ # not X11, not stdout
    -dCompatibilityLevel=1.4 -dPDFSETTINGS=/default \ # pdf settings, /ebook, /prepress, /default, ...
    -dDownsampleColorImages=true -dColorImageResolution=130 \ # degrade HD images, set 130 dpi
    -dNOPAUSE -dBATCH \ # no stupid interactive 'enter' with every page
    -sOutputFile=output.pdf input.pdf # out and in, NOTE that mistaking them will overwrite 'input.pdf', definitely a disaster.
    # better keep a input.pdf.bak for safety.
    ```
4. vim
    - `:set filetype=help`
    - `cmdline.txt`
        - Ex commands: `"`(qoute) and `|`(bar) can't be used after commands that take them as argument
            - _note_ vim interprete `|` as command separator (to execute multi commands), rather than `pipe`(in shell).
        - Ex command range: `:h :range`
            - `<specifier> [;|,] [specifier]`
    - `pattern.txt`
        - structure
            - pattern := br \| br
            - br := concat \& concat
            - concat := piece [piece] ...
            - piece := atom[multi]
        - vim's regex engine supports everything, `:help pattern` to learn.
            - e.g. `\{n,m}` and `\{-n,m}`, greedy and non-greedy multi.
    - `change.txt`
        - `:help :s`, `s_flags`
            - `g`, change every match on the line
            - `I`/`i`, noingore/ingore case


### 2020-12-29
1. leetcode 330
    - greedy. every time we patch $[0,miss)$ with a $x,x\le miss$ to reach $[0,miss+x)$, we choose the largest $x$ possible: $x = miss$.
    - what about dp?

2. leetcode 123,188做不出来 思考1
    - state or condition？
        - state：从$P_{i-1}$到$P_i$时需要对state进行判断，转到$P_i$之后还需要更新state。
        - condition: 不同的condition下，$P_i$的值也不同，因此实际上应该是$P_{c_1,c_2,c_3,\dots c_k},\ c_i \in C_i$


### 2020-12-30
1. leetcode 1046： 每次选出2个最大，模拟之后再插入
    - 快排再取出$O(n\log n)$
        - 快排一次，每次插入时二叉插入？找到插入位置$O(\log n)$，移动数组元素来插入$O(n)$
    - 遍历一遍找最大两个$O(n)$
    - 构造一次堆，取出两个最大的(两次$O(\log n)$)，再插入一个较小的差值$O(\log n)$
2. linux直播环境？
    - [弹幕库](http://bilibili.danmaku.live/)，支持Windows/Mac/Linux（页面根据User-Agent自动选择下载版本？）
        - 解压`unzip 弹幕库-linux-v2.2.2.zip -d /opt/danmuku`
        - 软链`sudo ln -s /opt/danmuku/弹幕库 /usr/bin/danmuku`
        - 运行，提示`chrome-sandbox`需要为`4755 root:root`，`chown root:root $file && chmod 4755 $file`
    - obs-studio, with browser source
        - obs studio on debian: `sudo apt-get install ffmpeg obs-studio obs-plugins`
            - 打开发现没有Browser源，速速google(bing属实拉跨，半天搜不到)
        - 下载插件: `curl -fLO https://github.com/bazukas/obs-linuxbrowser/releases/download/0.6.1/linuxbrowser0.6.1-obs23.0.2-64bit.tgz`
            - 解压: `tar -xaf linuxbrowser0.6.1-obs23.0.2-64bit.tgz -C ~/.config/obs-studio/plugins`


### 2020-12-31
1. Linux 时间
    - `/etc/localtime -> /usr/share/zoneinfo/...`: `man localtime`
        - NOTE: _Because the timezone identifier is extracted from the symlink target name, this file **may not be a normal file or hardlink**._
    - on a older system: `sudo unlink /etc/localtime && sudo ln -s /usr/share/zoneinfo/$zonename`
    - on `systemd` based distros: `man timedatectl`
    - on newer distros(like ubuntu): `vim /etc/timezone`?(not tested) `timedatectl` will update this file as well, so `timedatectl` is recommended.
2. bash和zsh的不同
    - zsh中`echo`为内建命令，类似`/bin/echo -e`
    - `$"string"`的不同：
        - bash: `A double-quoted string preceded by a dollar sign ($"string") will cause the string to be translated according to the current locale.`, **`If the current locale is C or POSIX, or if there are no translations available, the dollar sign is ignored.`**
        - zsh: info手册和man手册都**没有说明**，执行`echo $"\ta"`，`$`也被一并输出(可能需要进一步查找资料)
    - bash将`.*/`展开成`../ ./`，zsh不展开`.*/`


# 2021

## 2021-1

### 2021-1-1
1. `ssh-agent` foward
    - 启用: `ssh -A|-oForwardAgent=yes` (sshd AllowAgentForwarding=yes)
        - 持久化: `~/.ssh/config`/`/etc/ssh/ssh_config.d/*.conf`
        ```conf
        Host $host
            ForwardAgent yes
        ```
    - 启动: `ssh-agent <x-session>`(linux图形界面自动启动)/`eval $(ssh-agent -s)`
    - 添加密钥: _The agent initially does not have any private keys._
        - `ssh-add [-L|-D]`
        - `ssh -oAddKeysToAgent=yes $host`在连接**成功之后**才会添加Key
        ```txt
        82,84d80 # 无法使用公钥连接时，ssh-agent内没有密钥，连接失败，key也没添加
        < debug3: receive packet: type 7
        < debug1: SSH2_MSG_EXT_INFO received
        < debug1: kex_input_ext_info: server-sig-algs=<rsa-sha2-256,rsa-sha2-512>
        88a85,101 # 公钥连接成功，最后才添加key
        > debug3: receive packet: type 51
        > debug1: Authentications that can continue: publickey
        > debug3: start over, passed a different list publickey
        > debug3: preferred gssapi-with-mic,publickey,keyboard-interactive,password
        > debug3: authmethod_lookup publickey
        > debug3: remaining preferred: keyboard-interactive,password
        > debug3: authmethod_is_enabled publickey
        > debug1: Next authentication method: publickey
        > debug1: Offering public key: .ssh/id_rsa RSA SHA256:UJnSYwtQ7zgZUoIO8zKQ1UGtu3B6PVdtMzfmma6lZMk explicit
        > debug3: send packet: type 50
        > debug2: we sent a publickey packet, wait for reply
        > debug3: receive packet: type 60
        > debug1: Server accepts key: .ssh/id_rsa RSA SHA256:UJnSYwtQ7zgZUoIO8zKQ1UGtu3B6PVdtMzfmma6lZMk explicit
        > debug3: sign_and_send_pubkey: RSA SHA256:UJnSYwtQ7zgZUoIO8zKQ1UGtu3B6PVdtMzfmma6lZMk
        > debug3: sign_and_send_pubkey: signing using ssh-rsa SHA256:UJnSYwtQ7zgZUoIO8zKQ1UGtu3B6PVdtMzfmma6lZMk
        > debug1: identity added to agent: .ssh/id_rsa
        > debug3: send packet: type 50
        ```
        - 注意倒数第2行才添加Key
    - 总结：别用`AddKeysToAgent`，手动`ssh-add`算了


### 2021-1-4
1. `sort`
    - `-n`/`-g`/`-h` numeric/general-num/human-num(1k,2G): 10>2
    - `-t`: field separator
    - `-k, --key=KEYDEF`, `KEYDEF := F1[.C1][OPTS1][,F2.C2[OPTS2]]`
        - `-k ${F1}.${C1},${F2}.${C2}` 从第F1个field的第C1个字符，到第F2个field的第C2个字符


### 2021-1-14
1. win7安装office2016
    - 只支持SP1及以上
    - Windows Update 80072efe错误，尝试多种方案，解决失败
    - 从`uptodown`下载`Service Pack 1`直接离线安装
2. 相机RAW格式`ARW`转`jpg`
    - `sudo apt-get install exiftool`
    - `exiftool -b -PreviewImage -w .jpg -ext arw <directory>`


### 2021-1-16
1. 装机-硬件组装(视频教程[BV1jE411e7hw](https://www.bilibili.com/video/BV1jE411e7hw))
    1. 装主板
        - CPU
        - 内存条
        - SSD：带散热片/不带散热片
        - 装IO挡板，固定主板到机箱
    2. 装电源
    3. HDD、显卡、机箱前面板接线
2. 装机-软件
    1. **BIOS放电重置**：断电，取下主板电池，短接CLRTC(设错了内存频率过不去自检)
    2. BIOS设置内存超频
        - X.M.P., Intel Extreme Memory Profile，存入内存条EEPROM中的额外两组`CL-tRCD-tRP-tRAS-CMD`等数据
        - D.O.C.P., DRAM Over-Clock Profile(华硕主板B450M)，根据频率设定自动(？)选择参数
    3. 启动盘装windows
3. 问题：**`dd`制作windows启动盘失败**，安装时提示缺少驱动
    - `dd if=xxx.iso of=/dev/sdx`失败
    - _先分一个`sdx1`分区，再`dd`进`sdx1`，失败_(?)
    - U盘最后留一个30M分区`sdx2`放uefi驱动？失败


### 2021-1-18
1. 美赛流程理解
    1. 实际问题 分析抽象(查阅文献)
    2. 简化的问题 算法选择(经验)
    3. 编程实现+数据处理(语言和软件)
    4. 结果展示(文档和绘图)


### 2021-1-28
1. mtdps虚拟机环境搭建
    1. 安装虚拟机，配置ip，`apt`换源
    2. 运行`basics.sh -g -t`自动配置
        - zsh，vim，无密码sudo
        - 安装python2.7并修改python软链接，安装supervisor
        - mysql-5.7
    3. 配置git
        - 修改config：`user.name/email`, `push.default`, `alias.br/lg/co`
        - 生成ssh key并添加到远程仓库，配置ssh-agent
    4. 配置python venv虚拟环境
        - 新的虚拟环境先更新`pip`, `wheel`, `setuptools`，否则可能会有玄学问题
        - 安装mysql相关的模组时报错缺少`mysql_config`，需要装3个`apt`包：`python3-dev`, `default-libmysqlclient-dev`, `build-essential`
2. 搭建完毕后`flask run`报错: _connection refused_


### 2021-1-29
1. mtdps环境调试
    1. 猜测是找不到elasticsearch和sql，准备验证
    2. 使用tarball直接部署elg，复用12月1日的supervisor配置文件进行自启动管理
    3. 同样复用12月1日的`sqldump.sql`文件，导入数据库内容
        - 导出：`sqldump -u <user> -p --all-databases > sqldump.sql`
        - 导入：`sql -u debian-sys-maint -p<password> < sqldump.sql`
        - **问题**：导入数据之后，无法使用导入的用户/密码登录
        - **解决**：重新启动mysqld，可能它只在启动时load库里的用户/密码
    4. _connection refused_仍然没有解决
2. bibtex
    1. 基本结构`@entry_type{ citetag, tag1={xxx}, tag2={xxx}}`
    2. `entry`的类别，有些类被有必要的`tag`
        - string, comment, ...
        - article, inproceedings, techreport, ...
    3. 使用方式
        - 保存`xxxx.bib`文件，tex正文中`\bibliography{xxxx}`可在语句处生成参考文献目录，`\cite{citetag}`生成引用标号
        - `\bibliographystyle{xxxx}`控制参考文献样式


### 2021-1-30
1. 审稿子
2. mtdps环境搭建调试
    1. elasticsearch报错illegal index name(不影响es的服务)
        - indice目录下有人为创建的冗余内容，删除即可
    2. flask报错 _connection refused_解决
        - 部署完es后，**将`settings.py`中的IP和路径本地化**
    3. flask写sql时，报错主键重复
        - `LogExtract.py`生成`seq`(sql主键)的逻辑有问题，修复为`seq=sql_db.query.count()+i+1`(待测试)
    4. filebeat crash问题
        - 原因: filebeat设置`json.overwrite_keys: true`，且输入日志含有非空`@metadata`字段
        - 解决: 输入日志避免使用`@metadata`字段

### 2021-1-31
1. mtdps环境搭建调试
    - 测试`LogExtract.py`: 修复后问题已解决
    - 写`elg`+`supervisor`+`mysql`(+`filebeat`部署文档)
    - 更新部署tarball
2. faq补了点总述
3. `jounalctl`
    - `-f, --follow`
    - `-u, --unit=UNIT|PATTERN`


## 2021-2

### 2021-2-1
1. mtdps
    - `elasticsearch`的`index`名中不接受大写字母
        - 命名规则见[相关官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html)


### 2021-2-2
1. makefile
    1. 基本格式: 由多条构造规则组成，每条都有如下格式
    ```txt
    target: prerequisites
        commands
    ```
    2. 用法
        - `make`: 自动查找`Makefile`中第一个非通配符的`target`，进行构建
        - `make <target>`: 指定`target`进行构建
    3. 变量
        - 赋值与使用: `cc = gcc`, `$(cc)`
        - `$@`: 特殊变量，展开为本条构造规则的`target`
        - `$<`: 特殊变量，展开为本条构造规则的第一个`prerequisite`
    4. **命令**
        - `subst <this>,<that>,<string>`: substitude `this` into `that` in `string`(**NOTE** `,` is field separator)
        - `wildcard <pattern>`: output files matching `pattern`, separated by `<whitespace>`. e.g., `wildcard *.c`
        - 将命令展开为执行结果: `$(command arg1,arg2,$(command2 arg1))`
    5. **通配符**
        - `%`: 任意通配符。用在`target`中，当`make`查找某个`object`的构建法则时，一但匹配到该`target`，该条构造规则中的`%`都被展开为相应的匹配部分，e.g. `%.o: %.c some_headers.h`


### 2021-2-6
1. latex macros
    - plain tex: `\def\macroname #1<sep>#2{expanded str, possibly containing #1,#2}`
        - 不检查该macro是否已经定义，直接覆盖
    - latex: `\newcommad`, `\renewcommand`
2. bib reference
    - count into toc: `\usepackage[nottoc]{tocbibind}`
    - add numbering like a chapter: `\usepackage[numbib]{tocbibind}`


### 2021-2-7
latex:
1. `\usepackage{indentfirst}`
2. counter, label:
    - `table`/`figure`/`section`... $\longleftrightarrow$ `\thetable`/`\thefigure`/`\thesection`
    - `\setcounter{table}{0}`
    - `\renewcommand{\thetable}{\alpha{table}}`
3. caption specifying:`caption`, `subcaption` package
    - overall: `font=small`
    - `labelfont=bf, textfont=normalfont`
    - `labelformat=simple, labelsep=period`


### 2021-2-8
latex:
1. toc depth:
    - globally, invariable: `\setcounter{tocdepth}{2}`
    - variable at place: `\usepackage{tocvsec2}`, `\settocdepth{subsection}`
2. toc spacing:
    - `\usepackage{setspace}`, `\begin{spacing}{0.1}`
3. `\autoref` in `hyperref` package
    - red brackets: `hidelinks`
    - rename: `\def\<type>autorefname{<newname>}`
4. align numbering: `\notag`/`\nonumber`, `\tag{blablabla}`

overleaf:
1. user mapping/marcro like vimrc: using tampermonkey script

```javascript
// ==UserScript==
// @name         Overleaf Editor Custom VIM Keybindings
// @namespace    http://tampermonkey.net/
// @version      0.1
// @match        https://www.overleaf.com/project/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // poll until editor is loaded
    const retry = setInterval(() => {
        if (window._debug_editors === undefined) return
        clearInterval(retry)
        // get current editor instance
        const editor = window._debug_editors[window._debug_editors.length -1]
        // vim keyboard plugin
        const vimKeyboard = window.ace.require("ace/keyboard/vim")
        // add custom keybindings - insert mode applies on insert
        // normal mode applies while escaped
        vimKeyboard.Vim.map("j", "gj", "normal")
        vimKeyboard.Vim.map("k", "gk", "normal")
        // set the modified keyboard handler for editor
        editor.setKeyboardHandler(vimKeyboard.handler) console.log("Custom key bindings applied")
    }, 100)
})();
```


# 2021-2-9
1. newcommand: `\newcommand{\red}[1]{\textcolor{red}{#1}}`
    - `\renewcommand{\ref}[1]{Fig.\ref{#1}}` **failed** ?
2. appendix: `\usepackage[page,toc,titletoc,title]{appendix}`
    - page: Appendices start from a new page?
    - toc: Appendices start page added to toc
    - title: sections inside Appendices add `Appendix` before label
    - titletoc: similar to title, used in toc


## 2021-3

### 2021-3-1
1. C
    - `return &local_var`返回栈上的地址，程序可能直接crash
    - a better malloc: `int * aaa = malloc(sizeof *aaa * length);`


### 2021-3-2
1. 讨论会议 纪要
2. 通信原理开课


### 2021-3-3
1. 删除GNU `gettext` `read-mo.c`的sorted验证，安装后仍然无法反编译中文`mo`文件
    - `gettext`的`read-mo.c`不支持宽字符，但是含宽字符的`po`文件可以正常编译
2. 准备简历初稿+投递
3. clone了一下ATT&CK的开源网站
    - python `venv`的激活脚本`activate`必须用bash执行(用zsh直接source不会出错，但是source写进zsh脚本就报错)
4. leetcode 338, counting bits：任意`k`进制数，第`n`个数含有的1的个数`#n`？
    - `n = m * k`，则`#n = #m`
    - `n = m * k + 1`，则`#n = #m + 1`
    - 其他情况下，` #n = #(n/k) = #m`
5. Windows下，git安装目录单独挂载为根目录`/`
    - 如果git安装到D盘，则C盘被挂载到`/c`，安装到C盘则不挂载
    - 挂到`/c`后，`C:\xxx\xxx`路径对git目录下的binary失效
        - **那么从cmd/powershell里继承的环境变量，例如`$HOME`也会失效！**


### 2021-3-4
[`MkDocs`](https://www.mkdocs.org) & [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/)(theme)
1. **安装：**
    - `MkDocs`作为python package安装到`dist-packages`中的`mkdocs`
    - 各种主题也作为python package安装到`mkdocs`下的`themes`
2. **主题配置**
    - 在`yml`文件中配置`theme: theme_name`(或`theme.name`)
        - `theme`文件夹里安装了`theme_name`，load对应的theme`yml`文件
        - `theme_name`无效(比如`null`)，无theme加载，必须要求`theme.custom_dir`含有一个完整theme
    - 在`yml`文件中配置`custom_dir`
        - 需要使用相对路径
        - `custom_dir`中的主题`yml`不会被加载

MISC
1. `$HOME`的值由login, xdm等程序设置，先查询`/etc/nsswitch.conf`，再从`/etc/passwd`中读取
    - 没有继承`$HOME`时，bash也会以这种方式建立`$HOME`
2. python的package`path/to/pack`
    - `python -m path/to/pack`时，首先执行目录下的`__init__.py`

leetcode
1. 300, longest increasing subsequence (TODO)
2. 354, Russian doll envelopes (TODO)

### 2021-3-5
1. 通信原理课程
    - 确知信号 + 随机过程 快速回顾

2. C++多态的实现: `vitual`关键字、隐藏的`__vptr`(for object)，及其指向的函数指针数组`vtable`(for type)
    - 保证子类的方法可以覆盖父类
    - `(*(p->__vptr[n]))(p)`: if `p->__vptr` is `void **`, what is the type of `p->__vptr[n]`? `void *`?
    - `(*p->vptr->fn)(p)` ?

3. 阿里云面试
    - 基本问题：不要老是推迟、及时反馈、注意信号和设备状态、说话音量
    - 表述问题：
        - **提前准备文稿**: 自我介绍、项目介绍、项目关键技术/workflow、项目经典实例
    - 技术问题：二进制分析相关、操作系统(至少：装载、库、进/线程、内存池)相关、C语言相关(对齐，offsetof宏:对编译的理解)

4. 点石创校宣讲志愿者：步场、接待、递话筒、改卷、收场 (**注意清点试卷**)



### 2021-3-6
1. leetcode单调栈: 503.next greater element
    - 等效：柱状图能接住的最多水
    - 柱状图中的最大矩形：某个柱子左右，第一个小于它的
2. latex实验报告模板更新
    - 添加页眉页脚`fancyhdr`
    - 修改目录标题名`tocloft`(`\begin{center}`居中标题)
        - **这个宏包会覆盖toc页面的pagestyle**
    - 添加附录
        - `\begin{appendices}`而不是`\begin{appendix}`
        - `\appendix<type>name`,`type='', page, toc`

3. 数字图像处理课程
    - **matlab递归函数，进去一层，变量就undefined?**
4. bash重定向
    - `2>&1` -> `int dup2(int oldfd, int newfd); dup2(1,2);`


### 2021-3-7
1. att&ck网站简介文档
2. bash/zsh commandline editor mode: emacs/vi
    - bash: `set -o <emacs|vi>` (`bind -P`)
    - zsh: `bindkey <-e|-v>` (`bindkey -L`)
    - zsh vi模式的问题：从normal返回insert后`<backspace>`不起效
        - `bindkey "^?" backward-delete-char`
    - zsh vi模式优化
        - 保留emacs模式常用键位：`bindkey -L`后，选取`^W`, `^P`, `^N`等等
        - `zshrc`上传到[my-vim-config](https://github.com:144026/my-vim-config)的`zsh-config`分支
4. bash重定向帖子 50%


### 2021-3-8
1. 通信原理课程：信道

2. ATT&CK讨论
    - 拓展mtdps
3. NetTopo模块(grafana dependency graph)
    - 修改sql root用户密码
    - mysql创建用户bug: `drop`+`flush privileges`
4. elg调试
    - elasticsearch不通，重置虚拟机
    - 调试flask框架，记录三个error(bug待修)
        - TODO: 调试一键清空脚本
    - gitlab远程空间不够，报错`Failed xxxx`很像本地错误，push才看得出来错误在远程
4. 阿里云2面


### 2020-3-9
1. leetcode 1047,1209：消除重复字串，recursively
    - 递归/栈


### 2020-3-11
word标题格式调节
1. 标题构成: `缩进`+`编号`+`间隔`+`标题内容`
2. `编号`格式: 搜索功能`多级列表`->重新定义多级列表->更多->**链接到标题**
3. `编号`格式: 搜索功能`多级列表`->重新定义多级列表->更多->**链接到标题**
4. `间隔`格式: 搜索功能`多级列表`->重新定义多级列表->更多->**选择空格，而不是制表符**
5. `标题内容`格式: 样式库选中样式->修改->字体->中文、西文字体


### 2020-3-12
1. deepin chroot
    - mount失败,bad [superblock](https://en.wikipedia.org/wiki/Unix_File_System): `fdisk`找到start sector和sector size，`mount -o offset=<bytes>`
    - `cp`默认并不保留文件属性，拷贝后权限树混乱：`cp --preserve=all`, `cp -a/--archive`, `rsync -a`
    - `/proc`和`/sys`不起效：`mount -o bind /proc /newroot/proc`
        - `sys`和`proc`被重复mount?: **TODO**
    - `add-apt-repository`安装失败: **TODO**
    - deepin普通用户sudo会从pam唤起弹窗，弹不出来sudo会失败
2. 阿里在线笔试 **TODO**
    - 有向图单原最短路径
    - codeforces 1411


### 2020-3-13
1. 点石创校
    - 公司(定义、种类)、公司治理框架(股东与董事)、公司运营(资金)
    - 基金、合伙制(GP,LP,LLP)、投资(PE,VC)
    - 商业计划：公司、行业、市场、用户、产品服务
2. deepin chroot
    - sudo失败，`hostname`仍然是主机，解析不出`127.0.1.1`，修改`/etc/hosts`
    - dns解析问题：修改`resolv.conf`(Network Manager自动设置)
    - **参考[Arch Linux chroot Docs](https://wiki.archlinux.org/index.php/chroot)**
3. deepin chroot配置
    - mount sys，proc，run，dev等等
    - 应用程序位置`/opt/apps/com.qq.im.deepin/files/run.sh`
    - **GUI 应用**:`xhost +local:`, `export DISPLAY=xxxx`
    - **fcitx输入法**: 在`run.sh`里export环境变量(正常环境`export | grep fcitx`)
        - fcitx的工作原理？


### 2021-3-14
1. deepin chroot
    - qq
        - 撤回、回复无效，很多小bug
        - 气泡模式中文字体变成方框(是缺字体还是qq没能找到字体？缺是哪个字体？该装到哪里？)
    - 休眠之后死机，重新打开后，chroot权限树混乱，大量目录ower:group变成1000:1000


### 2021-3-15
1. C string cat `puts("hello" "world");` (a core language feature)
    > The C99 standard §5.1.1.2 defines translation phases for C code. Subsection 6 states:
    >> Adjacent string literal tokens are concatenated.
2. GNU [autotools intro](https://www.gnu.org/software/automake/manual/html_node/Autotools-Introduction.html)
    - **`autoreconf --install`**: `configure.ac`, `Makefile.am`
    - **`./configure`**: `configure`, `config.h.in`, `Makefile.in`
    - `make`, `make distcheck`

```txt
                        +--------+
configure.ac------>+--->|autoconf|------>configure
                   |    +--------+
                   |
                   v    +--------+
Makefile.am------->+--->|automake|------>Makefile.in
                        +--------+
```


### 2021-3-16
1. `git rebase <dst_ref> [branch]`

### 2021-3-17
1. cmake verbose: `make VERBOSE=1`
2. **link order matters**!逐个打开库文件，查找带解析的符号，一个库打开之后，连接器就会忘记它
	- static lib: `-lmost_dependent -lxxx -lyyy -lleast_dependent`
		- **OK**: `-lgtest -lgtest_main -lpthread`
		- 循环依赖: `-( -laaa -lbbb -)`(qoute `(`/`)` if needed)
		- bad: `-lpthread -lgtest -lgtest_main`
	- objects and libs:
		- **OK**: `gcc a.o -lbenchmark -lpthread`
		- BAD: `gcc -lbenchmark -lpthread a.o`
	- dynamic: they resolve smartly?
3. autoconf
	- 探测toolchain完整性
		- `AC_PROG_CC`, `AC_PROG_CXX`, `AC_PROG_RANLIB` - `AM_PROG_AR` - 检查库和数据类型
		- `AC_CHECK_LIB(lib,func)`, `AC_TYPE_UINT32_T`
4. automake
	- 安装路径：`noinst_`, `bin_`, `lib_`, `_include`, `canocalized_names_`
	- macro类型：`_PROGRAMS`, `_LIBRARIES`, `_SOURCES`, `_HEADERS`
		- `_LDADD`, `_LDFLAGS`, `_LIBADD`
	- 预编译和编译选项：`AM_CPPFLAGS`, `AM_CFLAGS`
		- `AM_CPPFLAGS = $(top_srcdir)/inlude`
5. libtools(`apt-get install libtools`)
	- 加入`configure.ac`工具链：`LT_INIT[(<enable|disable>-<shared|static>)]`(override `AC_PROG_RANLIB`)
	- 定义macro: `_LTLIBRARIES`, `_LDFLAGS = -version-info 0:0:0`
	- 添加m4宏
		- configurea.ac: `AC_CONFIG_MACRO_DIRS[m4]`
		- Makefile.am: `ACLOCAL_AMFLAGS = -I m4`

### 2021-3-18
1. matlab/octave function call: var 'xxxx' undefined：检查一下参数是不是合法，有没有漏掉
2. move a python virtualenv?(`venv` is a subset of `virtualenv`)
	- nop, `--relocatable` deprecated, no clean way to do it


### 2021-3-19
1. `ls`使用`isatty(int fd)`，向tty和其他文件输出的Field separator不同(full manual: `info ls`)
	- tty: 空格；文件: `\n`(`-C`来强制指定空格)
2. makefile
	- 空格前导行，由make解析；`<tab>`前导行有shell解析(默认`/bin/sh`)
		- recursive make: `<tab>cd dir && $(MAKE)`
	- subsitutiton: `$(var:from_a=to_b)`
	- simple assgin: `var := value`(gnu make), `var ::= value`(POSIX)
