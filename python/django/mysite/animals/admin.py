from django.contrib import admin
from animals.models import TreeNode

# Register your models here.

class TreeNodeAdmin(admin.ModelAdmin):
    fields = ['node_text','is_animal','yes_link','no_link']

admin.site.register(TreeNode,TreeNodeAdmin)
