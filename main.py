import download
print('堆糖网图片下载:\n1.64线程下载，速度快\n2.虽然不能保证百分百每页下载100张但是可以保证90%以上\n')
print('每页包含100张图片,区间[起始页，结束页），例如【1,2）只下载第一页，共100张')
keyword = input('输入查询关键字：')
statPage = input('输入起始页：')
endPage = input('输入结束页：')
download.downloadDuitangPicture(str(keyword), int(statPage)-1, int(endPage)-1)
download.pringThreadNumberEverySecond()