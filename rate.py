import time


class Leaky(object):
    water = 0
    pretime = 0
    def main(self, container, rate, addNum, limit):
        """
        :param container: 总容量
        :param rate: 每秒流出的量
        :param addNum: 注入量
        :param limit: 限制量
        :return:
        """
        # 当前时间
        nowTime = int(time.time())
        curWater = self.water - ((nowTime - self.pretime) * rate)
        # 水不能为负
        if curWater < 0:
            curWater = 0
        if curWater >= limit:
            addNum = 10
        # 更新本次注入时间
        self.pretime = nowTime
        # 水流出了一部分，不是上一次的水了，更新下，注入再更新，不注入则当前水量
        self.water = curWater
        if (curWater + addNum) <= container:
            # 通过，注水后更新水量
            self.water = curWater + addNum
            return True
        else:

            return False

l = Leaky()
for i in range(1, 100):
    time.sleep(0.1)
    res = l.main(100, 10, 15, 90)
    print(res)
