from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path("login/",login,name='login'),
   path('base/',base,name='base'),
   path('index/',index,name='index'),
   path('Logout/',Logout,name='Logout'),
   path('DoctorReg/',DoctorReg,name='DoctorReg'),
   path('addclinic/',addClinic,name='addclinic'),
   path('addslot/',addSlot,name='addslot'),
    path("pdf_view/",pdf_view,name='pdf_view'),
   path('leaves/',leaves,name='leaves'),
   path('fetch-timings/', fetch_timings, name='fetch_timings'),
   path("leavesystem/",leavesystem,name='leavesystem'),
   path("updateleave/<leave_date>/",updateleave,name='updateleave'),
   path('consultfee/',consultaion_fee,name='consultfee'),
   path('prescription_setting/',prescription_setting,name='prescription_setting'),
   path("update_prescription_setting/",update_prescription_setting,name='update_prescription_setting'),
   path("get_all_users/",get_all_users,name='get_all_users'),
   path('insert_user/',insert_user ,name='insert_user'),
   path('update_user/<int:user_id>/',update_user,name='update_user'),
   path("addpatient/",addPatient,name='addpatient'),
   path("all_patient/",all_patient,name='all_patient'),
   path("update_patient/<int:id>",update_patient,name='update_patient'),
   path("insert_medicine/",insert_medicine ,name="insert_medicine"),
   path("get_all_medicines/",get_all_medicines,name='get_all_medicines'),
   path('update_medicine/<int:doctor_medicine_id>/',update_medicine,name='update_medicine'),
   path("delete_medicine/<int:doctor_medicine_id>/",delete_medicine,name='delete_medicine'),
   path("add_lab_report/",add_lab_report,name='add_lab_report'),
   path("get_all_lab_report/",get_all_lab_report,name='get_all_lab_report'),
   path("update_lab_report/<int:investigation_id>/",update_lab_report,name='update_lab_report'),
   path("delete_lab_report/<int:investigation_id>/",delete_lab_report,name='delete_lab_report'),
   path("all_kco/",all_kco,name='all_kco'),
   path("insert_kco/",insert_kco,name='insert_kco'),
   path("update_kco/<int:id>",update_kco,name='update_kco'),
   path("all_advice/",all_advice,name='all_advice'),
   path("insert_advice/",insert_advice,name='insert_advice'),
   path("update_advice/<int:id>",update_advice,name='update_advice'),
   path("all_instruction/",all_instruction,name='all_instruction'),
   path("insert_instruction/",insert_instruction,name='insert_instruction'),
   path("update_instruction/<int:id>",update_instruction,name='update_instruction'),
   path("all_diseases/",all_diseases,name='all_diseases'),
   path("insert_disease/",insert_disease,name='insert_disease'),
   path("update_disease/<int:id>",update_disease,name='update_disease'),
   path("all_allergy/",all_allergy,name='all_allergy'),
   path("insert_allergy/",insert_allergy,name='insert_allergy'),
   path("update_allergy/<int:id>",update_allergy,name='update_allergy'),
   path('clinic_pdf/', clinic_pdf, name='clinic_pdf'),
   path('proxy-pdf/', proxy_pdf, name='proxy_pdf'),
   path('get_all_doctor_appointments/',get_all_doctor_appointments,name='get_all_doctor_appointments'),
   path("fetch_data/",fetch_data,name='fetch_data'),
   path('initial_assesment/<int:appointment_id>',initial_assesment,name='initial_assesment'),
   path('update_initial_assesment/',update_initial_assesment,name='update_initial_assesment'),
   path('consultation/<int:id>/', Consultation, name='consultation'),  # Define URL pattern with 'id' parameter
   path('for_user/<int:id>/', for_user, name='for_user'),
   path("patient_history/<int:id>",patient_history,name='patient_history'),
   path("patientselect/<int:id>",patientselect,name='patientselect'),
   path("add_member/",add_member,name='add_member'),
   path('paid/', paid, name='paid'),
   path('get_pdf_link/', get_pdf_link, name='get_pdf_link'),
   path('get_states/', get_states, name='get_states'),
   path('get_cities/', get_cities, name='get_cities'),
   path('planinfo/',planinfo,name='planinfo'),
   path('subscriptioninfo/',subscriptioninfo,name='subscriptioninfo'),
   path('popup/',popup,name='popup'),
   path('approvePharmacy/',approvePharmacy,name='approvePharmacy'),
   path('get_all_pharmacist/',get_all_pharmacist,name='get_all_pharmacist'),
   path('toggle_pharmacist_status/',toggle_pharmacist_status,name='toggle_pharmacist_status'),
   path('Add_pharmacist/',Add_pharmacist,name='Add_pharmacist'),
   path('get_all_laboratory/',get_all_laboratory,name='get_all_laboratory'),
   path('toggle_laboratory_status/',toggle_laboratory_status,name='toggle_laboratory_status'),
   path('Add_laboratory/',Add_laboratory,name='Add_laboratory'),
   path('showDeals/',showDeals,name='showDeals'),
   path('handle_deal_action/',handle_deal_action, name='handle_deal_action'),
   path('create_death_certificate/',create_death_certificate,name='create_death_certificate'),
   path('fetch_patient_list/',fetch_patient_list,name='fetch_patient_list'),
   path('fetch_selected_patient_details/',fetch_selected_patient_details,name='fetch_selected_patient_details'),
   path('generate_deathCertificate_pdf/',generate_deathCertificate_pdf,name='generate_deathCertificate_pdf'),
   path('medical_certificate/',medical_certificate,name='medical_certificate'),
   path('update_certificate_body/',update_certificate_body,name='update_certificate_body'),
   path('generate_MedicalCertificate_pdf/',generate_MedicalCertificate_pdf,name='generate_MedicalCertificate_pdf'),
   path('add_daycare/',add_daycare,name='add_daycare'),
   path('daycarebillcharges/',daycarebillcharges,name='daycarebillcharges'),
   path('daycare_finalize/',daycare_finalize,name='daycare_finalize'),
   path('get_unpaid_bills/',get_unpaid_bills,name='get_unpaid_bills'),
   path('daycarebillpdf/<int:consultationid>/',daycarebillpdf,name='daycarebillpdf'),
   path('daycarepayment/',daycarepayment,name='daycarepayment'),

]
