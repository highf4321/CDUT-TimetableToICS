# CDUT_TimetableToICS
> 直接从教务处导入课程表到日历📆的工具。

### 实现情况

- [x] HTML 的解析（是由 Java 写的，有时间再用 Python 重写）

- [x] 读取课程名、地点、课程持续节数（是由 Java 写的，有时间再用 Python 重写）

- [x] 将 HTML 信息导入进 json 文件（是由 Java 写的，有时间再用 Python 重写）

- [x] Python 读取 json 并转换为 ics

- [ ] 直接登录教务处网站，自动下载 HTML

- [ ] 重课的处理（可能会花费大量时间）



---

#### 重课的处理办法

1. 从附表（td2）读取课程 ID（比如 计1R1），教师姓名，然后到教师课表获取这门课的信息，而非到学生课表获取。
    但是这样需要知道教师 ID
2. 从 teachID 入手。在浏览器登录账号后，打开这个网址：http://202.115.133.173:805/Classroom/ProductionSchedule/TeachClassScheduled.aspx?TeachID=189493，这个网址是某一个课程单独的表格，不会重课。但是，如何得到 TeachID 是个难点。也许可以参考一下 [CDUT 教务处选课 | GitHub](https://github.com/zaxtyson/CDUT_SelectCourse) 是如何得到 TeachID 的？



### 参考资料

-   [A parser for CDUT classes scheme | GitHub](https://github.com/MikeAure/SchemeParse)
- [能通过python向mac的日历添加事件么？ - 无情的复读机的回答 - 知乎](https://www.zhihu.com/question/53205679/answer/133915824)
- [Python iCalendar 包的官方使用文档](https://icalendar.readthedocs.io/en/latest/usage.html#overview)
- [CDUT 教务处选课 | GitHub](https://github.com/zaxtyson/CDUT_SelectCourse) 

