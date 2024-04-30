from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from BloodOrganDonation import settings

admin.site.site_header='Novena'

from django.contrib.auth.views import LogoutView,LoginView
from MainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/', views.About),
    path('donateblood/', views.donateblood),
    path('donateorgan/', views.donateorgan),
    path('donatehistory/', views.donatehistory),
    path('requestblood/', views.requestblood),
    path('requestorgan/', views.requestorgan),
    path('requesthistory/', views.requesthistory),
    path('blooddonationadmin/', views.blooddonationadmin),
    path('bloodrequestadmin/', views.bloodrequestadmin),
    path('bloodhistoryadmin/', views.bloodhistoryadmin),
    path('organdonationadmin/', views.organdonationadmin),
    path('organrequestadmin/', views.organrequestadmin),
    path('organhistoryadmin/', views.organhistoryadmin),
    path('approve-donation/<int:pk>', views.approve_donation_view,name='approve-donation'),
    path('done-donation/<int:pk>', views.done_donation_view,name='done-donation'),
    path('reject-donation/<int:pk>', views.reject_donation_view,name='reject-donation'),
    path('update-approve-status/<int:pk>', views.update_approve_status_view,name='update-approve-status'),
    path('update-done-status/<int:pk>', views.update_done_status_view,name='update-done-status'),
    path('update-reject-status/<int:pk>', views.update_reject_status_view,name='update-reject-status'),
    path('approve-donation_organ/<int:pk>', views.approve_donation_view_organ,name='approve-donation_organ'),
    path('done-donation_organ/<int:pk>', views.done_donation_view_organ,name='done-donation_organ'),
    path('reject-donation_organ/<int:pk>', views.reject_donation_view_organ,name='reject-donation_organ'),
    path('update-approve-status_organ/<int:pk>', views.update_approve_status_view_organ,name='update-approve-status_organ'),
    path('update-done-status_organ/<int:pk>', views.update_done_status_view_organ,name='update-done-status_organ'),
    path('update-reject-status_organ/<int:pk>', views.update_reject_status_view_organ,name='update-reject-status_organ'),
    path('bloodstock/', views.bloodstock),
    path('organstock/', views.organstock),
    path('organstockdetails/<int:num>/', views.organstockdetails),
    path('services/<int:num>/', views.services),
    path('joinus/', views.joinus),
    path('team/', views.team),
    path('blogdetails/<int:num>/', views.blogdetails),
    path('blog/', views.blog),
    path('rewardsadmin/', views.rewardsadmin),
    path('done-withdrawn/<int:pk>', views.done_withdrawn_view,name='done-withdrawn'),
    path('rewards/', views.rewards),
    path('withdrawn/', views.withdrawn),
    path('rewardsdetails/<int:num>/', views.rewardsdetails),
    path('redeem/<int:pk>', views.redeem,name='redeem'),
    path('locations/', views.locations),
    path('profile/', views.profilePage),
    path('editprofile/', views.updateprofile),
    path('contact/', views.contact),
    path('login_register/', views.login_Register),
    path('logout/', views.logout),
    path('forgetusername/', views.forgetusername),
    path('forgetotp/', views.forgetotp),
    path('forgetpassword/', views.forgetpassword),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
