from .models import InfoPage
from django import forms
from tinymce.widgets import TinyMCE
from hvad.admin import TranslatableAdmin
from hvad.forms import TranslatableModelForm

class InfoPageFrom(TranslatableModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 200, 'rows': 30}))
    
    class Meta:
        model = InfoPage
        fields = ('page', 'title', 'text')


class AdminInfoPage(TranslatableAdmin):
    list_display = ('page', 'all_translations')
    form = InfoPageFrom

    class Media:
        js = ('/static/tinymce/tiny_mce_src.js', '/static/tiny_mce/tiny_mce.js')
        css = {'all': ('/static/css/tinymce-studio-content.css', '/static/css/tinymce-studio-content-fonts.css')}

admin.site.register(InfoPage, AdminInfoPage)

