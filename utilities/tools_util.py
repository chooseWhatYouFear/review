import random


class ToolsUtil:
    @staticmethod
    def rand_zh(length):
        results = []
        for i in range(length):
            result = random.randint(0x4e00, 0x9fbf)
            if not result:
                result = random.randint(0x4e00, 0x9fbf)
            results.append(chr(result))
        return ''.join(results)