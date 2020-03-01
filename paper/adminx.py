import xadmin

from paper.models import Paper


# Register your models here.
class PaperAdmin(object):
    list_display = ['id', 'name', 'score', 'choice_number', 'fill_number', 'judge_number', 'program_number', 'level']
    list_filter = ['level']
    search_fields = ['id', 'name']
    list_per_page = 10
    list_editable = ['name']


xadmin.site.register(Paper, PaperAdmin)