from django.db import models
from django.db.models import Sum,Avg
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import date

from django.db.models import F, Sum,Case, When,DecimalField, Value
import os
import sys
import csv
from datetime import timedelta
class Company(models.Model): #Truck Company


    FUEL = "Fuel"
    MANFACTURER= "Manfacturer"
    TECHNOLOGY = "Technology"
    RETAIL = "Retail"
    WHOLESALE_TRADE = "Wholesale"
    STATE_MILTARY_FEDERAL= "Goverment"
    OTHER = "Other"
    INDUSTRY = (
        (FUEL, 'fuel'),
        (MANFACTURER, 'nondurable manfacturer'),
        (TECHNOLOGY, 'tech'),
        (RETAIL, 'retail'),
        (WHOLESALE_TRADE, 'wholesale trade'),
        (STATE_MILTARY_FEDERAL, 'Goverment'),
        (OTHER,'other'),
        )
    company_id=models.CharField(null="True",max_length=9)
    user = models.OneToOneField(User,related_name='company', on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=500,null =True)
    trucking_specilization=models.CharField(choices= INDUSTRY,null =True, max_length=50)
    year_established=models.DateField(max_length=500,null =True)


    def get_unique_id(self):
        a = self.company[:5].upper()
        b =self.trucking_specilization[:3].upper()
        c= self.year_established.strftime('%y')

        return a + b + c


    def save(self, *args, **kwargs):
        self.company_id = self.get_unique_id()

        super(Company, self).save(*args, **kwargs)

    def get_company_name(self):
        return self.company
    def get_company_id(self):
        return self.company_id
    def get_company_name(self):
        return self.company
    def get_trucking_specilization(self):
         return self.get_trucking_specilization


class Driver(models.Model): #Driver for the Company
    MALE="M"
    FEMALE="F"
    SEX = (
        (MALE, 'male'),
        (FEMALE, 'female'),)
    HOURLY="Hourly"
    MILES="Miles"
    WAGE_PLAN=(
        (HOURLY, 'hourly'),
        (MILES, 'miles'),)

    CLASS_A ="A"
    CLASS_B = "B"
    CLASS_C = "C"
    LICENSE=(
        (CLASS_A, 'class a'),
        (CLASS_B, 'class b'),
        (CLASS_C, 'class c'),)
    driver_id=models.CharField(null="True",max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver',null=True)
    date_of_birth=models.DateField(null =True) #18 y.o min
    ssn=models.CharField(max_length=9, db_index=True,null =True)
    wage_plan=models.CharField(choices= WAGE_PLAN,null =True,max_length=50)
    license=models.IntegerField(choices= LICENSE,null =True)
    other_license=models.IntegerField(choices= LICENSE,null =True)
    other_license_2=models.IntegerField(choices= LICENSE,null =True)
    license_number=models.IntegerField(null =True)
    date_hired=models.DateField(null =True)
    company_id=models.ForeignKey(Company,related_name="c_id",null="True")



    #timeempl=models.IntegerField(null =True)

    def get_unique_id(self):
        a = self.ssn[4:].lower()
        b = self.wage_plan[:3].upper()
        c= self.date_hired.strftime('%y')
        #First 2 letters of city
        return a + b + c





    def drivers_name(self):
        return self.name
    def get_driver_license_number(self):
        return self.driver_id
    def get_driver_date_of_hire(self):

         return self.date_hired



    def get_drivers_social_security(self):
         return self.ssn
    def get_drivers_wage_plan(self):
        return self.wage_plan





    def save(self, *args, **kwargs):
        self.driver_id = self.get_unique_id()

        super(Driver, self).save(*args, **kwargs)

class Business(models.Model):
    FUEL = 1
    MANFACTURER= 2
    TECHNOLOGY = 3
    RETAIL = 4
    WHOLESALE_TRADE = 5
    STATE_MILTARY_FEDERAL= 6
    OTHER = 7
    INDUSTRY = (
        (FUEL, 'fuel'),
        (MANFACTURER, 'nondurable manfacturer'),
        (TECHNOLOGY, 'tech'),
        (RETAIL, 'retail'),
        (WHOLESALE_TRADE, 'wholesale trade'),
        (STATE_MILTARY_FEDERAL, 'state_military_federal'),
        (OTHER,'other'),
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business',null=True)
    business = models.CharField(max_length=150, db_index=True)
    industry = models.IntegerField(choices= INDUSTRY)
    business_id=models.CharField(null="True",max_length=25)



    def get_unique_id(self):
        a=  self.business[:4].upper()
        b=  self.user[:3].upper()
        c=  self.industry[:2].upper()

        return a + b + c


    def save(self, *args, **kwargs):
        self.business_id = self.get_unique_id()

        super(Cargo, self).save(*args, **kwargs)


    def get_business_name(self):
        return self.name
    def get_business_id(self):
        return self.business_id
    def get_point_of_contact(self):
        return self.point_of_contact
    def get_other_details(self):
        return self.other_details



    #Business have Can add what Cargo they want Transported
class Cargo(models.Model):
    FUEL = 1
    MANFACTURER_MACHINERY=2
    ELECTRONIC_ELECTRICAL=3
    RETAIL = 4
    FOOD_PERISHABLE= 5
    STATE_MILTARY_FEDERAL  = 6
    OTHER = 7
    INDUSTRY_TYPE = (
        (FUEL, 'fuel'),
        (MANFACTURER_MACHINERY, 'manfacturer'),
        (ELECTRONIC_ELECTRICAL, 'tech'),
        (RETAIL, 'retail'),
        (FOOD_PERISHABLE, 'perishable'),
        (STATE_MILTARY_FEDERAL, 'state_military_federal'),
        (OTHER, 'other' ),
        )
    LIQUID = 1
    SOLID=2
    GAS=3
    PLASMA = 4
    MATTER_STATE = (
        (LIQUID, 'liquid'),
        (SOLID, 'solid'),
        (GAS, 'gas'),
        (PLASMA, 'plasma'),)\

    cargo_id= models.CharField(null="True",max_length=25,blank="True")
    cargo = models.CharField(max_length=500,null =True)
    price=  models.DecimalField(max_digits=4,decimal_places=1,null=True)
    category = models.IntegerField(choices= INDUSTRY_TYPE,null =True)
    state_of_matter=models.IntegerField(choices= MATTER_STATE,null =True)
    weight=models.IntegerField(null=True) #LBS
    volume=models.IntegerField(null=True) #FT CUBIC FEET
    short_description = models.CharField(max_length=500,null =True)
    def get_unique_id(self):
        a = self.cargo[:4].upper()
        b =self.state_of_matter[:3].upper()
        c= self.weight[:2].upper()

        return a + b + c

    def save(self, *args, **kwargs):
        self.cargo_id = self.get_unique_id()

        super(Cargo, self).save(*args, **kwargs)

    def get_cargo_name(self):
        return self.name
    def get_cargo_id(self):
        return self.cargo_id



class BusinessOrder(models.Model):#Business and Company only
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    PREFERRED_DAY = (
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
        )
    NON_HAZARDOUS = 1
    EXPLOSIVE = 2
    GAS = 3
    LIQUID_FLAMMABLE = 4
    COMBUSTIBLE = 5
    SOLID_FLAMMABLE=6
    SPONTANEOUS = 7
    DANGEROUS_WHEN_WET = 8
    OXIDIZER=10
    TOXIC = 11
    RADIOACTIVE = 12
    MISC= models.TextField(blank=True)
    HAZMAT_CLASS = (
        (NON_HAZARDOUS, 'Non-hazard'),
        (EXPLOSIVE, 'Explosive'),
        (GAS, 'Gases'),
        (LIQUID_FLAMMABLE, 'Flammable Liquid'),
        (COMBUSTIBLE, 'Combustible Liquid'),
        (SOLID_FLAMMABLE, 'Flammable Solid'),
        (SPONTANEOUS, 'Spontanaeously Combustible'),
        (DANGEROUS_WHEN_WET, 'Dangerous When Wet'),
        (OXIDIZER, 'Oxidizer and Organic Peroxide'),
        (TOXIC, 'Poison (Toxic) and Poison Inhalation Hazard'),
        (RADIOACTIVE, 'Radioactive'),
          (MISC, 'Miscellaneous, and the general Dangerous placard')
        )
    PICKUP=0
    DELIVERY=1
    SERVICE=((PICKUP, 'pickup'),
        (DELIVERY, 'delivery'),)
    order_id=models.CharField(null=True,max_length=25)
    date_created = models.DateField(auto_now_add=True,null =True, blank=True)

    business_id=models.ForeignKey(Business, related_name='b_id_set',on_delete=models.CASCADE,null =True)

    service_type=models.IntegerField(choices= SERVICE,null =True)
    company=models.ForeignKey(Company,related_name="company_set", on_delete=models.CASCADE, null=True)
    cargo = models.ForeignKey(Cargo,related_name='cargo_set',on_delete=models.CASCADE,null =True)
    quantity=models.IntegerField(default=0)
    weight = models.ForeignKey(Cargo,related_name='weight_set',on_delete=models.CASCADE,null =True)
    volume=models.ForeignKey(Cargo,related_name='volume_set',on_delete=models.CASCADE,null =True)


    distance = models.DecimalField(max_digits=10,decimal_places=2)
    hazmat_class=models.IntegerField(choices= HAZMAT_CLASS,null =True)

    def get_unique_id(self):

        a = self.business_id[:3].upper()
        b =self.service_type[:3].upper()
        c= self.cargo[:3].upper()
        d= self.hazmat_class.strftime('%y')

        return a + b + c + d
    def save(self, *args, **kwargs):
        self.order_id = self.get_unique_id()

        super(BusinessOrder, self).save(*args, **kwargs)

    def get_business_id(self):
        return self.business_id
    def get_service_type(self):
        return self.service_type
    def get_estimated_distance_from_company(self):
        return self.cargo_id
    def get_volume(self):
        return self.quantity * self.volume
    def get_weight(self):
        return self.quantity * self.weight
    def get_hazmat_class(self):
         return self.overall_hazmat_class

    def get_price_by_volume(self):
        return self.quantity * self.volume*self.distance
    def get_price_by_weight(self):
        return self.quantity * self.weight*self.distance
    def get_price_volume_hazmat(self):
         if self.HAZMAT_CLASS== range(1,4):
            return get_price_by_volume(self)* 1
         if self.HAZMAT_CLASS== range(5,7):
            return get_price_by_volume(self)* 1.33
         if self.HAZMAT_CLASS== range(8,11):
            return get_price_by_volume(self)* 1.75
         if self.HAZMAT_CLASS== 12:
            return get_price_by_volume(self)* 3.25

    def get_price_weight_hazmat(self):
         if self.HAZMAT_CLASS== range(1,4):
            return get_price_by_weight(self)* 1
         if self.HAZMAT_CLASS== range(5,7):
            return get_price_by_weight(self)* 1.33
         if self.HAZMAT_CLASS== range(8,11):
            return get_price_by_weight(self)* 1.75
         if self.HAZMAT_CLASS== 12:
            return get_price_by_weight(self)* 3.25




class CargoManifest(models.Model): #For Driver and Company only #STATIC INFORMATION
    #STATIC INFORMATION : For Company and Employee usage. Heavy usage of "_id" extension.
    ##The driver/company can determine the Truck he will need for the trip and distance from facility. The overall hazmat class is listed as well

    manifest_id=models.IntegerField(null=True)
    driver_id=models.ForeignKey(Driver, related_name="cargomanifests_driver_id_set",null=True)
    date_created = models.ForeignKey(BusinessOrder, related_name="cargomanifests_date_created_set",null=True)
    company_id = models.ForeignKey(BusinessOrder, related_name="cargomanifests_company_id_set",null=True)
    order_id = models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="cargomanifests_order_id_set",null=True)
    cargo_id = models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="cargomanifests_cargo_id_set",null=True)
    hazmat_class=models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="cargomanifest_hazmat_class_set",null=True)
    service_type=models.ForeignKey(BusinessOrder, related_name="cargomanifests_service_type_set",null=True)


    weight= models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="cargomanifests_weight_set",null=True)
    volume= models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="cargomanifests_volume_set",null=True)
    quantity=models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="cargomanifests_quantity_set",null=True)
    estimated_trip_distance=models.DecimalField(max_digits=4,decimal_places=1,null=True)


    def get_manifest_id(self):
        return self.manifest_id
    def get_hazmat_class(self):
         return self.overall_hazmat_class
    def get_total_weight(self):
        return self.weight * self.quantity
    def get_total_volume(self):
        return self.volume * self.quantity

class Trip(models.Model): #Driver and Company
    NORMAL = 1
    CLOUDY = 2
    RAIN = 3
    SNOW = 4
    HAZARDOUS = 5
    EXTREMELY_HAZARDOUS = 6
    WEATHER_CONDITIONS = (
        (NORMAL, 'normal'),
        (CLOUDY, 'cloudy'),
        (RAIN, 'rain'),
        (SNOW, 'snow'),
        (HAZARDOUS, 'hazardous'),
        (EXTREMELY_HAZARDOUS, 'extremly hazardous'),
        )
    YES="Yes"
    NO="No"
    CARD=((YES,'yes'),
              (NO,'no'),)
    trip_id=models.IntegerField(null=True)
    date=models.DateField(auto_now_add=False,null =True)
    driver_id=models.ForeignKey(CargoManifest, related_name="trips_driver_id_set",null=True)
    company_id = models.ForeignKey(CargoManifest,related_name='trips_company_id_set',on_delete=models.CASCADE,null =True)
    manifest_id=models.ForeignKey(CargoManifest, related_name='trips_manifest_id_set',on_delete=models.CASCADE,null =True)

    estimated_arrival=models.DateField(auto_now_add=False,null =True, blank=True)
    order_created = models.ForeignKey(CargoManifest,related_name='trips_order_created_set',on_delete=models.CASCADE,null =True)

    trailer_license=models.CharField(null =True,max_length=7)
    beginnning_weather_conditions = models.IntegerField(choices=WEATHER_CONDITIONS, default=NORMAL,null=True)
    estimated_trip_distance=models.ForeignKey(CargoManifest,on_delete=models.CASCADE,null =True,related_name= 'estimated_distance_set')



    midway_weather_conditions= models.IntegerField(choices=WEATHER_CONDITIONS, default=NORMAL,null=True)
    ending_weather_conditions = models.IntegerField(choices=WEATHER_CONDITIONS, default=NORMAL,null=True)
    fuel_card_usage=models.IntegerField(choices=CARD, default=YES,null=True)
    average_price_per_gallon=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    gallons_of_gas_used=models.IntegerField(null =True)
    number_of_unscheduled=models.IntegerField(null =True)
    total_miles_traveled=models.DecimalField(max_digits=4,decimal_places=1,null=True)
    order_details = models.TextField(null =True)



class OrderStatus(models.Model): # Delivery or Trucking company handles this . Company,Driver and Representative can see this!
    #DYNAMIC INFORMATION: limited usage of "_id". This view is for the Business(customer) Specifcally.
    PREPARING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4
    FAILED= 5
    STATUS_CHOICES = (
        (PREPARING, "Preparing"),
        (READY, "Ready"),
        (ONTHEWAY, "en route"),
        (DELIVERED, "Delivered"),
        (FAILED, "failed"),
    )
    order_id = models.ForeignKey(BusinessOrder,on_delete=models.CASCADE,related_name="orderstatus_order_id_set",null=True)
    name = models.ForeignKey(Trip,on_delete=models.CASCADE,related_name="orderstatus_name_set",null=True)
    date_created = models.ForeignKey(BusinessOrder,related_name="orderstatus_date_created_set",null=True)
    business_id=models.ForeignKey(BusinessOrder,null=True)
    company_id = models.ForeignKey(BusinessOrder, related_name="o_c_id_set",null=True)

    service_type=models.ForeignKey(BusinessOrder, related_name="orderstatus_service_type_set",null=True)
    cargo= models.ForeignKey(BusinessOrder, related_name="orderstatus_cargo_set",null=True)
    quantity=models.ForeignKey(BusinessOrder, related_name="orderstatus_quanity_set",null=True)

    status = models.IntegerField(choices = STATUS_CHOICES,null=True)



    def _str_(self):
        return self.estimated_arrival
    def _str_2(self):
        return self.company_id
    def _str_2(self):
        return self.order_id
    def status(self):
        return self.status






class Stop(models.Model): #Driver and Company only
    FUEL = 1
    MEAL= 2
    RESTROOM = 3
    LODGING = 4
    ACCIDENT = 5
    OTHER= 6
    STOP_TYPE = (
        (FUEL, 'fuel'),
        (MEAL, 'meal'),
        (RESTROOM, 'restroom'),
        (LODGING, 'lodging'),
        (ACCIDENT, 'accident'),
        (OTHER, 'other')
        )
    stop_id= models.CharField(null="True",max_length=25,blank="True")
    driver_id = models.ForeignKey(Trip, related_name='stop_driver_id_set',on_delete=models.CASCADE,null =True)
    trip_id= models.ForeignKey(Trip, related_name='stop_trip_id_set',on_delete=models.CASCADE,null =True)
    stop_type=models.IntegerField(choices=STOP_TYPE,null =True)

    time_stop = models.TimeField(auto_now_add=True, blank=True)
    departed_stop = models.TimeField(auto_now_add=False, blank=True)



    def get_unique_id(self):

        a = self.trip_id[:3].upper()
        b =self.stop_type[:3].upper()
        c= self.time_stop[:6].upper()

        return a + b + c
    def save(self, *args, **kwargs):
        self.stop_id = self.get_unique_id()

        super(Stop, self).save(*args, **kwargs)

    def get_stop_id(self):
        return self.stop_id


class DriverExpense(models.Model): #Driver and Company only

    FUEL = 1
    MEAL= 2
    EMERGENCY = 3
    OTHER = 4
    EXPENSE_TYPE = (
        (FUEL, 'fuel'),
        (MEAL, 'meal'),
        (EMERGENCY, 'emergency'),
        (OTHER, 'other'),
        )
    expenses_id=models.CharField(null=True,max_length=25)
    driver_id= models.ForeignKey(CargoManifest, related_name='driverexpenses_driver_id_set',on_delete=models.CASCADE,null =True)
    stop_id=models.ForeignKey(Stop,related_name="driverexpenses_stop_id_set",on_delete=models.CASCADE,null =True)
    expense_type= models.IntegerField(choices=EXPENSE_TYPE,null=True)
    amount_of_expense = models.IntegerField(default=0,null=True)
    def get_unique_id(self):

        a = self.trip_id[:3].upper()
        b =self.expense_type[:3].upper()
        c= self.stop_id[:6].upper()

        return a + b + c
    def save(self, *args, **kwargs):
        self.expense_id = self.get_unique_id()

        super(DriverExpense, self).save(*args, **kwargs)
    def _str_(self):
        return self.expenses_id



