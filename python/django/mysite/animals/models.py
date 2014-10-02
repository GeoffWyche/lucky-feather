from django.db import models

class TreeNode(models.Model):
    node_text = models.CharField(max_length=200)
    is_animal = models.BooleanField(default=False)
    yes_link = models.ForeignKey('self',related_name='yes_ans',null=True)
    no_link = models.ForeignKey('self',related_name='no_ans',null=True)
    def __str__(self):
        return self.node_text

    def article(self):
        if len(self.node_text) < 1:
            return "a"
        elif self.node_text[0] in "aeiouAEIOU":
            return "an"
        else:
            return "a"

# retrieve starting node
#(because the start node was the first one added to the db...)
# x = TreeNode.objects.filter(id__exact='1')
