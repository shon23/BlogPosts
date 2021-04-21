from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['username'].label = "Foydalanuvchining ismi"
    #     self.fields['password1'].label = "Parol"
    #     self.fields['password2'].label = "Parolni tasdiqlash"
    #
    #     # Help text for helping users to enter required data
    #
    #     self.fields['username'].help_text = "Talablar. Maksimal 150ta harf yoki undan kamroq. Harflar, raqamlar va " \
    #                                         "@/./+/-/_ faqat. "
    #     self.fields['email'].help_text = "Shaxsiy emailingizni kiriting."
    #     self.fields['password1'].help_text = "Parolingiz boshqa shaxsiy ma'lumotlaringizga juda o'xshash bo'lishi " \
    #                                          "mumkin emas. "
    #
    #     self.fields['password1'].help_text = """<ul><li>Parolingiz boshqa shaxsiy ma'lumotlaringizga juda o'xshash bo'lishi mumkin emas.</li>
    #                             <li>Parolingiz kamida 8 ta belgidan iborat bo'lishi kerak.</li>
    #                             <li>Parolingiz odatda ishlatiladigan parol bo'lishi mumkin emas.</li>
    #                             <li>Parolingiz to'liq raqamli bo'lishi mumkin emas.</li>
    #                         </ul>"""
    #     self.fields['password2'].help_text = "Tasdiqlash uchun avvalgidek parolni kiriting"

    """
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        if User.objects.filter(username=username):
            raise forms.ValidationError(f"{username} allaqachon ro'yhatdan o'tgan!")
        if User.objects.filter(email=email):
            raise forms.ValidationError(f"{email} allaqachon ro'yhatdan o'tgan!")
        return self.cleaned_data
    """


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']