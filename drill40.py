class poem(object):

    def __init__(self):  
        self.poems = ["牛渚西江夜", "青天无片云",   
             "登舟望秋月", "空忆谢将军",
             "余亦能高咏", "斯人不可闻",
             "明朝挂帆去", "枫叶落纷纷"]
    
    def poem_prt(self):  # 必须要有self
        for line in self.poems: # 这里也必须是self.poems
            print(line)

thing = poem()

thing.poem_prt() # 引用function
