from pdfHandle.downloadPdf import downloadPdf
from readPdf import getPdfContent
from fileOpeate import writeContent,getList

"""
库需求：
    requests:网络请求
    pdfplumber:读取pdf数据
    
文件解析
用户层：
    ans.csv:结果保存位置
    cachePdf.pdf:pdf临时存储文件
    url.txt:把所有url输入进去就行了
代码层：
    dowloadPdf.py:从网页上下载pdf，如果要设置爬取等待，在这里面设置
    fileOperate.py:所有文件相关操作
    main.py:主逻辑
    readPdf.py:从pdf中读取数据
    
容错：提示框会报错，同时ans.csv中数据为erro
"""


if __name__ == '__main__':
    urlList = getList()

    index = 1
    n= len(urlList)
    for url in urlList:
        # 提示信息
        erroInf = '获取({}/{})失败\n'.format(str(index), str(n))
        successInf = '成功获取({}/{})\n'.format(str(index),str(n))

        # 正在下载提示
        print('正在下载({}/{})...'.format(str(index), str(n)))

        # 容错，如果失败则计erro
        try:
            # 下载pdf，保存到cachepdf.pdf中
            downloadPdf(url)

            # 从cachepdf.pdf中读取
            content = getPdfContent('cachepdf.pdf')
        except:
            # 错误信息写入
            writeContent(index,'erro')

            # 打印错误信息
            print(erroInf)
        else:
            # 写入文件ans.csv
            writeContent(index,content)

            # 下载成功提示
            print(successInf)

        # 编号+1
        index+=1
