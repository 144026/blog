---
title: kali
date: 2020-9-28
categories:
- 技能
- 经验

tags:
- linux
- kali

mathjax: true
---

A blog learning both kali and general linux usage and skills.



<!--more-->



# 0 Install

1. Need network.
2. Missing  wireless firmware. Better have a cable network, allowing post-installation firmware download and install, with `apt list|grep firmware`. If not, prepare a 2nd disk containing those firmware, and insert it after the warning pop up.

## 0.1 Basic System Config

### 0.1.0 users and groups

#### 0.1.0.1 change username & groupname (manually)

There should be and actually are some packages and utilities to achieve this, though.
1. how about `useradd <newname> && userdel <oldname>`/`groupadd <newname> && group <oldname>` ?
	- the `newname` user/group will have a different `uid`/`gid`, and won't bear its predecessor position or privileges. e.g. `A` is in `sudo` group, `sudo useradd B && sudo su && userdel A && su B` won't add B into `sudo` group.
2. change usr/grp files:
	- change group name: substitute all `oldname` into `newname`, in both `/etc/group` and `/etc/gshadow`, note this IS dangerous and can cause system-wide errors. e.g. `sed -i 's/^oldGroupName/^newGroupName/g' /etc/{group,gshadow}`.
	- change user name: similarly, `sudo mv /home/OldUserName /home/NewUserName && sudo sed -i 's/oldUserName/newUserName/g' /etc/{passwd,shadow,group,gshadow} && sudo sed -i 's/^newUserName/^oldUserName/g' /etc/{group,gshadow}`. Note that password authentication will fail if `shadow` files not changed, and group privileges(like `sudo` group) won't be granted if `/etc/group` not changed.

**NOTE:** mistakenly deleting or changing `/etc/{group,passwd,gshadow,shadow}`: recover with the system-default auto-backup `/etc/{group,passwd,gshadow,shadow}-` AS SOON AS POSSIBLE!


### 0.1.0.2 trusted sudoers

```bash
sudo groupadd trusted-sudoers
sudo usermod -a -G trusted-sudoers <user>
# user/group privilege spec('%' means group)
# user specification is "who where = (as_whom) what", `man sudoers` to learn more
sudo echo "%trusted-sudoers ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers.d/trusted-grant-root
sudo chmod 0440 /etc/sudoers.d/trusted-grant-root
```

On kali there is a group named `kali-trusted` and file `/etc/sudoers.d/kali-grant-root`, so `usermod` is enough. Note that in `/etc/sudoers.d/README` :
> `#includedir /etc/sudoers.d`
>
> This will cause sudo to read and parse any files in the /etc/sudoers.d
> directory that do NOT **end** in '~' or **contain** a '.' character.

After changing `/etc/sudoers` or `/etc/sudoers.d/*`, ALWAYS run `sudo visudo -c` to check syntax (both file name and content).

### 0.1.1 DNS

Networkmanager(and some applications) will overwrite `/etc/resolv.conf`, set immutable file attribute to prevent this:

```bash
echo "nameserver 114.114.114.114" > /etc/resolv.conf
sudo chattr +i /etc/resolv.conf
```


### 0.1.2 shortcuts

I'm using xfce4 desktop, there's several sets of shortcuts to use:

##### 1 xfce seetings: hardware.keyboard

Some core shortcuts in the application Shortcuts tab. Adding Custom ones allowed.

|Purpose|Command|Shortcut|
|:-:|:-:|:-:|
|lock screen|xflock4|Ctrl+Alt+L|
|screenshot.clip|xfce4-screenshooter -r |Shift+PrtSc|
|screenshot.region.clip|xfce4-screenshooter -r -c|Shift+Ctrl+PrtSc|
|app finder/menu|xfce4-appfinder/xfce4-popup-whiskermenu|Super|
|browser|chrome|Alt+W|
|terminal emulator|qterminal(there's problems)|Alt+T|
|dropdown terminal|qterminal -d|Alt+Shift+D|


##### 2 xfce settings: personal.window_manager

Custom ones not allowed.

|Window Action|Shortcut|
|:-:|:-:|:-:|
|cylce fwd/bck|Alt/(Shift+Alt)+Tab|
|close |Shift+Ctrl+W|
|Maximize|Ctrl+Super+Up|
|tile to t/b/l/r|Super+k/j/h/l|

|Workspace Action|Shortcut|
|:-:|:-:|:-:|
|add/del|Alt+Insert/Delete|
|goto l/r|Alt+Ctrl+Left/Right|



##### 3 common terminal shortcuts

- `tab`(auto-complete)
- `ctrl+p/n`(history-nav), `^S/^R`(fwd/bck_i_search),
- `ctrl+a/e/b/f`(move)
- `^W/^H`(bck_dw/dl), `^D/^K`(fwd_dl/d\$)


##### 4 qterminal shortcuts and configs

QTerminal(0.14.1) stores configs in `~/.config/qterminal.org/qterminal.ini`, and its `-p,--profile` option can **NOT** designate a custom config file like `~/.myqterm.ini`(only custom options allowed)

Even **worse**, QTerminal flushes its config file with its on-exit configs, which means you can **NOT** make effective changes to `qterminal.ini` using qterminal. ：/

Still, with MATE terminal, `qterminal.ini` can be changed: (below is a backup) 

```ini
[General]
AskOnExit=false                 # default true
BookmarksFile=                  # not used
BookmarksVisible=false		
Borderless=true                 # default false
ChangeWindowIcon=true
ChangeWindowTitle=true
ConfirmMultilinePaste=false     # used to avoid accidental execution
FixedTabWidth=true
FixedTabWidthValue=250
HideTabBarWithOneTab=true       # cleaner look
HistoryLimited=true
HistoryLimitedTo=1000
KeyboardCursorShape=0           # block type cursor
LastWindowMaximized=false       # depend if next opening is maxed
MenuVisible=false               # CLOSE, avoid Alt shortcuts conflict
MotionAfterPaste=0
SavePosOnExit=true              # save on-exit pos/size
SaveSizeOnExit=true             # NOTE: qterminal still flush other on-exit configs
ScrollbarPosition=0             # none
ShowCloseTabButton=false
TabBarless=true                 # default false
TabsPosition=0
Term=xterm-256color
TerminalBackgroundImage=
TerminalMargin=10               # NOTE this would cause vim display margin. Vim itself shows margin when scaling, though.
TerminalTransparency=0
TerminalsPreset=2
TrimPastedTrailingNewlines=false
UseBookmarks=false              # no need
UseCWD=false                    # no need
colorScheme=Kali-Dark
emulation=linux
enabledBidiSupport=false
fontFamily=Fira Code            # quite good terminal font
fontSize=14                     # choose your best
guiStyle=
highlightCurrentTerminal=false
showTerminalSizeHint=true
version=0.14.1

[DropMode]
Height=45
KeepOpen=false                  # NOTE: use false, since qterm is always on top in this mode
ShortCut=
ShowOnStart=true
Width=70

[MainWindow]
ApplicationTransparency=5
isMaximized=false
pos=@Point(960 29)
size=@Size(950 1018)
state=@ByteArray(\0\0\0\xff\0\0\0\0\xfd\0\0\0\x1\0\0\0\0\0\0\0\0\0\0\0\0\xfc\x2\0\0\0\x1\xfb\0\0\0&\0\x42\0o\0o\0k\0m\0\x61\0r\0k\0s\0\x44\0o\0\x63\0k\0W\0i\0\x64\0g\0\x65\0t\0\0\0\0\0\xff\xff\xff\xff\0\0\0\x8c\0\xff\xff\xff\0\0\x3\xb6\0\0\x3\xfa\0\0\0\x4\0\0\0\x4\0\0\0\b\0\0\0\b\xfc\0\0\0\0)

[Sessions]
size=0

[Shortcuts]
Add%20Tab=Ctrl+Shift+T
Bottom%20Subterminal=Alt+J                  # move sub
Clear%20Active%20Terminal=Ctrl+Shift+X
Close%20Tab=                                # no need
Collapse%20Subterminal=Alt+X                # collapse sub
Copy%20Selection=Ctrl+Shift+C
Find=Ctrl+Shift+F
Fullscreen=F11
Hide%20Window%20Borders=Alt+Shift+H
Left%20Subterminal=Alt+H                    # move sub
Move%20Tab%20Left=Alt+Shift+Left
Move%20Tab%20Right=Alt+Shift+Right
New%20Window=Ctrl+Shift+N
Next%20Tab=Ctrl+PgDown
Next%20Tab%20in%20History=Ctrl+Shift+Tab
Paste%20Clipboard=Ctrl+Shift+V
Paste%20Selection=Shift+Ins
Preferences...=Alt+Shift+P                  # ctrl+shift+p is used by picgo
Previous%20Tab=Ctrl+PgUp
Previous%20Tab%20in%20History=Ctrl+Tab
Quit=
Rename%20Session=Alt+Shift+S
Right%20Subterminal=Alt+L                   # move sub
Show%20Tab%20Bar=
Split%20Terminal%20Horizontally=Alt+Shift+J # split sub
Split%20Terminal%20Vertically=Alt+Shift+L   # split sub
Toggle%20Bookmarks=Ctrl+Shift+B
Toggle%20Menu=Ctrl+Shift+M
Top%20Subterminal=Alt+K                     # move sub
Zoom%20in=Ctrl++
Zoom%20out=Ctrl+-
Zoom%20reset=Ctrl+0
```

core needs:

- clean look
- fast subterminal operations
- no conflict with existing shortcuts


##### 5 Yakuake & Tilda

Yakuake comes with lots of kde dependencies, while Tilda fits better into xfce4. Tilda config in `~/.config/tilda/config_$n`, `config_$n` for the n-th session simultaneously opened.

Add tilda to xfce settings::session and startup::application autostart, and change the default config: (below is a backup)

```ini
tilda_config_version="1.5.2"
command=""
font="Fira Code weight=453 11"
key="<Shift><Alt>d"
addtab_key="<Shift><Control>t"
fullscreen_key="F11"
toggle_transparency_key="F12"
toggle_searchbar_key="<Shift><Control>f"
closetab_key="<Shift><Control>w"
nexttab_key="<Control>Page_Down"
prevtab_key="<Control>Page_Up"
movetableft_key="<Shift><Control>Page_Up"
movetabright_key="<Shift><Control>Page_Down"
gototab_1_key="<Alt>1"
gototab_2_key="<Alt>2"
gototab_3_key="<Alt>3"
gototab_4_key="<Alt>4"
gototab_5_key="<Alt>5"
gototab_6_key="<Alt>6"
gototab_7_key="<Alt>7"
gototab_8_key="<Alt>8"
gototab_9_key="<Alt>9"
gototab_10_key="<Alt>0"
copy_key="<Shift><Control>c"
paste_key="<Shift><Control>v"
quit_key="<Shift><Control>q"
title="Tilda"
background_color="white"
# working_dir=""
web_browser="xdg-open"
increase_font_size_key="<Control>equal"
decrease_font_size_key="<Control>minus"
normalize_font_size_key="<Control>0"
show_on_monitor=""
word_chars="-A-Za-z0-9,./?%&#:_"
lines=5000
x_pos=0
y_pos=29
tab_pos=4
expand_tabs=false
show_single_tab=false
backspace_key=0
delete_key=1
d_set_title=3
command_exit=2
command_timeout_ms=3000
scheme=7
slide_sleep_usec=10000
animation_orientation=0
timer_resolution=200
auto_hide_time=2000
on_last_terminal_exit=0
prompt_on_exit=true
palette_scheme=8
non_focus_pull_up_behaviour=0
cursor_shape=0
title_max_length=25
palette = {10280, 10794, 13878, 65535, 23644, 22359, 23130, 63479, 36494, 62451, 63993, 40349, 22359, 51143, 65535, 65535, 27242, 49601, 39578, 60909, 65278, 61937, 61937, 61680, 26728, 26728, 26728, 65535, 23644, 22359, 23130, 63479, 36494, 62451, 63993, 40349, 22359, 51143, 65535, 65535, 27242, 49601, 39578, 60909, 65278, 61937, 61937, 61680}
scrollbar_pos=2
back_red=10486
back_green=10486
back_blue=13762
text_red=61603
text_green=61603
text_blue=60292
cursor_red=65535
cursor_green=65535
cursor_blue=65535
width_percentage=2147483647
height_percentage=2147483647
scroll_history_infinite=false
scroll_on_output=false
notebook_border=false
scrollbar=false
grab_focus=true
above=true
notaskbar=true
blinks=true
scroll_on_key=true
bell=false
run_command=false
pinned=false
animation=true
hidden=false
set_as_desktop=false
centered_horizontally=false
centered_vertically=false
enable_transparency=true
auto_hide_on_focus_lost=false
auto_hide_on_mouse_leave=false
title_behaviour=2
inherit_working_dir=true
command_login_shell=false
start_fullscreen=false
confirm_close_tab=true
back_alpha=62258
show_title_tooltip=true
# max_width=0
# max_height=0
# image=""
# show_on_monitor_number=0
# transparency=0
# bold=false
# title_max_length_flag=false
# antialias=false
# double_buffer=false
# scroll_background=false
# use_image=false
# min_width=0
# min_height=0
```

### 0.1.3 desktop-theme

`sudo update-alternatives --config desktop-theme && sudo update-grub2` will ONLY update "post-grub" images. To actually modify the theme:

- change desktop wallpaper in xfce4-settings.desktop

- change login background in xfce4-settings.lightdm-gtk+-greeter

- change grub background: override `/boot/grub/theme/kali/{backround,grub-4x3,grub-9x16}`


### 0.1.4 network config

When a userspace app, like`ssh`, needs to access a `ip`, it usaully passes the `ip` to kernel and let the kernel decide which `interface` and `route` will be used according to the _route table_. (This means `ssh [ -B <interface>] [ -b <ipaddr> ]` won't change route, thus can't solve 'unreachable' problem on a dual-interface machine)

use `route -n` or `ip route { list | show }` to display the route table.

use `ip route del $route` and `ip route add $route` to change existing routes.

**NOTE**: `ip route { change | replace }` is documented capable to change routes atomically, **BUT** `metrics` can NOT be changed in this way (get ENOENT, Error NO such ENTry), since the `rtnetlink` protocol uses `metrics` as separate fieleds to select routes and does not support this operation. When used, `ip route change $route` requires `$route` existing, and one or more fields (except `metrics`) may be specified differently to cause a change, the first matched record (match `metrics`?) will be changed.

**SYNOPSIS:** DO NOT use `ip route change`, use `del`&`add` instead.

### 0.1.5 sound config

#### 0.1.5.1 default sound card

List sound devices: `cat /proc/asound/cards`, or `aplay -l` with `alsa-utils` installed.

NOTE that (alsa or pulseaudio ?) always point `default` sound device to the one that has smallest card-device number.

Change by point `default` to some other `card.device`: `vim /etc/asound` or `vim ~/.asoundrc` (system-wide or user-specific)

Change by assign a different `card.device` to actual hardwares: change modprobe configs, **todo**.

# 1 Software Config

## 1.1 Debian Software General Management

### 1.1.1 apt tools


1. install

```bash
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install ${PackageName} && sudo apt clean
```
Use `sudo apt-get clean` to caches for install in `/var/cache/apt/archives/` and `/var/cache/apt/archives/partial/`.

Add `--fix-missing` parameter and execute install again if interrupted by network failures. If a broken package error stops the installation, use `sudo apt-get install $broken_package_name --fix-missing` to solve it.

Software will be installed into `/usr` dir (being left for apt tools' management recommended). 


2. uninstall

to remove a package but retain the config files (in `/etc`, `~`, `$PATH` or somewhere else), use
```bash
sudo apt-get remove ${PackageName}
```

to remove a package and the config files, use
``` shell
sudo apt-get remove --purge ${PackageName}
```

to remove the dependencies, use
```bash
sudo apt autoremove
```

to sum up, to completely remove a software, use
```bash
sudo apt-get remove --purge ${PackageName} && sudo apt auto remove
```



### 1.1.2 dpkg

1. install

```bash
sudo dpkg -i ${PackageName}.deb
```

Normally the package is installed in `/usr/local` (`--relocate` may be used to specify a different folder).

to list installed packages, use 
```bash
sudo dpkg -l
```


2. uninstall

to remove a package but retain the config files, use
```bash
sudo dpkg -r ${PackageName}
```

to remove a package and the config files, use
```bash
sudo dpkg --purge ${PackageName}
```



### 1.1.3 make install

Software installed in this way is hard to remove. Better setting a `PREFIX="/path/to/install` and deleting the whole `$PREFIX` folder to uninstall. 
```bash
# tar -tvf ${PackageName}.tar.gz
tar -xzf ${PackageName}.tar.gz
# tar -xJf ${PackageName}.tar.xz
cd ${PackageName}
less README
./configure --prefix /path/to/install 
make && make install
```


## 1.2 Documentation software

### 1.2.1 Input Method

#### im framework

- fcitx(4.0) (apt)
- fcitx5(5.0) (apt)

#### pinyin support

- fcitx-googlepinyin (apt)
- fcitx-libpinyin (apt) (recommended)
- fcitx-sunpinyin (apt)

#### config

- fcitx configure

- local config dir: `~/.config/fcitx` **(remove it if there's a config corruption)**

**Appearence**

fcitx configure, or `usr/share/fcitx/skin/${skin}/fcitx_${Pskin}.conf`
- input/menu fontszie
- add a skin
- ...

### 1.2.2 the Fonts

Copy fonts to a dir, and change font in Appearance.
```bash
sudo mkdir ${FontDir}; sudo cp ${FontName}.[ttf|TTF] /usr/share/fonts/${FontDir}
```

Manually install fonts for all apps.
```bash
su && cd /usr/share/fonts/${FontDir}
mkfontscale && mkfontdir && fc-cache -fv
source /etc/profile && fc-list |wc -l
```

or use apt tools, e.g. wenquanyi fonts (fira code fonts)
```bash
sudo apt install fonts-wqy-microhei ttf-wqy-zenhei xfonts-wqy
```



### 1.2.3 Office

wps office: Download linux version and use dpkg to install. Remember to copy and install fonts from  windows.

libreoffice:bad performance, ver 7.1



### 1.2.4 markdown and tex

**install**: texlive, download dvd-image from mirror sites and run `install-pl`(need to add to `$PATH`).

From here, editing a document is more similiar to coding, which is why vim comes in (see [learn-Vim](https://leoharry.com/2020/10/03/%E6%8A%80%E8%83%BD/%E5%B7%A5%E5%85%B7/learn-Vim/)). 

Generally, filetype-recongnition, syntax-highlight, autocompletion, tags, snippets, compile-preview, etc. will be needed.

### 1.2.5 hexo blog

(see [learn-blog](https://leoharry.com/2020/08/26/%E6%8A%80%E8%83%BD/%E7%BB%8F%E9%AA%8C/learn-blog/))

**install**: 
- apt: nodejs, npm, git
- npm: hexo-cli, and other plugins
- manual: picgo.appimg

**config**
- hexo: `_config.yaml`
- theme: `_config.yaml`


## 1.3 Aux Software 

### 1.3.1 Social

linuxqq: dpkg install.


### 1.3.2 xfce touchpad config

```bash
sudo apt-get install xserver-xorg-input-synaptics && cp -r /usr/share/X11/xorg.conf.d/ /etc/X11/ && sudo vim /etc/X11/xorg.conf.d/70-synaptics.conf
```

now add the following options to the first inputclass
```bash
# Option "TapButton1" "1" # left mouse
Option "TapButton2" "3" # middle mouse
Option "TapButton3" "2" # right mouse
Option "VertEdgeScroll" "off"
Option "VertTwoFingerScroll" "on"
Option "HorizEdgeScroll" "off"
Option "HorizTwoFingerScroll" "on"
Option "CornerCoasting" "on"
Option "CircularScrolling" "on"
Option "CircScrollTrigger" "2"
Option "EmulateTwoFingerMinZ" "40"
Option "EmulateTwoFingerMinW" "8"
Option "CoastingSpeed" "0"
Option "FingerLow" "30"
Option "FingerHigh" "70"
Option "MaxTapTime" "125"
Option "VertScrollDelta" "-111"
Option "HorizScrollDelta" "-111"
```



### 1.3.3 Web Browser

1. chrome: just download the official package.
2. firefox esr, kali original.


### 1.3.4 socks proxy client

```bash
sudo apt install shadowsocks-libev simple-obfs 
```

Server config template in  `/etc/shadowsocks-libev/`.

Client config with obfs-local (no space between `plugin_opts` recommended):
```bash
{
"server":"<ip>",
"server_port":<"port>",
"local_address":"<localhost>",
"local_port":"<port2>",
"password":"<pass>",
"timeout":"<sec>",
"method":"<encry>",
"fast_open":true,
"plugin":"obfs-local",
"plugin_opts":"obfs=http;obfs-host=www.baidu.com;fast-open=true"
}
```

**Auto-start with `systemd`**

Create the config file below, then `sudo systemctl enable ss-locald.service`
```ini
; /{lib,usr/lib}/systemd/system/ss-locald.service
[Unit]
Description=Shadowsocks client service
; Documentation=http://xxx
; After=xxx.target

[Service]
User=username
Group=groupname
ExecStart=/usr/bin/ss-local -c /etc/shadowsocks-libev/config.json
; ExecStop=xxx
; ExecReload=xxx
KillMode=process
Restart=on-failure
RestartSec=50s

[Install]
WantedBy=multi-user.target
```

Use proxy `socks5h://${ip}:${port}` to hide DNS. (`socks5://` DOES NOT proxy DNS traffic)

In firefox, set the SOCKS Host v5 proxy in preferences -> general -> network settings. ALWAYS check "Proxy DNS when using Socks v5".



## 1.4 Virtualize

### 1.4.0 Architecture
1. Bare-metal
Userspace Management tool $\rightarrow$ Management API $\rightarrow$ Hypervisor software $\rightarrow$ Hardware resource(CPU/Memory/NIC/Disk)

2. Host OS
Userspace Management tool $\rightarrow$ API $\rightarrow$ Hypervisor $\rightarrow$ Host OS $\rightarrow$ Hardware (CPU/Memory/NIC/Disk)

### 1.4.1 VMware .vmdk

### 1.4.2  VirtualBox .vdi

### 1.4.3 Qemu .qcow,.qcow2

Detailed qemu usage guide on [archlinux-wiki/qemu](https://wiki.archlinux.org/index.php/QEMU).

#### 1.4.3.0 install & check suppport
Install qemu and qemu-system
```bash
apt list|grep qemu && sudo apt-get install qemu [qemu-system qemu-utils]
```

Check host hardware support for KVM
```bash
grep -E 'vmx|svm' /proc/cpuinfo
```

Check if kvm module is loaded on host
```bash
lsmod | grep kvm
```

#### 1.4.3.1 Basic Usage

Create vitual disk by `qemu-img [-f FMT] <filename> [SIZE]`.
```bash
qemu-img -f qcow2 ubuntu-1804-server-x86_64.qcow2 4G
```

OS install from `.iso`:
```bash
qemu-system-x86_86 -enable-kvm \ #  use `-enable-kvm` to accelerate.
-m 512 \
-cdrom ./your-boot-img.iso \
./your-virtual-disk.qcow2 
```

> Tips on downloading iso images:
>> `thunder://{$link}==`: use `echo "$link" | base64 -d` to decode

>> `ed2k` links: amule


Start from `qcow2` disk image:
```bash
qemu-system-x86_64 -enable-kvm \
-m 1024 \
-hda test-img.qcow2
```

#### 1.4.3.2  Network Config

Config first a host-only virtual network, then change into NAT mode using iptables. See Network options in `man qemu-system-x86_64`.

**Host Config**

NOTE: DO check kernel support for tap/tun: `modprobe tun && lsmod|grep tun`. Kernel module recompile needed if unsupported.

Use `-netdev tap,id=<id>,ifname=<name>,script=<file>[,downscript=<dfile>]` to config a host TAP network backend (bring up an interface **virtually connected to the Guest NIC**). 

Or just use `-nic tap` to bring up the default tap0 interface, and manually config it using `ifconfig`.


**Guest Config**

Set guest interface(check with `ifconfig -a`) to fit in the Host TAP network. Host-only finished.

**NAT Config**
Set the guest gateway to host tap-interface ip. Now switch to host, use
```bash
iptables -F # this brings risks
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -s ${Host_Tap_Ip}/${Mask_Width} -j SNAT --to-source ${Host_eth0_ip}
```

#### 1.4.3.3 9P Filesystem Passthrough

Check guest/host kernel support:
```bash
modprobe -l | grep 9p
lsmod | grep 9p
grep 9P /boot/config-$(uname -r)
grep CONFIG_9P_FS /boot/config-$(uname -r)
```

setup guide on [linux-kvm.org/page/9p_virtio](http://www.linux-kvm.org/page/9p_virtio).


#### 1.4.5 GUI Management(Virt-Manager Series)
install the **virt-manager** tool series (virsh, virt-viewer, virt-install, ...)
```bash
sudo apt-get install virt-manager
```

Now with command `virt-manager`, geust OS devices can be easily configured, including the NAT virtual network manaully set up above.

Host support for tap/tun still needed, though. Run `modprobe tun && lsmod|grep tun` again if the network option in vir-manager turns grey.

#### Others
Xen,...



## 1.5 wine
```bash
sudo apt-get install winetricks
```

## 1.6 Process Management

### 1.6.1 supervisor

install: `sudo apt-get install supervisor && sudo systemctl enable supervisor.service`

config: 
1. systemd config: `locate supervisor.service`, `vim /lib/systemd/system/supervisor.service`
2. supervisor config: `vim /etc/supervisor/supervisord.conf`. Use `echo_supervisord_conf` to generate a template.

### 1.6.2 systemd

`man systemd`

`man systemd.unit`

```ini
[Unit]
Description=aaa
After=xxx.service

[Service]
User=user
Group=group
ExecStart=/absolute/path
ExecRestart=bbb
ExecStop=ccc
KillMode=process
Restart=on-failure
RestartSec=30s

[Install]
WantedBy=multi-user.target
```


## 1.7 Profiling

- cProfile/yappi -> `.pstats`file -> flameplot/flameplot.pl 


# 2 Shells

## 2.0 shell basic
what is a shell ?
- program parsing user input, and do corresponding things: run binary as usr:group, etc.

install a shell 
- apt tools

choose a shell
- current shell: `echo $SHELL`
- supported shell: `cat /etc/shells`
- run a shell: `$shell_name`
- change login shell: `chsh` or `chsh -s $shell_path`

config a shell
- `~/.${shell_name}rc`
- `man ${shell_name}`


## 2.1 Command line (CLI)

### 2.1.1 general commands
(need a big picture)

`sort`
- `-t` field seperator
- `-k` key to sort
- `-n` numerical sort

e.g. scan a subnet and sort output: `nmap x.x.x.0/24 |& grep 'scan report' | awk '{print $5}' | sort -t'.' -k4n`


`ssh`: note that its options must be specified in a certain 
- Port forwarding
	- Local forwarded to remote: `ssh -L local_addr:remote_addr`
	- Remote forwarded to local: `ssh -R remote_addr:local_addr`
	- global port access: `-g`, same as `0.0.0.0:<port>`
	- background and detach: `-f`, implies `-n`, so a command must be specified
		- `-n`: redirect stdin from `/dev/null`
		- `-N`: no commands, use for forwarding only, override `-f`'s compulsory command specifying.
	- e.g. `ssh -gfNL 3000:localhost:3000 <usr>@<host> [ -p <port> ]`(can be used with `systemd`)


`grep`: note different Regex standards support different syntaxes
- `-e` basic regex, `|`,`()`,`+`,`etc` not supported
- `-E` extended regex, note that the GNU `grep` BRE has all features of its ERE, except that metacharacters like `|` should be escaped to `\|`
- `-P` Perl regex, the only `grep` regex type that sopport **non-greedy** match like `grep -P '<start_pattern>.*?<end_pattern>'`

### 2.1.2 specs
pipe, redirection, etc...

#### 2.1.2.1 piplines

`<command> |` and `<command> |&`(short for `2>&1 |`) are performed after any redirections specified by `<command>`.

#### 2.1.2.2 EXPANSION

man-pages description:

> **EXPANSION**
>
> Expansion is performed on the command line after it has been  split  into  words. There are seven  kinds  of expansion performed: **brace expansion, tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, word splitting, and pathname expansion.**
> 
> The _order of expansions_ is: _**brace expansion; tilde expansion, parameter  and  variable  expansion,  arithmetic  expansion, and command substitution (done in a left-to-right fashion); word splitting; and pathname expansion.**_
> 
> On systems that can support it, there is an additional expansion available: process  substitution.  This is performed at the same time as tilde, parameter, variable, and arithmetic expansion and command substitution.
> 
> **After** these expansions are performed, quote characters present in the original  word are removed unless they have been quoted themselves (**quote removal**).
> 
> Only brace expansion, word splitting, and pathname expansion can increase the number of words of the expansion; other expansions expand a single word to a single word. The only exceptions to this are the expansions of `$@` and `${name[@]}`, and, in most cases, `$*` and `${name[*]}` as explained above (see **PARAMETERS**).

According to the expansion order:

```bash
└─$ echo $((1+2)) # arithmic expansion
3

└─$ cat file
$((1+2))

└─$ echo $(cat file) # command expansion (after arithmic)
$((1+2))
```

```bash
└─$ var=1

└─$ echo $var # variable expansion
1

└─$ cat file
$var

└─$ echo $(cat file) # command expansion (after variable)
$var
```


#### 2.1.2.3 Qouting

man-pages description:

> **Qouting** is used to remove the special meaning of certain characters or words to the shell. Qouting can be used to disable special treatment for special characters, to prevent reserved words from being recognized as such, and to prevent parameter expansion.

> Each of the **metacharacters** listed under **DEFINITIONS**, Manual page bash(1) has special meaning to the shell and must be quoted if it is to represent itself.

> When the command history expansion facilities are being used (see **HISTORY EXPANSION**), the **history expansion** character, usually `!`, must be quoted to prevent history expansion.

> There are three quoting machanisms: escaped character, single quotes, double quotes.

> ##### escape character

> A **non-quoted** backslash `\` is the escape character. It preserves the literal value of the next character that follows, with the exception of `<newline>`. (which is treated as line continuation)

> ##### single quotes

> Enclosing characters in single quotes `'` preserves the literal value of each character (even it's `\`)within the quotes. **A single quote may not occur between single quotes, even when proceeded by a backslash**.

> ##### double quotes

> Enclosing characters in double quotes preserves the literal value of all characters with the quotes, with the exception of `$`, \`, `\`, and, when history expansion is enabled, `!`. When the shell is in **posix mode**, the `!` has no special meaning within double quotes, even when history expansion is enabled. The characters `$` and \` retain their special meaning within double quotes. The backslash retains its special meaning only when followed by one of the following characters: `$`, \`, `"`, `\` or`<newline>`. A double quote may be quoted within double quotes by preceding it with a backslash. If enabled, history expansion will be performed unless an `!` apppearing in double quotes  is escaped using a backslash. The backslash preceding the ! is not removed.
>
> The special parameters `*` and `@` have special meaning when in double quotes.
> 
> ##### $'**string**'
>
> Words of the form `$'string'` are treated specially. The word expands to `string`, with backslash-escaped characters replaced as specified by the ANSI C standard. Backslash escape sequences, if present, are decoded.
> 
> The expanded result is single-quoted, as if the dollar sign had not been present.
> 
> A double-quoted string preceded by a dollar sign (`$"string"`) will cause the string to be translated according to the current locale. If the current locale is C or POSIX, the dollar sign is ignored. If the string is translated and replaced, the replacement is double-quoted.

To sum up, without using histoty expansion, there's four mechanisms:

1. `\`
	1. plain: preserve the next char
	2. in s-quotes: just literal `\`
	3. in d-quotes: 
		- preserve next: `$`, \`,`"` , `\`
		- line-continuation: `<newline>`
	4. in `$'string'`: by ANSI C std
2. single quotes `'`
	1. pairs: anything inside it, except itself
3. double quotes `"`
	1. pairs: `\` can still escape `$`, \`, `"` and `\`. (`'` doesn't need to be quoted within double quotes)
4. `$'string'`
	1. used to expand characters like `\n` in bash strings. e.g. `'f\ile.txt'$'\n'`. `'\n'` will only be expanded to literal string `\` and `n`.



##### the `ls` problem

Use `mkdir test && touch 'f\ile.txt'` to create a file containing `\`, now its _interesting_:

```bash
└─$ ls
'f\ile.txt'

└─$ ls | cat 
f\ile.txt

└─$ strace ls
...
write(1, "'f\\ile.txt'   log\n", 18'f\ile.txt'   log
)    = 18

└─$ strace ls 1>/dev/null
...
write(1, "f\\ile.txt\nlog\n", 14)       = 14
```

Seems `ls` alters its output depending if the dst is a tty/console or not.


## 2.2 Shell Script
pros:
- batch commands
- string processing

cons
- arithmetic

### 2.2.1 variable
strings ?

### 2.2.2 operaters
()
(())
[]
[[]]
{}
'
"
\$
\<
\>
...

### 2.2.3 keywords
if, case, for, while, repeat


