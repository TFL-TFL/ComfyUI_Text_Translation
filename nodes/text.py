
from ..utils.translation import  translators

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

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "trans_switch": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "trans_text": ("STRING",  {"multiline": True}),
                "translator": (["Bing", "Google", "Alibaba"],), 
                "source_language": (["auto", "中文(zh)", "English(en)", "Español(es)", "عربية(ar)", "हिन्दी(hi)", "Русский(ru)", "Français(fr)", "Deutsch(de)", "Português(pt)", "한국어(ko)", "日本語(ja)"],),    
                "target_language": (["English(en)", "中文(zh)", "Español(es)", "عربية(ar)", "हिन्दी(hi)", "Русский(ru)", "Français(fr)", "Deutsch(de)", "Português(pt)", "한국어(ko)", "日本語(ja)"],),    
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
            translator = translator.lower()
            if(source_language != "auto"):
               source_language = source_language.split("(")[1].split(")")[0]
            target_language = target_language.split("(")[1].split(")")[0]
            output_text = translators(text = trans_text, translator = translator, source_language = source_language, target_language = target_language)
        else:
            output_text = trans_text
        return (output_text,)
    
class Text_Translation_V2_Full:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "trans_switch": ("BOOLEAN", {"default": True, "label_on": "on", "label_off": "off"}),
                "trans_text": ("STRING",  {"multiline": True}),
                "translator": (["Alibaba", "Apertium", "Argos", "Baidu", "Bing", "Caiyun", "CloudTranslation", "DeepL", "Elia", "Google", "Hujiang", "Iciba", "Iflytek", "Iflyrec", "Itranslate", "Judic", "LanguageWire", "Lingvanex", "Niutrans", "Mglip", "Mirai", "ModernMt", "MyMemory", "Papago", "QqFanyi", "QqTranSmart", "Reverso", "Sogou", "SysTran", "Tilde", "TranslateCom", "TranslateMe", "Utibet", "VolcEngine", "Yandex", "Yeekit", "Youdao"],),  
                "source_language": (["auto", "中文(zh)", "English(en)", "عربية(ar)", "Русский(ru)", "Français(fr)", "Deutsch(de)", "Español(es)", "Português(pt)", "Italiano(it)", "日本語(ja)", "한국어(ko)", "Ελληνικά(el)", "Nederlands(nl)", "हिन्दी(hi)", "Türkçe(tr)", "Melayu(ms)", "ไทย(th)", "Tiếng Việt(vi)", "Indonesia(id)", "עברית(he)", "Polski(pl)", "Монгол(mn)", "Čeština(cs)", "Magyar(hu)", "Eesti(et)", "Български(bg)", "Dansk(da)", "Suomi(fi)", "Română(ro)", "Svenska(sv)", "Slovenščina(sl)", "فارسی(fa)", "Bosanski(bs)", "Српски(sr)", "Fijian(fj)", "Tagalog(tl)", "Kreyòl ayisyen(ht)", "Català(ca)", "文言文 WYW(wyw)", "粵語(yue)", "内蒙语 Монгол(mn)", "维吾尔语 Уйгурча(uy)", "藏语 ትግርኛ(ti)", "白苗文 Hmoob(mww)", "彝语(ii)", "苗语 Hmong(hmn)", "壮语(zyb)"],),    
                "target_language": (["English(en)", "中文(zh)", "عربية(ar)", "Русский(ru)", "Français(fr)", "Deutsch(de)", "Español(es)", "Português(pt)", "Italiano(it)", "日本語(ja)", "한국어(ko)", "Ελληνικά(el)", "Nederlands(nl)", "हिन्दी(hi)", "Türkçe(tr)", "Melayu(ms)", "ไทย(th)", "Tiếng Việt(vi)", "Indonesia(id)", "עברית(he)", "Polski(pl)", "Монгол(mn)", "Čeština(cs)", "Magyar(hu)", "Eesti(et)", "Български(bg)", "Dansk(da)", "Suomi(fi)", "Română(ro)", "Svenska(sv)", "Slovenščina(sl)", "فارسی(fa)", "Bosanski(bs)", "Српски(sr)", "Fijian(fj)", "Tagalog(tl)", "Kreyòl ayisyen(ht)", "Català(ca)", "文言文 WYW(wyw)", "粵語(yue)", "内蒙语 Монгол(mn)", "维吾尔语 Уйгурча(uy)", "藏语 ትግርኛ(ti)", "白苗文 Hmoob(mww)", "彝语(ii)", "苗语 Hmong(hmn)", "壮语(zyb)"]
,),      
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
            translator = translator.lower()
            if(source_language != "auto"):
               source_language = source_language.split("(")[1].split(")")[0]
            target_language = target_language.split("(")[1].split(")")[0]
            output_text = translators(text = trans_text, translator = translator, source_language = source_language, target_language = target_language)
        else:
            output_text = trans_text
        return (output_text,)
    
    
# class Get_Translator:
#     def __init__(self):
#         pass

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": { },
#         }

#     RETURN_TYPES = ("STRING",)
#     RETURN_NAMES = ("string",)

#     FUNCTION = "func"

#     #OUTPUT_NODE = False

#     CATEGORY = CATEGORY_NAME

#     def func(self):
#         translator = get_translator()
#         return (translator,)

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
    "Text_Translation_V2_Full": Text_Translation_V2_Full,
    "Text_Switch": Text_Switch,
    "Text_Concatenate": Text_Concatenate,
    # "Get_Translator": Get_Translator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text": "Text",
    "Text_Translation": "Text Translation",
    "Text_Translation_V2": "Text Translation V2",
    "Text_Translation_V2_Full": "Text Translation V2 (Full)",
    "Text_Switch": "Text Switch",
    "Text_Concatenate": "Text Concatenate",
    # "Get_Translator": "Get Translator",
}


