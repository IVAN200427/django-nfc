
from django import forms
from .models import QuoteInquiry
from .models import ContactMessage


class QuoteInquiryForm(forms.ModelForm):

    class Meta:
        model = QuoteInquiry

        fields = [
            'customer_name',
            'company_name',
            'email',
            'phone_number',
            'message',
        ]

widgets = {

    'customer_name': forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
        }
    ),

    'company_name': forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Company Name',
        }
    ),

    'email': forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
        }
    ),

    'phone_number': forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
        }
    ),

    'message': forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Project Requirements',
            'rows': 5,
        }
    ),
}
        
class ContactMessageForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            'full_name',
            'email',
            'subject',
            'message',
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Name',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email Address',
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Subject',
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Message',
                    'rows': 6,
                }
            ),
        }