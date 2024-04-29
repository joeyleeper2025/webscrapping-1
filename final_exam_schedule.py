
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

url = 'https://registrar.web.baylor.edu/exams-grading/spring-2024-final-exam-schedule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

myclasses_file = open('class_schedule.csv', 'r')
myclasses = csv.reader(myclasses_file)

tables = soup.findAll('table')
finals_table = tables[1]  

rows = finals_table.findAll('tr')

for rec in myclasses:
    myclassday = rec[0]
    myclasstime = rec[1]

    for row in rows:
        td = row.findAll('td')
        if td:
            sch_class = td[0].text.strip('\n')
            sch_time = td[1].text.strip('\n')
            sch_exam_day = td[2].text.strip('\n')
            sch_exam_time = td[3].text.strip('\n')

            if sch_class == myclassday and sch_time == myclasstime:
                print(myclassday, myclasstime, sch_exam_day, sch_exam_time)

myclasses_file.close()
