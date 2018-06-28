''' 使用說明
song = youtube()
song_data = song.search("周杰倫")

for i in range(0, 5):
    print(song_data[0][i] + ",\n" + song_data[1][i] + '\n\n')
'''

from bs4 import BeautifulSoup
import requests

class youtube:
    def __init__(self):
        self.redata = []        
        self.redata.append(["", "", "", "", ""]) #data[0][] 影片名
        self.redata.append(["", "", "", "", ""]) #data[1][] 影片 url
        
    def search(self, text): 
        search_query = text
        url = "https://www.youtube.com/results?search_query=" + search_query
        req = requests.get(url)
        content = req.content
        soup = BeautifulSoup(content, "html.parser")    

        out_times = 0

        for all_mv in soup.select(".yt-lockup-video"):      
            # 抓取 Title & Link
            data = all_mv.select("a[rel='spf-prefetch']")
            if len(data[0].get("href")) < 150:
                self.redata[0][out_times] = ("{}".format(data[0].get("title"))) # 影片名
                self.redata[1][out_times] = ("https://www.youtube.com{}".format(data[0].get("href"))) # 網址
                out_times += 1
                if out_times == 5:
                    break
        return self.redata




