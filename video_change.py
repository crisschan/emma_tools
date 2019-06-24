#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 8:59 AM
# @Author  : Criss Chan
# @Site    : 
# @File    : video_change_proprity.py
# @Software: PyCharm
# @instruction: 视频修改码率的，为创建各种不同测试使用的视频文件做准备
from pydub import AudioSegment

class VideoChange(object):

    def __init__(self,video_path):
        self.__video_path = video_path
        self.change_frame_rate()
    def change_frame_rate(self):
        '''
        z转换码率（到喜马拉雅可以识别）
        :return: null
        '''
        # 读取音频文件，设置采样率<default=44100>
        song = AudioSegment.from_mp3(self.__video_path).set_frame_rate(128050)
        # 按32k的bitrate导出文件到指定路径,这里是直接覆盖原文件
        song.export(self.__video_path, format='mp3', bitrate='64k')


if __name__ == '__main__':
    VideoChange('自动化通用架构.mp3')

