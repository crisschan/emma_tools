#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'PythonSpace'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2017/11/21'
#__instruction__='图片分割'

import os
from PIL import Image


class SplitImg(object):

    def __init__(self,src, rownum, colnum, dstpath):
        '''

        Args:
            src: 原图片绝对地址
            rownum: 分割行数
            colnum: 分割列数
            dstpath: 输出目录
        '''
        img = Image.open(src)
        w, h = img.size
        if rownum <= h and colnum <= w:
            print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
            print('开始处理图片切割, 请稍候...')

            s = os.path.split(src)
            if dstpath == '':
                dstpath = s[0]
            fn = s[1].split('.')
            basename = fn[0]
            ext = fn[-1]

            num = 0
            rowheight = h // rownum
            colwidth = w // colnum
            for r in range(rownum):
                for c in range(colnum):
                    box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                    img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                    num = num + 1

            print('图片切割完毕，共生成 %s 张小图片。' % num)
        else:
            print('不合法的行列切割参数！')

if __name__=="__main__":
    src = '/Users/chancriss/Downloads/1/1.png'
    if os.path.isfile(src):
        dstpath = '/Users/chancriss/Downloads/1/'
        if (dstpath == '') or os.path.exists(dstpath):
            row = 3
            col = 4
            if row > 0 and col > 0:
                SplitImg(src, row, col, dstpath)
            else:
                print('无效的行列切割参数！')
        else:
            print('图片输出目录 %s 不存在！' % dstpath)
    else:
        print('图片文件 %s 不存在！' % src)