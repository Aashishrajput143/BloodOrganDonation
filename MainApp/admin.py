from django.contrib import admin

from .models import*
# Register your models here.\

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['bloodgroup','unit']

@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(OrganStock)
class OrganStockAdmin(admin.ModelAdmin):
    list_display = ['organname','bloodgroup','quantity']

@admin.register(BloodDonate)
class BloodDonateAdmin(admin.ModelAdmin):
    list_display = ['id','donor','disease','age','bloodgroup','location','unit','status','date','ondate','ontime']

@admin.register(OrganDonate)
class OrganDonateAdmin(admin.ModelAdmin):
    list_display = ['id','donor','disease','donorstatus','Report','age','bloodgroup','location','organ','status','date','ondate','ontime']

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['id','patient','reason','age','bloodgroup','doctor','unit','status','date','ondate','ontime']

@admin.register(OrganRequest)
class OrganRequestAdmin(admin.ModelAdmin):
    list_display = ['id','patient','reason','age','bloodgroup','organ','doctor','status','date','ondate','ontime']

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','username','email','phone','gender','bloodgroup','age','addressline1','addressline2','addressline3','disease','pin','city','state','pic']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','username','email','phone','gender','bloodgroup','age','doctor','addressline1','addressline2','addressline3','reason','pin','city','state','pic']

@admin.register(Newslater)
class NewslaterAdmin(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle','description','quotes','excert','date','place','eventdate','status','pic1','pic2','pic3','video']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['id','company','currency','title','subtitle','details1','details2','details3','details4','details5','terms1','terms2','terms3','terms4','terms5','banner','logo','aboutcompany']

@admin.register(Rewards)
class RewardsAdmin(admin.ModelAdmin):
    list_display = ['id','donor','currency','date','status','company','title','subtitle','details1','details2','details3','details4','details5','terms1','terms2','terms3','terms4','terms5','banner','logo','aboutcompany']

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','address','pin','city','state','pic']

@admin.register(Withdrawn)
class WithdrawnAdmin(admin.ModelAdmin):
    list_display = ['id','name','upi','amount','phone','email','donor','status']

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','address','pin','city','state','pic']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name','position','description','tag1','tag2','tag3','tag4','social1','social2','social3','social4','status','pic']

@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','pin','city','state']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id','name','occupasion','email','comment','stars']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','quotes','excert','tag1','tag2','tag3','tag4','tag5','tag6','tag7','tag8','pic','pic1','pic2','pic3']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','subject','message','status']




