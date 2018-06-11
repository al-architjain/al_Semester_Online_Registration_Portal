from django.db import models

class student_basic_info(models.Model):

    jee_roll_no=models.BigIntegerField(primary_key=True)
    year_of_admission=models.IntegerField(primary_key=True)
    student_name_eng=models.CharField(max_length=60)
    #student_name_hindi=models.CharFeild()

     gender_choices=(
        ('M','Male'),
        ('F','Female'),
        ('O','others')
        )
    gender=models.CharField(max_length=1,choices=gender_choices)

    date_of_birth=models.DateField(max_length=8)

    father_name=models.CharField(max_length=60)
    mother_name==models.CharField(max_length=60)

    jee_AI_rank=models.IntegerField()
    jee_category_rank=models.IntegerField()

    bonafied_state=models.CharField(max_length=30)
    intermediate_pass_state=models.CharField(max_length=30)
    intermediate_percentage=models.DecimalFiels(max_digits=5,decimal_places=3)
    intermediate_school=models.CharField(max_length=100)

    school_type=(
            ('govt','goverment_school'),
            ('private','private_school')
        )
    type_school=models.CharField(max_length=20,choices=school_type)

    #make chane in year field
    year_12_pass=models.CharField(max_length=4)

    board=models.CharField(max_length=15)
    jee_score=models.IntegerField(max_length=4)

    main_category=models.CharField(max_length=10)
    admission_category=models.CharField(max_length=10)
    aadhar_no=models.IntegerField(unique='True')

    class_choice=(
            ('b.tech','b.tech'),
            ('m.tech','m.tech'),
            ('dual_degree','dual_degree')
        )
    class_=models.CharField(max_length=20,choices=class_choice)

    branch=models.CharField(max_length=20)

    #
    religion=models.CharField(max_length=30)

    hostel_choice=(
           ('Yes','Yes'),
           ('No','No')
        )
    hostel_req=models.CharField(max_length=10,choices=hostel_choice)
    #
    region_choice=(
        ('Rural','Rural'),
        ('Urban','Urban')
    )
    region=models.CharField(choices=region_choice)
    nearest_railway_st=models.CharField(max_length=70)
    correspondence_add=models.CharField(max_length=1000)
    permanent_add=models.CharField(max_length=10)
    ####### find a better way to save contacts
    contact_father=models.IntegerField(max_length=10)
    contact_mother=
    contact_candidate=
    contact_other=

    #
    fee_josaa_amount=models.IntegerField()
    fee_josaa_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NITH_amount=models.IntegerField()
    fee_NIT_receipt_no=models.CharField()
    fee_nith_date=models.DateField(auto_now=False,auto_now_add=False,default=None)

    #
    entry_no=models.charfield(default=None)
    section=models.CharField()
    subsection=models.CharField()


class DocumentInfo(models.Models) :
    jee_roll_no=models.BigIntegerField(primary_key=True)
    year_of_admission=models.IntegerField(primary_key=True)

    ###documents
    provisional_admission_letter=models.BooleanField(default=False)
    jee_score_card=models.BooleanField(default=False)
    jee_admit_card=models.BooleanField(default=False)
    class_10_certificate=models.BooleanField(default=False)
    class_12_marksheet=models.BooleanField(default=False)
    character_certificate=models.BooleanField(default=False)
    migration_certificate=models.BooleanField(default=False)
    remaining_Instititute_fee=models.BooleanField(default=False)
    hostel_fee=models.BooleanField(default=False)
    medical_fitness_certificate=models.BooleanField(default=False)
    certificate_of_disability=models.BooleanField(default=False)
    certificate_of_category=models.BooleanField(default=False)
    undertaking=models.BooleanField(default=False)
    affidavit_year_gap=models.BooleanField(default=False)
    affidavit_anti_ragging=models.BooleanField(default=False)
    parent_affidavit_anti_ragging=models.BooleanField(default=False)
    ##
    fee_status_josaa==models.BooleanField(default=False)
    fee_status_nit_hamirpur=models.BooleanField(default=False)


class StudentMedicalInfo(models.Model) :
    jee_roll_no=models.BigIntegerField(primary_key=True)
    year_of_admission=models.IntegerField(primary_key=True)

#######define age again
    date_of_birth=models.DateField()
    age=models.CharField(max_length=20)

    #
    sex=models.CharField(max_length=1)
    identification_mark=models.CharField(max_length=40)
    mojor_illness=models.CharField(max_length=40)
    vision=models.CharField(max_length=3)
    hearing=models.CharField(max_length=10)
    height_in_cm=models.IntegerField()
    weight_kg=models.IntegerField()
    past_mental_illness=models.CharField(max_length=30)
    past_epileptic_fit=models.CharField(max_length=30)
    chest_inspiration_in_cm=models.IntegerField()
    chest_expiration_in_cm=models.IntegerField()

    vision_without_glass_rt_eye=models.CharField(max_length=3)
    vision_without_glass_lt_eye=models.CharField(max_length=3)
    clour_blindness=models.CharField(max_length=10)

    abdomen_liver=models.CharField(max_length=30)
    abdomen_spleen=models.CharField(max_length=30)
    respiratory_system=models.CharField(max_length=30)
    nervous_system=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=5)

    heart_sound=models.CharField(max_length=30)
    heart_murmur=models.CharField(max_length=30)

    hernia=models.CharField(max_length=30)
    hydrocele=models.CharField(max_length=30)

    any_other_defect=models.CharField(max_length=30)































