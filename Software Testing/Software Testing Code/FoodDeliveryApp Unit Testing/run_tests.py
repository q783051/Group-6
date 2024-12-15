import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover('tests')  # 指定测试文件所在的目录
    testRunner = unittest.TextTestRunner()
    testRunner.run(tests)