---
title: 软件工程 敏捷mini培训
date: 2020-10-10 17:57:37
tags:
- 软件工程
- 敏捷开发
- Scrum
categories:
- 知识
- 计算机
---

国庆4+1天软件工程培训(简要)笔记。

<!--more-->


# 软件工程

## 1 敏捷开发基础知识

### 1.1 发展和分类
CMM -> Agile -> DevOps

需求稳定->需求变化快->云业务/分布式  团队规模变小，分工细化

- CMM: 大量文档、返工、文档，保证开发质量可控。5个可控等级。

- Agile: 需求不断变化，不同功能逐次交付。

- eXtreme Programming: 偏重编程

技术实践->团队实践->过程实践

- Scrum：偏重项目管理

定义了一个项目管理框架、方式，包括需求搜集、团队协作、项目运作等

- 电信业：大规模产品实践

- 敏捷宣言

- 敏捷开发的原则


### 1.2 Scrum 3-3-4
团队：三个角色
- Product Owner：开发和维护product backlog，澄清需求优先级
- Scrum Master：辅导团队用正确的敏捷方法做事
- Team：产品研发主要实体

三个工作件
- 产品backlog
- 迭代backlog，
- 燃尽图burndown

管理：四个会议
- 迭代计划会议sprint planning meeting
- 每日站立会议 daily Scrum/standup meeting
- 迭代验收会议 sprint review meeting
- 迭代回顾会议 sprint respective meeting

### 1.3 迭代
计划-站会-站会...验收-回顾

迭代0额外计划
- 需求解析
- 工作量估计
排序，估算最简单的任务，计算点数，给出总时间估计。

### 1.4 User story
story描述了对于系统/软件的客户/用户有价值的一个功能点。

构成
- 简短描述，在开发过程中起提醒作用
- 针对描述的交流，澄清细节
- 记录/传递story细节的测试信息，用来确定开发是否完成


story的描述格式(3段式)
- 作为X
- 为了Y
- 我希望Z

story判断标准
- INVEST原则

Story不是万灵药
- 用户界面：大量截图
- 系统接口：文档

Story的依赖关系
- 接口、功能、测试依赖
- 依赖关系图
- 存在循环依赖则story划分不合理

Story的优先级：must/should/could/won‘t
- 对客户/用户的影响
- 依赖
- 内聚性-->相似的story
- 规模-->点数估计



### 1.5 敏捷开发演练
手工机器人制作：迭代0、迭代1、迭代2


## 2 测试基础

### 2.1 软件质量模型
Functionality | Reliability ...

### 2.2 测试分层
单元测试(UT)、集成测试(IT)、系统测试(ST)、验收测试

### 2.3 测试技术

- 静态/动态

- 黑盒/白盒


**黑盒测试**

- 等价类划分：有效/无效等价类
- 边界值分析
- 判定表
- 错误推测法

白盒测试
- 语句覆盖
- 判定-条件覆盖



## 2.4 持续集成与TDD (Test Driven Development)
test-->code-->refractor

**自动化测试**
- 预留测试指令，使用重定向，批量测试

# 大富翁项目

反思：
1. 数据结构的商讨

确定数据结构的格式后，要澄清每个字段的作用，确保对数据执行操作时，相应的字段正确更新。


# 附录
### `autosvn.sh`
自动将github仓库同步到svn的脚本。自己写着用的，正常使用需要满足条件：
- git clone不需要用户输入
- svn已经在本地checkout


```bash
#!/bin/bash

# rm repo, clone the newest
cd ~/Workspace/software-engineering
rm -rf hust-software-engineering
git clone git@github.com:npurson/hust-software-engineering.git
cd hust-software-engineering/

# check git log to check user
msg=$(git log| head -n 6| tail -n 5)

name="su0"
pass="p0"

if [ -n "$(echo "$msg" | grep "gu1")" ]
then
                name="su1"
                pass="p1"
fi

if [ -n "$(echo "$msg" | grep "gu2")" ]
then
                name="su2"
                pass="p2"
fi

# cp to svn dir and commit
rm -rf .git .gitignore
svn cleanup ../sw2020
cp -rp ./* ../sw2020/group2/
cd ../sw2020/group2
svn add --force ./
svn commit -m "${msg}" --username $name --password $pass
svn cleanup

echo "${msg}"
```

### `git2svn.sh`
更通用的git同步svn脚本

```bash
#!/bin/bash

########################################################################
# This shell script sync a git repo to a svn one
#
# Config the script in ./git2svn.conf
########################################################################

# check software install
NoSvn=0
NoGit=0

if [ -n "$(svn --version | grep "command not found")" ]
then
        echo -e "\e[31m[-]\e[0m svn not installed"
        NoSvn=1
fi

if [ -n "$(git --version | grep "command not found")" ]
then
        echo -e "\e[31m[-]\e[0m git not installed"
        NoGit=1
fi

if [[ $NoSvn == 1 || $NoGit == 1 ]]
then
        exit
fi
unset NoSvn
unset NoGit



# check arg number
# ConfFile=git2svn.conf
mode="none"
file="./.git2svn.conf"

if [ $# == 0 ]
then
        mode="prompt"
fi

if [[ $# == 1 && ($1 = "--help" || $1 = "-h") ]]
then
        mode="help"
        echo "usage: git2svn.sh [-h] [-f FILE]"
        echo ""
        echo "optional arguments:"
        echo "  -h, --help              print this message"
        echo "  -f, --file              specify a file to load as script config"
        echo ""
        echo ""
        echo "example"
        echo "-------"
        echo "run with prompt :"
        echo "  git2svn.sh"
        echo ""
        echo "specify a config file, none interactive :"
        echo "  git2svn.sh -f yourgit2svn.conf"
        echo ""
        echo "It is recommanded to directly run this script first, since a wrong config format might crash the script."
        echo ""
        echo "config file format"
        echo "-------------------"
        echo "<Git_Repo_Addr>"
        echo "<Git_Repo_Dir>"
        echo "<Svn_Repo_Addr>"
        echo "<Svn_Repo_Dir>"
        echo "<UserNumber>"
        echo "[User1_Git_Username]"
        echo "[User1_Svn_Username]"
        echo "[User1_Svn_Password]"
        echo "[User2_Git_Username]"
        echo "..."
        exit
fi

if [[ $# == 2 && ($1 = "--file" || $1 = "-f") ]]
then
        mode="file"
        file="$2"
fi

if [ $mode = "none" ]
then
        echo -e "\e[31m[-]\e[0m incorrect parameter"
        echo -e "\e[0m[*] use \"$0 -h\" for help"
        exit
fi



# ready to load config file
GitAddr="https://github.com"
DirInGit="./"
SvnAddr="https://subversion.apache.org"
DirInSvn="./"

UserNum=8
GitNameTab=()
# GitPassTab=()
SvnNameTab=()
SvnPassTab=()

# test file existence
if [ $mode = "file" ]
then
        echo -e "\e[0m[*] loading script configuration from ${file}"
fi

cat "$file" > /dev/null 2>&1
if [ $? != 0 ]
then
        if [ $mode = "file" ]
        then
                echo -e "\e[31m[-]\e[0m failed to open $file"
                exit
        fi
else
        # read file to vars
        i=0
        n=1
        # cat "$file" | while read line # NOTE: `while read` runs in sub shell, can't modify a parent shell vars
        while (( $i <= $UserNum ))
        do
                line=$(sed -ne "${n},${n}p" "${file}")

                if [ $i != 0 ]
                then
                        GitNameTab[$i]="$line"

                        let "++n"
                        line=$(sed -ne "${n},${n}p" "${file}")
                        SvnNameTab[$i]="$line"

                        let "++n"
                        line=$(sed -ne "${n},${n}p" "${file}")
                        SvnPassTab[$i]="$line"
                        let "++i"
                fi

                if [ $n == 1 ]
                then
                        GitAddr="$line"
                fi

                if [ $n == 2 ]
                then
                        DirInGit="$line"
                fi

                if [ $n == 3 ]
                then
                        SvnAddr="$line"
                fi

                if [ $n == 4 ]
                then
                        DirInSvn="$line"
                fi

                if [ $n == 5 ]
                then
                        UserNum=$(($line))
                        i=1
                fi

                let "++n"
        done
fi



# prompt (read settings from stdin)
if [ $mode = "prompt" ]
then
        echo "==================================="
        echo -e "\e[0m[*] prompt script configs"
        echo "==================================="

        # read git addr
        echo -ne "\e[34m[?]\e[0m Github repository address [$GitAddr] : "
        read strGitAddr
        if [ -n "$strGitAddr" ]
        then
                GitAddr="$(echo "$strGitAddr"| sed -e 's/\/$//g')"
        fi
        echo -e "\e[0m[*] set GitAddr ==> $GitAddr"
        echo ""


        echo -ne "\e[34m[?]\e[0m storage dir in git repository [$DirInGit] : "
        read strDirInGit
        if [ -n "$strDirInGit" ]
        then
                DirInGit=./"$(echo "$strDirInGit"| sed -E 's/^[\/\.]{0,2}//g')"
        fi
        echo -e "\e[0m[*] set DirInGit ==> $DirInGit"
        echo ""

        # read svn addr
        echo -ne "\e[34m[?]\e[0m Svn repository address [$SvnAddr] : "
        read strSvnAddr
        if [ -n "$strSvnAddr" ]
        then
                SvnAddr="$(echo "$strSvnAddr" | sed -e 's/\/$//g' )"
        fi
        echo -e "\e[0m[*] set SvnAddr ==> $SvnAddr"
        echo ""

        # read dir in svn
        echo -ne "\e[34m[?]\e[0m storage dir in svn repository [$DirInSvn] : "
        read strDirInSvn
        if [ -n "$strDirInSvn" ]
        then
                DirInSvn=./"$(echo "$strDirInSvn"| sed -E 's/^[\/\.]{0,2}//g')"
        fi
        echo -e "\e[0m[*] set DirInSvn ==> $DirInSvn"
        echo ""

        # read user number
        echo -ne "\e[34m[?]\e[0m git/svn user number [$UserNum] : "
        read strUserNum
        if [ $(($strUserNum)) != 0 ]
        then
                UserNum=$(($strUserNum))
        fi
        echo -e "\e[0m[*] set UserNum ==> $UserNum"

        # read each user's info
        i=1
        while (( i <= $UserNum ))
        do
                echo -e "\e[0m[*] User $i's config"

                # read git username
                echo -ne "  \e[34m[?]\e[0m Git user $i's username [${GitNameTab[$i]}] : "
                read strGitName
                if [ -n "$strGitName" ]
                then
                        GitNameTab[$i]="$strGitName"
                fi
                echo -e "  \e[0m[*] set Git user $i ==> ${GitNameTab[$i]}"

                # read svn username
                echo -ne "  \e[34m[?]\e[0m Svn user $i's username [${SvnNameTab[$i]}] : "
                read strSvnName
                if [ -n "$strSvnName" ]
                then
                        SvnNameTab[$i]="$strSvnName"
                fi
                echo -e "  \e[0m[*] set Svn user $i ==> ${SvnNameTab[$i]}"

                # read svn password
                echo -ne "  \e[34m[?]\e[0m Svn user $i's password [${SvnPassTab[$i]}] : "
                read strSvnPass
                if [ -n "$strSvnPass" ]
                then
                        SvnPassTab[$i]="$strSvnPass"
                fi
                echo -e "  \e[0m[*] set Svn password $i ==> ${SvnPassTab[$i]}"
                if [ $i != $UserNum ]
                then
                        echo ""
                fi

                let "++i"
        done

        echo -e "\e[32m[*]\e[0m $(( $i - 1 )) user(s) configured"
        echo -e "\e[32m[+]\e[0m script config saved to $file"
        echo ""

        # save info to file
        echo "$GitAddr" > "${file}"
        echo "$DirInGit" >> "$file"
        echo "$SvnAddr" >> "${file}"
        echo "$DirInSvn" >> "$file"
        echo "$UserNum" >> "${file}"

        i=1
        while (( $i <= $UserNum ))
        do
                echo "${GitNameTab[$i]}" >> "${file}"
                echo "${SvnNameTab[$i]}" >> "${file}"
                echo "${SvnPassTab[$i]}" >> "${file}"
                let "++i"
        done


        # prompt info statistic
        echo -e "\e[31m[!]\e[0m script ready to excute"
        echo ""
        echo -e "script configs"
        echo -e "=============="
        echo ""
        echo -e "Name\e[50D\e[16Cvalue"
        echo -e "-----\e[50D\e[16C------"
        echo -e "GitAddr\e[50D\e[16C${GitAddr}"
        echo -e "DirInGit\e[50D\e[16C${DirInGit}"
        echo -e "SvnAddr\e[50D\e[16C${SvnAddr}"
        echo -e "DirInSvn\e[50D\e[16C${DirInSvn}"
        echo ""

        i=0
        while (( $i <= $UserNum ))
        do
                if [ $i == 0  ]
                then
                        echo "----------------------------------------------------"
                        echo -e "Git Username\e[50D\e[24CSvn Username\e[50D\e[40CSvn Password"
                        echo "----------------------------------------------------"
                else
                        echo -e "${GitNameTab[$i]}\e[50D\e[24C${SvnNameTab[$i]}\e[50D\e[40C${SvnPassTab[$i]}"
                fi
                let "++i"
        done
        echo ""

        echo -ne "\e[34m[?]\e[0m execute script ? [y/n] : "
        read strexec
        while [[ $strexec != "n" && $strexec != "N" && $strexec != "y" && $strexec != "Y" ]]
        do
                echo -e "\e[31m[-]\e[0m input \"y\" or \"n\" to continue"
                echo -ne "\e[34m[?]\e[0m execute script ? [y/n] : "
                read strexec
        done
        if [[ $strexec = "n" || $strexec = "N" ]]
        then
                echo -e "\e[0m[*] script exit on user input"
                exit
        fi
fi


# check user-specified file contents
TabLen=${#GitNameTab[*]}
if [ $mode = "file" ]
then
        # check config format
        if [ $TabLen != $UserNum ]
        then
                echo -e "\e[31m[-]\e[0m user number error in $file"
                exit
        fi

        if [[ $TabLen == ${#SvnNameTab[*]} && $TabLen == ${#SvnPassTab[*]} ]]
        then
                echo -e "\e[32m[+]\e[0m configuration loaded from $file"
        else
                echo -e "\e[31m[-]\e[0m number of user names does not equal that of passwords"
                echo -e "\e[0m[-] wrong format in $file"
                exit
        fi
fi


# execute
GitDir="$(echo "$DirInGit" | sed -E "s/^[\.\/]{0,2}//g")"
SvnDir="$(echo "$DirInSvn" | sed -E "s/^[\.\/]{0,2}//g")"
name=""
pass=""

rm -rf ./.git2svn.cache/git-repo 2>/dev/null
mkdir -p ./.git2svn.cache/git-repo 2>/dev/null
echo -ne "\n\e[0m[*] git: "
git clone "$GitAddr" ./.git2svn.cache/git-repo
if [ $? != 0 ]
then
        echo -e "\e[31m[-]\e[0m git: :/"
        exit
else
        echo -e "\e[32m[+]\e[0m git: clone finished"
        echo ""
fi

cd "./.git2svn.cache/git-repo/"
msg="$(git log |head -n 6 |tail -n 5)"
rm -rf .git .gitignore 2>/dev/null

# determine name and pass for svn repo
for i in `seq 1 $TabLen`
do
        if [ -n "$(echo "$msg" | grep "${GitNameTab[$i]}")" ]
        then
                        name="${SvnNameTab[$i]}"
                        pass="${SvnPassTab[$i]}"
                        break
        fi
done

if [[ -z $name && -z $pass ]]
then
        echo -e "\e[31m[-]\e[0m can't determine svn user from git log"
        exit
else
        echo -e "\e[32m[*]\e[0m found '"${GitNameTab[$i]}"' in git log"
        echo -e "\e[32m[+]\e[0m set SvnUser ==> "$name"\n"
fi

rm -rf ../svn-repo 2>/dev/null
mkdir ../svn-repo 2>/dev/null
echo -e "\e[0m[*] svn: checking out '"$SvnAddr"' as '"$name"'"
svnmsg="$(svn checkout "$SvnAddr" ../svn-repo --username "$name" --password "$pass" | grep "Checked out")"
if [ $? == 0 ]
then
        echo -e "\e[32m[+]\e[0m svn: $svnmsg\n"
else
        echo -e "\e[31m[-]\e[0m svn: :/"
        exit
fi


cp -rp "./$GitDir" "../svn-repo/$SvnDir"
cd "../svn-repo/$SvnDir"
svn add --force ./
# echo -e "\e[0m[*] svn: "
svn commit -m "$msg" --username "$name" --password "$pass"
svn cleanup

# echo $name $pass
# echo "$msg"
# echo end
```
