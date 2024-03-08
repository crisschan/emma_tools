#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   try_audio.py
@Time    :   2023/01/16 10:03:00
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   合并音频文件
'''

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import concatenate_audioclips


class MergeAudio(object):
    def __init__(self,audio_list,output_audio='final_audio.mp3') -> None:
        '''
        @des  :构造函数
               
        @params  :audio_list,存储音频文件绝对地址的列表
                  output_audio,默认值为final_audio.mp3的输出文件

        @return  :none
                  
        '''
        
        
        self.audio_list = audio_list
        self.output_audio = output_audio
        pass
    def merge(self):
        '''
        @des  :合并音频文件
               
        @params  :audio_list,存储音频文件绝对地址的列表
        
        @return  :none

        '''
        
        # 合并音频文件
        audio_clip_list =[]
        for i in range(len(self.audio_list)):
            audio_clip = AudioFileClip(self.audio_list[i])
            audio_clip_list.append(audio_clip)
        final_clip = concatenate_audioclips(audio_clip_list)
        final_clip.write_audiofile(self.output_audio)
 

if __name__ == '__main__':
    alist = ['1.flac','2.flac','3.flac','4.flac','5.flac']
    merge_audio = MergeAudio(alist)
    merge_audio.merge()