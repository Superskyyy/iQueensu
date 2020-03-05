"""scrape grade distribution on qubirdhunter"""
import requests
from bs4 import BeautifulSoup
from QCumber.scraper.assets.models import GradeDistribution


class SpiderGrade:
    """scrape grade distribution on qubirdhunter"""

    def __init__(self):

        """init function implements flush_db every time"""

        def flush_db():
            """clean previous outcome"""
            GradeDistribution.objects.all().delete()

        flush_db()

    @staticmethod
    def get_web(currenturl):
        """request web"""

        try:
            # pretend to be a browser header
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
            res = requests.get(currenturl, headers=headers)
            res.raise_for_status()
            return res.content
        except requests.RequestException as exception:
            print(exception)
            return exception

    @staticmethod
    def get_para(url):
        """use beautifulsoup to extract the table"""
        text = SpiderGrade().get_web(url)
        soup = BeautifulSoup(text, 'html.parser')
        para_list = soup.find_all("td")

        stmp = []
        res = []
        oneline = 0
        for stc in para_list:
            if oneline == 17:
                oneline = 0
                res.append(stmp)
                stmp = []

            stmp.append(stc.get_text())
            oneline += 1
        return res

    @staticmethod
    def save_dict(content):
        """save data as dictionary"""
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
            grade_distribution = GradeDistribution.objects.create(
                name=grade['course_name'], data=grade
            )
            grade_distribution.save()

    @staticmethod
    def main():
        """main function"""
        url = "http://www.qubirdhunter.com/?page_id=283#"
        content = SpiderGrade().get_para(url)
        print(content)
        SpiderGrade().save_dict(content)


if __name__ == "__main__":
    a = SpiderGrade()
    a.main()
