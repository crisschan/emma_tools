#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'EMMATools'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2018/4/9'
#__instruction__=''

from PIL import Image
import sys





class InfoHidden2Img(object):

    def __init__(self,sImg):
        self.image = Image.open(sImg)
    def makeImageEven(self):
        '''
        取得一个 PIL 图像并且更改所有值为偶数（使最低有效位为 0）
        :return:  image对象
        '''
        if self.image.mode != "RGBA":
            self.image = self.image.convert("RGBA")
        pixels = list(self.image.getdata())  # 得到一个这样的列表： [(r,g,b,t),(r,g,b,t)...]
        evenPixels = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1, t >> 1 << 1) for [r, g, b, t] in pixels]  # 更改所有值为偶数（魔法般的移位）
        evenImage = Image.new(self.image.mode, self.image.size)  # 创建一个相同大小的图片副本
        evenImage.putdata(evenPixels)  # 把上面的像素放入到图片副本
        return evenImage




    def constLenBin(slef,int):
        '''
        内置函数 bin() 的替代，返回固定长度的二进制字符串
        :param int: 位数标记
        :return: 二进制
        '''
        binary = "0" * (8 - (len(bin(int)) - 2)) + bin(int).replace('0b',
                                                                    '')  # 去掉 bin() 返回的二进制字符串中的 '0b'，并在左边补足 '0' 直到字符串长度为 8
        return binary

    def encodeDataInImage(self, sSecret):
        '''
          将字符串编码到图片中
        :param sSecret: 因此信息到图片
        :return:
        '''
        evenImage = self.makeImageEven()  # 获得最低有效位为 0 的图片副本
        binary = ''.join(map(self.constLenBin, bytearray(sSecret, 'utf-8')))  # 将需要被隐藏的字符串转换成二进制字符串
        if len(binary) > len(self.image.getdata()) * 4:  # 如果不可能编码全部数据， 抛出异常
            raise Exception("Error: Can't encode more than " + len(evenImage.getdata()) * 4 + " bits in this image. ")
        encodedPixels = [(r + int(binary[index * 4 + 0]), g + int(binary[index * 4 + 1]), b + int(binary[index * 4 + 2]),
                          t + int(binary[index * 4 + 3])) if index * 4 < len(binary) else (r, g, b, t) for
                         index, (r, g, b, t) in enumerate(list(evenImage.getdata()))]  # 将 binary 中的二进制字符串信息编码进像素里
        encodedImage = Image.new(evenImage.mode, evenImage.size)  # 创建新图片以存放编码后的像素
        encodedImage.putdata(encodedPixels)  # 添加编码后的数据
        return encodedImage


    def binaryToString(slef,binary):
        '''
           从二进制字符串转为 UTF-8 字符串
        :param binary: 二进制文件
        :return: 字符串
        '''
        index = 0
        string = []
        fun = lambda x, i: x[0:8]

        while index + 1 < len(binary):
            chartype = binary[index:].index('0')  # 存放字符所占字节数，一个字节的字符会存为 0
            if chartype == 0:
                chartype = 1
            length = chartype * 8

            for i in range(chartype):
                ascode = int(binary[index + i * 8:index + i * 8 + 8], 2)
                string.append(chr(ascode))
            index += length

        return ''.join(string)

    def decodeImage(self):
        '''
           解码隐藏数据
        :return: 返回隐藏的信息
        '''
        pixels = list(self.image.getdata())  # 获得像素列表
        binary = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) + str(
            int(t >> 1 << 1 != t)) for (r, g, b, t) in pixels])  # 提取图片中所有最低有效位中的数据

        # 找到数据截止处的索引
        locationDoubleNull = binary.find('0000000000000000')
        endIndex = locationDoubleNull + (
        8 - (locationDoubleNull % 8)) if locationDoubleNull % 8 != 0 else locationDoubleNull
        data = self.binaryToString(binary[0:endIndex])
        return data

if __name__=='__main__':
    infoHidden2Img= InfoHidden2Img('1.jpg')
    infoHidden2Img.encodeDataInImage('I am CrissChan. I want to build the DevOps.I am the king in this area1').save('2.png')
    infoHidden2Img2 = InfoHidden2Img('2.png')
    
    print(infoHidden2Img2.decodeImage())


