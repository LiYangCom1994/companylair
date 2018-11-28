from wdapp.models import Business,Business,Driver
import factory  
import factory.django
class CompanyFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Company

    name = factory.Faker('name')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')
    
class BusinessFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Business

    name = factory.Faker('name')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')

class DriverFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Driver

    name = factory.Faker('name')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')
