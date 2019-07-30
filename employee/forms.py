from .models import Post
from employee.models import Employee,Document
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Title New'
        }
        help_texts = {
            'title': 'Yardum edelum'
        }
        error_messages = {
            'title': {
                'max_length': 'cok uzun baba'
            }
        }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = 'required'
        self.fields['title'].error_messages = {
            'max_length': 10,
            'required': 5
        }
        for field in self.fields.values():
            field.error_messages = {
                'required': '{} field is required.'.format(field.label)
            }


SOME_CHOICES = (
    ('db-value', 'Display Value'),
    ('db-value2', 'Display Value2'),
)
INT_CHOICES = [tuple([x, x]) for x in range(0, 100)]
YEARS = [x for x in range(1980, 2031)]


class SearchForm(forms.Form):
    q = forms.CharField(label='Text', widget=forms.Textarea(attrs={'rows': 4, 'cols': 10}))
    IntegerField = forms.IntegerField(widget=forms.Select(choices=INT_CHOICES))
    EmailField = forms.EmailField()
    DateField = forms.DateField(
        initial='2010-01-10', widget=forms.SelectDateWidget(years=YEARS))

    def clean_q(self, *args, **kwargs):
        q = self.cleaned_data.get('q')
        if q == 'vishal':
            raise forms.ValidationError('You cant search')
        return q

    def clean_IntegerField(self, *args, **kwargs):
        IntegerField = self.cleaned_data.get('IntegerField')
        if IntegerField < 10:
            raise forms.ValidationError('The integer must be greater than 10')
        return IntegerField
