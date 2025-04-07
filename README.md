# COM3D2 插件中文翻译

[![Github All Releases](https://img.shields.io/github/downloads/90135/COM3D2_Plugin_Translate_Chinese/total.svg)]()

本项目是游戏 [COM3D2](https://com3d2.jp/)（カスタムオーダーメイド3D 2 / CUSTOM ORDER MAID 3D2）的插件的中文翻译（插件汉化）。 

This project is the Chinese translation of the COM3D2 plugin (plugin localization).

目前本项目目前使用 [IMGUITranslationLoader](https://github.com/ghorsington/IMGUITranslationLoader) 所以只能翻译使用 IMGUI 的插件，以后可能会扩展。

IMGUI 就是插件的半透明黑色窗口，示例请查看下面的截图。

```
手动翻译，但本人非专业，看不懂的就结合机翻了（那时还没有 AI）。
要看到的字才能 dump 下来翻译，所以可能并不是完全翻译。

2025 更新：
以前有很多上千行的技能、场景名无力翻译，如今有了 AI，这部分将由 AI 处理 + 人工大致校对
```

有没翻译或者错翻译或是想添加的插件等，欢迎反馈或直接贡献翻译，使用 Issues 或 Discussions 或其他任何方式，贡献翻译请使用 Pull requests 如果不会用直接 Issues 附上文件提交也行。

由于翻译方式的局限性，会有一些字无法汉化，或者是漏掉的。

本汉化最初发布于 ZODGAME

<br>
<br>

## 插件汉化列表


<details>
  <summary>插件汉化列表</summary>

 - com3d2.addyotogisliderse.plugin
 - com3d2.addyotogisliderse2.plugin
 - com3d2.alwayscolorchangeex.plugin
 - com3d2.atcc.plugin
 - com3d2.autoeraseoutline.plugin
 - com3d2.backgroundscreen.plugin
 - com3d2.changedressing.plugin
 - com3d2.changeskirtmotion.plugin
 - com3d2.dancecameramotion.plugin
 - com3d2.dancestudio.plugin
 - com3d2.dressdamage.plugin
 - com3d2.dresspainter.plugin
 - com3d2.dynamicboneedit.plugin
 - com3d2.dynboneedit.plugin
 - com3d2.editsceneundo.plugin
 - com3d2.facecontrol.plugin
 - com3d2.futa.plugin
 - com3d2.halfundressing.plugin
 - com3d2.inoutanimation.plugin
 - com3d2.lookatonemaiddance.plugin
 - com3d2.mancall
 - com3d2.mtaccutil.plugin
 - com3d2.motiontimelineeditor.plugin
 - com3d2.multiplemaids.plugin
 - com3d2.nprshader.plugin
 - com3d2.partsedit.plugin
 - com3d2.partseditwithstudio.plugin
 - com3d2.passthru.plugin
 - com3d2.poseselect
 - com3d2.propmyitem.plugin
 - com3d2.scenecapture.plugin
 - com3d2.shaderchange.plugin
 - com3d2.shapeanimator.plugin
 - com3d2.shapeanimator_allsceneedition.plugin
 - ~~com3d2.shapekeymaster.plugin~~ （翻译已提交至官方，可以在配置文件中启用，或使用 [ConfigurationManager](https://github.com/BepInEx/BepInEx.ConfigurationManager) 默认快捷键 F1 修改设置）
 - com3d2.skaccutil.plugin
 - com3d2.slimeshader.plugin
 - com3d2.smoothanimutil.plugin
 - com3d2.variousmaidviewer.plugin
 - com3d2.vibedancemaid.plugin
 - com3d2.vibeyourmaid.plugin
 - com3d2.vym_api_testsample.plugin
 - com3d2.xtmasterslave.plugin
 - com3d2.yotogiutil.plugin
 - configurationmanager
 - meidophotostudio.plugin
</details>


<br>
<br>


## 使用方法
登陆后点击仓库右上角的 Watch 按钮可以在更新时获得邮件提醒。

如果你真的不知道，Github 下载一般在仓库主页右边的 Releases 标签中，点进去 Releases 后，在 Assets 标签中有下载；如果要下载整个仓库，点击仓库主页绿色的 Code 按钮，然后点击 Download ZIP。

0. 确保你已安装 BpeinEX 插件框架，如果你还没有请使用 [https://github.com/krypto5863/COM-Modular-Installer](https://github.com/krypto5863/COM-Modular-Installer) 来安装框架和基础插件。但是安装这个以后需要删掉自带的英文翻译。

1. 安装 IMGUITranslationLoader
    [https://github.com/ghorsington/IMGUITranslationLoader](https://github.com/ghorsington/IMGUITranslationLoader)
    
    下载 `IMGUITranslationLoader_xxxxx.7z`
    
    复制 `IMGUITranslationLoader.Managed.dll` 和 `IMGUITranslationLoader.Sybaris.Patcher.dll` 到 `COM3D2\Sybaris` 文件夹。
    
     <img src="https://github.com/user-attachments/assets/5f91581c-30e8-4a6e-9fb7-7112fe33a9cf" width="50%" />

3. 下载本仓库 Releases 中的压缩包，或是下载源代码。

    找到对应路径
    
    把 `翻译.txt` 放到 `COM3D2\IMGUITranslationLoader\IMGUIStrings` 文件夹中，如图所示
    
     <img src="https://github.com/user-attachments/assets/a0f0a057-47ed-42d1-ac3e-90668b48cb01" width="50%" />
    
4. 记得在 `COM3D2\IMGUITranslationLoader` 中的 `IMGUITranslationLoader.ini` 里设置 `Load=True` 启用（应该是会自动启用的）
    
    没有就先启动一次游戏

<br>

`IMGUITranslationLoader.ini` 里还可以设置全局模式 `GlobalMode=True`

启用后就会无视插件限制，无论什么插件，只要有相同字符串就能翻译，但也可能造成问题。

<br>
<br>

## 常见问题

### CM3D2 能用吗？
能，如果插件名不一样的，更改翻译文件名就行了。比如 `com3d2.vibeyourmaid.plugin.txt` 改成 `cm3d2.vibeyourmaid.plugin.txt`

遇到一样的插件和一样的字符就会翻译。

或者开全局模式。

### COM3D2.5 3.40.0- (unity 5.6) 能用吗？
能，同样的，遇到不一样名字的插件 如 `com3d2_5.xxxxx.plugin` 把对应的翻译文件改一下名即可。

遇到一样的插件和一样的字符就会翻译。

或者开全局模式。

### COM3D2.5 3.40.0+ (unity 2022) 能用吗？
能，但 IMGUITranslationLoader 需要使用此版本 [https://github.com/krypto5863/IMGUITranslationLoader](https://github.com/krypto5863/IMGUITranslationLoader)

其他同 2.5 说明

### 如何与 XUnity.AutoTranslator 插件共存？
注意不要用 `turtle_formatter.exe` 处理，否则会被删掉。

在 `COM3D2\BepinEx\config\AutoTranslatorConfig.ini` 里面设置 `EnableIMGUI=false` 就好

<br>
<br>

## 去哪里找插件

### CM3D2
1. [https://github.com/krypto5863/Legacy-Meido-s-Modular-Toolbox](https://github.com/krypto5863/Legacy-Meido-s-Modular-Toolbox)
2. [https://motimoti3d.jp/blog-entry-37.html](https://motimoti3d.jp/blog-entry-37.html)
3. [https://github.com/search?q=CM3D2&type=repositories](https://github.com/search?q=CM3D2&type=repositories)
4. [https://www.google.com](https://www.google.com)
是的，CM3D2也可以用 BepinEX，但有一些兼容问题所以不推荐。

### COM3D2
1. [https://github.com/krypto5863/COM-Modular-Installer](https://github.com/krypto5863/COM-Modular-Installer)
2. [https://motimoti3d.jp/blog-entry-590.html](https://motimoti3d.jp/blog-entry-590.html)
3. [https://github.com/search?q=COM3D2&type=repositories](https://github.com/search?q=CMO3D2&type=repositories)
4. [https://www.google.com](https://www.google.com)
COM3D2 你应该无条件使用 BepinEX。

<br>
<br>

## 我也想参与汉化

本项目目前使用 IMGUITranslationLoader 来进行翻译，因此请先阅读插件说明：

[https://github.com/ghorsington/IMGUITranslationLoader/wiki](https://github.com/ghorsington/IMGUITranslationLoader/wiki)

[https://github.com/ghorsington/IMGUITranslationLoader/blob/master/README.md](https://github.com/ghorsington/IMGUITranslationLoader/blob/master/README.md)

简单来说就是在插件设置 `IMGUITranslationLoader.ini` 内设置 `Dump=True`，然后启动游戏 打开想要翻译的插件，把没翻译的地方全部点一遍

然后在 `COM3D2\IMGUITranslationLoader\IMGUITranslationDumps` 内就会有对应的 `插件名.txt` 文件（游戏运行中无法打开 dump 内的文件是正常的）。

把翻译后的文件放置到 `COM3D2\IMGUITranslationLoader\IMGUIStrings` 即可加载

注：翻译过的文本一般情况下是不会再次被 dump 的，因此翻译后可以删除 dump，再次进游戏检查是否有遗漏，有遗漏的部分就会被 dump 下来。

翻译格式为
```
原文			译文
```
中间的是 tab 键（\t 制表符）不是空格，可以有多个制表符，但至少有一个制表符。

<br>

支持正则表达式，详见原插件说明

例如 dump 下来的文件内有很多变量
```
前髪：某某
前髪：xxxx
広さ: 1.256165
広さ: 257
VRカメラ: AAAA
VRカメラ: BBBB
```
那么正则表达式翻译要写为
```
$前髪：(.+)				前发：$1
$広さ: (.+)				大小：$1
$VRカメラ: (.+)		VR摄像机: $1
```
这样就能翻译变量了

翻译后进入游戏检查，一切正常就可以提交啦！

贡献翻译请使用 Pull requests 如果不会用直接 Issues 附上文件提交也行

### 使用 AI 参与翻译

如今 AI 技术发展，使用 AI 往往也能获得令人满意的效果，特别是一些人工无力翻译的超长文本。

**使用 AI 翻译后请进行人工校对，否则不予合并**

注意：使用脚本需要安装 [Python3](https://www.python.org/downloads/)

在仓库的 script 文件夹中有一个 `script.py` 脚本，可以通过 `json2txt.bat` 和 `txt2json.bat` 来快捷使用

首先使用 IMGUITranslationLoader 的 dump 功能获取 `要翻译的文本.txt`，然后手动或者用 `ai.py`，`ai2.py` 清理掉不需要翻译的文本

然后把要转换的文本放置到 `.\inputs` 文件夹，运行 `txt2json.bat`，这会将 .txt 转换为 json 格式并输出到 `.\outputs` 文件夹

输出的 JSON 格式恰好和 MTool 导出的格式一致，因此可以使用支持此格式的工具进行翻译，这里推荐使用 [AiNiee](https://github.com/NEKOparapa/AiNiee)，在 AiNiee 中将项目格式设置为 Mtool导出文件 然后进行翻译即可

AiNiee 翻译完后把要转换的 json 放置到 `.\inputs` 文件夹，运行 `json2txt.bat`，这会将 .json 转换为 IMGUITranslationLoader 能读取的 txt 格式并输出到 `.\outputs` 文件夹

然后进行人工校对，校对完后进行测试，正常就可以贡献翻译啦

<br>
<br>

## 图片

只是随便截了两张图

 <img src="https://github.com/user-attachments/assets/46c2ea63-14d2-4eb7-a7ab-210d2d2cafd8" width="50%" />
 <img src="https://github.com/user-attachments/assets/b5d6f30f-4218-44bf-a22c-591dc3d652d2" width="50%" />


<br>
<br>

## 也可以看看我的其他仓库

 - [COM3D2 简明 MOD 教程](https://github.com/90135/COM3D2_Simple_MOD_Guide_Chinese)
 - [COM3D2 MOD 编辑器](https://github.com/90135/COM3D2_MOD_EDITOR)
 - [COM3D2 插件中文翻译](https://github.com/90135/COM3D2_Plugin_Translate_Chinese)
 - [90135 的 COM3D2 中文指北](https://github.com/90135/COM3D2_GUIDE_CHINESE)

<br>
<br>


## 贡献名单

杂酱 zaj2001 及其群友（未告诉我，所以无法署名）补充并调整了一些插件：

 - meidophotostudio.plugin
 - com3d2.scenecapture.plugin
 - com3d2.multiplemaids.plugin
 - com3d2.vibeyourmaid.plugin
 - 主要是增加了一些场景、道具的机翻文本，MeidoPhotoStudio 则是以人工为主，此外需要注意 SceneCapture 插件的场景是不能翻译的，否则会失效。

znq19 贡献了新插件翻译：

 - com3d2.motiontimelineeditor.plugin

<br>
<br>

## 许可证

本仓库使用 BSD 3-Clause 许可证，你只需要保留版权和免责声明，就可以随意更改和分发、整合等等。

分发时请最好带上本仓库地址，谢谢。

本仓库地址 [https://github.com/90135/COM3D2_Plugin_Translate_Chinese](https://github.com/90135/COM3D2_Plugin_Translate_Chinese)


