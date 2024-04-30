from django.db import models
from random import choices


class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.bloodgroup)

class Organ(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class OrganStock(models.Model):
    organname=models.ForeignKey(Organ,on_delete=models.CASCADE)
    bloodgroup=models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.organname)

class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    bloodgroup=models.CharField(max_length=10)
    currency=models.PositiveIntegerField(default=0)
    addressline1 = models.CharField(max_length=100,default=None,null=True,blank=True)
    addressline2 = models.CharField(max_length=100,default=None,null=True,blank=True)
    addressline3 = models.CharField(max_length=100,default=None,null=True,blank=True)
    disease=models.CharField(max_length=100,default="Nothing",null=True,blank=True)
    age=models.PositiveIntegerField(default=0,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.FileField(upload_to="images",default="noimage.jpg",null=True,blank=True)

    def __str__(self):
        return self.username
    
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    bloodgroup=models.CharField(max_length=10)
    addressline1 = models.CharField(max_length=100,default=None,null=True,blank=True)
    addressline2 = models.CharField(max_length=100,default=None,null=True,blank=True)
    addressline3 = models.CharField(max_length=100,default=None,null=True,blank=True)
    reason=models.CharField(max_length=100,default=None,null=True,blank=True)
    age=models.PositiveIntegerField(default=0,null=True,blank=True)
    doctor = models.CharField(max_length=50,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.FileField(upload_to="images",default="noimage.jpg",null=True,blank=True)

    def __str__(self):
        return self.username

class Newslater(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50,unique=True)

contactstatuschoice =((1,'Active'),(2,'Done'))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.TextField()
    message = models.TextField()
    status = models.IntegerField(choices=contactstatuschoice,default=1)

blogstatuschoice =((1,'Upcoming'),(2,'Latest'))
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    quotes = models.TextField(default="")
    excert = models.TextField(default="")
    date = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=100,default="Dehradun")
    eventdate = models.DateField(default="2024-04-01",null=True,blank=True)
    status = models.IntegerField(choices=blogstatuschoice,default=1)
    pic1 = models.FileField(upload_to="images",default="default1.jpg",null=True,blank=True)
    pic2 = models.FileField(upload_to="images",default="default.jpg",null=True,blank=True)
    pic3 = models.FileField(upload_to="images",default="default2.jpg",null=True,blank=True)
    video = models.FileField(upload_to="images",default="video.webm",null=True,blank=True)

    def __str__(self):
        return self.title
    
class Services(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    quotes = models.TextField(default="")
    excert = models.TextField(default="")
    tag1 = models.TextField(default="")
    tag2 = models.TextField(default="",blank=True)
    tag3 = models.TextField(default="",blank=True)
    tag4 = models.TextField(default="",blank=True)
    tag5 = models.TextField(default="",blank=True)
    tag6 = models.TextField(default="",blank=True)
    tag7 = models.TextField(default="",blank=True)
    tag8 = models.TextField(default="",blank=True)
    pic = models.FileField(upload_to="images",default="default5.jpg",null=True,blank=True)
    pic1 = models.FileField(upload_to="images",default="noimage6.jpg",null=True,blank=True)
    pic2 = models.FileField(upload_to="images",default="noimage7.jpg",null=True,blank=True)
    pic3 = models.FileField(upload_to="images",default="noimage4.jpg",null=True,blank=True)

    def __str__(self):
        return self.title

doctorstatuschoice =((1,'left'),(2,'right'))
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField(default="",blank=True)
    tag1 = models.TextField(default="",blank=True)
    tag2 = models.TextField(default="",blank=True)
    tag3 = models.TextField(default="",blank=True)
    tag4 = models.TextField(default="",blank=True)
    social1 = models.TextField(default="",blank=True)
    social2 = models.TextField(default="",blank=True)
    social3 = models.TextField(default="",blank=True)
    social4 = models.TextField(default="",blank=True)
    status = models.IntegerField(choices=doctorstatuschoice,default=1)
    pic = models.FileField(upload_to="images",default="default8.jpg",null=True,blank=True)

    def __str__(self):
        return self.name

    
class Join(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    pin = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
paymentchoice =((1,'pending'),(2,'Done'))
class Withdrawn(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    upi= models.CharField(max_length=50)
    amount = models.PositiveIntegerField(default=0)
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    status = models.IntegerField(choices=paymentchoice,default=1)

    def __str__(self):
        return str(self.donor)
    
class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    occupasion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment = models.CharField(max_length=100)
    stars=models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name

class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.FileField(upload_to="images",default="default8.jpg",null=True,blank=True)

    def __str__(self):
        return self.name
    
class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.FileField(upload_to="images",default="default8.jpg",null=True,blank=True)

    def __str__(self):
        return self.name

blooddonationstatuschoice =((1,'pending'),(2,'Approved'),(3,'Rejected'),(4,'Done'))
class BloodDonate(models.Model): 
    id = models.AutoField(primary_key=True)
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE)
    disease=models.CharField(max_length=100,default="Nothing")
    age=models.PositiveIntegerField()
    location = models.ForeignKey(Locations,on_delete=models.CASCADE)
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=blooddonationstatuschoice,default=1)
    date = models.DateTimeField(auto_now=True)
    ondate=models.DateField()
    ontime=models.TimeField()

    def __str__(self):
        return str(self.donor)

organdonationstatuschoice =((1,'pending'),(2,'Approved'),(3,'Rejected'),(4,'Done'))
donorstatuschoice =((1,'Alive'),(2,'Death'))
class OrganDonate(models.Model): 
    id = models.AutoField(primary_key=True)
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE)
    disease=models.CharField(max_length=100,default="Nothing")
    donorstatus = models.IntegerField(choices=donorstatuschoice,default=1)
    Report = models.CharField(max_length=300,default=None,null=True,blank=True)
    age=models.PositiveIntegerField()
    location = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    bloodgroup = models.ForeignKey(Stock,on_delete=models.CASCADE)
    organ = models.ForeignKey(Organ,on_delete=models.CASCADE)
    status = models.IntegerField(choices=organdonationstatuschoice,default=1)
    date = models.DateTimeField(auto_now=True)
    ondate=models.DateField()
    ontime=models.TimeField()

    def __str__(self):
        return str(self.donor)
    
bloodrequeststatuschoice =((1,'pending'),(2,'Approved'),(3,'Rejected'),(4,'Done'))
class BloodRequest(models.Model): 
    id = models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    reason=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    doctor = models.CharField(max_length=100,default="")
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=bloodrequeststatuschoice,default=1)
    date = models.DateTimeField(auto_now=True)
    ondate=models.DateField()
    ontime=models.TimeField()

    def __str__(self):
        return str(self.patient)

organrequeststatuschoice =((1,'pending'),(2,'Approved'),(3,'Rejected'),(4,'Done'))
class OrganRequest(models.Model): 
    id = models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    reason=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    doctor = models.CharField(max_length=100,default="")
    bloodgroup=models.CharField(max_length=10)
    organ=models.ForeignKey(Organ,on_delete=models.CASCADE)
    status = models.IntegerField(choices=organrequeststatuschoice,default=1)
    date = models.DateTimeField(auto_now=True)
    ondate=models.DateField()
    ontime=models.TimeField()

    def __str__(self):
        return str(self.patient)
    
class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    currency=models.PositiveIntegerField(default=None,null=True,blank=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250,default=None,null=True,blank=True)
    details1 = models.TextField(default=None,null=True,blank=True)
    details2 = models.TextField(default=None,null=True,blank=True)
    details3 = models.TextField(default=None,null=True,blank=True)
    details4 = models.TextField(default=None,null=True,blank=True)
    details5 = models.TextField(default=None,null=True,blank=True)
    terms1 = models.TextField(default=None,null=True,blank=True)
    terms2 = models.TextField(default=None,null=True,blank=True)
    terms3 = models.TextField(default=None,null=True,blank=True)
    terms4 = models.TextField(default=None,null=True,blank=True)
    terms5 = models.TextField(default=None,null=True,blank=True)
    banner = models.FileField(upload_to="images",default="noimage.jpg",null=True,blank=True)
    logo = models.FileField(upload_to="images",default="noimage.jpg",null=True,blank=True)
    aboutcompany = models.TextField(default=None,null=True,blank=True)

    def __str__(self):
        return str(self.title)

rewardsstatuschoice =((1,'Claim Now'),(2,'Claimed'),(3,'Expired'))
class Rewards(models.Model):
    id = models.AutoField(primary_key=True)
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.IntegerField(choices=rewardsstatuschoice,default=1)
    company = models.CharField(max_length=100,default=None)
    currency=models.PositiveIntegerField(default=None,null=True,blank=True)
    title = models.CharField(max_length=100,default=None)
    subtitle = models.CharField(max_length=250,default=None,null=True,blank=True)
    details1 = models.TextField(default=None,null=True,blank=True)
    details2 = models.TextField(default=None,null=True,blank=True)
    details3 = models.TextField(default=None,null=True,blank=True)
    details4 = models.TextField(default=None,null=True,blank=True)
    details5 = models.TextField(default=None,null=True,blank=True)
    terms1 = models.TextField(default=None,null=True,blank=True)
    terms2 = models.TextField(default=None,null=True,blank=True)
    terms3 = models.TextField(default=None,null=True,blank=True)
    terms4 = models.TextField(default=None,null=True,blank=True)
    terms5 = models.TextField(default=None,null=True,blank=True)
    banner = models.FileField(upload_to="images",default="noimage.jpg",null=True,blank=True)
    logo = models.FileField(upload_to="images",default="noimage.jpg",null=True,blank=True)
    aboutcompany = models.TextField(default=None,null=True,blank=True)

    def __str__(self):
        return str(self.donor)

    