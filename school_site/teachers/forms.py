from django import forms
from teachers.models import subjects, teachers

class subjects_add(forms.ModelForm):
    subject_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть назву предмету"
    }))

    class Meta:
        model = subjects
        fields = ("subject_name",)


class teacher_add(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть ім'я вчителя"
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть прізвище вчителя"
    }))
    by_father = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть по батькові вчителя"
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть вік вчителя"
    }))
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть роки досвіду вчителя"
    }))
    subject = forms.ModelMultipleChoiceField(
        queryset=subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    education =  forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть освіту вчителя"
    }))
    image = forms.ImageField(required=False)

    class Meta:
        model = teachers
        fields = ("name","second_name","by_father","age","experience","subject", "education", "image")
