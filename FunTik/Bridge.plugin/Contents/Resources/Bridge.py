#!/usr/bin/env python3
#coding:utf-8

#import requests
#import json
#import re
#import time
#import datetime

import sys
import objc
from Foundation import NSObject

# description = '''usage:
#
# This is the tool for generate the average work hours
# Run it like this:
#     python spider.py username passwd starttime(format:2018.3.1)  endtime[option]'''
#
# parser = argparse.ArgumentParser(description)
# parser.add_argument('username')
# parser.add_argument('passwd')
# parser.add_argument('starttime')
# parser.add_argument('endtime', nargs='?', default=localtime)
# args=parser.parse_args()
#

# Load the protocol from Objective-C
BridgeInterface = objc.protocolNamed("FunTik.BridgeInterface")

#localtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

class Bridge(NSObject, protocols=[BridgeInterface]):
    @classmethod
    def createInstance(self):
        return Bridge.alloc().init()

    def getPythonInformation(self):
        return sys.version

#class Attendance:
#    def __init__(self):
#        self.loginUrl = 'http://kaoqin.funshion.com/'
#        self.timeFilterUrl = 'http://kaoqin.funshion.com/Staff/EmpRegisterData/SetCardDetailFilter'
#        self.refreshRecordUrl = "http://kaoqin.funshion.com/Staff/EmpRegisterData/RefreshRecordDetail"
#        self.session = requests.Session()
#
#    def login(self, username, passwd):
#        data = {
#            'loginName': username,
#            'password': passwd,
#            'isRemember': 'undefined'
#        }
#        headers = {
#            'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
#        }
#
#        result = self.session.post(self.loginUrl, data=data, headers=headers)
#        return result.text
#
#    def get_card_detail_data(self, starttime, endtime):
#        data = {'Date': starttime + ' - ' + endtime}
#
#        result = self.session.post(self.timeFilterUrl, data=data)
#
#        _dict = json.loads(result.text.replace("'", '"'))
#        #print (_dict)
#        if _dict['issuccess']:
#            data_list = []
#            while True:
#                data['PageIndex'] = data.get('PageIndex', 0) + 1
#                result = self.session.post(self.refreshRecordUrl, data=data)
#                print(data['PageIndex'])
#                if re.compile("无数据").findall(result.text):
#                    break
#                tmp_list = re.compile("\d+-\d+-\d+\s\d+:\d+:\d+").findall(result.text)
#                data_list.extend(tmp_list)
#                if starttime is endtime:
#                    break
#        return data_list
#
#    def get_card_detail(self, starttime, endtime):
#        data_list = self.get_card_detail_data(starttime, endtime)
#        day_list, hour_list = parse_data(data_list)
#        return day_list, hour_list
#
#    def get_username(self):
#        return "陈海"
#
#    def get_today_hours(self):
#        time_in = 0
#        data_list = self.get_card_detail_data(localtime, localtime)
#        if len(data_list):
#            time_in = time.mktime(time.strptime(data_list[0], '%Y-%m-%d %H:%M:%S'))
#            time_current = time.mktime(time.localtime(time.time()))
#            hours = time_current - time_in
#            #print(round(hours/3600 - 1, 2))
#            #del 1 for 12:00-13:00
#            return round(hours/3600, 2)
#        else:
#            return 'no data'
#
#    def get_week_hours(self):
#        week_day = datetime.datetime.strptime(localtime, '%Y-%m-%d').strftime("%w")
#        if week_day:
#            start_time = datetime.datetime.now() - datetime.timedelta(days=int(week_day))
#            day_list, hour_list = self.get_card_detail(str(start_time).split(" ")[0], localtime)
#
#        return round(sum(hour_list), 2)
#
#
#def calc_average_hours():
#    return
#
#
#def calc_total_hours():
#    return
#
#
#def calc_current_hours():
#    return
#
#
#def parse_data(data_list):
#    day_list = []
#    hour_list = []
#    time_in = 0
#    time_out = 0
#
#    for i in data_list:
#        day_list.append(i.split(" ")[0])
#    day_list = sorted(list(set(day_list)))
#
#   # time_list.append(time.strptime(i, '%Y-%m-%d %H:%M:%S'))
#
#    for i in day_list:
#        for idx,item in enumerate(data_list):
#            if item.split(" ")[0] == i and i is not localtime:
#                if time_in == 0 :
#                    time_in = time.mktime(time.strptime(item, '%Y-%m-%d %H:%M:%S'))
#                else:
#                    time_out = time.mktime(time.strptime(item, '%Y-%m-%d %H:%M:%S'))
#
#            if idx+1< len(data_list) and (i == data_list[idx+1].split(" ")[0]):
#                continue
#            if time_out:
#                hour = time_out - time_in
#                time_in = 0
#                time_out = 0
#                if hour:
#                    hour_list.append(round(hour/3600 - 1, 2))
#
#    if len(day_list) - len(hour_list) == 1:
#        hour_list.append(0)
#    return day_list, hour_list
#
#
## def create_chart(day_list, hour_list):
##     page = Page()
##
##     days = time.mktime(time.strptime(day_list[-1], '%Y-%m-%d')) - time.mktime(time.strptime(day_list[0], '%Y-%m-%d'))
##     weeks = int(days/3600/24/7)+1
##     for i in range(0, weeks):
##         week_day = datetime.datetime.strptime(day_list[i*7], '%Y-%m-%d').strftime("%w")
##         week = datetime.datetime.strptime(day_list[i*7], '%Y-%m-%d').strftime("%W")
##         bar = Bar()
##         for j in range(0, 7):
##             if j < int(week_day):
##                 day_list.insert(i*7, '0')
##                 hour_list.insert(i*7, '0')
##             elif j == int(week_day):
##                 pass
##             else:
##                 if len(day_list) > i*7+j and week != datetime.datetime.strptime(day_list[i*7+j], '%Y-%m-%d').strftime("%W"):
##                     day_list.insert(i*7+j, '0')
##                     hour_list.insert(i*7+j, '0')
##
##         if len(day_list) > 7*(i+1)-1:
##             x_axis = day_list[i*7 : 7*(i+1)-1]
##             y_axis = hour_list[i*7 : 7*(i+1)-1]
##         else:
##             x_axis = day_list[i*7:]
##             y_axis = hour_list[i*7:]
##
##         bar.add(str(week) + "周", x_axis, y_axis)
##         page.add_chart(bar)
##
##     page.render()
#
## def main(argv):
##
##     print("the argv is username=%s , passwd=%s , starttime=%s , endtime=%s" % (args.username, args.passwd, args.starttime, args.endtime))
##     spider = Attendance()
##
##     ret = spider.login(args.username, args.passwd)
##     print("login ret = %s" % (ret,))
##     if ret == '-2':
##         print('error password')
##     elif ret == '-1':
##         print('error username')
##     elif ret == '-7':
##         print('Account has been logged in!')
##     elif ret == '1':
##         print('login OK!')
##         day_list, hour_list = spider.get_card_detail(args.starttime, args.endtime);
##
##     create_chart(day_list, hour_list)
##
##     exit(0)
##
##
## if __name__ == '__main__':
##     main(sys.argv[1:])
