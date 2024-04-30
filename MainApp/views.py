from random import randint
from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth

from django.db.models import Sum, Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User

from MainApp import models
from .models import *


def home(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    blogs = Blog.objects.order_by("-id")[:3]
    if request.method == "POST":
        if "subscribe" in request.POST:
            try:
                email = request.POST.get("email")
                if(email==""):
                    return HttpResponseRedirect("/")
                n = Newslater()
                n.email = email
                n.save()
                subject = 'Thank you! To Subscribe our Newslater : Team Novena'
                message =  """
                                ! Thank you to Subscribe our Newslater! 
                                Thanks to Join with Us.
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [n.email, ]
                send_mail( subject, message, email_from, recipient_list )
            except:
                pass
            return HttpResponseRedirect("/")
        if "join" in request.POST:
            u = Join()
            u.name = request.POST.get("name")
            u.email = request.POST.get("email")
            u.phone = request.POST.get("phone")
            u.city = request.POST.get("city")
            u.state = request.POST.get("state")
            u.pin = request.POST.get("pin")
            u.save()
            messages.success(request, "Join Us Sucessfully....")
    return render(request, "index.html", {"Blogs": blogs, "Users": users})


def About(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    testimonial = Testimonial.objects.all()
    testimonial=testimonial[::-1]
    return render(request, "about.html", {"Users": users,'Testimonial':testimonial})


@login_required(login_url="/login_register/")
def donateblood(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    donor = Donor.objects.get(username=request.user)
    dict = {
        "requestpending": BloodDonate.objects.all()
        .filter(donor=donor)
        .filter(status=1)
        .count(),
        "requestapproved": BloodDonate.objects.all()
        .filter(donor=donor)
        .filter(status=2)
        .count(),
        "requestmade": BloodDonate.objects.all().filter(donor=donor).count(),
        "requestrejected": BloodDonate.objects.all()
        .filter(donor=donor)
        .filter(status=3)
        .count(),
    }
    count=0
    location = Locations.objects.all()
    if request.method == "POST":
        c = BloodDonate()
        c.donor = Donor.objects.get(username=request.user)
        c.bloodgroup =Stock.objects.get(bloodgroup=donor.bloodgroup)
        c.disease = request.POST.get("disease")
        c.age = request.POST.get("age")
        ondate = request.POST.get("ondate")
        da = ondate.split("/")
        m = da[0]
        d = da[1]
        y = da[2]
        c.ondate = y + "-" + m + "-" + d
        c.ontime = request.POST.get("ontime")
        c.unit = request.POST.get("amount")
        c.location = Locations.objects.get(id=request.POST.get("location"))
        c.save()
        messages.success(request, "Send Request Sucessfully....")
        subject = 'Thank You for Donating Blood and Saving Lives : Team Novena'
        message =  """
                                %s! Thank You for Donating Blood 
                                and Saving Lives! 
                                Thanks to Donte the Blood 
                                and connect with Us.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donor.firstname+" "+donor.lastname)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [donor.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(
        request,
        "donateblood.html",
        {"User": donor, "Dict": dict, "Users": users, "Locations": location},
    )


@login_required(login_url="/login_register/")
def donateorgan(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    donor = Donor.objects.get(username=request.user)
    dict = {
        "requestpending": OrganDonate.objects.all()
        .filter(donor=donor)
        .filter(status=1)
        .count(),
        "requestapproved": OrganDonate.objects.all()
        .filter(donor=donor)
        .filter(status=2)
        .count(),
        "requestmade": OrganDonate.objects.all().filter(donor=donor).count(),
        "requestrejected": OrganDonate.objects.all()
        .filter(donor=donor)
        .filter(status=3)
        .count(),
    }
    location = Hospital.objects.all()
    organ = Organ.objects.all()
    if request.method == "POST":
        c = OrganDonate()
        c.donor = Donor.objects.get(username=request.user)
        c.bloodgroup =Stock.objects.get(bloodgroup=donor.bloodgroup)
        c.donorstatus = request.POST.get("status")
        c.Report = request.POST.get("Report")
        c.disease = request.POST.get("disease")
        c.age = request.POST.get("age")
        c.organ = Organ.objects.get(id=request.POST.get("organ"))
        ondate = request.POST.get("ondate")
        da = ondate.split("/")
        m = da[0]
        d = da[1]
        y = da[2]
        c.ondate = y + "-" + m + "-" + d
        c.ontime = request.POST.get("ontime")
        c.location = Hospital.objects.get(id=request.POST.get("location"))
        c.save()
        print("success")
        messages.success(request, "Send Request Sucessfully....")
        subject = 'Thank You for Donating Organ and Saving Lives : Team Novena'
        message =  """
                                %s! Thank You for Donating Organ 
                                and Saving Lives! 
                                Thanks to Donte the Organ 
                                and connect with Us.
                                A Organ Can Saves Lives the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donor.firstname+" "+donor.lastname)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [donor.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(
        request,
        "donateorgan.html",
        {"User": donor, "Dict": dict, "Users": users, "Locations": location,"Organ":organ},
    )


@login_required(login_url="/login_register/")
def donatehistory(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    donor = Donor.objects.get(username=request.user)
    dict = {
        "requestpending": BloodDonate.objects.all()
        .filter(donor=donor)
        .filter(status=1)
        .count(),
        "requestapproved": BloodDonate.objects.all()
        .filter(donor=donor)
        .filter(status=2)
        .count(),
        "requestmade": BloodDonate.objects.all().filter(donor=donor).count(),
        "requestrejected": BloodDonate.objects.all()
        .filter(donor=donor)
        .filter(status=3)
        .count(),
    }
    dicts = {
        "requestpending": OrganDonate.objects.all()
        .filter(donor=donor)
        .filter(status=1)
        .count(),
        "requestapproved": OrganDonate.objects.all()
        .filter(donor=donor)
        .filter(status=2)
        .count(),
        "requestmade": OrganDonate.objects.all().filter(donor=donor).count(),
        "requestrejected": OrganDonate.objects.all()
        .filter(donor=donor)
        .filter(status=3)
        .count(),
    }
    donations = BloodDonate.objects.all().filter(donor=donor)
    donations = donations[::-1]
    organdonations = OrganDonate.objects.all().filter(donor=donor)
    organdonations = organdonations[::-1]
    return render(
        request,
        "donatehistory.html",
        {"donations": donations,"organdonations": organdonations, "Dict": dict,"Dicts": dicts, "Users": users},
    )


@login_required(login_url="/login_register/")
def requestblood(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    patient = Patient.objects.get(username=request.user)
    dict = {
        "requestpending": BloodRequest.objects.all()
        .filter(patient=patient)
        .filter(status=1)
        .count(),
        "requestapproved": BloodRequest.objects.all()
        .filter(patient=patient)
        .filter(status=2)
        .count(),
        "requestmade": BloodRequest.objects.all().filter(patient=patient).count(),
        "requestrejected": BloodRequest.objects.all()
        .filter(patient=patient)
        .filter(status=3)
        .count(),
    }
    if request.method == "POST":
        c = BloodRequest()
        c.patient = Patient.objects.get(username=request.user)
        c.bloodgroup = Stock.objects.get(bloodgroup=patient.bloodgroup)
        c.reason = request.POST.get("reason")
        c.age = request.POST.get("age")
        c.doctor = request.POST.get("doctor")
        ondate = request.POST.get("ondate")
        da = ondate.split("/")
        m = da[0]
        d = da[1]
        y = da[2]
        c.ondate = y + "-" + m + "-" + d
        c.ontime = request.POST.get("ontime")
        c.unit = request.POST.get("amount")
        c.save()
        print("success")
        messages.success(request, "Send Request Sucessfully....")
        subject = 'Congratulations! Your Request for the Blood Submitted Successfully : Team Novena'
        message =  """
                                %s! Thank You for Connecting Us for 
                                Blood and Saving Lives! 
                                We will Approved your request 
                                according to our stock of Blood 
                                then we will connect with You.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donor.firstname+" "+donor.lastname)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [donor.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(
        request,
        "requestblood.html",
        {"User": patient, "Dict": dict, "Users": users},
    )


@login_required(login_url="/login_register/")
def requestorgan(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    patient = Patient.objects.get(username=request.user)
    organ = Organ.objects.all()
    dict = {
        "requestpending": OrganRequest.objects.all()
        .filter(patient=patient)
        .filter(status=1)
        .count(),
        "requestapproved": OrganRequest.objects.all()
        .filter(patient=patient)
        .filter(status=2)
        .count(),
        "requestmade": OrganRequest.objects.all().filter(patient=patient).count(),
        "requestrejected": OrganRequest.objects.all()
        .filter(patient=patient)
        .filter(status=3)
        .count(),
    }
    if request.method == "POST":
        c = OrganRequest()
        c.patient = Patient.objects.get(username=request.user)
        c.bloodgroup = Stock.objects.get(bloodgroup=patient.bloodgroup)
        c.reason = request.POST.get("reason")
        c.age = request.POST.get("age")
        c.doctor = request.POST.get("doctor")
        c.organ = Organ.objects.get(id=request.POST.get("organ"))
        ondate = request.POST.get("ondate")
        da = ondate.split("/")
        m = da[0]
        d = da[1]
        y = da[2]
        c.ondate = y + "-" + m + "-" + d
        c.ontime = request.POST.get("ontime")
        c.save()
        print("success")
        messages.success(request, "Send Request Sucessfully....")
        subject = 'Congratulations! Your Request for the Organ Submitted Successfully : Team Novena'
        message =  """
                                %s! Thank You for Connecting Us for Organ 
                                and Saving Lives! 
                                We will Approved your request 
                                according to our stock of Organ
                                then we will connect with You.
                                A Organ Can Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donor.firstname+" "+donor.lastname)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [donor.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(
        request,
        "requestorgan.html",
        {"User": patient, "Dict": dict, "Users": users,"Organ":organ},
    )


@login_required(login_url="/login_register/")
def requesthistory(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    patient = Patient.objects.get(username=request.user)
    dict = {
        "requestpending": BloodRequest.objects.all()
        .filter(patient=patient)
        .filter(status=1)
        .count(),
        "requestapproved": BloodRequest.objects.all()
        .filter(patient=patient)
        .filter(status=2)
        .count(),
        "requestmade": BloodRequest.objects.all().filter(patient=patient).count(),
        "requestrejected": BloodRequest.objects.all()
        .filter(patient=patient)
        .filter(status=3)
        .count(),
    }
    dicts = {
        "requestpending": OrganRequest.objects.all()
        .filter(patient=patient)
        .filter(status=1)
        .count(),
        "requestapproved": OrganRequest.objects.all()
        .filter(patient=patient)
        .filter(status=2)
        .count(),
        "requestmade": OrganRequest.objects.all().filter(patient=patient).count(),
        "requestrejected": OrganRequest.objects.all()
        .filter(patient=patient)
        .filter(status=3)
        .count(),
    }
    patient = Patient.objects.get(username=request.user)
    requestblood = BloodRequest.objects.all().filter(patient=patient)
    requestblood = requestblood[::-1]
    requestorgan = OrganRequest.objects.all().filter(patient=patient)
    requestorgan = requestorgan[::-1]
    return render(
        request,
        "requesthistory.html",
        {"Requests": requestblood,"organRequests": requestorgan, "Dict": dict, "Dicts": dicts, "Users": users,'Patient':patient},
    )

@login_required(login_url="/login_register/")
def blooddonationadmin(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        'totalrequest':BloodDonate.objects.all().count(),
        'totalapprovedrequest':BloodDonate.objects.all().filter(status=2).count()
    }
    donations=BloodDonate.objects.all()
    donations=donations[::-1]
    return render(request, "blooddonationadmin.html", {"Users": users,'Stocks':dict,'donations':donations})

@login_required(login_url="/login_register/")
def approve_donation_view(request,pk):
    donation=BloodDonate.objects.get(id=pk)

    donation.status=2
    donation.save()
    subject = 'Congratulations! Your Request for the Blood Donation Approved : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Blood 
                                and Saving Lives! 
                                You will Visit to the selected Camp or 
                                Blood Bank to donate blood.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donation.donor.firstname+" "+donation.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [donation.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/blooddonationadmin/')

@login_required(login_url="/login_register/")
def done_donation_view(request,pk):
    donation=BloodDonate.objects.get(id=pk)
    donation_blood_group=donation.bloodgroup
    donation_blood_unit=donation.unit

    stock=Stock.objects.get(bloodgroup=donation_blood_group)
    stock.unit=stock.unit+donation_blood_unit
    stock.save()

    donation.status=4
    donation.save()
    counting=Offer.objects.all().count(),
    for i in counting:
        count=i
    num=randint(1,count)
    print(num)
    rewards = Rewards()
    offer = Offer.objects.get(id=num)
    rewards.donor=donation.donor
    rewards.company=offer.company
    rewards.currency=offer.currency
    rewards.title=offer.title
    rewards.subtitle=offer.subtitle
    rewards.subtitle=offer.subtitle
    rewards.details1=offer.details1
    rewards.details2=offer.details2
    rewards.details3=offer.details3
    rewards.details4=offer.details4
    rewards.details5='This Rewards Earned for the Donation of Blood, "Keepit up"'
    rewards.terms1=offer.terms1
    rewards.terms2=offer.terms2
    rewards.terms3=offer.terms3
    rewards.terms4=offer.terms4
    rewards.terms5=offer.terms5
    rewards.banner=offer.banner
    rewards.logo=offer.logo
    rewards.aboutcompany=offer.aboutcompany
    rewards.save()
    print('success')
    subject = 'Congratulations! Your Blood Donation Completed Successfully : Team Novena'
    message =  """
                                %s! Thank You for Donating Blood 
                                and Saving Lives! 
                                You will Enjoy with rewards and 
                                saves the lives of the peoples.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donation.donor.firstname+" "+donation.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [donation.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/bloodhistoryadmin/')


@login_required(login_url="/login_register/")
def reject_donation_view(request,pk):
    donation=BloodDonate.objects.get(id=pk)
    donation.status=3
    donation.save()
    subject = 'We reget to announce that  Your Request for the Blood Donation was rejected : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Blood 
                                and Saving Lives! 
                                You will Donate the Blood next Time. 
                                we reject due the health issues.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donation.donor.firstname+" "+donation.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [donation.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/blooddonationadmin/')


@login_required(login_url="/login_register/")
def bloodrequestadmin(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        'totalrequest':BloodRequest.objects.all().count(),
        'totalapprovedrequest':BloodRequest.objects.all().filter(status=2).count()
    }
    requests=BloodRequest.objects.all().exclude(status=3).exclude(status=4)
    requests=requests[::-1]
    return render(request, "bloodrequestadmin.html", {"Users": users,'Stocks':dict,'requests':requests})


@login_required(login_url="/login_register/")
def update_approve_status_view(request,pk):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        'totalrequest':BloodRequest.objects.all().count(),
        'totalapprovedrequest':BloodRequest.objects.all().filter(status=2).count()
    }
    req=BloodRequest.objects.get(id=pk)

    reqts=BloodRequest.objects.filter(status=2)
    u=0
    for i in reqts:
        u=u+i.unit

    message=None
    bloodgroup=req.bloodgroup
    unit=req.unit
    stock=Stock.objects.get(bloodgroup=bloodgroup)
    if stock.unit-u >= unit:
        req.status=2
        req.save()
        
    else:
        message="Stock Doest Not Have Enough Blood To Approve This Request, Only "+str(stock.unit)+" Unit Available and "+str(u)+" Unit Already Approved..."
    req.save()
    subject = 'Congratulations! Your Request for the Blood Request Approved : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Blood 
                                and Saving Lives! 
                                You will Visit to the selected Camp or 
                                Blood Bank to donate blood.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(req.patient.firstname+" "+req.patient.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [req.patient.email, ]
    send_mail( subject, message, email_from, recipient_list )
    requests=BloodRequest.objects.all().exclude(status=3).exclude(status=4)
    return render(request, "bloodrequestadmin.html", {"Users": users,'Stocks':dict,'requests':requests,'message':message})

@login_required(login_url="/login_register/")
def update_done_status_view(request,pk):
    req=BloodRequest.objects.get(id=pk)
    unit=req.unit
    bloodgroup=req.bloodgroup
    stock=Stock.objects.get(bloodgroup=bloodgroup)
    if stock.unit>= unit:
        stock.unit=stock.unit
        stock.save()
        req.status=4
        req.save()
        subject = 'Congratulations! Your Blood Request Completed Successfully : Team Novena'
        message =  """
                                %s! Thank You for Connecting with us 
                                and Saving Lives! 
                                We will Saves lives of every person 
                                and saves the Nation.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(req.patient.firstname+" "+req.patient.lastname)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [req.patient.email, ]
        send_mail( subject, message, email_from, recipient_list )
    else:
        return HttpResponseRedirect('/bloodrequestadmin/')
    return HttpResponseRedirect('/bloodhistoryadmin/')

@login_required(login_url="/login_register/")
def update_reject_status_view(request,pk):
    req=BloodRequest.objects.get(id=pk)
    req.status=3
    req.save()
    subject = 'We reget to announce that  Your Request for the Blood Request was rejected : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Blood 
                                and Saving Lives! 
                                You will Connect for the Blood next Time. 
                                we reject due the Lack of stock of blood.
                                A Bag of Blood Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(req.patient.firstname+" "+req.patient.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [req.patient.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/bloodrequestadmin/')


@login_required(login_url="/login_register/")
def bloodhistoryadmin(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        'totalrequest':BloodDonate.objects.all().count(),
        'totalapprovedrequest':BloodDonate.objects.all().filter(status=2).count()
    }
    requests=BloodRequest.objects.all().exclude(status=1).exclude(status=2)
    requests=requests[::-1]
    return render(request, "bloodhistoryadmin.html", {"Users": users,'Stocks':dict,'requests':requests})

def bloodstock(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    st=Stock.objects.all()
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={

        'A1':Stock.objects.get(bloodgroup="A+"),
        'A2':Stock.objects.get(bloodgroup="A-"),
        'B1':Stock.objects.get(bloodgroup="B+"),
        'B2':Stock.objects.get(bloodgroup="B-"),
        'AB1':Stock.objects.get(bloodgroup="AB+"),
        'AB2':Stock.objects.get(bloodgroup="AB-"),
        'O1':Stock.objects.get(bloodgroup="O+"),
        'O2':Stock.objects.get(bloodgroup="O-"),
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        'totalrequest':BloodDonate.objects.all().count(),
        'totalapprovedrequest':BloodDonate.objects.all().filter(status=2).count()
    }
    if request.method=='POST':
        try:
            stock = Stock.objects.get(bloodgroup=request.POST.get("bloodgroup"))
            stock.unit=request.POST.get("unit")
            stock.save()
            HttpResponseRedirect("/bloodstock/")
        except:
            HttpResponseRedirect("/bloodstock/")
    return render(request, "bloodstock.html", {"Users": users,'Stocks':dict,'St':st})

@login_required(login_url="/login_register/")
def organdonationadmin(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=OrganStock.objects.aggregate(Sum('quantity'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['quantity__sum'],
        'totalrequest':OrganDonate.objects.all().count(),
        'totalapprovedrequest':OrganDonate.objects.all().filter(status=2).count()
    }
    donations=OrganDonate.objects.all()
    donations=donations[::-1]
    return render(request, "organdonationadmin.html", {"Users": users,'Stocks':dict,'donations':donations})

@login_required(login_url="/login_register/")
def approve_donation_view_organ(request,pk):
    donation=OrganDonate.objects.get(id=pk)

    donation.status=2
    donation.save()
    subject = 'Congratulations! Your Request for the Organ Donation Approved : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Organ 
                                and Saving Lives! 
                                You will Visit to the selected Camp or 
                                Hospital to donate Organ.
                                A Organ Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donation.donor.firstname+" "+donation.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [donation.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/organdonationadmin/')

@login_required(login_url="/login_register/")
def done_donation_view_organ(request,pk):
    donation=OrganDonate.objects.get(id=pk)
    donation_blood_group=donation.bloodgroup
    donation_organ=donation.organ

    stock=OrganStock.objects.get(bloodgroup=donation_blood_group,organname=donation_organ)
    stock.quantity=stock.quantity+1
    stock.save()

    donation.status=4
    donation.save()
    counting=Offer.objects.all().count(),
    for i in counting:
        count=i
    num=randint(1,count)
    print(num)
    rewards = Rewards()
    offer = Offer.objects.get(id=num)
    rewards.donor=donation.donor
    rewards.company=offer.company
    rewards.currency=offer.currency+100
    rewards.title=offer.title
    rewards.subtitle=offer.subtitle
    rewards.subtitle=offer.subtitle
    rewards.details1=offer.details1
    rewards.details2=offer.details2
    rewards.details3=offer.details3
    rewards.details4=offer.details4
    rewards.details5='This Rewards Earned for the Donation of Organ, "Keepit up"'
    rewards.terms1=offer.terms1
    rewards.terms2=offer.terms2
    rewards.terms3=offer.terms3
    rewards.terms4=offer.terms4
    rewards.terms5=offer.terms5
    rewards.banner=offer.banner
    rewards.logo=offer.logo
    rewards.aboutcompany=offer.aboutcompany
    rewards.save()
    subject = 'Congratulations! Your Organ Donation Completed Successfully : Team Novena'
    message =  """
                                %s! Thank You for Donating Organ and Saving Lives! 
                                You will Enjoy with rewards and saves 
                                the lives of the peoples.
                                A Organ Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donation.donor.firstname+" "+donation.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [donation.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/organhistoryadmin/')


@login_required(login_url="/login_register/")
def reject_donation_view_organ(request,pk):
    donation=OrganDonate.objects.get(id=pk)
    donation.status=3
    donation.save()
    subject = 'We reget to announce that  Your Request for the Organ Donation was rejected : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Blood and Saving Lives! 
                                A Organ Saves the lives
                                You will Donate the Organ next Time. 
                                we reject due the health issues.
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donation.donor.firstname+" "+donation.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [donation.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/organdonationadmin/')


@login_required(login_url="/login_register/")
def organrequestadmin(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=OrganStock.objects.aggregate(Sum('quantity'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['quantity__sum'],
        'totalrequest':OrganRequest.objects.all().count(),
        'totalapprovedrequest':OrganRequest.objects.all().filter(status=2).count()
    }
    requests=OrganRequest.objects.all().exclude(status=3).exclude(status=4)
    requests=requests[::-1]
    return render(request, "organrequestadmin.html", {"Users": users,'Stocks':dict,'requests':requests})

@login_required(login_url="/login_register/")
def update_approve_status_view_organ(request,pk):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=OrganStock.objects.aggregate(Sum('quantity'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['quantity__sum'],
        'totalrequest':OrganRequest.objects.all().count(),
        'totalapprovedrequest':OrganRequest.objects.all().filter(status=2).count()
    }
    req=OrganRequest.objects.get(id=pk)
    reqts=OrganRequest.objects.filter(status=2)

    u=0
    for i in reqts:
        u=u+1

    message=None
    bloodgroup=req.id
    organ=req.organ
    qty=1

    stock=OrganStock.objects.get(bloodgroup=bloodgroup,organname=organ)
    if stock.quantity-u >= qty:
        req.status=2
        req.save()
        
    else:
        message="Stock Doest Not Have Enough Quantity To Approve This Request, Only "+str(stock.quantity)+" Quantity Available and"+str(u)+"Quantity Already Approved..."
    req.save()
    subject = 'Congratulations! Your Request for the Organ Request Approved : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Organ
                                and Saving Lives! 
                                You will Visit to the selected Camp or
                                Hospital for transplant.
                                A Organ Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(req.patient.firstname+" "+req.patient.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [req.patient.email, ]
    send_mail( subject, message, email_from, recipient_list )
    requests=OrganRequest.objects.all().exclude(status=3).exclude(status=4)
    return render(request, "organrequestadmin.html", {"Users": users,'Stocks':dict,'requests':requests,'message':message})

@login_required(login_url="/login_register/")
def update_done_status_view_organ(request,pk):
    req=OrganRequest.objects.get(id=pk)
    reqts=OrganRequest.objects.filter(status=2)

    u=0
    for i in reqts:
        u=u+1
    bloodgroup=req.bloodgroup
    bloodgroup=Stock.objects.get(bloodgroup=bloodgroup)
    organ=req.organ
    qty=1

    stock=OrganStock.objects.get(bloodgroup=bloodgroup,organname=organ)
    if stock.quantity-u >= qty:
        stock.quantity=stock.quantity-1
        stock.save()
        req.status=4
        req.save()
        subject = 'Congratulations! Your Organ Request Completed Successfully : Team Novena'
        message =  """
                                %s! Thank You for Connecting with us
                                and Saving Lives! 
                                We will Saves lives of every person
                                and saves the Nation.
                                A Organ Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(req.patient.firstname+" "+req.patient.lastname)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [req.patient.email, ]
        send_mail( subject, message, email_from, recipient_list )
    else:
        return HttpResponseRedirect('/organrequestadmin/')
    return HttpResponseRedirect('/organhistoryadmin/')

@login_required(login_url="/login_register/")
def update_reject_status_view_organ(request,pk):
    req=OrganRequest.objects.get(id=pk)
    req.status=3
    req.save()
    subject = 'We reget to announce that Your Request for the Organ Request was rejected : Team Novena'
    message =  """
                                %s! Thank You for Connecting Us for Organ
                                and Saving Lives! 
                                You will Connect for the Organ next Time. 
                                we reject due the Lack of stock of Organ.
                                A Organ Saves the lives
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(req.patient.firstname+" "+req.patient.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [req.patient.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/organrequestadmin/')


@login_required(login_url="/login_register/")
def organhistoryadmin(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    totalunit=OrganStock.objects.aggregate(Sum('quantity'))
    dict={
        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['quantity__sum'],
        'totalrequest':OrganDonate.objects.all().count(),
        'totalapprovedrequest':OrganDonate.objects.all().filter(status=2).count()
    }
    requests=OrganRequest.objects.all().exclude(status=1).exclude(status=2)
    requests=requests[::-1]
    return render(request, "organhistoryadmin.html", {"Users": users,'Stocks':dict,'requests':requests})

def organstock(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    st=Organ.objects.all()
    stocks = Stock.objects.all()
    totalunit=OrganStock.objects.aggregate(Sum('quantity'))
    
    total1=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=1,bloodgroup=i)
        total1=total1+ostock.quantity
    total2=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=2,bloodgroup=i)
        total2=total2+ostock.quantity
    total3=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=3,bloodgroup=i)
        total3=total3+ostock.quantity
    total4=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=4,bloodgroup=i)
        total4=total4+ostock.quantity
    total5=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=5,bloodgroup=i)
        total5=total5+ostock.quantity
    total6=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=6,bloodgroup=i)
        total6=total6+ostock.quantity
    total7=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=7,bloodgroup=i)
        total7=total7+ostock.quantity
    total8=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=8,bloodgroup=i)
        total8=total8+ostock.quantity
    total9=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=9,bloodgroup=i)
        total9=total9+ostock.quantity
    total10=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=10,bloodgroup=i)
        total10=total10+ostock.quantity
    total11=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=11,bloodgroup=i)
        total11=total11+ostock.quantity
    total12=0
    for i in range(1,8):
        ostock=OrganStock.objects.get(organname=12,bloodgroup=i)
        total12=total12+ostock.quantity
    
    dict={
        'Heart':total1,
        'Lungs':total2,
        'Liver':total3,
        'Kidney':total4,
        'Pancreas':total5,
        'LargeIntestine':total6,
        'SmallIntestine':total7,
        'Corineas':total8,
        'Valves':total9,
        'Veins':total10,
        'Skin':total11,
        'Bones':total12,

        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['quantity__sum'],
        'totalrequest':OrganDonate.objects.all().count(),
        'totalapprovedrequest':OrganDonate.objects.all().filter(status=2).count()
    }
    if request.method=='POST':
        try:
            stock = OrganStock.objects.get(organname=request.POST.get("organ"),bloodgroup=request.POST.get("bloodgroup"))
            stock.quantity=request.POST.get("quantity")
            stock.save()
            HttpResponseRedirect("/organstock/")
        except:
            HttpResponseRedirect("/organstock/")
    return render(request, "organstock.html", {"Users": users,'Stocks':dict,'St':st,'stock':stocks})

def organstockdetails(request,num):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    st=Organ.objects.all()
    stocks = Stock.objects.all()
    totalunit=OrganStock.objects.aggregate(Sum('quantity'))
    
    dict={
        'A1':OrganStock.objects.get(organname=num,bloodgroup=1),
        'A2':OrganStock.objects.get(organname=num,bloodgroup=2),
        'B1':OrganStock.objects.get(organname=num,bloodgroup=3),
        'B2':OrganStock.objects.get(organname=num,bloodgroup=4),
        'AB1':OrganStock.objects.get(organname=num,bloodgroup=5),
        'AB2':OrganStock.objects.get(organname=num,bloodgroup=6),
        'O1':OrganStock.objects.get(organname=num,bloodgroup=7),
        'O2':OrganStock.objects.get(organname=num,bloodgroup=8),

        'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['quantity__sum'],
        'totalrequest':OrganDonate.objects.all().count(),
        'totalapprovedrequest':OrganDonate.objects.all().filter(status=2).count()
    }
    return render(request, "organstockdetails.html", {"Users": users,'Stocks':dict,'St':st,'stock':stocks})

def services(request, num):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    ser = Services.objects.all()
    service = Services.objects.get(id=num)
    if request.method=='POST':
            test = Testimonial()
            test.name=request.POST.get("name")
            test.email=request.POST.get("email")
            test.occupasion=request.POST.get("occupasion")
            test.comment=request.POST.get("comment")
            test.stars=request.POST.get("star")
            test.save()
            messages.success(request, "Commented Sucessfully....")
    return render(
        request, "services.html", {"Users": users, "Ser": ser, "Service": service}
    )

def rewards(request):
    user=''
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
                user=donor
        except:
            users = dic
    rewards = Rewards.objects.all().filter(donor=user)
    rewards = rewards[::-1]
    return render(request, "rewards.html", {"Reward": rewards, "Users": users, "User": user})

def rewardsadmin(request):
    user=''
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
                user=donor
        except:
            users = dic
    rewards = Withdrawn.objects.all()
    rewards = rewards[::-1]
    return render(request, "rewardsadmin.html", {"Withdrawn": rewards, "Users": users, "User": user})

@login_required(login_url="/login_register/")
def done_withdrawn_view(request,pk):
    withdrawn=Withdrawn.objects.get(id=pk)

    withdrawn.status=2
    withdrawn.save()
    subject = 'Congratulations! Your Withdrwan Request Completed Successfully : Team Novena'
    message =  """
                                %s! Thank You for Connecting with us
                                and Saving Lives! 
                                We Transfer the balance to Your UPI
                                which you enter during withdrawn..
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(withdrawn.donor.firstname+" "+withdrawn.donor.lastname)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [withdrawn.donor.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/rewardsadmin/')

def withdrawn(request):
    user=''
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
                user=donor
        except:
            users = dic

    if request.method == "POST":
        u = Withdrawn()
        u.name = request.POST.get("name")
        u.email = request.POST.get("email")
        u.phone = request.POST.get("phone")
        u.upi = request.POST.get("upi")
        amount = request.POST.get("amount")
        u.donor = Donor.objects.get(username=request.user)
        if(donor.currency > int(amount)):
            donor.currency=donor.currency-int(amount)
            u.amount=amount
            donor.save()
            u.save()
            messages.success(request, "Request Send Sucessfully....")
            subject = 'Your Request for Withdrawn Send Successfully : Team Novena'
            message =  """
                                %s! Thank You for Donating Organ and Saving Lives! 
                                Thanks to Donte the Organ and Blood and connect with Us.
                                A Organ and a bag of blood Can Saves Lives the lives.
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(donor.firstname+" "+donor.lastname)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [donor.email, ]
            send_mail( subject, message, email_from, recipient_list )
        else:
            messages.success(request, "You have not enough Balance to Withdrawn")
    return render(request, "withdrawn.html", {"Users": users,"Userdonor":user})

@login_required(login_url="/login_register/")
def redeem(request,pk):
    rew=Rewards.objects.get(id=pk)
    rew.status=2
    donor=Donor.objects.get(username=request.user)
    donor.currency=donor.currency+rew.currency
    donor.save()
    rew.save()
    return HttpResponseRedirect('/rewards/')

def rewardsdetails(request,num):
    user=''
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
                user=donor
        except:
            users = dic
    rewards = Rewards.objects.get(id=num)
    reward = Rewards.objects.all().filter(donor=user,status=1).exclude(id=num).order_by("-id")[:3]
    return render(request, "rewardsdetails.html", {"Reward": rewards,"Rewards": reward, "Users": users, "User": user})

def joinus(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    if request.method == "POST":
        u = Join()
        u.name = request.POST.get("name")
        u.email = request.POST.get("email")
        u.phone = request.POST.get("phone")
        u.city = request.POST.get("city")
        u.state = request.POST.get("state")
        u.pin = request.POST.get("pin")
        u.save()
        messages.success(request, "Join Us Sucessfully....")
        subject = 'Congratulations! From Now You are the member of our community: Team Novena'
        message =  """
                                %s! Thank You for Connecting with us and Saving Lives! 
                                We Comes together to saves the lives..
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """%(u.name)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [u.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(request, "joinus.html", {"Users": users})


def team(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    doctor = Doctor.objects.all()
    doctor = doctor[::-1]
    return render(request, "doctor.html", {"Users": users,'Doctor':doctor})


def blog(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    blog = Blog.objects.all()
    blog = blog[::-1]
    blogs = Blog.objects.order_by("-id")[:9]
    return render(request, "Blog.html", {"Blog": blog, "Blogs": blogs, "Users": users})


def blogdetails(request, num):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    blog = Blog.objects.get(id=num)
    try:
        prevblog = Blog.objects.get(id=num-1)
    except:
        prevblog = Blog.objects.get(id=num)
    try:
        nextblog = Blog.objects.get(id=num+1)
    except:
        nextblog = Blog.objects.get(id=num)
    blogs = Blog.objects.order_by("-id")[:3]
    return render(
        request, "blogdetails.html", {"Blog": blog,"prevBlog": prevblog,"nextBlog": nextblog, "Blogs": blogs, "Users": users}
    )


def locations(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    location = Locations.objects.all()
    location = location[::-1]
    hospital = Hospital.objects.all()
    hospital = hospital[::-1]
    return render(request, "locations.html", {"Users": users, "Locations": location,"Hospital":hospital})

def contact(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    try:
        if request.method == "POST":
            c = Contact()
            c.name = request.POST.get("name")
            c.email = request.POST.get("email")
            c.phone = request.POST.get("phone")
            c.subject = request.POST.get("subject")
            c.message = request.POST.get("message")
            c.save()
            messages.success(
                request,
                "Your Query Has Been Submitted Successfully! Our Team Will Contact You Soon!",
            )
            subject = 'Your Query Has been Submitted : Team Novena'
            message =  """
                            Thanks to Share your Query with us
                            Our Team will Contact You Soon
                            Team : Novena
                            keep In Touch with us
                            http://localhost:8000                    
                       """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [c.email, ]
            send_mail( subject, message, email_from, recipient_list )
    except:
        HttpResponseRedirect("/contact/")
    return render(request, "contact.html", {"Users": users})


def login_Register(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    bloodgroup = Stock.objects.all()
    if request.method == "POST":
        if "LOGIN" in request.POST:
            try:
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    if user.is_superuser:
                        return HttpResponseRedirect("/admin/")
                    else:
                        return HttpResponseRedirect("/profile/")
                else:
                    messages.error(request, "Invalid User Name or Password")
            except:
                return HttpResponseRedirect("/login_register/")
        if "register" in request.POST:
            try:
                actype = request.POST.get("actype")
                if actype == "Donor":
                    u = Donor()
                else:
                    u = Patient()
                u.firstname = request.POST.get("firstname")
                u.lastname = request.POST.get("lastname")
                u.username = request.POST.get("username")
                u.gender = request.POST.get("gender")
                u.email = request.POST.get("email")
                u.phone = request.POST.get("phone")
                password = request.POST.get("password")
                cpassword = request.POST.get("cpassword")
                u.bloodgroup = request.POST.get("bloodgroup")
                print(bloodgroup)
                if password == cpassword:
                    try:
                        user = User.objects.create_user(
                            username=u.username, password=password, email=u.email
                    )
                        user.save()
                        u.save()
                        messages.success(request, "Account Created Sucessfully....")
                        subject = 'Congratulations! Your Account Has been Created Successfully : Team Noven'
                        message =  """
                                %s! Your Account Has Been Created Sucessfully! 
                                Thanks to create an account with Us.
                                Team : Novena
                                keep Shopping with us
                                keep In Touch with us                    
                           """%(u.firstname+" "+u.lastname)
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [u.email, ]
                        send_mail( subject, message, email_from, recipient_list )
                        return render(request, "login.html")
                    except:
                        messages.error(request, "User Name already Exists...")
                        return render(request, "login.html")
                else:
                    messages.error(
                    request, "Password and Confirm Password does not matched!!!!"
                )
            except:
                return HttpResponseRedirect("/login_register/")
    return render(request, "login.html", {"BloodGroup": bloodgroup})


@login_required(login_url="/login_register/")
def profilePage(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect("/admin/")
    else:
        try:
            donor = Donor.objects.get(username=request.user)
            return render(request, "donorprofile.html", {"User": donor, "Users": users})
        except:
            patient = Patient.objects.get(username=request.user)
            return render(
                request, "patientprofile.html", {"User": patient, "Users": users}
            )


@login_required(login_url="/login_register/")
def updateprofile(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    doct = False

    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect("/admin/")
    else:
        try:
            user = Donor.objects.get(username=request.user)
        except:
            user = Patient.objects.get(username=request.user)
            doct = True
        if request.method == "POST":
            user.firstname = request.POST.get("firstname")
            user.lastname = request.POST.get("lastname")
            user.email = request.POST.get("email")
            user.phone = request.POST.get("phone")
            user.gender = request.POST.get("gender")
            user.addressline1 = request.POST.get("addressline1")
            user.addressline2 = request.POST.get("addressline2")
            user.addressline3 = request.POST.get("addressline3")
            if doct:
                user.reason = request.POST.get("reason")
            else:
                user.disease = request.POST.get("disease")
            if doct:
                user.doctor = request.POST.get("doctor")
            user.age = request.POST.get("age")
            user.pin = request.POST.get("pin")
            user.city = request.POST.get("city")
            user.state = request.POST.get("state")
            if request.FILES.get("pic"):
                user.pic = request.FILES.get("pic")
            user.save()
            return HttpResponseRedirect("/profile/")
    return render(
        request, "editprofile.html", {"User": user, "Doct": doct, "Users": users}
    )


@login_required(login_url="/login_register/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login_register/")


def forgetusername(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            user = User.objects.get(username=username)
            if user is not None:
                try:
                    user = Donor.objects.get(username=username)
                except:
                    user = Patient.objects.get(username=username)
                num = randint(100000, 999999)
                request.session["otp"] = num
                request.session["user"] = username
                subject = "OTP for Password Reset : Team Novena"
                message = (
                    """
                                OTP : %d
                                Team : Novena
                                Donate Blood and Organ
                                http://localhost:8000                    
                           """
                    % num
                )
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    user.email,
                ]
                send_mail(subject, message, email_from, recipient_list)
                return HttpResponseRedirect("/forgetotp/")
            else:
                messages.error(request, "Username not Found")
        except:
            messages.error(request, "Username not Found")
    return render(request, "forgetusername.html", {"Users": users})


def forgetotp(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    if request.method == "POST":
        otp = int(request.POST.get("otp"))
        sessionotp = request.session.get("otp", None)
        if otp == sessionotp:
            return HttpResponseRedirect("/forgetpassword/")
        else:
            messages.error(request, "Invalid OTP")
    return render(request, "forgetotp.html", {"Users": users})


def forgetpassword(request):
    if User.is_authenticated:
        dict = {"donor": 1}
        dic = {"super": 1}
        di= {"doctor":1}
        if User.is_superuser:
            users = dic
        try:
            try:
                patient = Patient.objects.get(username=request.user)
                users = di
            except:
                donor = Donor.objects.get(username=request.user)
                users = dict
        except:
            users = dic
    if request.method == "POST":
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        if password == cpassword:
            user = User.objects.get(username=request.session.get("user"))
            user.set_password(password)
            user.save()
            subject = 'Congratulations! Your Password Changed Successfully : Team Novena'
            message =  """
                                Thank You for Connecting
                                with us and Saving Lives! 
                                Team : Novena
                                keep In Touch with us
                                http://localhost:8000                    
                           """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect("/login/")
        else:
            messages.error(request, "Password and Confirm Doesn't Match")
    return render(request, "forgetpassword.html", {"Users": users})
