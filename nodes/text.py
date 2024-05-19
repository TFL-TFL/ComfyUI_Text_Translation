
from ..utils.translation import  translators, get_translator

# 适应不同地区的人使用该节点，当前默认类别名为英文，按需自行更改
# Adapt to people from different regions using this node. 
# The current default class alias is in English and can be changed as needed

# CATEGORY_NAME = "文本翻译"
CATEGORY_NAME = "Text Translation"

class Text:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "text": ("STRING", {"multiline": True}),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "func"
    #OUTPUT_NODE = False
    CATEGORY = CATEGORY_NAME

    def func(self, text):
        return (text,)


class Text_Translation:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "trans_switch": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "trans_text": ("STRING",  {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "func"

    #OUTPUT_NODE = False

    CATEGORY = CATEGORY_NAME

    def func(self, trans_switch, trans_text):
        output_text = ""
        if trans_switch:
            output_text  = translators(text = trans_text)
        else:
            output_text = trans_text
        return (output_text,)

class Text_Translation_V2:
    def __init__(self):
        pass

    #  截止 [Translators](https://github.com/UlionTse/translators) 版本：v5.9.1 支持如下翻译平台：
    # alibaba, apertium, argos, baidu, bing, caiyun, cloudTranslation, deepl, elia, 
    # google, hujiang, iciba, iflytek, iflyrec, itranslate, judic, languageWire, lingvanex,
    # niutrans, mglip, mirai, modernMt, myMemory, papago, qqFanyi, qqTranSmart, reverso, 
    # sogou, sysTran, tilde, translateCom, translateMe, utibet, volcEngine, yandex, yeekit, youdao

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "trans_switch": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "trans_text": ("STRING",  {"multiline": True}),
                "translator": (["alibaba", "bing", "google", ],),   #直接再此添加 翻译平台
                "source_language": (["auto", "zh", "en", ],),     #直接再此添加 相应支持的源语言
                "target_language": (["en", "zh", ],),      #直接再此添加 相应支持的目标语言
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "func"

    #OUTPUT_NODE = False

    CATEGORY = CATEGORY_NAME

    def func(self, trans_switch, trans_text, translator, source_language, target_language):
        output_text = ""
        if trans_switch:
            output_text = translators(text = trans_text, translator = translator, source_language = source_language, target_language = target_language)
        else:
            output_text = trans_text
        return (output_text,)
    
class Get_Translator:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "func"

    #OUTPUT_NODE = False

    CATEGORY = CATEGORY_NAME

    def func(self):
        translator = get_translator()
        return (translator,)

class Text_Switch:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "switch": ("BOOLEAN", {"default": True,  "label_on": "on", "label_off": "off"}),
                "text": ("STRING", {"forceInput": True})
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "func"

    #OUTPUT_NODE = False

    CATEGORY = CATEGORY_NAME

    def func(self, switch, text):
        output_text = ""
        if switch:
            output_text = text
        return (output_text,)
    
class Text_Concatenate:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"

    CATEGORY = CATEGORY_NAME

    def func(self, **kwargs):
        text = ""
        for k, v in kwargs.items():
            text = text + v
        return (text, )
    


NODE_CLASS_MAPPINGS = {
    "Text": Text,
    "Text_Translation": Text_Translation,
    "Text_Translation_V2": Text_Translation_V2,
    "Text_Switch": Text_Switch,
    "Text_Concatenate": Text_Concatenate,
    "Get_Translator": Get_Translator,
}


# 适应不同地区的人使用该节点，当前默认节点名为英文，按需自行更改
# Adapt to people from different regions using this node. 
# The current default node name is English and can be changed as needed

# NODE_DISPLAY_NAME_MAPPINGS = {
#     "Text": "文本",
#     "Text_Translation": "文本翻译",
#     "Text_Translation_V2": "文本翻译V2",
#     "Text_Switch": "文本开关",
#     "Text_Concatenate": "文本联接",
#     "Get_Translator": "获取翻译平台",
# }

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text": "Text",
    "Text_Translation": "Text Translation",
    "Text_Translation_V2": "Text Translation V2",
    "Text_Switch": "Text Switch",
    "Text_Concatenate": "Text Concatenate",
    "Get_Translator": "Get Translator",
}


