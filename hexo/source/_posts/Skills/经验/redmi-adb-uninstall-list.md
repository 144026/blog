---
title: Redmi ADB Uninstall List
date: 2021-3-23 17:00:00
categories:
- 技能
- 经验
tags:
- android
---


Package list for uninstall/disable on Redmi5 K30 Pro. 

<!--more-->

### Packages List

#### Safe to delete

```txt
com.miui.analytics
com.xiaomi.mipicks
com.miui.msa.global
com.miui.cloudservice
com.miui.cloudbackup
com.miui.backup
com.xiaomi.glgm
com.xiaomi.payment
com.tencent.soter.soterserver
cn.wps.xiaomi.abroad.lite
com.miui.video
com.miui.player
com.mi.globalbrowser
com.xiaomi.midrop
com.miui.yellowpage
com.miui.gallery
com.miui.android.fashiongallery
com.miui.bugreport
com.miui.weather2
com.miui.voiceassist
com.miui.huanji
com.miui.hybrid
com.miui.global.packageinstaller
com.xiaomi.joyose

com.google.android.ncadapters.contacts
com.google.android.gms.location.history
com.google.android.videos
com.google.android.music
com.google.android.apps.photos
com.google.android.youtube
com.google.android.apps.tachyon
com.google.ar.lens
com.google.android.googlequicksearchbox
com.google.android.apps.wellbeing
com.google.android.apps.googleassistant

com.android.browser
com.android.wallpaper.livepicker
com.android.dreams.basic
com.android.dreams.phototable
com.android.providers.downloads.ui

com.netflix.partner.activation
com.zhiliaoapp.musically
ru.yandex.searchplugin
com.yandex.zen
com.ebay.mobile
ru.ozon.app.android
com.alibaba.aliexpresshd
sg.bigo.live
ru.auto.ara

com.xunmeng.pinduoduo
com.duokan.phone.remotecontroller
com.xiaomi.jr
com.sina.weibo
cn.wps.moffice_eng
com.baidu.searchbox
com.ss.android.article.news
com.ss.android.ugc.aweme
com.qiyi.video
com.tencent.qqlive
com.dragon.read
com.UCMobile
com.xiaomi.shop
com.achievo.vipshop
com.zhihu.android
com.xiaomi.youpin
com.xiaomi.vipaccount
com.xiaomi.smarthome
com.mi.health
com.miui.virtualsim
com.tencent.mtt

com.android.stk
com.android.stk2

com.miui.miservice
com.miui.notes
com.mipay.wallet
com.xiaomi.gamecenter
com.android.calendar
com.miui.personalassistant
com.miui.thirdappassistant
com.miui.newhome
com.xiaomi.xmsf
com.miui.compass
com.miui.userguide
com.miui.smarttravel
com.miui.newmidrive
com.miui.tsmclient
com.xiaomi.drivemode
com.duokan.reader
com.mfashiongallery.emag
com.xiaomi.market
com.mi.liveassistant
com.xiaomi.mibrain.speech
com.baidu.input_mi
com.iflytek.inputmethod.miui
com.android.thememanager
```

#### Untested (by me), probably unsafe

```txt
com.xiaomi.account
```


#### Do NOT delete

```txt
# stuck into boot loop, can't be fixed even if you install them back
# good luck with a hard reset
com.miui.securitycore
com.miui.securitycenter
com.miui.securityadd
com.xiaomi.finddevice

# lose your phone icon forever, even you have com.google.android.contacts, etc.
com.android.contacts
```


### `adb` Commands

#### Single line version

Easy for copy-paste in a `adb`'s `/bin/sh`

```bash
for pkg in $pkgs; do echo $pkg; echo ------------; pm uninstall $pkg || pm uninstall -k $pkg; pm uninstall --user 0 $pkg || pm uninstall -k --user 0 $pkg; pm disable-user $pkg; pm disable-user --user 0 $pkg; echo; done
```

#### More readable

```bash
for pkg in $pkgs; do 
	echo $pkg
	echo ------------
	pm uninstall $pkg || pm uninstall -k $pkg
	pm uninstall --user 0 $pkg || pm uninstall -k --user 0 $pkg
	pm disable-user $pkg ; pm disable-user --user 0 $pkg
	echo
done
```
