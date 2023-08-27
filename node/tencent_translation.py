import json
import re
import os
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

# 腾讯翻译安装 Python SDK https://cloud.tencent.com/document/sdk/Python
# pip install --upgrade tencentcloud-sdk-python

# 腾讯翻译文档 https://cloud.tencent.com/document/api/551/15619


# region 腾讯翻译全局对象 起始
httpProfile = HttpProfile()
httpProfile.endpoint = "tmt.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
# 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
# 有两种方式设置密钥
# （1）硬编码密钥到代码中，这有可能随代码泄露而暴露，有安全隐患，不推荐 （简单）
# cred = credential.Credential("secretId", "secretKey")
# （2）密钥设置在环境变量中，推荐 （稍微多些步骤，请在开启ComfyUI前设置好，若已开启需要重启ComfyUI）
#       可在终端使用  echo %环境变量名称%  查看是否正确设置
cred = credential.Credential(
    os.environ.get("TENCENTCLOUD_SECRET_ID"),
    os.environ.get("TENCENTCLOUD_SECRET_KEY"))
# 操作的资源所属的地域 如、ap-beijing、ap-chengdu、ap-chongqing、ap-guangzhou、ap-shanghai
# 可以选择离自己近的地域，更多详情见 https://cloud.tencent.com/document/api/551/15615#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8
tmt_client_instance = tmt_client.TmtClient(cred, "ap-guangzhou", clientProfile)
# endregion


# 调用腾讯翻译API
def tencent_api(text_to_translate):
    try:
        req = models.TextTranslateRequest()
        params = {
            "SourceText": text_to_translate,
            "Source": "auto",  # 翻译前的语言类型，默认 自动（auto）
            "Target": "en",  # 翻译后的语言类型，默认 英语（en）
            "ProjectId": 0,
        }
        req.from_json_string(json.dumps(params))
        resp = tmt_client_instance.TextTranslate(req)
        return resp.TargetText
    except TencentCloudSDKException as err:
        print("文本翻译错误：" + err)
        return ""


# 判断是否包含中文
def contains_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(text))


class TencentTextTranslation:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_trans": ("STRING", {"multiline": True}),
                "text_normal": ("STRING", {"multiline": True}),
                "trans_switch": (["enabled", "disabled"],),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "translation"
    CATEGORY = "utils"

    # trans_switch 翻译功能的开关，enabled 开启；disabled 关闭
    def translation(self, text_trans, text_normal, trans_switch, ):
        if text_trans == "undefined":
            text_trans = ""
        if text_normal == "undefined":

            text_normal = ""
        is_enabled = trans_switch == "enabled"
        target_text = ""
        if is_enabled and contains_chinese(text_trans):
            target_text = tencent_api(text_trans)
            # 在终端打印翻译后的内容，不需要可删除或注释
            print("文本翻译结果: " + target_text)
        else:
            target_text = text_trans
        output_text = ", ".join(filter(None, [target_text, text_normal]))
        output_text = output_text.replace('，', ',').replace('。', ',').replace("  ", " ").replace(" ,", ",").replace(",,", ",")
        # 在终端打印翻译后的内容，不需要可删除或注释
        print("文本最终结果: " + output_text)
        return (output_text,)


# NODE_CLASS_MAPPINGS = {
#     "TencentTranslation": TencentTextTranslation,
# }
#
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "TencentTranslation": "文本翻译",
# }
