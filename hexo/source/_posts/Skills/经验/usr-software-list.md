---
title: my software list
date: 2020-12-1 17:00:00
categories:
- 技能
- 经验
tags:
- software
---


My temporary software list on debian.

<!--more-->


# 1 document

## input
1. fcitx4 + libpinyin (apt)
2. baidu(dpkg)

## 1.1 Text Sourced 
1. vim + vim-plug 
2. texlive `latex`, `xelatex`, etc. (perl install-pl. how to remove: official website)
3. textlive (apt list | grep texlive |xargs apt install -y)

## 1.2 office
1. zathura(apt install) (atril)
2. wps-office (`dpkg -i .deb`. remove: dpkg --purge \<name\>)

## notes
1. xmind(.deb + crack)
2. inkscape (apt)

# 2 Co-Op

## 2.1 version control
1. subversion `svn` (apt)
2. git

# blog
1. nodjs, npm (apt)
2. hexo(hexo-cli -g) (npm remove)
3. picgo (appimg)

# social
1. wine(wine32, wine64, wine, winetricks)

# aux
1. ?????-synaptics(apt) for xfce touchpad
	- `cp /usr/share/X11/xorg.conf.d` -r /etc/X11/`, add some config to /etc/X11/xorg.conf.d/70-synaptics.conf`
2. wenquanyi font (apt)
	- `sudo apt install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy`

3. time correction: ntpdate(manaully), ntpd(auto), `sudo ntpdate-debian`

# web
1. google chrome(dpkg)
2. vivaldi(dpkg)
2. shadowsocks-libev, simple-obfs(apt).
3. postfix(apt). used for crontab MTA error report.

# virtualize
## user space management tools (IMPORTANT)
1. virt-manager series(apt)
2. virtual box(apt) : with enhanced addons to easily passthrough filesystem

## management API
1. libvirt(apt), with daemon `libvirtd`. Installed by apt upon getting virt-manager (also with a bunch of drivers for different virtualize software).

## Virtualize Software
1. qemu qemu-system **qemu-utils** with kvm (apt-get)
2. Others uninstalled (Xen, VMware, VirtualBox, Hyper-V, ...)
