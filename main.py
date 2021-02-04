
# 接收者，也就是你的邮箱, 这里我写到list.yml里面去进行设置了
file = open('list.yml', encoding='utf-8')
reciver = file.readline().split(':')[1].replace('\n', '')
# reciver = '2892211452@qq.com'


from 农历生日计算与提醒判断 import 农历birthday

if __name__ == '__main__':

    # birthdayList = [
    #     ['12-25', 'test1']  #第一个是农历生日，第二个是名字
    # ]
    birthdayList = []



    lines =  file.readlines()

    for i in lines:
        i = i.split(':')
        birthdayList.append([i[0], i[1].replace('\n', '')])



    农历birthday.main(list=birthdayList)
