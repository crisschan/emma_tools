#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 4:38 PM
# @Author  : Criss Chan
# __from__='EmmaTools https://github.com/crisschan/EMMATools'
# @File    : image_chage.py
# @Software: PyCharm
# @instruction：所有图片的转换类

from PIL import Image
import os
class ImageChange(object):
    def __init__(self,image_file,image_path):
        '''

        :param image_file: 输入图片文件名
        :param image_path: 输入图片存储路径，以/结尾
        '''
        self.image_file=image_file
        self.image_path=image_path

    def is_valid(self,img_path):
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
    def change_type(self,pic_type='.jpg'):
        '''
        转换图片格式
        :param pic_type:图片类型，默认是jgp，支持png、gif等主流的图片格式
        :return: True：成功 False：失败
        '''
        if self.is_valid(self.image_path+self.image_file):
            # try:
            str = self.image_file.rsplit(".", 1)
            output_image= self.image_path+str[0] + pic_type
            im = Image.open(self.image_path+self.image_file)
            im=im.convert('RGB')
            im.save(output_image)
            return True
            # except:
            #     return False
        else:
            return False
    def change_size(self,new_hight,new_width,org_proportion=False):
        '''
        改变图片高宽像素大小
        :param new_hight:新的 高的像素值
        :param new_width: 新的宽的像素值
        :param org_proportion: 是否维护远比例也就是原来图片的高/宽比例，如果选择了True，那么new_width不起作用
        :return:True：成功 False：失败
        '''
        if self.is_valid(self.image_path + self.image_file):
            str = self.image_file.rsplit(".", 1)
            output_image = self.image_path + str[0]+'.' + str[1]
            im = Image.open(self.image_path + self.image_file)
            if org_proportion:
                (width, hight) = im.size  #读取当前长和宽
                new_width = int(width *  new_hight / hight)

            out = im.resize((new_hight, new_width), Image.ANTIALIAS)  # 以高质量转存新比例图片，
            out.save(output_image)
            return True
        else:
            return False
if __name__ == '__main__':


    a = 1
    while a<17:
        if a/10 >=1:
            in_file=str(a)+'.PNG'
        else:
            in_file = '0'+str(a) + '.PNG'
        in_path = '/Users/crisschan/Downloads/'
        ic = ImageChange(in_file,in_path)
        print(ic.change_size(120,20,org_proportion=True))
        a=a+1

