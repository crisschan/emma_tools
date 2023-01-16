#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   try_pic_video.py
@Time    :   2023/01/16 11:44:30
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   图片转换成视频
'''


from moviepy.editor import *
from get_dirAndfiles import DirAndFiles
class Pic2Video:
    
    def __init__(self, pics_path, pic_type = '.png', out_file_path='video_tmp.mp4', fps=24, size=(1280, 720),duration = 10):
        '''
        @des  : 初始化函数
        @params  :pics_path存储png图片的目录
                  pic_type存储图片的后缀名(默认是PNG)
        @params  :out_file_path输出视频的路径，默认video_tmp
        @params  :fps视频的帧率，默认24
        @params  :size视频的尺寸，默认1280*720
        @params  :duration视频的时长，默认10秒
        @return  :none
                  
        '''
        
        
        self.pics_path = pics_path
        self.out_file_path = out_file_path
        self.fps = fps
        self.size = size
        self.duration = duration
        self.pic_type = pic_type
    def pic2video(self):
        '''
        @des  :# 创建视频文件
        @params  :none
        @return  : none
                  
        '''
        
        
        df = DirAndFiles()
        files_list = df.filesWithFilter(self.pics_path, self.pic_type)
        clips = [ImageClip(m).set_duration(self.duration) for m in files_list]
        # 获取视频的尺寸
        concat_clip = concatenate_videoclips(clips, method="compose")
        concat_clip.write_videofile(self.out_file_path, fps=self.fps)
if __name__ == '__main__':
    Pic2Video('/Users/crisschan/workspace/PySpace/try/pic',fps=24,size=(1280,720)).pic2video()