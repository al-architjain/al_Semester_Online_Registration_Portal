from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

import datetime

current_date = datetime.datetime.now()

class Board(models.Model):
    name = models.CharField(primary_key=True, max_length=12)
    id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=12)
    id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100)

class UGClass(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=25)
    full_name = models.CharField(max_length=100)

class UGBranch(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    full_name = models.CharField(max_length=400)
    code = models.CharField(max_length=10)
    section = models.CharField(max_length=5)

class Subjects(models.Model):
    classname = models.ForeignKey(UGClass, on_delete=models.CASCADE)
    branch = models.ForeignKey(UGBranch, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=20)
    year = models.IntegerField()




class StudentBasicInfo(models.Model):
    user_id = models.OneToOneField(
        User, on_delete=models.PROTECT, default=0
    )
    #
    # Personal Details
    student_name_eng = models.CharField(max_length=60)
    student_name_hindi = models.CharField(max_length=60, null=True)
    email = models.EmailField()
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'other')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    date_of_birth = models.DateField(max_length=8)
    religion = models.CharField(max_length=30)
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    student_contact = models.IntegerField(null=True)
    aadhar_no = models.IntegerField(unique='True', null=True)
    area_choice = (
        ('Rural', 'Rural'),
        ('Urban', 'Urban')
    )

    area = models.CharField(max_length=10, choices=area_choice)
    bonafide_country = models.CharField(max_length=30)
    bonafide_state = models.CharField(max_length=30)
    region = models.CharField(max_length=25, choices=region_choice)
    nearest_railway_st = models.CharField(max_length=70)
    correspondence_add = models.CharField(max_length=1000)
    permanent_add = models.CharField(max_length=1000)
    nearest_railway_st = models.CharField(max_length=70)
    #
    # Academics Details
    year_of_admission = models.IntegerField()
    jee_roll_no = models.BigIntegerField()
    jee_score = models.IntegerField()
    jee_AI_rank = models.IntegerField()
    jee_category_rank = models.IntegerField()
    admission_category = models.CharField(max_length=10)
    intermediate_pass_country = models.CharField(max_length=30)
    intermediate_pass_state = models.CharField(max_length=30)
    intermediate_percentage = models.DecimalField(max_digits=5, decimal_places=3)
    intermediate_pass_year = models.CharField(max_length=4)
    school_type_choices = (
        ('Government', 'Government School'),
        ('Private', 'Private School')
    )
    intermediate_school_type = models.CharField(max_length=20, choices=school_type_choices)
    intermediate_school_area = models.CharField(max_length=10, choices=area_choice)
    intermediate_school_name = models.CharField(max_length=60)
    intermediate_school_board = models.ForeignKey(Board, on_delete=models.PROTECT)
    ug_class = models.ForeignKey(UGClass, on_delete=models.PROTECT)
    ug_branch = models.ForeignKey(UGBranch, on_delete=models.PROTECT)
    # section = models.CharField(max_length=25)
    hosteler = models.BooleanField()
    hostel_choices=(
        ('KBH', 'Kailash Boys Hostel'),
        ('Satpura', 'Satpuara Hostel'),
        ('Himadri', 'Himadri Boys Hostel'),
        ('Himgiri', 'Himgiri Boys Hostel'),
        ('NBH', 'Neelkanth Boys Hostel'),
        ('MMH', 'Manimahesh Boys Hostel'),
        ('VBH', 'Vindhyanchal Boys Hostel'),
        ('DBH', 'Dauladhar Boys Hostel'),
        ('AGH', 'Ambika Girls Hostel'),
        ('PGH', 'Parvati Girls Hostel'),
    )
    hostel_name = models.CharField(max_length=50, choices=hostel_choices)
    entry_no = models.IntegerField(default=None)
    reg_no = models.CharField(max_length=50)
    roll_no = models.CharField(unique=True, max_length=10)
    #
    # Guardian Details
    father_name = models.CharField(max_length=60)
    father_contact = models.IntegerField()
    father_email = models.EmailField()
    mother_name = models.CharField(max_length=60)
    mother_contact = models.IntegerField()
    mother_email = models.EmailField()
    guardian_name = models.CharField(max_length=60)
    guardian_contact = models.IntegerField()
    guardian_email = models.EmailField()
    family_income = models.IntegerField(default=0)
    fee_waiver_claim = models.CharField(max_length=60)

class StudentMedicalInfo(models.Model):
    student_id = models.OneToOneField(
        StudentBasicInfo, on_delete=models.CASCADE, default=0
    )
    age = models.IntegerField()
    identification_mark = models.CharField(max_length=40)
    major_illness = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=5)
    vision = models.CharField(max_length=3)
    height_in_cm = models.IntegerField()
    # weight_kg = models.IntegerField()
    past_mental_illness = models.CharField(max_length=30)
    clour_blindness = models.CharField(max_length=10)
    any_other_defect = models.CharField(max_length=30)


class StudentFirstFeeStatus(models.Model):
    #
    student_id = models.OneToOneField(
        StudentBasicInfo, on_delete=models.CASCADE
    )
    fee_josaa_amount = models.IntegerField()
    fee_josaa_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NITH_amount = models.IntegerField()
    fee_nith_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NIT_receipt_no = models.CharField(max_length=25)


class Result(models.Model):
    student_id = models.OneToOneField(
        StudentBasicInfo, on_delete=models.CASCADE
    )
    semester = models.IntegerField(),
    sgpi = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(0.00))
    cgpi = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(0.00))



class Documents(models.Model):
    year = models.IntegerField(default=current_date.year)
    document = models.CharField(max_length=500)
    stud_doc = models.ManyToManyField(StudentBasicInfo, through='DocumentInfo')


class DocumentInfo(models.Model):
    stud_id = models.ForeignKey(StudentBasicInfo, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Documents, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)
