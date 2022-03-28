# 库需求
    requests:网络请求
    pdfplumber:读取pdf数据
    
# 文件解析
## 用户层：
    ans.csv:结果保存位置
    cachePdf.pdf:pdf临时存储文件
    url.txt:把所有url输入进去就行了
## 代码层：
    dowloadPdf.py:从网页上下载pdf，如果要设置爬取等待，在这里面设置
    fileOperate.py:所有文件相关操作
    main.py:主逻辑
    readPdf.py:从pdf中读取数据
    
# 容错
提示框会报错，同时ans.csv中数据为erro
