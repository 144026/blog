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
com.miui.videoplayer
com.miui.player
com.mi.globalbrowser
com.xiaomi.midrop
com.miui.yellowpage
com.miui.gallery
com.miui.android.fashiongallery
com.miui.bugreport
com.miui.weather2
com.miui.hybrid
com.miui.global.packageinstaller
com.xiaomi.joyose

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
```

### `adb` commands

single line command for adb's `/bin/sh`:

```bash
for pkg in $pkgs; do echo $pkg; echo ------------; pm uninstall $pkg || pm uninstall -k $pkg; pm uninstall --user 0 $pkg || pm uninstall -k --user 0 $pkg; pm disable-user $pkg; pm disable-user --user 0 $pkg; echo; done
```

more readable:

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
