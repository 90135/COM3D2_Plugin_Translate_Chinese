# COM3D2_Plugin_Translate_Chinese
COM3D2 中文插件翻译 / COM3D2 Chinese plugin translation


这是 COM3D2 的 IMGUI 插件的中文翻译，本项目使用 [IMGUITranslationLoader](https://github.com/ghorsington/IMGUITranslationLoader) 所以只能翻译使用 IMGUI 的插件。

IMGUI 就是半透明的黑色窗口。

```
本人非专业，看不懂的就结合机翻了。
要看到的字才能 dump 下来翻译，所以可能并不是完全翻译。
```
有没翻译的欢迎反馈或直接贡献翻译，本汉化最初发布于 ZODGAME。

## 使用方法

1. 安装 IMGUITranslationLoader
[https://github.com/ghorsington/IMGUITranslationLoader](https://github.com/ghorsington/IMGUITranslationLoader)

下载 IMGUITranslationLoader_xxxxx.7z
复制 IMGUITranslationLoader.Managed.dll 和 IMGUITranslationLoader.Sybaris.Patcher.dll 到 COM3D2\Sybaris 文件夹。

![图片](https://github.com/user-attachments/assets/5f91581c-30e8-4a6e-9fb7-7112fe33a9cf)


2. 下载本仓库 Release 中的压缩包，或是下载源代码。

找到对应路径

把翻译.txt放到 COM3D2\IMGUITranslationLoader\IMGUIStrings 文件夹中，如图所示

![图片](https://github.com/user-attachments/assets/a0f0a057-47ed-42d1-ac3e-90668b48cb01)

3. 记得在 COM3D2\IMGUITranslationLoader 中的 IMGUITranslationLoader.ini 里设置 Load=True 启用（应该是会自动启用的）

没有就先启动一次游戏

<br>

IMGUITranslationLoader.ini 里还可以设置全局模式 GlobalMode=True

启用后就会无视插件限制，无论什么插件，只要有相同字符串就能翻译，但也可能造成问题。

## 常见问题

### CM3D2 能用吗
能，如果插件名不一样的，更改翻译文件名就行了。比如 com3d2.vibeyourmaid.plugin.txt 改成 cm3d2.vibeyourmaid.plugin.txt
遇到一样的插件和一样的字符就会翻译。
或者开全局模式。


### CM3D2.5 能用吗
能，同样的，遇到不一样名字的插件 如 com3d2_5.xxxxx.plugin 把对应的翻译文件改一下名即可。
遇到一样的插件和一样的字符就会翻译。
或者开全局模式。


### XUnity.AutoTranslator 共存
注意不要用 turtle_formatter.exe 处理，否则会被删掉。
在 AutoTranslatorConfig.ini 里面设置 EnableIMGUI=false 就好

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


## 我想汉化其他插件怎么办
顾名思义，使用 IMGUI 制作的插件都可以翻译，读一读插件说明就会了，欢迎贡献到本仓库，发 PR，不会的话 发 Issue 附上文件也可以

[https://github.com/ghorsington/IMGUITranslationLoader/wiki](https://github.com/ghorsington/IMGUITranslationLoader/wiki)

[https://github.com/ghorsington/IMGUITranslationLoader/blob/master/README.md](https://github.com/ghorsington/IMGUITranslationLoader/blob/master/README.md)


## 贡献

杂酱 zaj2001 补充并调整了一些插件：meidophotostudio.plugin      com3d2.scenecapture.plugin   com3d2.multiplemaids.plugin    com3d2.vibeyourmaid.plugin

主要是增加了一些场景、道具的机翻文本，meidophotostudio 则是以人工为主 此外，scenecapture 的场景是不能翻译的 否则会失效

这些文本已合并到本包。
