import pandas as pd
import time
import logging
from googleapiclient.discovery import build
from dbms.models.api_models import YoutubeKeword
from dbms.common.common_func import save_data
from dbms.common import config

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class YoutubeApi:
    
    def __init__(self,api_key):        
        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def video_search_list(self,query,max_results=10):
        search_response = self.youtube_api.search().list(
        q=query,
        part='id,snippet',
        maxResults=10
        ).execute()

        video_ids = []
        for item in search_response.get("items", []):
            if item["id"]["kind"] == "youtube#video":
                video_ids.append(item["id"]["videoId"])
        return ",".join(video_ids)

    def video(self,video_ids):
        videos_list_response = self.youtube_api.videos().list(
            id=video_ids,
            part='snippet,statistics'
        ).execute()

        r = []
        for item in videos_list_response.get("items",[]):
            # print(item)
            r.append({"video_id":item['id'], "title":item["snippet"]["title"],
                    "channelTitle":item["snippet"]["channelTitle"],
                    "commentCount":item["statistics"]["commentCount"]})
        return r

    def comment(self, keyword, video_id, max_cnt=10):
        comment_list_response = self.youtube_api.commentThreads().list(
            videoId=video_id,
            part='id,replies,snippet',
            maxResults=max_cnt

        ).execute()

        strd_dt = time.strftime(('%Y%m%d'))
        ins_dt = time.strftime(('%Y%m%d%H%M%S'))


        comments = []
        for comment in comment_list_response.get("items", []):
            
            snippet = comment['snippet']['topLevelComment']['snippet']
            
            map = {"strd_dt":strd_dt, "keword":keyword, "link": f"https://www.youtube.com/watch?v={snippet['videoId']}", "video_id": snippet["videoId"],
                "main_text": snippet['textOriginal'][:10], "comment_author": snippet['authorDisplayName'], "ins_dt":ins_dt}
            comments.append(map)
            
        return comments

    # 미사용
    def save_to_excel(self, search_results, filename):        
        df = pd.DataFrame(search_results)
        df.to_excel(filename)

    def crawl_comment_by_keyword(self, keyword, video_cnt=5):        
        video_ids = self.video_search_list(keyword, video_cnt)
        r_video = self.video(video_ids)
        l = []
        for video in r_video:
            cnt = int(video['commentCount'])
            if cnt > 100:
                cnt = 100
            comment_list = self.comment(keyword, video['video_id'], cnt)
            l += comment_list
        return l

    def run_crawl_google_youtube_comment(self,searchKeyword):
        
        logger.info('--05 [run_crawl_google_youtube_comment] Start !!')         
        
        DEVELOPER_KEY = config.DEVELOPER_KEY
        # search_keyword = "19인치노트북"        
        search_keyword = searchKeyword
        api = YoutubeApi(DEVELOPER_KEY)

        df_dic = api.crawl_comment_by_keyword(search_keyword,10)
        
        save_data(df_dic, YoutubeKeword)
        
        logger.info('--05 [run_crawl_google_youtube_comment] End !!')
        print('\n\n')    
