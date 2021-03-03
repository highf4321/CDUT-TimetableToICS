import json
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
from uuid import uuid1
import pytz


def main():
    json2ics()


def json2ics():
    # Calendar 对象
    cal = Calendar()
    cal['version'] = '2.0'
    # *mandatory elements* where the prodid can be changed, see RFC 5445
    cal['prodid'] = '-//CDUT//TimeTable//CN'
    

    firstDay = datetime(2021, 3, 1, tzinfo=pytz.timezone("Asia/Shanghai")) - timedelta(days=1)  # 开学第一周星期一的时间

    lessonTime = {1: timedelta(hours=8, minutes=10), 2: timedelta(hours=9, minutes=45),
                  3: timedelta(hours=10, minutes=15),
                  4: timedelta(hours=11, minutes=50), 6: timedelta(hours=14, minutes=30),
                  7: timedelta(hours=16, minutes=5), 8: timedelta(hours=16, minutes=25),
                  9: timedelta(hours=18, minutes=0),
                  10: timedelta(hours=19, minutes=10), 11: timedelta(hours=20, minutes=45),
                  12: timedelta(hours=21, minutes=35)}

    # 打开 JSON 文件
    with open("./classInfo.json", "r") as f:
        classList = json.load(f)
        print(type(classList))
        for item in classList:
            event = Event()
            event['uid'] = str(uuid1())

            description = "教师：" + item['teacherName'] + \
                "  " + "学时：" + item['学时'] + "  学分：" + item['学分']
            event.add('summary', item['课程名称'])
            event.add('description', description)
            event.add('location', item['地点'])

            # 时间
            event.add('tzid', 'Asia/Shanghai')
            startDateTime = firstDay + \
                timedelta(days=item['累计开学天数']) + \
                lessonTime[item['begin']]
            endDateTime = firstDay + \
                timedelta(days=item['累计开学天数']) + \
                lessonTime[item['end']]

            event.add('dtstart', startDateTime)
            event.add('dtend', endDateTime)

            # 在 上课前 30 分钟前发出通知
            alarm = Alarm()
            alarm.add('action', 'DISPLAY')
            alarm.add('description', '上课前 30 分钟通知')
            alarm.add('trigger', timedelta(minutes=-30))
            event.add_component(alarm)

            # 将 Event 添加到 Calendar
            cal.add_component(event)

    with open(file="./TimeTable.ics", mode="w", encoding="UTF-8") as icsFile:
        icsFile.write(display(cal))


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\,', ',').strip()


if __name__ == '__main__':
    main()
