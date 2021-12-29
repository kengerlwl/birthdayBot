# borax==3.3.1
import copy

from borax.calendars.lunardate import LunarDate
from 农历生日计算与提醒判断 import facade


def main(list):
    # list = [
    #     ['12-25', 'test1']  #第一个是农历生日，第二个是名字
    # ]

    # 获取今天的农历日期
    today = LunarDate.today()

    year = today.year
    month = today.month
    day = today.day

    for i, name in list:

        i = i.split('-')
        tmpMonth = int(i[0])
        tmpDay = int(i[1])
        tmpNow = LunarDate(year, tmpMonth, tmpDay)  # 今年的生日日期
        if tmpNow < today:
            tmpNow = LunarDate(year+1, tmpMonth, tmpDay)  # 今年的生日日期
        # print(tmpNow)
        dis = today - tmpNow
        dis = dis.days



        message = None
        if  dis == 0:
            message = '今天'
        elif dis == -1:
            message = '明天'
        elif dis == -2:
            message = '后天'
        elif dis == -3:
            message = '大后天'

        # print(message, dis)

        # 若在范围内
        if message:
            # 转化为公历
            solarDay = tmpNow.to_solar_date()
            try:
                message= message + '是' + name + '的生日' +'  具体日期是: '+ str(solarDay)
                facade.update(message, flag= True)
            except:
                pass


        else:
            facade.update(message=name+ '的生日 今天不需要通知')



if __name__ == '__main__':
    list = [
        ['1-1', 'test1']  #第一个是农历生日，第二个是名字
    ]
    main(list)
