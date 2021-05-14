---
title: 日志 2020
date: 2020-09-20 23:30:37
tags:
- journal
categories:
- journal

mathjax: true
---

journal 2020

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

