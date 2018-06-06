
import requests,re,os,json,threading,time

#  图片下载
def downloadPicture(url,name,type):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
    try:
        # 设置30秒timeout
        picture = requests.get(url=url, headers=headers, timeout=30)
        # 写入文件
        f = open(name + type, 'wb')
        f.write(picture.content)
        f.close()
    except:
        print('图片下载超时，正在下载下一张')

# 创建文件夹 用来存放图片
def makedir(dirname):
    if os.path.lexists(dirname):
        os.chdir(dirname)
    else:
        os.makedirs(dirname)
        os.chdir(dirname)

#         每秒打印线程数目
def pringThreadNumberEverySecond():
    while(threading.activeCount()>1):
        print(str(threading.activeCount()) + 'actived thread')
        time.sleep(1)


#通过获取json来得到picture地址并组成list返回
# 关键字 起始页 结束页
def getPictureList(keyword,startPage,endPage):
    start = int(startPage)*100
    pictureList = []
    if(startPage<=endPage):
        # limit用来限制获取到的图片数目 最大为100 start为开始页数
        url = 'https://www.duitang.com/napi/blog/list/by_search/?kw='+str(keyword)+'&start='+str(start)+'&limit=100'
        # startPage+=1
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36"}
        text = requests.get(url=url,headers=headers).text
        # print(text)
        # print(type(text))
        jsonobj = json.loads(text)
        # print(type(jsonobj))
        # print(jsonobj)
        data = jsonobj['data']
        # print(data)
        # print(type(data))
        object_list = data['object_list']
        # print(object_list)
        # print(type(object_list))
        for list0 in object_list:
            # print(list0)
            # list0 = object_list[i]
            # print(list0['photo'])
            photo = list0['photo']
            path = photo['path']
            # print(path)
            pictureList.append(path)
    return pictureList


# 下载堆糖网图片
def downloadDuitangPicture(keyword,startPage,endPage):
    # 创建文件夹
    makedir(keyword)
    for page in range(startPage,endPage):
        # 获取图片地址列表 100z张
        pictureList = getPictureList(keyword,startPage,endPage)
        # print(pictureList)
        # 用户输入第1页 传进来的参数为0 ，为了显示一致，将0加回1，使图片命名页数为1
        print('第'+str(page+1)+'页,获得图片数：'+str(len(pictureList)))
        for count in range(0,len(pictureList)):
            try:
                # 用户输入第1页 传进来的参数为0 ，为了显示一致，将0加回1，使图片命名页数为1
                name = str(keyword) + '_' + str(page+1) + '_' + str(count)
                type = '.jpg'
                # 多线程下载
                mythread = threading.Thread(target=downloadPicture, args=(pictureList[count], name, type))
                mythread.start()
                # 打印线程名 和线程数目
                print('thread name:' + str(mythread.name))
                print(str(threading.activeCount()) + 'actived thread')
                # 设置线程为64 当线程数目超过64时阻塞当前线程
                if(threading.activeCount()>=64):
                    mythread.join()
            except:
                print(print('当前（第' + str(count) + '）图片下载超时，正在下载下一张'))

if __name__ =='__main__':
    downloadDuitangPicture('设计',0,2)
    pringThreadNumberEverySecond()



