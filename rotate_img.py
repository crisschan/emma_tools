#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__from__ = 'PythonSpace'
#__title__='PyCharm'
#__author__ = 'chancriss'
#__mtime__ = '2017/10/9'
#__instruction__='图片旋转'

from PIL import Image
from numpy import *

class RotateImg(object):

    def __init__(self,sOrgImgFile,sTargetImgFile):
        '''
        Args:
            sOrgImgFile: 原始图片地址
            sTargetImgFile: 转存图片地址
        '''
        self.sOrgImgFile=sOrgImgFile
        self.sTargetImgFile=sTargetImgFile
    def rotate(self,nRotate=0):
        '''
        按照nRotate旋转
        Args:
            nRotate: 旋转角度-360 到 360 之间
        Returns:

        '''
        self.nRotate = nRotate
        pil_im = Image.open(self.sOrgImgFile)
        pil_im = pil_im.rotate(self.nRotate)
        sTargetRotate = self.sTargetImgFile[:self.sTargetImgFile.find('.')]+'_rotate'+str(nRotate)+self.sTargetImgFile[self.sTargetImgFile.find('.'):]
        pil_im.save(sTargetRotate)
    def Counterclockwise90(self):
        '''
        逆时针旋转90度
        Returns:

        '''
        pil_im = Image.open(self.sOrgImgFile)
        dx, dy = pil_im.size
        pil_im=pil_im.transpose(Image.ROTATE_90)
        pil_im = pil_im.resize((dy, dx))
        sTargetRotate = self.sTargetImgFile[:self.sTargetImgFile.find('.')] + '_Counterclockwise90' + self.sTargetImgFile[self.sTargetImgFile.find('.'):]
        pil_im.save(sTargetRotate)
    def Clockwise90(self):
        '''
        顺时针旋转90度
        Returns:

        '''
        pil_im = Image.open(self.sOrgImgFile)
        dx,dy=pil_im.size

        pil_im=pil_im.transpose(Image.ROTATE_270)

        pil_im=pil_im.resize((dy,dx))
        sTargetRotate = self.sTargetImgFile[:self.sTargetImgFile.find('.')] + '_Clockwise90' + self.sTargetImgFile[self.sTargetImgFile.find('.'):]
        pil_im.save(sTargetRotate)
    def ToptoBottom(self):
        pil_im = Image.open(self.sOrgImgFile)
        pil_im=pil_im.transpose(Image.FLIP_TOP_BOTTOM)
        sTargetRotate = self.sTargetImgFile[:self.sTargetImgFile.find('.')] + '_ToptoBottom' + self.sTargetImgFile[self.sTargetImgFile.find('.'):]
        pil_im.save(sTargetRotate)
    def LefttoRight(self):
        pil_im = Image.open(self.sOrgImgFile)
        pil_im=pil_im.transpose(Image.FLIP_LEFT_RIGHT)
        sTargetRotate = self.sTargetImgFile[:self.sTargetImgFile.find('.')] + '_LefttoRight' + self.sTargetImgFile[self.sTargetImgFile.find('.'):]

        pil_im.save(sTargetRotate)
# if __name__=='__main__':
#     ri  = RotateImg('0001.jpg','5.jpg')
#     ri.LefttoRight()
#     ri.ToptoBottom()
#     ri.Clockwise90()
#     ri.Counterclockwise90()
#     ri.rotate(nRotate=45)




