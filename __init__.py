from .node.tencent_translation import *


__version__ = "1.0.0"

NODE_CLASS_MAPPINGS = {
    "TencentTextTranslation": TencentTextTranslation,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TencentTextTranslation": "文本翻译",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
