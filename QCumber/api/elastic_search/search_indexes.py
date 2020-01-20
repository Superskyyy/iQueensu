from haystack import indexes

from QCumber.scraper.assets.models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="course.txt")
    number = indexes.CharField(model_attr="number")
    name = indexes.CharField(model_attr="name")

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
