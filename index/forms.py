from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.models import User
from .models import Cita, Doctor

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=12)
    correo = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')

        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data

    def save(self):
        usuario = User.objects.create_user(
            username=self.cleaned_data['correo'],
            email=self.cleaned_data['correo'],
            password=self.cleaned_data['contraseña'],
            first_name=self.cleaned_data['nombre']
        )
        # Otros campos del modelo de usuario si los hay
        usuario.save()

class LoginForm(forms.Form):
    correo = forms.EmailField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput)

    fields = ['correo', 'contraseña']

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get('correo')
        contraseña = cleaned_data.get('contraseña')

        if correo and contraseña:
            pass

        return cleaned_data
    

class CitaForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    especialidad = forms.ChoiceField(choices=Doctor.ESPECIALIDADES)

    class Meta:
        model = Cita
        fields = ('doctor', 'fecha', 'hora', 'especialidad')


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('doctor', 'fecha', 'hora')
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
