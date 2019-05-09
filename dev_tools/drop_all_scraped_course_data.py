from QCumber.scraper.assets.models import *

# to run this >>> python manage.py shell < dev_tools/drop_all_scraped_course_data.py
# will flush all qcumber-scraped-courses info but not drop the tables.

Course.objects.all().delete()
CourseDetail.objects.all().delete()
AcademicGroupPossibleValues.objects.all().delete()
AcademicOrganizationPossibleValues.objects.all().delete()
CampusPossibleValues.objects.all().delete()
CareerPossibleValues.objects.all().delete()
Components.objects.all().delete()
CourseDescription.objects.all().delete()
EnrollmentInformation.objects.all().delete()
GradingPossibleValues.objects.all().delete()
SubjectPossibleValues.objects.all().delete()

# Log model

# Log.objects.all().delete()
