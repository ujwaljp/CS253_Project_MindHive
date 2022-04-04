from django.db import models
from home.models import Content

# Answer model inherits from Content model and adds a field for the target quesion
# on_delete=models.CASCADE means that if the question is deleted, the answer is deleted as well
class Answer(Content):
    to_question = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE)

    def get_votes(self):
        return self.likedBy.count() - self.dislikedBy.count()