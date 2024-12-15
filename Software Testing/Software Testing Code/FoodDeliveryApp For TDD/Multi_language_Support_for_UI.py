import unittest
#红阶段
class TestMultiLanguageSupport(unittest.TestCase):
    def test_translate_text(self):
        # 测试文本翻译
        pass

#绿阶段
class Translator:
    def translate(self, text, target_language):
        # 简单翻译逻辑
        return f"Translated {text} to {target_language}"


# 重构代码
class Translator:
    def __init__(self, translation_service):
        self.translation_service = translation_service

    def translate(self, text, target_language):
        return self.translation_service.translate(text, target_language)