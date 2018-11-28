from wdapp.models import BusinessOrder
import factory  
import factory.django

class from wdapp.models import BusinessOrder
Factory(factory.django.DjangoModelFactory):  
    class Meta:
        model = from wdapp.models import BusinessOrder


    name = factory.Faker('name')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')