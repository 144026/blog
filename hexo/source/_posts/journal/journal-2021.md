---
title: 日志 2021
date: 2021-01-02 23:30:37
tags:
- journal
categories:
- journal

mathjax: true
---

journal 2021

<!--more-->

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


### 2021-2-9
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
        - 注意函数名与文件名一致，检查变量个数是否一致
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
    - 公司与企业(定义、种类)、公司治理框架(股东与董事)、公司运营(资金)
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
    >
    > > Adjacent string literal tokens are concatenated.
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
        - **循环依赖**: `-( -laaa -lbbb -)`(qoute `(` and `)` if needed)
        - bad: `-lpthread -lgtest -lgtest_main`
    - objects and libs:
        - **OK**: `gcc a.o -lbenchmark -lpthread`
        - BAD: `gcc -lbenchmark -lpthread a.o`
    - dynamic: they resolve smartly?
3. autoconf
    - 探测toolchain完整性
        - `AC_PROG_CC`, `AC_PROG_CXX`, `AC_PROG_RANLIB`, `AM_PROG_AR`
    - 检查库和数据类型
        - `AC_CHECK_LIB(lib,func)`, `AC_TYPE_UINT32_T`
4. automake
    - 安装路径：`noinst_`, `bin_`, `lib_`, `include_`, `canocalized_names_`
    - macro类型：`_PROGRAMS`, `_LIBRARIES`, `_HEADERS`, `_SOURCES`
        - `_LDADD`, `_LDFLAGS`, `_LIBADD`
    - 预编译和编译选项：`AM_CPPFLAGS`, `AM_CFLAGS`
        - `AM_CPPFLAGS = -I$(top_srcdir)/inlude`
5. **libtools**(`apt-get install libtools`)
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
    - 空格前导行，由make解析；`<tab>`前导行由shell解析(默认`/bin/sh`)
        - recursive make: `<tab>cd $@ && $(MAKE)`, 或者`$(MAKE) -C $@`
    - subsitutiton: `$(var:from_a=to_b)`
    - simple assgin: `var := value`(gnu make), `var ::= value`(POSIX)
        - make是**Marco language**，变量全是纯字符串(例如`$(subst .o,.c,$(wildcard *.c))`)，实际引用时现场defer(delayed expansion)。simple assign在复制时即展开，随后始终保持不变。


### 2021-3-21
1. 什么是flask？就是跑了几个`.py`脚本，还能让他们之间通过http请求互相通信
2. C language
    - `sizeof`: unary operator(单目运算符), 返回operand所占的存储空间
        - usage: `sizeof <expression|data_type_cast>`, **`cast` is a data type enclosed in parenthesis**.
        - exceptions: in `sizeof arr_name`, `arr_name` will not be converted into a pointer to the first element
        - note: typically, `sizof` exps are replaced with constants in complilation (**before link?**), 所以`extern int arr[]`+`sizeof arr`时，编译器无法确定`arr`的大小
            - C99引入的VLA，sizeof只能在运行时确定大小
    - `void *`, `void **`
        - `void *`: 通用指针，赋值和被赋值时，编译器会自动做impplicit cast。不允许de-reference和指针运算
        - `void **`: 不是通用指针，反而和`int *`类似。函数接受`void **`参数，一般是需要修改一个`void *`指针的值，才只好把它的地址传进来。


### 2021-3-22
1. Vim语法高亮错误debug
    - 首先找到上下文，使用`:echo synIDAttr(synID(line('.'), col('.'), 1), 'name')`查看syntax type，然后去源码(vim script)里找匹配规则
    - 如果没用插件，一般是`/usr/share/vim/vim<version>/syntax`；用了插件，可能是`<plugin_dir>/{syntax,autoload}`
    - 遇到不认识的匹配符号、函数，直接在vim里`:h <topic>`，比如`:h /\_`, `:h map()`, `:h \%(\)`


### 2021-3-30
1. 忙各种杂七杂八的事情
2. `.gitlab-ci.yml` + `mkdocs-material`
3. 本机`npm`版本太低，升级`npm`和`node`报错: 用官网下载最新`npm`的binary来装
    - 但是不能用它来更新本地的`node`？使用本地升级后的`npm`倒是很OK？


### 2021-3-31
1. python常见基类操作
    - list `[]`: `l.append(a)`, `if a in l`
    - dict `{}`: `d[key]=value`(追加/更新), `if a in d.keys()`/`d.items()`
    - string `str(var)`: `"a" + "b"`, `"a".join("b")`, `"a".split("b")`
    - `isinstance(var, keyword)`

## 2021-4

### 2021-4-1
1. flask run忽略`app.run`以及lazy loading(遇到错误不会停止)+web debugger
2. python import
    - 目录scope: `form <mod> import *`，在`sys.path`下查找，找到则以模块导入
        - 但是`<mod>`里的文件不能import `mod`目录之外的内容
    - 模块scope: `from .<mod> import *`，根据当前模块名称(`__package__`+`__name__`)解析出子模块名，当前模块名里`.`的个数不少于import里的`.`才能解析成功
        - 直接执行这样import的文件，会被解析成`__main__.<mod>`而报错
    - 一种解决方案？
```python
if __name__ == '__main__':
    from . import *
    # from <mod> import *
else:
    from .<mod> import *
```


### 2021-4-2
1. CVE-2018-1111(dynoRoot)重新分析+复现
    - 看`dhclient.c`+`11-dhclient`源码做分析：不一定是252字段
        - 但是`dhclient`和`11-dhclient`之间到底是怎么样的调用关系?

```txt
1. dhclient -> nm-dhcp-helper -> 11-dhclient ?
但是如果不设置NetworkManager `managed=true`,实际修改11-dhclient发现它并没有被调用
2. dhclient -> nm-dhcp-helper -> NetworkManager -> 11-dhclient ?
```

2. filetype `htmldjango`
    - `div`, `form`, `label`, `input`, `button`
    - `name`, `id`, `style`, `class`


### 2021-4-3
1. 解决kali的qt程序theme错误问题：直接运行`qt5ct`修改主题
    - Kali xfce提供的Appearance配置出的主题只对xfce系列软件有效
    - 而普通Qt程序读取的是`qt5ct`的标准配置文件`{/etc/xdg, $HOME/.config}/qt5ct/qt5ct.conf`


### 2021-4-8
1. Ubuntu1804的`Unix/_git`版本过低，导致`<tab>`无法自动补全git分支
    - zsh会检查同名`.zwc`文件，如果时间戳比对应脚本新，就不读取脚本，直接使用`.zwc`


### 2021-4-9
1. getopt(1,3), getopt_long(3), argp(glibc)
2. C traps & pitfalls:
    - 差一问题：上界出点-下界入点
    - 数组越界覆盖栈：`int i; int a[10]; a[10]=0`

### 2021-4-12
1. 修复`Unix/_git` zsh脚本找不到`Unix/_ssh_hosts`问题
2. `CR2` raw格式转换
    - 使用imageMagick自带的`convert`命令，然而它调用的`ufraw-batch`已经停止维护，无法直接下载
    - 使用替代品`dcraw`解码Raw图片，然后让convert从标准输入读取：`dcraw -c -w <raw image> | convert - out.jpg`
        - `-c`: **c**at decoded raw image to stdout
        - `-w`: use **w**hite balance specified by camera


### 2021-4-13
1. latex & vim
    - xelatex: `-output-directory=`, `-aux-directory=` (dir must exist)
    - latexmk: `-outdir=`, `-auxdir=`, `-c`, `-C`
    - `.latexmkrc`: `$out_dir`, `$aux_dir`, `$clean_ext`
        - `$clean_ext`: clean file with **ext**ensions specified in it
    - vimtex: `g:vimtex_compiler_latexmk = { 'build_dir' : 'build' }`


### 2021-4-15
1. xmind2020 latex公式：一旦使用`\def`覆盖了宏，本次运行时的宏就会被污染

### 2021-4-16
1. 图像运动模糊 频域滤波：维纳逆滤波零点导致图像全是黑白条纹：自己猜一个高斯噪声/求一个自相关，再维纳滤波
2. LaTeX：
    - pgffor：`\foreach \i in {1...5}{code}`
    - `\includepdf`/`\includegraphics`: `[page=1-4]`
    - `\equationautorefname`
3. 修改文件/目录名encoding：`convmv`失败
    - `cat dirname`失败：Linux不允许`read()`目录二进制内容
4. bash直接执行systemcall: `ctypes.sh`
    - 不支持`zsh`，必须根据`zmodload`重新开发
    - 编译安装了动态库`ctypes.so`，bash使用`enable -f <SHARED_OBJ> BUILTINS`从动态库加载dlcall等命令，调用外部动态库内容
    - `struct`功能，字段和value不匹配，乱序了，未找到原因
5. `sash`与POSIX


### 2021-4-17
git internals:
1. objects
    - hash-file/cat-file
    - update-index/read-tree/write-tree/commit-tree
2. ref
3. packfile
    - verify-pack
4. refspec
5. protocol


### 2021-4-19
zeek scripts:
- variable: count, enum, str, record, set, table...
- `var$field=value`
- operator, conditional and loops
- function, callback, hook, event
- scope: module, global, local

### 2021-4-20
makefile traps:
1. 空变量导致危险操作
2. 依赖链：每次都重新构建
    - `_FORCE` target: no pre, no recipe
    - `.PHONY` target: no pre, has recipe


### 2021-4-22
1. git 'local' remote: `git remote add path/to/repo`
2. zsh history expansion: !, !! and the special ^foo^bar(!!:s^foo^bar)
3. flask/django project layout: project excuted as a package
    - only `top dir` in the sys.path: even if `flask run` directly executed inside dir `aaa/`
```txt
top
├── aaa
│   └── app.py
└── bbb
    └── app.py
```
4. python relative import a billionth times
5. bash `>&` duplicate: no overwrite, but append


### 2021-4-26
Plain tex
1. tex primitive: `\left`, `\right`, `\catcode`, `\sfcode`
2. use primitives to define macro: `\def`, `\let`
3. tex/latex core: plain.tex/latex.ltx, a set of essential macros
5. math typesetting: box, mathlist, spacing atom

Linux:
1. `-staticgcc`, `nostdlib`
2. ldd，strace
3. brk()? how is execve() excuted?

Git:
1. the real git clean:
```bash
git -c gc.reflogExpire=0 -c gc.reflogExpireUnreachable=0 \
  -c gc.rerereresolved=0 -c gc.rerereunresolved=0 \
  -c gc.pruneExpire=now gc
```

### 2021-4-28
1. block -> inode -> dir as inode -> special dir `/`


## 2021-5

### 2021-5-3

1. github CI actions
    - `.github/workflows/<NAME>.yml`
    - 在ci中使用token操作自己的github仓库
        - 使用变量展开避免明文写入token: `{{ $secrets.VARNAME }}`(需在仓库设置界面配置)
    - 可以引用大量别人写好的插件


### 2021-5-5
1. grpc添加时间参数

### 2021-5-7
1. ramsay复现
    - exe感染: `bindsvc.exe`在64位系统`sysWOW64`目录找到`bindsvc.exe`和`wideshut.exe`后，才能正常感染exe
    - word感染：将`rundll32.exe`复制为`BON.exe`，运行`BON.exe msfte.dll,DllEntryPoint()`
        - 只能收集信息并打包rar，不能将信息附加到其他word文件里


### 2021-5-8
1. `man signal(1) signal(7)`, `sighandler_t`
2. C: VLA(variable length array)
    - since C99
    - gcc extension (even before C99)
3. QA steps
    - build test
    - lint test: cppcheck, scan-build
    - runtime test: valgrind, DrMemory, ASan(AddressSanitizer), LSan(LeakSanitizer)
    - regression test: test past bugs
4. suricata/zeek debug (reload/start)

```txt
suricata
--------
data structure
├── DetectEngineMasterCtx g_master_de_ctx
├── DetectEngineCtx * de_ctx
└── DetectEngineThreadCtx * det_ctx

routines
└── DetectEngineReload()
    ├── ConfYamlLoadFileWithPrefix()
    ├── ConfGetNode()
    ├── DatasetReload()
    ├── DetectEngineCtxInitWithPrefix()
    ├── SigLoadSignatures()
    ├── DetectEngineAddToMaster()
    └── DetectEngineReloadThreads()
        ├── TmThreadCountThreadsByTmmFlags()
        └── FlowWorkerReplaceDetectCtx()


zeek
----
zeekctl.in
└─ zeekctl.start()
   └─ controller.start()
      └─ controller._start_nodes()
         ├─ cmds = [(node, "start", [])]
         └─ executor.run_helper(cmds, shell=True)
            └─ run_cmds(shell=True, helper=True)
               ├─ cmdargs = helperdir+ "/start"
               ├─ nodecmdlist = ("localhost", cmdargs)
               └─ sshrunner.exec_multihost_commands(shell=True)
                  └─ helpers/start
                     ├─ source zeekctl-config.sh
                     └─ $scriptdir/run-zeek
```


### 2021-5-9
1. latex: `\lstset{numbers=none}`
2. html header meta: generator: GravCMS
    - CMS
    - RTFM: initialism/internet slang
    - Grav
        - PHP markdown extra
        - antimatter theme


### 2021-5-10
1. 信息论习题
    - 信息量与概率：$I(a_i) = -\log p(a_i)$
    - 信源概率分布与信源熵
        - 单符号、无记忆
            - $H(X) = E(I(X)) = \sum\limits_i p(x_i)I(x_i)$
            - $H_c(X) \ne \int p(x)\log [ p(x)dx]\ dx$, $H_c(X) = \int p(x)\log p(x)\ dx$
        - 单符号扩展: $H_N(X) = N\cdot H(X)$
        - 有记忆：马尔可夫信源
            - 极限分布、极限熵: $H_\infty = ?$
    - 信道容量$C$, $C_t$
        - 信道特性$p(b_i | a_i)$固定，改变信源$p(a_i)$求$\max\{I(Y; X)\}$
    - 信息率失真
        - 失真函数$D = d(a_i, b_j)$，平均失真度$\overline D = \sum\limits_{i, j} p(a_i b_j) d(a_i, b_j)$
        - 失真约束条件$\overline D \le D$
        - 信源特性$p(a_i)$固定，改变信道$p(b_i | a_i)$求$\min\{I(Y; X)\}$
2. 团队文档学习
    - 团队文件2011
        - 总则
            - 师生联席会、核心层？
        - 质量部
            - 组长相关
        - 人力资源部
            - 新人培训：大一/其他年级
            - 预备队：与团队正规招新并不相同
        - 教学管理
            - 外出毕设、实习管理办法
    - ftp: 团庆总结ppt
        - 8、15周年团庆总结ppt
    - ftp上的简报组文件亟需整理
3. 系统启动与linux
    - BIOS
        - legacy: 直接启动grub？
        - efi: 执行`xxx.efi`二进制文件，由该`.efi`程序接管(因为BIOS能做的事情很有限)
    - EFI
        - 需要单独磁盘分区，类型为`EFI system`，内容为`EFI/xxxxx/xxx.efi`
        - `grubx64.efi`: 仅仅用来启动`grub`
        - `systemd-boot.efi`: ???
        - `bootctl`, `/sys/firmware/efi/efivars/`
    - grub
        - `/etc/default/grub` ->`grub-mkconfig` -> `/boot/grub/grub.cfg`
        - grub shell
            - `set root=`
            - `linux /boot/vmlinuz-xxx root=xxx`
            - `initrd /boot/initrd-xxx`
            - `boot`
        - grub rescue shell?


### 2021-5-11
1. github
    - TexText: `textext/textext`
    - lervag/wiki.vim: just another text template engine(similar to markdown, or vim help files)
        - vimwiki, vimwaikiki
    - lervag/wiki-ft.vim: ftplugin
        - `syntax/<type>.vim`: highlite
        - `ftplugin/<type>.vim`: custom settings
        - `ftdetect/<type>.vim`: autocmds to set filetype
        - `autoload/wiki_ft/text_obj.vim`: custom text ojects
            - **vim text objects**
                - not available in `vi`
                - editing cmd structure: `[number][cmd][text_obj|motion]`
                - for plain text
                    - word:
                        - `aw`: a word (include surrounding whitespaces)
                        - `iw`: inner word (not include)
                    - sentence: `as`, `is`
                    - paragraph: `ap`, `ip`
                - for programming languages
                    - strings
                    ```txt
                    a", i", a', i', a`, i`
                    ```
                    - parentheses, brakets, braces
                    ```txt
                    a), i), a], i], a}, i}
                    ```
                    - for markup language
                        - tag blocks: `at`, `it`
                        - tag itself: `a>`, `i>`
    - lervag/apy:
        - `click`, `CliRunner()`
        - zsh completion handler: `_apy`
2. 编程培训
    - 链接task
        - `ar -rcs ARCHIVE MEMBER`
            - `-r`: **r**eplacement
            - `-c`: **c**reate
            - `-s`: generate index for every **s**ymbol in archive members
                - equivalent to `ranlib`
                - `ARCHIVE`链接起来会更快
        - `gcc -shared -fpic` ?
            - 动态库最初就应该支持基址随机：`-fpic`, `-fPIC`  -> `-shared`
                - **PLT**(procedure linkage table), **GOT**(global offset table)
            - ASLR出现后，才支持单个ELF装载基址随机：`-fpie`, `fPIE` -> `-static-pie`, `-pie`
                - PIE, position independent executable
                    - ASLR, address space layout randomization
                    - gdb: `set disable-randomization off` (on by default, for better dbg experience)


### 2021-5-12
1. gcc: a strange loop, self-referential backdoor insertion
2. latex: `\documentclass{beamer}`
3. socket programming
    - **basics**:
        - `getaddrinfo(host, port, hints, res_list)`: set type (in `hints`), get `sockaddr`
        - `int fd = socket(type)`
    - client
        - `connect(fd, sockaddr)`, `read()`, `write()`
    - UDP server
        - `bind()`
        - `recvfrom(&peer_addr, &addrlen)`
            - `getnameinfo(&peer_addr, host_bf, port_bf)`
        - `sendto(&peer_addr, addrlen)`
    - TCP server
        - `bind()`, `listen()`
        - `accept(fd, &peer_addr, &addrlen)`
            - `getnameinfo(&peer_addr, host_bf, port_bf)`
            - **`recvfrom()`, `sendto()`在connection-oriented协议下不处理`peer_addr`, 必须使用`accept()`获取**
        - `recv()`, `send()`


### 2021-5-13
1. the `glibc`'s `memcpy()`: set Copy-on-Write page with `__vm_copy()`
    - `COW`: implicit sharing, shadowing: defer copy until modification
    - paging
        - The Paging Game
    - MMU(memory management unit)
        - CPU <-> MMU <-> TLB


### 2021-5-14

1. latex: `lstlisting` env fail in `beamer`? see CTAN `beameruserguide` (offical doc)
    - **3.13 Verbatim Text, 12.9 Verbatim and Fragile Text**
        - > If you wish to use a `{verbatim}` environment in a frame, you have to add the option `[fragile]` to the `{frame}` environment. (or use `\defverbatim[colored]`)
        - > **You must also use the `[fragile]` option for frames that include any “fragile” text, which is any text that is not “interpreted the way text is usually interpreted by TEX.”**
    - **2.6 Compatibility with Oher Pckages and Classes**
        - > Note that you must treat `lstlisting` environments exactly the same way as you would treat `verbatim` environments.
2. latex: `beamer` usage: `<(action specification)>`
    - `\onslide<1, 3-4, 6->`, `\uncover`, `\only`
    - `\begin{uncoverenv}`, `\being{onlyenv}`


### 2021-5-16
1. kfifo
    - simple version: kernel 2.6.26.4
    - general version 1: kernel 2.6.33-rc2/rc3
    - general version 2: kernel 2.6.39.3
2. C99 standard
    - address constant


### 2021-5-18
1. `echo 0 | sudo tee /sys/devices/system/cpu/cpu0/online`: ENOENT
    - but what is `sysfs`? `man 5 sysfs`
        - kernel提供的修改内核态数据结构的接口
            - 文件可读写，不能删除也不能新增
            - 写入的内容必须严格符合内核对数据结构的定义，否则为`write error: invalid argument`
    - 所以一定是内核没有提供`cpu0/online`文件
        - `CONFIG_HOTPLUG_CPU=y` (by default)
        - `CONFIG_BOOTPARAM_HOTPLUG_CPU0` is not set! (by default)
            - 为什么不将CPU0设置为热插拔？(允许CPU0下线)
                - **Resume from hibernate or suspend always starts from CPU0. So hibernate and suspend are prevented if CPU0 is offline.**
                - **PIC interrupts always go to CPU0. CPU0 can not offline if any interrupt can not migrate out of CPU0.**
                - 可能还有其他的内核机制依赖于CPU0
    - 如果一定要配置CPU0热插拔？
        - 重新编译内核：`CONFIG_BOOTPARAM_HOTPLUG_CPU0=y`
        - 修改内核启动参数，增加`cpu0_hotplug`
            - 单次启动增加：安全起见
                - 强制进入grub界面: 反复按下`ESC`(UEFI)或`SHIFT`(BIOS)
                - press `e` when cusor is on a boot entry
                - `ctlr + x`  or  `F10` to boot
            - 永久增加
                - `vim /etc/default/grub`
                - 在`GRUB_CMDLINE_LINUX_DEFAULT`中增加参数
                - `update-grub` or `update-grub2`
2. latex
    - TeX book: boxes, treated as single character, tex won't break it
    - ctex docs: [Spaces  and Boxes](http://www.ctex.org/documents/latex/latex2e-html/ltx-143.html)
        - `\makebox[width][position]{text}`, `\framebox[width][position]{text}`
            - position
                - `l`: flushleft
                - `r`: flush right
                - `s`: interword space adjusted so `text` fills box exactly
                - default(omit this argument): center
        - `\mbox`: robust and simple `\makebox`


### 2021-5-19
1. linux
    - bash & zsh difference: parameter expansion
        - bash: `"$var"`
        - zsh: `$var` is already similar?
    - kali `manpages`, `manpages-dev`(5.10-1)缺少`man 3 list`
        - 从[The Linux *man-pages* project](https://www.kernel.org/doc/man-pages/)下载最新tar包安装
    - linux kernel `list`
        - `LIST_ENTRY()`: `container_of()`
            - 链表ENTRY才是外部结构，相当于绑定了数据和一个简单列表，`list` api只处理简单列表部分。
2. Ramsay感染doc文件
    - `LoadLibrary("msfte.dll")`的猜想
        - `kernel32.dll`以COW模式，装载到`BON.exe`进程空间
        - 操作系统执行`DllEntryPoint()`，该函数hook进程空间中的`kernel32.dll`，但是必须调用被hook的函数才能执行相关代码
        - `BON.exe`调用被hook的函数，doc文件被感染
3. **windows patching tech**
    - modify the behavior of an executable
        - source modification
            - re, patching
            - executable signing
        - runtime modification
            - implemented by OS APIs
                - API hooks
                    - local hooks: influence only specific apps
                    - global hooks: affect all processes
                - **DLL injector**
                    - get process handle, write `dllname` into its virtual memory
                        - run target process, or just **search it in process lists** for its id
                    - create a thread inside it to run `LoadLibrary(dllname)`
    - process system calls
        - `CreateProcess()`
            - `CREATE_SUSPENDED`, `ResumeThread()`
            - `CloseHandle()`
        - `VirtualAllocEx()`, `WriteProcessMemory()`, `VirtualFreeEx()`
        - `CreateRemoteThread()`
            - `GetProcAddress()`: get `LoadLibrary()` procedure address
                - `GetModuleHandleA()`
    - Hook Engine
        - [Microsoft Detour](https://www.microsoft.com/en-us/research/project/detours/)
        - [NtHookEngine ](https://ntcore.com/files/nthookengine.htm)(Recommended)


### 2021-5-20
1. 密码含特殊字符的7z文件解压
    - 文件内容如何重定向到`7z`, `ssh`？
        - `strace 7z`: 读入密码前直接打开`/dev/tty`
        - `strace 7z x -p$'\x12\x34\x56' file.7z`
            - strace: `$'\x12\xf2\x00\x56'` translated to '`\22\362'`
                - hex to **octal**: octal better?
                - `tr` only supports octal
            - ANSI C translation: `\x00` terminates a string
    - **`tcl`, `expect`**
        - Tool Command Language (pronounced "tickle"): automate interactive command line task
2. deepin安装腾讯会议`apt-get install com.tencent.meeting.deepin`
    - Errors were encountered while processing: `linux-image-5.4.70-amd64-desktop`


### 2020-5-21
1. zip包编码混乱问题
    - [Arch wiki: **garbled problem**](https://wiki.archlinux.org/title/Localization/Simplified_Chinese#Garbled_problem)
        - `man zip`, `/Unicode<cr>`: fuck the `zip` implementation
        - > Unicode.  **Though the zip standard requires storing paths in an archive using a specific character set, in practice zips have stored  paths  in  archives in whatever the local character set is.**  This creates problems when an archive is created or updated on a system using one character set and then extracted on another system using a different character set.
        - **非unicode环境下，避免使用`zip`进行压缩**
    - **保留zip原编码**解压: `LANG=C 7z x file.zip`
        - 默认`LANG=en_US.UTF-8`解压：non-UTF8的二进制内容被强制解释为UTF8，然后写入为UTF8编码
            - 编码彻底损坏，不可恢复
        - `LANG=C unzip file.zip`并不能保持原编码: fuck unzip
    - 确定zip原编码格式: `chardet`, `encguess`
        - 解压目录下`ls | chardet`
        - 不解压：`cat file.zip | grep -a 'filename_ascii_part' > out.bin`， vim删除多余内容再`chardet out.bin`
2. latex: RASIZE the BOX with `xeCJK` !
    - 右下角评分表
        - 右下：`\hfill`, `\vfill`, `\begin{flushright}`
        - 表格宽高：`\raisebox[distance][extend-above][extend-below]{text}`
        - 字体：`\textxx` -> `\xxfamily`, `\xxshape`, `\xxseries`
    - **修复CJK字体baseline**
        - Wrapping every character in a `raisebox`，**并且在切换字体时使用`xpatch`重置**
        ```latex
        \usepackage{xeCJK}
        \usepackage{xpatch}

        % Raise the baseline of CJK characters by 0.1em
        % This is done by wrapping every CJK character in a raisebox
        \makeatletter
        \let\original@CJKsymbol\CJKsymbol
        \let\original@CJKpunctsymbol\CJKpunctsymbol
        \edef\CJKmovesymbol#1{\raise.1em\hbox{\original@CJKsymbol{#1}}}
        \edef\CJKmovepunctsymbol#1{\raise.1em\hbox{\original@CJKpunctsymbol{#1}}}
        % Only shift non-puncts because puncts seems in their place
        \def\CJKraisebaseline{%
            \let\CJKsymbol\CJKmovesymbol
        }
        \def\CJKresetbaseline{%
            \let\CJKsymbol\original@CJKsymbol
        }
        % When switching to Heiti and FangSong, revert settings
        \xpretocmd\heiti{\CJKresetbaseline}{}{}
        \xpretocmd\fangsong{\CJKresetbaseline}{}{}
        \xpretocmd\texttt{\CJKresetbaseline}{}{}
        \makeatother

        % Activate!
        \CJKraisebaseline

        % fix possible fontsize problem
        \setmainfont[Scale=1.18]{Cambria}
        ```
3. linux: 把文件`file`的内容作为命令行参数
    - 作为直接参数：`echo PARAMETER`
        - `echo “$(cat file)”`
            - > Word Splitting
                > The  shell  scans the results of parameter expansion, command substitution, and arithmetic expansion **that did not occur within double quotes** for word splitting.
            - > Quote Removal
              > After  the  preceding  expansions, all unquoted occurrences of the characters `\`, `'`, and `"` **that did not result from one of the above expansions** are removed.
        - `cat file| xargs echo`
            -  guess it's `read(0, buf, count); execve(/bin/echo, buf.split('\n'));`
    - 更复杂的情况: `echo "{\"This\": \"is\", \"a\": [\"json\", \"PARAMETER\"]}"`
        - `echo "{\"This\": \"is\", \"a\": [\"json\", \"$(cat file)\"]}"`
4. json常见操作
    - 压缩：去除换行`\r`, `\n`，去除空白`\s`
    - **转义**：`"`替换为`\"`，`\`替换为`\\`，之后再用`"`括起来即等效于一个字符串？
        - json standard, `string` specification
            - 可以包含任何Unicode字符
            - `\`和`"`必须转义
            - `U+0000`到`U+001F`之间的控制字符必须转义
        - 更好的转义方式：gzip + base64


### 2021-5-22
1. bash urlencode: `printf "%x" "'c"`，语法太过细节，google不到，需要查手册
    - `man printf`内容太少，`info printf`
    - > If the leading character of a numeric argument is `"` or `'` then its value is the numeric value of the immediately following character.
2. 《活出生命的意义》书评
    - 存在主义、弗洛伊德、马洛斯、弗兰克尔
        - 意义疗法与精神分析：创伤者与观察者
    - 意义是否应该刻意追求？弗兰克尔的三种意义
        - 创造、体验、挑战(斗争)
    - 马洛斯的困境：意义的超越：狂信徒与抑郁症


### 2021-5-23
1. filesystem and file management system
    - process fd -> open file table -> inode table
    - `lsof`: list open files
    - `ll /proc/$$/fd`, `cat /proc/$$/fdinfo/1`
2. `tty` drivers ?


### 2021-5-27
1. C
    - `x86_64` LP64: long and point 64bit
        - 栈对齐大小8字节
    - `__builtin_offsetof()`：编译器防止C++运算符重载导致经典C定义`&( (type *) 0)->member`失效
    - `#define multiline_macro()`
        - 使用`{ }`包括宏内容：保证`if(cond) multiline_macro()`不出错，但是宏后面不能带上`;`
        - 使用`do { } while (0)`包括宏内容：允许`if(cond) multiline_macro();`用法
            - 或用`if(1) { } else`包括宏内容


### 2021-5-29
1. linux: `dpkg`
    - `.deb` files:  `ar` archive
        ```txt
        xxx.deb
        ├── debian-binary
        ├── control.tar.gz
        │   ├── control
        │   ├── md5sums
        │   ├── postinst
        │   └── postrm
        └── data.tar.gz
            ├── etc
            └── usr
        ```
    - `man dpkg-deb`
        - `-R, --raw-extract ARCHIVE DIR`
        - `-b, --build DIR ARCHIVE`, the `DEBIAN` sub-directory



### 2021-6

### 2021-6-1
1. python: everything is object
    - `import`时模块代码被执行
        - `def main()`, `if __name__ == 'main': main()`
    - 跨module变量：`config.py`
        - 修改必须在同一个进程内
    - [python namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
        - builtin, global, enclosing, local
            - `__builtins__` module
            - `globals()`, `locals()` dict: `name -> object`
            - `dir([object]) -> list of str`
        - `global`, `nonlocal` declaration


### 2021-6-2
1. linux
    - zsh & bash: `/etc/profile`, `/etc/zsh/zprofile`
    - `sudo -H pip install`
    - supervisorctl: `reread`只读，`update`才会更新
    - apt & dpkg
        - `apt download package=version`, version: `apt search package`
            - 下载完整依赖：apt
        - `apt --fix-missing|--fix-broken install`


### 2021-6-3
1. linux system administration
    - `/etc/sysctl.conf`, `/etc/sysctl.d/{10,30,60,90}-*.conf`
        - `sysctl -p, --load`
    - `pam_limits.so`
        - `/etc/security/limits.conf`, `limits.d/*.conf`
            - 需要重启session
        - `/etc/pam.d/{common-session,common-session-noninteractive}`
            - 需要reboot？
        - `cat /proc/$proc_num/limits`
            - **子进程会继承`limits`**
        - `setrlimits()`: 进程的limits可以被管理软件轻易修改！
            - `[supervisord]` section: `minfds=4096` (必须使用`systemd`重启，`reload`不改变pid)
2. shell: bash & tcl
    - `pushd DIR`, `popd`
    - `expect`: just a `tcl` extension
        - `#!/usr/bin/env -S expect -f`
        - `spawn`, `expect`, `send`, `interact`
            - how does `send` (or tty) work?
        - `{*}$list_var`: expand list variable
3. latex
    - `\fancyhead[RE,RO,LE,LO]{text}`: right/left, even/odd
    - `\documentclass[twoside]{article}`
4. zeek
    - zeekctl `logRotationInterval`
    - `@load` syntax v.s. normal `statement;`
    - `redef xxx=xxx;`

