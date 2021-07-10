---
title: my software list
date: 2020-12-1 17:00:00
categories:
- 技能
- 经验
tags:
- software
---


My temporary software list.

<!--more-->

# Linux (kali-rolling)

## 1 Document

### 1.1 Input
1. fcitx4 + libpinyin (apt)
2. baidu(dpkg)

### 1.2 Text Based
1. general: vim + vim-plug
2. markdown: typora(dpkg)
3. tex: textlive (apt list | grep texlive |xargs apt install -y)

### 1.3 Office
1. pdf
	- zathura(apt install) (atril)
	- ms edge
2. word/excel/ppt
	- wps-office (`dpkg -i .deb`. remove: dpkg --purge \<name\>)
	- libreoffice

### 1.4 notes
1. xmind(.deb + crack)
2. inkscape (apt)

## 2 Co-Op

### 2.1 version control
1. subversion `svn` (apt)
2. git
3. sublime merge(dpkg)

## blog
1. nodjs, npm (apt)
2. hexo(hexo-cli -g) (npm remove)
3. picgo (appimg)

## social
1. deepin raw disk (`dd offset=`, `cp -a`, `chroot`)
	- qq, wechat
	- txmeet

## aux
1. ?????-synaptics(apt) for xfce touchpad
	- `cp /usr/share/X11/xorg.conf.d` -r /etc/X11/`, add some config to /etc/X11/xorg.conf.d/70-synaptics.conf`
2. wenquanyi font (apt)
	- `sudo apt install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy`

3. time correction: `ntpdate -buv`(manaully), ntpd(auto), `sudo ntpdate-debian`

4. baidu netdisk(dpkg)

5. filezilla(dpkg)

## web
1. google chrome(dpkg)
2. vivaldi(dpkg)
2. shadowsocks-libev, simple-obfs(apt).
3. postfix(apt). used for crontab MTA error report.

## virtualize
### user space management tools (IMPORTANT)
1. virt-manager series(apt)
2. virtual box(apt) : with enhanced addons to easily passthrough filesystem

### management API
1. libvirt(apt), with daemon `libvirtd`. Installed by apt upon getting virt-manager (also with a bunch of drivers for different virtualize software).

### Virtualize Software
1. qemu qemu-system **qemu-utils** with kvm (apt-get)
2. Others uninstalled (Xen, VMware, VirtualBox, Hyper-V, ...)


# Windows 10 Pro (21H1, US)

## 1 Document

### 1.1 Input
1. Microsoft Pinyin

### 1.2 Text Based
1. general: vscode (vim plugin)
> vim + vim-plug
2. markdown: typora
3. tex: texlive `latex`, `xelatex`, etc. (perl install-pl. how to remove: official website)

### 1.3 Office
1. pdf: adobe acrobat pro dc
2. word/excel/ppt: office 2019

### 1.4 Notes
1. > Xmind Zen(crack)
	> OneNote
2. Visio 2019

## 2 Co-Op

### 2.1 version control
1. subversion `svn` (apt)
2. git
3. sublime merge(dpkg)

### Management
1. project 2019

## blog
1. nodjs, npm (apt)
2. hexo(hexo-cli -g) (npm remove)
3. picgo (appimg)

## social
1. TIM, wechat
2. txmeet

## aux
1. baidu netdisk
2. filezilla

## web
1. google chrome(dpkg)
2. vivaldi(dpkg)
2. shadowsocks-libev, simple-obfs(apt).
3. postfix(apt). used for crontab MTA error report.

## virtualize
### user space management tools (IMPORTANT)
1. virt-manager series(apt)
2. virtual box(apt) : with enhanced addons to easily passthrough filesystem

### management API
1. libvirt(apt), with daemon `libvirtd`. Installed by apt upon getting virt-manager (also with a bunch of drivers for different virtualize software).

### Virtualize Software
1. qemu qemu-system **qemu-utils** with kvm (apt-get)
2. Others uninstalled (Xen, VMware, VirtualBox, Hyper-V, ...)
