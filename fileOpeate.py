def writeContent(index,content):
    index = str(index)
    # 删除换行
    content = content.replace('\n','')

    # 删除空格
    content = content.replace(' ', '')+'\n'

    with open('ans.csv','a+') as wfile:
        wfile.write('{},{}'.format(index,content))

def getList():
    urlList = []
    with open('url.txt','r') as rfile:
        urlList = rfile.read().split('\n')

    return urlList