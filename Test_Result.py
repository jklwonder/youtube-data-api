# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:45:31 2019

@author: klwonder
"""
import datetime
def main():
    from youtube_api import YouTubeDataAPI
    
    api_key = "AIzaSyAB5Dg1HeqzlV6y2d37-tektKrts2bNOSc"
    yt = YouTubeDataAPI(api_key)
    
    zout=yt.get_video_metadata(video_id='k7DGeWlKu0Q')
    Num_likes=zout['video_like_count']
    Num_dislikes=zout['video_dislike_count']
    Num_comments=zout['video_comment_count']
    zcomment=yt.get_video_comments(video_id='k7DGeWlKu0Q')
    Commentlist=[]
    for item in zcomment:
        Commentlist.append(item['text'])
    zcaption=yt.get_captions(video_id='k7DGeWlKu0Q')
    Transcript=zcaption['caption']
    Result1={'Num_likes':Num_likes,
            'Num_dislikes':Num_dislikes,
            'Num_comments':Num_comments,
            'Transcript':Transcript,
            'Commentlist':Commentlist}
    Result2=yt.search(q='vaccine',published_after=datetime.datetime(2018,1,1),
                      published_before=datetime.datetime(2019,1,1))
    return Result1,Result2

if __name__ == "__main__":
    Task1_Result,Task2_Result=main()
    