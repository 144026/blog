---
title: 博客搭建笔记
date: 2020-08-26 11:39:28
categories:
- 技能
- 经验
tags:
- hexo
- 前端
---

在写了，在写了（新建文件夹）

<!--more-->


# 0 Build the Enviroment

## 0.1 Nodejs & npm.

`sudo apt install nodejs npm`


## 0.2 Hexo

### 0.2.1 Global Install

`sudo npm install hexo-cli -g`

### 0.2.1 Local Install

To be detailed.


## 0.3 Hexo Modules

1. the deploy. 
2. the mathjax.
3. music player.


# 1 Name Sevice

add subdomain record:`A blog.example.com <your_blog_ip>`, or `CNAME blog.example.com <username>.github.io`

also use `echo blog.example.com > $hexo_dir/source/CNAME && hexo d -g`

# 2 Image Hosting

## 2.1 PicGo

### 2.1.1 Install

Install from [Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo). For linux:

```bash
wget "https://github.com/Molunerfinn/PicGo/releases/download/v2.2.2/PicGo-2.2.2.AppImage"
# VERSION=2.2.2
chmod+x PicGo-${VERSION}.AppImage
./PicGo-${VERSION}.AppImage
```

possibly an error would occur:

```txt
The SUID sandbox helper binary was found, but is not configured correctly. 
Rather than run without sandboxing I'm aborting now. 
You need to make sure that /tmp/.mount_PicGo-${random_string}/chrome-sandbox is owned by root and has mode 4755.
```

solution:
- enable user namespace: `sudo sysctl kernel.unprivileged_userns_clone=1`
- or run without sandbox: `./PicGo-${VERSION}.AppImage --no-sandbox`

NOTE: "sandbox" provides a high level of security, except for 0-day exploits of linux kernel. Make your own choice.

to simplify things and finish install:

```bash
[ -d /usr/local/picgo ] || sudo mkdir -p /usr/local/picgo
sudo mv PicGo-${VERSION}.AppImage /usr/local/picgo/PicGo-${VERSION}.AppImage
sudo echo -e "sudo sysctl kernel.unprivileged_userns_clone=1 && /usr/local/picgo/PicGo-${VERSION}.AppImage" \
> /usr/local/bin/picgo && sudo chmod 755 /usr/local/bin/picgo
export PATH=/usr/local/bin:$PATH
```


### 2.1.2 Usage

**quick capture**

Use `ctrl+shift+P` (default keybindings) to upload clipboard image. (run `sudo apt-get install xclip` first)

To speed things up, install `picgo-plugin-quick-capture` (in the plugin config tab), and use `ctrl+shift+0` to launch screenshot script (`xfce4-screenshooter -r -c` with xfce4 desktop). 

**host config**

- github host

![](https://raw.githubusercontent.com/144026/rsrc/master/img/20201016144246.png)

- gitee host (need `gitee` plugin) (faster)

![20201016144508](https://raw.githubusercontent.com/144026/rsrc/master/img/20201016144508.png)

NOTE: GitHub upload is done with APIs at `api.github.com:443`, which is resolved to `13.250.168.23`(blocked) by default. This would cause "Error: connect ECONNREFUSED 13.250.168.23:443". To test available api addresses:

```python
import socket

def main():

    ips = [
            "13.230.158.120",
            "18.179.245.253",
            "52.69.239.207",
            "13.209.163.61",
            "54.180.75.25",
            "13.233.76.15",
            "13.234.168.60",
            "13.250.168.23",
            "13.250.94.254",
            "54.169.195.247",
            "13.236.14.80",
            "13.238.54.232",
            "52.63.231.178",
            "18.229.199.252",
            "54.207.47.76"
           ]


    for ip in ips:
        print(ip)
        x = socket.socket()
        try:
           x.connect((ip, 443))
        except:
           print("fail ",ip)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
```

and use `sudo echo -e "\n$ip_available	api.github.com" >> /etc/hosts` to fix.
