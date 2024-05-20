
def  translators(text : str , translator: str = "bing", source_language = "auto", target_language = "en", timeout: float = 10.0):
    if not text:
        return ""
    try:
        import translators  
        result = translators.translate_text(query_text = text, translator = translator,from_language = source_language, to_language= target_language, timeout= timeout)
        return result 
    except Exception as e:
        raise Exception(f"Error:  Translation failed , Message : {e}")

def get_translator():
    try:
        import translators  
        translators_list = translators.translators_pool
        result = '\n'.join(translators_list)
        print(f"Text Translation translator: \n{result}")
        return result

    except Exception as e:
        raise Exception(f"Error:  Translation failed , Message : {e}")


    
