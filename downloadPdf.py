import requests as r


def downloadPdf(url):
    # 此处设置等待时间
    # time.sleep(1)
    html = r.get(url)
    with open('cachePdf.pdf','wb') as wfile:
        wfile.write(html.content)
