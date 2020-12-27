---
title: linux初步
date: 2020-10-15 18:37:51
tags:
- linux

categories:
- 知识
- 计算机
---

linux初步课程笔记（草稿）

<!--more-->

# linux初步

## 1 课程要求

### 1.1 教学目的
- 熟练使用linux
- 了解linux运作，理解内核与外围的关系
- 实验定制内核与外围文件系统，加深对开源操作系统的认识
- 输出，自启动最小系统Kernel+FS小于32M

### 1.2 实验安排
1. 完成外围FS定制
2. 内核定制
3. OS loader的安装应用

## 2 内容

### 2.1 Power on

| 					|DOS 				| Windows 		| Linux 	 |
|:-:				|:----:				|:----:			|:----:		 |
|BIOS 				| -- 				| -- 			| -- 		 |
|MBR/GPT			| -- 				| --			| --		 |
|OS Loader			| -- 				|NTLDR/BootMgr	|grub/grub2	 |
|OS kernel			|`IO.SYS` `MSDOS.SYS` 	|`ntoskrnl.exe`	|vimlinuz	 |
|Application Manager|`command.com`		|`explorer.exe`	|init/systemd|
|Applications		|...				|...			|...		 |


实验：
- 安装linux
	- 英文缺省字体
- ssh远程登录
- 查找文件位置

||ubuntu 1804.5 | CentOS 6.9|
|:-:|:-:|:-:|
| OS Loader| `/boot/grub`| `/boot/grub`|
|OS Loader 配置 |`/boot/grub/grub.cfg`, `/etc/default/grub`| `/boot/grub.conf`|
|内核|`/vmlinuz` -> `/boot/vmlinuz-x.x.x-xxx-amd64`| `/boot/vmlinuz-$(uname -r)`|
|应用管理器| `/sbin/init` -> `/lib/systemd/systemd`| `/sbin/init`|
		


小结
- Makefile，autoconfig，……
- virtual network editing: VMware, virt-manager

### 2.2 Acess file

#### 驱动从哪儿来？

```txt
+------------------+      
|  disk            |    
|      +-------+   |    driver  + - - -+      +-------+				
|      |files  |   |----x-x-x-->|driver|----->|kernel |
|      +-------+   |    files   +- - - +      +-------+
|      |driver |   |
|      |files  |   |
|      + - - - +   |
|                  |
+------------------+
```

#### `initrd.img`/`initramfs.img`

OS Loader载入的镜像文件，一个临时的RAM Disk根文件系统

`initrd.img`加载后，执行`init`：
- 加载必要的驱动
	- 磁盘控制器驱动
	- 文件系统驱动（ext3/ext4, ...）
- 查找OS Loader传给内核的参数`/proc/cmdline`，根据`root=xxxx`挂载真正的根文件系统（内核2.6以后）
	- `root=/sda1` 插口位置改变?
	- `root=LABEL=/` 两个/硬盘?
	- `root=UUID=xxxx-xxxx-...-xxxx`
- 切换根文件系统
- `exec /sbin/init`


`initrd.img`的打包方式
```bash
# low kernel version
dd if=/dev/zero of=filename bs=1M count=4
mkfs.ext2 filename
mount filename /mnt -o loop
# do anything to copy file into /mnt
umount /mnt
cat filename | gzip > initrd.img
```

```bash
# higher kernel version
mkdir tmpdir
# do anything to copy file into tmpdir
cd tmpdir
find . | cpio -H newc -o | gzip > /boot/initrd.img
```

#### /sbin/init
`ps -eaf`
`ps -axj`

实验返工
- 解包initramfs
- LVM -> raw disk


### 2.3 v0.5
定制FS的思路
- 在原有系统测试
- 复制原有系统的必备部件到新存储器
- 利用initrd.img在ram disk中测试

难题
- 应用程序及其依赖的动态库查询
	- `ldd`(`ld-linux-x86_64.so.2`/`ld.so --library-path=$PATH $instr`指定动态库目录)
	- `chroot`验证新环境是否完备: `chroot . /bin/bash`
- 应用程序及其依赖的配置文件
	- `man $app`的FILES章节
	- `strace`命令（输出到stderr）获得程序调用历史：`strace ls 2>&1 | grep open` (Advanced Programming in Unix Enviroment)


实验
- 利用initrd建立最简单FS，v0.5
- grub启动配置中增加入口，测试v0.5

### 2.4
- 构建便捷实验通路：小系统/标准系统
- 小系统访问标准系统的途径
	- 修改标准系统`initramfs.img`
	- 手工加载驱动`insmod`/`modprobe` v0.55
		- where: `/lib/modules/VERSION`
		- who: `lsmod`查看标准系统使用的驱动
		- how: `/lib/modules.dep`(run `depmod`) + `insmod`/`modprobe`
	- 自动加载驱动`udevd` v0.6
		- 内核接口`proc`、`/sys`（手动）
		- 规则和工具`/etc/udev`，`/lib/udev`
		- 维护`/dev`设备目录
		- 启动脚本`start_udev`
		- 其他手工加载也需要的文件

内核提供的接口：`/proc`，`/sys`内存目录
- `/proc/devices`，裸设备`/proc/bus/pci/devices`


### 2.4.5

1. 0.6 + cpdd mingetty, /init: mingetty; bash
	- 停顿后出现bash，提示inappropriate ioctl(io ctrl) for device; no job ctrl
	- 输入内容进入bash
2. bash：mingetty命令
	- 同上
3. man mingetty，man tty，mingetty --loginprog=/bin/bash /dev/tty1，
	cat initrd/etc/issue xxx /r /m
	- 直接效果同上
4. 加入init，同上
	- issue没有出现
	- 标准系统直接执行，效果同上

猜测原因：

![20201019045122](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019045122.png)

![20201019045343](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019045343.png)



先解决帐号验证login
1. 主系统bash多次login，bash和login进程数不叠加（`pstree`）
2. initrd bash(cpdd login之后): login，PAM failure
3. man login 
	- usrname check: root: /etc/securetty | others: /etc/{nologin,usertty}
	- password auth：/etc/passwd, /etc/shadow
	- auth方式：the PAM library
	- ![20201019070442](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019070442.png)

4. `man pam`; `vim /usr/share/doc/pam-$ver/*.txt`
	- see ch1 in The Linux-PAM System Administrators' Guide
	- ![20201019131235](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019131235.png)

5. `cp --parents -dr`的隐患
	- 手动拷贝pam.d, OK
	- cpdd.sh使用-d拷贝/lib64/security，-x判断是否递归时，symlink始终不满足条件，且缺少实际的库文件
		```bash
		# note that `which $unhidden_abusolute_path_file` output is same as input
		for file in `find /lib64/security/*`; do ./scripts/cpdd.sh $file ./myinitrd.0.7.0/ ; done
		```

6. 直接运行login或whoami
![20201019145128](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019145128.png)
	- root登录流程：type "root" -> find **uid** for "root" -> execute login as uid ? 
	- whoami流程：get uid -> 查找uid对应username？
	- 执行id，解析不出name ![20201019150201](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019150201.png)

7. **man nss; man nsswitch.conf** (注意需要安装man和man-pages)

![20201019153300](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019153300.png)

```bash
for file in `find /lib64/ | grep -E 'libnss.*so.+'`; do ./scripts/cpdd.sh $file ./myinitrd.0.7.0/ ; done
```

8. id和whoami正常工作，login仍然无法工作
	- **strace 跟踪问题**
	![20201019155828](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019155828.png)

	- 低级错误：没有为login创建文件夹`mkdir -p /var/run`
	- 递归脚本也没拷贝的依赖？`cpdd.sh /lib64/libfreeblpriv3.so myinitrd.0.7.0`
	- 基本成功（还可以继续用strace查错）
	![20201019161642](https://raw.githubusercontent.com/144026/rsrc/master/img/20201019161642.png)

9. **`ldd`的隐患**
	- `which ldd |xargs file` -> ldd是shell脚本
	- 实际是`objdump | grep NEEDED | cut xxxx`，即ldd无法列出非obj依赖？
问题：libfreeblpriv3.so到底是个啥？为什么依赖递归脚本会漏掉？

### 2.5
`sbin/init`之后

/etc/rc.sysinit
- probe mods
- fsck 正常关机标志位
- mount /proc /sys ,remout /
- 
/etc/rc
- start service

/sbin/mingetty
- mingetty/agetty + login


dlopen() & libnss




## 3 linux kernel
kernel+modules(内核级功能)

1. 下载5.9.1源码[tarball(xz)](https://kernel.org)，解压`tar -xJf ${file}.tar.xzi $ksrc`

2. 载入`/boot/config-$(uname -r)`作为内核配置：`make localmodconfig`, 出现输入提示后`^C`
	- `$ksrc` 下存在`.config`时，默认载入`.config`而不是`/boot/config`?

3. `make memuconfig`，genereal -> `kernel compress mode: XZ`（better than gz），save（应用缺省值）
	- 缺少依赖: `ncurses-devel`, `open-ssl`

4. `make -j8`, ksize: 4.9M
	- gcc版本过低
		```bash
		yum install -y centos-release-scl
		yum install -y devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils
		. /opt/rh/devtoolset-9/enable
		```
	- 缺少依赖: `bc`, `elfutils-libelf-devel`

5. general -> `[ ] include all symbols in kallsyms`, `make -j8`, ksize: 4.7M
	- gcc9 `make menuconfig`出错？换回gcc4.4执行
	- 取消多种initramfs的支持，ksize仍然4.7M

6. fs -> `[ ] network fs; [ ] ext2/4 security labels` ; sec opts -> `[ ] en diff sec mods; [ ] en sec fs; [ ] rm kmap in u mod`  ksize: 4.0M
