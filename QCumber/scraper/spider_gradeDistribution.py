import requests
from bs4 import BeautifulSoup
from QCumber.scraper.assets.models import (
    GradeDistribution
)

class Spider_grade:
    def __init__(self):

        ######for testing flush db before doing

        def flush_db():
            GradeDistribution.objects.all().delete()
        flush_db()

    @staticmethod
    def get_web(currenturl):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
            res = requests.get(currenturl, headers=headers)
            res.raise_for_status()
            return res.content
        except requests.RequestException as e:
            print(e)
            return e

    @staticmethod
    def get_para(url):
        text = Spider_grade().get_web(url)
        soup = BeautifulSoup(text, 'html.parser')
        para_list = soup.find_all("td")

        stmp = []
        res = []
        i = 0
        for stc in para_list:
            if i == 17:
                i = 0
                res.append(stmp)
                stmp = []

            stmp.append(stc.get_text())
            i += 1
        return res

    @staticmethod
    def save_dict(content):
        grade = {}
        for ele in content:
            grade['course_name'] = ele[0]
            grade['description'] = ele[1]
            grade['enrollment_num'] = ele[2]
            grade['A+'] = ele[3]
            grade['A'] = ele[4]
            grade['A-'] = ele[5]
            grade['B+'] = ele[6]
            grade['B'] = ele[7]
            grade['B-'] = ele[8]
            grade['C+'] = ele[9]
            grade['C'] = ele[10]
            grade['C-'] = ele[11]
            grade['D+'] = ele[12]
            grade['D'] = ele[13]
            grade['D-'] = ele[14]
            grade['F'] = ele[15]
            grade['GPA'] = ele[16]
            gradeDistribution = GradeDistribution.objects.create(
                name=grade['course_name'], data=grade
            )
            gradeDistribution.save()

    @staticmethod
    def main():
        url = "http://www.qubirdhunter.com/?page_id=283#"
        content = Spider_grade().get_para(url)
        print(content)
        Spider_grade().save_dict(content)

if __name__ == "__main__":
    a = Spider_grade()
    a.main()
