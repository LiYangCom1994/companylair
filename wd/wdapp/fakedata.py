import factory

from wdapp.models import Company, Cargo, Business, BusinessOrder, Stop,DriverExpense,Trip,Driver

class UserFactory(factory.Factory):
    # = Faker('en_US')
    class Meta:
        user = factory.Sequence(lambda n: 'user%s' % n)
        email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
        first_name = factory.Sequence(lambda n: 'first_name{0}'.format(n))
        last_name = factory.Sequence(lambda n: 'last_name{0}'.format(n))
        phone = factory.Sequence(lambda n: '123-555-%04d' % n)
        address=factory.Sequence(lambda n: 'street%d' % n)
        city=factory.Sequence(lambda n: 'city%d' % n)
        state=factory.Sequence(lambda n: 'state%d' % n)

        date_joined = factory.fuzzy.FuzzyDate(datetime.date(2013, 1, 1))
class CompanyFactory(factory.Factory):
    class Meta:
        model = Company
        user=factory.SubFactory(UserFactory)

        company = name = factory.Sequence(lambda n: 'TruckBoyz{0}'.format(n))
        year_established=factory.fuzzy.FuzzyDate(start_date=datetime.date(1969, 1, 1),end_date=datetime.date(2017, 12, 31))

#American Based Names

#for _ in range(10):
    #print(fake.name())
class DriverFactory(factory.Factory):
    class Meta:
        model = Driver



        user=factory.SubFactory(UserFactory)

        company=factory.SubFactory(CompanyFactory)

        ssn=factory.Sequence(lambda n: '123-555-%04d' % n)
        license_number=factory.Sequence(lambda n: '123%04d' % n)

        date_hired=factory.fuzzy.FuzzyDate(start_date=datetime.date(1990, 1, 1))






