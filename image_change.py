#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 4:38 PM
# @Author  : Criss Chan
# @Site    : https://blog.csdn.net/crisschan
# @File    : image_chage.py
# @Software: PyCharm
# @instruction：所有图片的转换类

from PIL import Image
import os
class ImageChange(object):
    def __init__(self,image_inpath,image_outpath):
        '''

        :param image_path: 图片的路径
        '''
        self.image_inpath=image_inpath
        self.image_outpath=image_outpath

    def IsValidImage(self,img_path):
        '''
        判断文件是否为有效（完整）的图片
        :param img_path:图片路径
        :return:True：有效 False：无效
        '''
        bValid = True
        try:
            Image.open(img_path).verify()
        except:
            bValid = False
        return bValid
    def ChangeImage(self):
        '''
        转换图片格式
        :param img_path:图片路径
        :return: True：成功 False：失败
        '''
        if self.IsValidImage(self.image_inpath):
            try:
                str = self.image_inpath.rsplit(".", 1)
                output_img_path = str[0] + ".jpg"
                im = Image.open(self.image_inpath)
                im.save(self.image_outpath)
                return True
            except:
                return False
        else:
            return False
#
# if __name__ == '__main__':
#     ff = os.getcwd()
#     for root, dirs, files in os.walk(ff+'/in/'):
#         for afile in files:
#             ic = ImageChange(ff+'/in/'+afile,ff+'/out/')
#             ic.ChangeImage()