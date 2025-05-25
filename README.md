# 文本翻译
该自定义节点扩展 适用于 [ComfyUI](https://github.com/comfyanonymous/ComfyUI)。

现版本无需申请翻译API的密钥，直接使用即可。

#### 该节点调用 [Translators](https://github.com/UlionTse/translators) 库进行翻译，在此由心的感谢该库的作者，为我们提供免费、多样性的翻译途径。

## 注意：
1、更新前 需要将2024年05月19日前使用的老项目删除，当前项目与老项目完全不兼容。

2、该项目之前的项目名为 `ComfyUI_Text_Translation_zh_CN` 现修改为     `ComfyUI_Text_Translation`。

## 1、节点如下：
### 文本翻译
<img src="images/Text_Translation.png" width="512" />

默认使用必应翻译平台，自动识别语言翻译成英文。

### 文本翻译 V2
<img src="images/Text_Translation_V2.png" width="1024" />

节点中只含有部分翻译平台和语言。

默认隐藏多余选项，点击 `Show / Hide button` 显示或隐藏更多选项。

### 文本翻译 V2 (完整版)
<img src="images/Text_Translation_V2_Full.png" width="1024" />

节点中包含全部翻译平台和语言，使用前请测试，该翻译平台是否支持当前选择的语言。可参考 [Translators](https://github.com/UlionTse/translators) 上列举的信息。

默认隐藏多余选项，点击 `Show / Hide button` 显示或隐藏更多选项。

### 文本联接
<img src="images/Text_Concatenate.png" width="200" />

<img src="images/Text_Concatenate2.png" width="700" />

自动根据连接的数量增加/减少 输入端，将输入端的值拼接成一个字符串。

### 文本
<img src="images/Text.png" width="512" />

文本输入框。

### 文本开关
<img src="images/Text_Switch.png" width="256" />

文本开关，关闭则输出空字符串。


提示：想要在ComfyUI上显示输出文本，例如 可以使用 [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) 中的 `ShowText` 或其他节点

## 2、安装

###  (1)添加该节点到&nbsp;ComfyUI

#### &ensp;1) 方式一：克隆本项目

  ```
  cd custom_nodes
  ```

  ```
  git clone https://github.com/TFL-TFL/ComfyUI_Text_Translation.git
  ```
#### &ensp;2) 方式二：直接下载ZIP

下载解压后放入`custom_nodes`内

###  (2)配置环境

  ```
  cd ComfyUI_Text_Translation
  ```

如果你下载的是&ensp;ComfyUI&ensp;的 便携版本，可直接执行下面代码，否则请将 `requirements.txt` 内的依赖安装到对应位置。
  ```
  ..\..\..\python_embeded\python.exe -s -m pip install -r requirements.txt
  ```


###  (3)重启ComfyUI

  所有的步骤都操作完啦，可以愉快的创作呦！

## 3、支持的翻译平台和语言

### 支持的翻译平台
```
alibaba -- 阿里巴巴 (Alibaba)
apertium -- Apertium
argos -- Argos
baidu -- 百度 (Baidu)
bing -- 必应 (Bing)
caiyun -- 彩云 (Caiyun)
cloudTranslation -- 云翻译 (CloudTranslation)
deepl -- DeepL
elia -- Elia
google -- 谷歌 (Google)
hujiang -- 沪江 (Hujiang)
iciba -- 金山词霸 (ICIBA)
iflytek -- 讯飞 (iFlytek)
iflyrec -- 讯飞语音识别 (iFlyrec)
itranslate -- iTranslate
judic -- Judic
languageWire -- LanguageWire
lingvanex -- Lingvanex
niutrans -- 牛翻译 (Niutrans)
mglip -- Mglip
mirai -- Mirai
modernMt -- ModernMT
myMemory -- MyMemory
papago -- Papago
qqFanyi -- QQ翻译 (QQFanyi)
qqTranSmart -- QQ智能翻译 (QQTranSmart)
reverso -- Reverso
sogou -- 搜狗 (Sogou)
sysTran -- Systran
tilde -- Tilde
translateCom -- Translate.com
translateMe -- TranslateMe
utibet -- UTibet
volcEngine -- VolcEngine
yandex -- Yandex
yeekit -- Yeekit
youdao -- 有道 (Youdao)
```
### 支持的语言
```
中文 (zh)
English (en)
عربية (ar)
Русский (ru)
Français (fr)
Deutsch (de)
Español (es)
Português (pt)
Italiano (it)
日本語 (ja)
한국어 (ko)
Ελληνικά (el)
Nederlands (nl)
हिन्दी (hi)
Türkçe (tr)
Melayu (ms)
ไทย (th)
Tiếng Việt (vi)
Indonesia (id)
עברית (he)
Polski (pl)
Монгол (mn)
Čeština (cs)
Magyar (hu)
Eesti (et)
Български (bg)
Dansk (da)
Suomi (fi)
Română (ro)
Svenska (sv)
Slovenščina (sl)
فارسی (fa)
Bosanski (bs)
Српски (sr)
Fiji (fj)
Tagalog (tl)
Kreyòl ayisyen (ht)
Català (ca)
文言文 WYW (wyw)
粵語 (yue)
内蒙语 Монгол (mn)
维吾尔语 Уйгурча (uy)
藏语 ትግርኛ (ti)
白苗文 Hmoob (mww)
彝语 (ii)
苗语 Hmong (hmn)
壮语 (zyb)
```

### 4、更新日志

#### 2025-05-25
1、修复当前版本的comfy中，Text Concatenate节点的连接在刷新和复制粘贴时的异常问题。
感谢由 MakkiShizu 提出的修复方案。

#### 2024-05-20
1、文本翻译 V2：新增一些语言。

2、新增 “文本翻译 V2  (完整版)” 节点。

3、删除 “获取翻译平台列表” 节点。

#### 2024-05-19
1、弃用腾讯翻译API，简化配置，使用&nbsp;[Translators](https://github.com/UlionTse/translators)&nbsp;提供的方式进行翻译，无需申请密钥了。

2、完全重写节点，新增或修改 “文本翻译”、“文本翻译 V2”、 “获取翻译平台列表”、“文本”、“文本开关”、“文本联接” 节点。


#### 2023-08-27

&emsp;去除“翻译开关”的默认值，以便适配&nbsp;[StableSwarmUI](https://github.com/Stability-AI/StableSwarmUI)&nbsp;，不然该开关的值会由“可选择类型”变成“要输入类型的文字”。

#### 2023-08-22

&emsp;初始提交，节点采用了[腾讯翻译API](https://cloud.tencent.com/product/tmt)进行文本翻译。

### 5、报错
如果有类似以下的报错信息，请删除该节点并重新添加。
```
Prompt outputs failed validation
Text_Translation_V2:
- Value not in list: translator: 'alibaba' not in ['Bing', 'Google', 'Alibaba']
```



  