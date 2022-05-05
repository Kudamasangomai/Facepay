from django.forms import ModelForm
from pos.models import Customer

class CustomerForm(ModelForm):
   class Meta:
      model = Customer
      fields = '__all__'

   def __init__(self, *args, **kwargs):
      super(CustomerForm, self).__init__(*args, **kwargs)

      for name, field in self.fields.items():
         field.widget.attrs.update({'class': 'form-control'})