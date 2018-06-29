import jieba

class talk:
    def __init__(self, text):
        self.istalk = False
        self.singer = ""
        self.determineIstalk(text)
    def determineIstalk(self,INtext):
        seg_list = jieba.cut(text, cut_all=True)
        for seg in seg_list:
            if seg == '聽' or '看' or '找' or '要':
                self.istalk = True
                self.singer = INtext[INtext.find(seg):]
