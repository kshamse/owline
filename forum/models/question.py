from django.db import models
from .base_post import BasePost


class Question(BasePost):
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE,
    #                                related_name='created_posts')
    # created_on = models.DateTimeField(auto_now_add=True)
    # modifed_by = models.ForeignKey(User, on_delete=models.CASCADE,
    #                                related_name='modified_posts')
    # modified_on = models.DateTimeField(auto_now=True)
    # body = models.TextField()
    # archive = models.BooleanField(default=False)
    # votes = models.IntegerField()
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title