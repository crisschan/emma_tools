from email import header
from email.mime import image
from ensurepip import version
from importlib import import_module
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   qrcode4test.py
@Time    :   2022/09/19 16:13:10
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   为测试封装的二维码生成、识别的class
'''
import os
from enum import Enum
import qrcode
from PIL import Image
import zxing

class Error_Coorrect(Enum):
    '''错误的Enum类'''
    # L 最多可以矫正7%的错误
    L=qrcode.constants.ERROR_CORRECT_L
    # M 最多可以矫正15%的错误，这个是默认值
    M=qrcode.constants.ERROR_CORRECT_M
    # Q 最多可以矫正25%的错误
    Q=qrcode.constants.ERROR_CORRECT_Q
    # H 最多可以矫正30%的错误
    H=qrcode.constants.ERROR_CORRECT_H


class QRcodeEncode(object):
    ''' 生成二维码的类，  
    qr = QRcodeEncode(content='ffffff')
    qr.encode_qrcode()
    二维码的属性可以通过setter设置'''
    def __init__(self,save_path=None,content=None) -> None:
        '''
        @des  : QRcodeEncode的构造函数
               
        @params  :save_path 二维码存储地址，如果没有就直接打开
                  content   需要存储到二维码中的信息             
        @return  :无           
        '''
        self.__save_path=save_path
        self.__content = content
        self.__version = 2
        self.__error_correction = Error_Coorrect.M.value
        self.__box_size=8 # 每一个二维码中的box占据的像素
        self.__border = 4 # 控制QR Code的空白边距大小，默认值为4
        self.__fill_color=(55, 95, 35)# 填充色
        self.__back_color = (255, 195, 235) # 背景色
        
    def encode_qrcode(self):
        '''
        @des  :生成二维码
               
        @params  :无
                 
        @return  :在save_path中设置的位置存储突破，如果该参数是None，直接打开二维码图片
                  
        '''
        
        
        encode_qr = qrcode.QRCode(version = self.__version,error_correction=self.__error_correction,box_size=self.__box_size,border=self.__border)
        encode_qr.add_data(data = self.__content)
        encode_qr.make(fit=True)
        img = encode_qr.make_image(fill_color = self.__fill_color,bakc_color = self.__back_color)
        if self.__save_path:
            img.save(self.__save_path)
        else:
            img.show()

    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self,version):
        if 40-version<=0:
            self.__version = version
        else:
            print('版本取在1-40之间的整数')

    @property
    def error_correction(self):
        return self.__error_correction
    @error_correction.setter
    def error_correction(self,error_correction):
        if any(error_correction == e.key for e in Error_Coorrect):
            self.__error_correction=error_correction
        else:
            print('error_correction 是 枚举类型Error_Coorrect')

    @property
    def box_size(self):
        return self.__box_size
    @box_size.setter
    def box_size(self,box_size):
        self.__box_size = box_size

    @property
    def border(self):
        return self.__border
    @border.setter
    def boder(self,boder):
        self.__border = boder

    @property
    def fill_color(self):
        return self.__fill_color
    @fill_color.setter 
    def fill_color(self,fill_color):
        self.__fill_color = fill_color
    @property
    def back_color(self):
        return self.__back_color
    @back_color.setter
    def back_color(self,back_color):
        self.__back_color = back_color

class QRCodeDecode(object):
    def __init__(self,image_path = None ) -> None:
        self.__image_path = image_path
        pass
    def decode_qrcode(self):
        if not os.path.exists(self.__image_path):
            raise  FileExistsError(self.__image_path)
        qr = zxing.BarCodeReader()
        qrinfo = qr.decode(self.__image_path)
        return qrinfo.parsed

        
        

# if __name__ == '__main__':
    # print(Error_Coorrect.M.value)
    # print( qrcode.constants.ERROR_CORRECT_M)
    # qr = QRcodeEncode(content='ffffff')
    # qr.encode_qrcode()
    # qrde=QRCodeDecode('2.png')
    # print(qrde.decode_qrcode())