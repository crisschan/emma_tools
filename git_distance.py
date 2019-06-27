#encoding=utf8
#!/usr/bin/env python
# __author_='crisschan'
# __data__='20160908'
# __from__='EmmaTools'
#__instruction__=计算两经纬度间的距离
from math import radians, cos, sin, asin, sqrt
class GetDistance(object):
    def __init__(self,lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
        '''
        计算两个地理坐标之间的距离
        Args:
            lon1: 经度1（十进制度数）
            lat1: 纬度1（十进制度数）
            lon2: 经度2（十进制度数）
            lat2: 纬度2（十进制度数）
        return：
            返回之间的直线距离(米）
        '''

        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # 地球平均半径，单位为公里
        self.distance=c * r * 1000
'''
if __name__=='__main__':
    print GetDistance(39.9,116.3,33.3,114.9).distance
'''