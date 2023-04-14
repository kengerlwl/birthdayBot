import yaml
import os
from datetime import date
from borax.calendars.lunardate import LunarDate
from borax.calendars.birthday import actual_age_lunar
from src.SendMail import SendMail
from config import *




def getMessage(Distance, DistanceConfig, name, Age, calendar, BirthDay, BirthMonth, BirthYear):
    message = None
    if DistanceConfig > 3:
        print("Distance error Need between 0 and 3 !")
        exit()
    if Distance <= DistanceConfig:
        if Distance == 0:
            message = "今天"
        elif Distance == 1:
            message = "明天"
        elif Distance == 2:
            message = "后天"
        elif Distance == 3:
            message = "大后天"
        else:
            return message
    else:
        return message
    template = getTemplate()
    if BirthYear == "0000":
        if calendar == "lunar":
            message = message + template["MessageTmp"].format(name, BirthMonth + "月" + BirthDay + "日", "阴历")
        elif calendar == "solar":
            message = message + template["MessageTmp"].format(name, BirthMonth + "月" + BirthDay + "日", "阳历")
    else:
        if calendar == "lunar":
            message = message + template["HaveAgeMessageTmp"].format(name, str(Age),
                                                                     str(
                                                                         BirthYear) + "年" + BirthMonth + "月" + BirthDay + "日",
                                                                     "阴历")
        elif calendar == "solar":
            message = message + template["HaveAgeMessageTmp"].format(name, str(Age),
                                                                     str(
                                                                         BirthYear) + "年" + BirthMonth + "月" + BirthDay + "日",
                                                                     "阳历")
    return message


class Calendar:
    def __init__(self):
        self.people = getPeople()
        self.message = None
        self.title = None
        self.Run()

    def Run(self):
        for friend in self.people:
            if friend["Calendar"] == "solar":
                self.SolarCalendar(friend)
            elif friend["Calendar"] == "lunar":
                self.LunarCalendar(friend)
            else:
                print("Calendar format error,  Need solar or lunar!")
                exit()
            if self.message is not None:
                print(self.message)
                self.title = self.message.split('，')[0]
                SendMail(self.title, self.message)
            else:
                continue

    def SolarCalendar(self, friend):
        today = date.today()
        try:
            BirthYear, BirthMonth, BirthDay = friend["Day"].split('-')
        except:
            print("Day format error,  Need yyyy-MM-dd!")
            exit()
        if BirthYear != "0000":
            Age = today.year - int(BirthYear)
        else:
            Age = None
        try:
            BirthNow = date(today.year, int(BirthMonth), int(BirthDay))  # 今年的生日日期
            if BirthNow < today:
                BirthNow = date(today.year + 1, int(BirthMonth), int(BirthDay))  # 明年的生日日期
        except:
            print("Day error,  Maybe not this day!")
            return
        Distance = BirthNow - today
        Distance = Distance.days
        self.message = getMessage(Distance, friend["DistanceConfig"], friend["Name"], Age, friend["Calendar"],
                                  BirthDay,
                                  BirthMonth,
                                  BirthYear)

    def LunarCalendar(self, friend):
        today = LunarDate.today()
        try:
            BirthYear, BirthMonth, BirthDay = friend["Day"].split('-')
        except:
            print("Day format error,  Need yyyy-MM-dd!")
            exit()
        if BirthYear != "0000":
            Age = today.year - int(BirthYear)
        else:
            Age = None
        try:
            BirthNow = LunarDate(today.year, int(BirthMonth), int(BirthDay))  # 今年的生日日期
            if BirthNow < today:
                BirthNow = LunarDate(today.year + 1, int(BirthMonth), int(BirthDay))  # 明年的生日日期
        except:
            print("Day error,  Maybe not this day!")
            return
        Distance = BirthNow - today
        Distance = Distance.days
        self.message = getMessage(Distance, friend["DistanceConfig"], friend["Name"], Age, friend["Calendar"],
                                  BirthDay,
                                  BirthMonth,
                                  BirthYear)


if __name__ == "__main__":
    Calendar()
