#!/usr/bin/python
#encoding=utf8
import base64
import os

class Img2Base64(object):
    '''
    将图片变成base64编码，然后在web中打开，不用引入图片外部图片文件
    '''
    def __init__(self,sImgDir):
        fr = open(sImgDir, 'rb')
        self.hexImg=base64.b64encode(fr.read())
        fr.close()



'''if __name__=='__main__':

    print ' <img src = "data:image/bmp;base64,'+Img2Base64('/Users/chancriss/Desktop/WorkSpace/PythonSpace/EmmaTools/ocr.jpg').hexImg+'\"/>'
'''