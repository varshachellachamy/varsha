from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view),
    path('patientsignup', views.patient_signup_view),

    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'), name='logout'),

    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),

    path('admin-doctor', views.admin_doctor_view, name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view, name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,
         name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view, name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view, name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view, name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view, name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view, name='reject-doctor'),
    path('admin-view-doctor-specialisation', views.admin_view_doctor_specialisation_view,
         name='admin-view-doctor-specialisation'),

    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view, name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,
         name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view, name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view, name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view, name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view, name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view, name='reject-patient'),

]

