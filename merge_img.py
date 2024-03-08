#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   merge_img.py
@Time    :   2024/03/04 13:59:42
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   将多张图片合并成一个图片
'''
import numpy as np
import cv2

class MergeImg(object):
    def __init__(self,img_file_list,output_img_file="output_finale.png") -> None:
        '''
        @des  :构造函数
        @params  :
            img_file_list:存储图片文件绝对地址的列表
            output_img：输出文件的地址，默认值为output_finale.png

        '''
        self.img_file_list = img_file_list
        self.output_img_file = output_img_file
    
    def merge(self):
        '''
        @des  :合并img_file_list里面的图片，结果存为output_img_file
        @params  :无
        '''
        
        
        imgs = []
        aimg =""
        for aimg in self.img_file_list:
            img = cv2.imread(aimg)
            imgs.append(img)
        merge_img = np.vstack(imgs)
        cv2.imwrite(self.output_img_file,merge_img)


if __name__ == '__main__':
    alist=['./from/1.png','./from/2.png','./from/3.png']
    mi = MergeImg(alist)
    mi.merge()
