from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

from datetime import datetime
import os


## Function to calculate current year :)
def currYear():
    now = datetime.now()
    return now.year


## For profile picture
def get_image_path(instance, filename):
    return os.path.join(str(instance.id), 'profile_pic.jpg')


##################################################################
############################# TABLES #############################
##################################################################

class Board(models.Model):
    id = models.SmallIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=16)
    full_name = models.CharField(max_length=128)
    #
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.SmallIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=16)
    full_name = models.CharField(max_length=64)
    #
    def __str__(self):
        return self.name




class UGClass(models.Model):
    id = models.SmallIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=16)
    full_name = models.CharField(max_length=64)
    #
    def __str__(self):
        return self.name

class UGBranch(models.Model):
    id = models.SmallIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=32)
    full_name = models.CharField(max_length=128)
    code = models.CharField(max_length=16, unique=True)
    section = models.CharField(max_length=8, unique=True)
    #
    def __str__(self):
        return self.full_name

class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    year_onwards = models.SmallIntegerField()
    classname = models.ForeignKey(UGClass, on_delete=models.CASCADE,db_column='class')
    branch = models.ForeignKey(UGBranch, on_delete=models.CASCADE,db_column='branch')
    semester_choice = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    )
    semester = models.IntegerField(choices=semester_choice)
    sub_code = models.CharField(max_length=16)
    sub_name = models.CharField(max_length=256)
    sub_L = models.SmallIntegerField()
    sub_T = models.SmallIntegerField()
    sub_P = models.SmallIntegerField()
    sub_C = models.SmallIntegerField()
    #
    def __str__(self):
        return self.sub_name




class Documents(models.Model):
    #default autofield id is pk
    doc_name = models.CharField(max_length=512)
    doc_imp_choice=(
        ('M' , 'Mandatory'),
        ('O' , 'Optional'),
        ('NA', 'Not Applicable')
    )
    doc_imp = models.CharField(max_length=2, default = 'M', choices=doc_imp_choice)
    #
    def __str__(self):
        return self.doc_name


class StudentInfo(models.Model):
    #defualt user is pk
    user = models.OneToOneField(
        User, on_delete=models.PROTECT
    )

    # Student Image
    img = models.ImageField(upload_to=get_image_path, default = 'def_profile_pic.jpg')
    year_of_admission = models.SmallIntegerField(default=currYear)
    active_status = models.BooleanField(default=True)  # (1 is active) and (0 is inactive)
    ug_sem = models.SmallIntegerField(default=1)

    # Documents
    stud_doc = models.ManyToManyField(Documents, through='DocumentInfo')
    #
    # Institute Info
    insti_choices = (
        ('NIT Hamirpur', 'NIT Hamirpur'),
        ('IIIT Una', 'IIIT Una'),
    )
    institute = models.CharField(max_length=16, choices=insti_choices)
    #
    # Personal Details #
    #
    #
    name_eng = models.CharField(max_length=64)
    name_hindi = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField()
    gender_choices = (
        ('---------', '---------'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=8, choices=gender_choices)
    dob = models.DateField()
    religion = models.CharField(max_length=16)
    category_main = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='main', db_column='Main Category')
    contact = models.CharField(max_length=16)
    aadhar_no = models.CharField(max_length=16, unique=True, null=True)
    area_choice = (
        ('---------', '---------'),
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    )
    area = models.CharField(max_length=16, choices=area_choice)
    b_country = models.CharField(max_length=32)
    b_state = models.CharField(max_length=32)
    nearest_rs = models.CharField(max_length=64, null=True, blank=True)
    corr_addr = models.CharField(max_length=256)
    perm_addr = models.CharField(max_length=256)
    #
    #
    # Academics Details
    #
    #
    jee_roll_no = models.BigIntegerField()
    jee_score = models.PositiveIntegerField()
    jee_ai_rank = models.PositiveIntegerField()
    jee_cat_rank = models.PositiveIntegerField(null=True, blank=True)
    category_admission = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='admission', db_column='Admitted Category')
    int_country = models.CharField(max_length=32)
    int_state = models.CharField(max_length=32)
    int_percentage = models.DecimalField(max_digits=5, decimal_places=3, db_column='12th Percentage')
    int_pass_year = models.IntegerField(default=currYear, db_column='10+2 Pass Year')
    school_type_choices = (
        ('---------', '---------'),
        ('Government', 'Government School'),
        ('Private', 'Private School')
    )
    int_school_type = models.CharField(max_length=16, choices=school_type_choices, db_column='12th School type')
    int_school_area = models.CharField(max_length=8, choices=area_choice,db_column='12th School Area')
    int_school_name = models.CharField(max_length=64, db_column='12th School name')
    int_school_board = models.ForeignKey(Board, on_delete=models.PROTECT, db_column='12th Board')
    ug_class = models.ForeignKey(UGClass, on_delete=models.PROTECT, db_column='UGClass')
    ug_branch = models.ForeignKey(UGBranch, on_delete=models.PROTECT, db_column='UGBranch')
    hosteler = models.BooleanField()
    hostel_choices=(
        ('KBH', 'Kailash Boys Hostel'),
        ('Satpura', 'Satpura Hostel'),
        ('Himadri', 'Himadri Boys Hostel'),
        ('Himgiri', 'Himgiri Boys Hostel'),
        ('NBH', 'Neelkanth Boys Hostel'),
        ('MMH', 'Manimahesh Boys Hostel'),
        ('VBH', 'Vindhyanchal Boys Hostel'),
        ('DBH', 'Dauladhar Boys Hostel'),
        ('AGH', 'Ambika Girls Hostel'),
        ('PGH', 'Parvati Girls Hostel'),
    )
    hostel_name = models.CharField(max_length=16, choices=hostel_choices, null=True, blank=True)
    entry_no = models.PositiveIntegerField(unique=True)
    reg_no = models.CharField(unique=True,max_length=64)
    roll_no = models.CharField(unique=True, max_length=16)
    #
    #
    # Guardian Details
    #
    #
    father_name = models.CharField(max_length=64)
    father_contact = models.CharField(max_length=16,null=True,blank=True)
    father_email = models.EmailField(null=True,blank=True)
    mother_name = models.CharField(max_length=64)
    mother_contact = models.CharField(max_length=16,null=True,blank=True)
    mother_email = models.EmailField(null=True,blank=True)
    guardian_name = models.CharField(max_length=64,null=True,blank=True)
    guardian_contact = models.CharField(max_length=16,null=True,blank=True)
    guardian_email = models.EmailField(null=True,blank=True)
    family_income = models.PositiveIntegerField(default=0)
    waiver_choices = (
        ('Not Claimed', 'Not Claimed'),
        ('SC/ST/PwD', 'SC/ST/PwD'),
        ('Income Less than 1 Lakhs', 'Income Less than 1 Lakhs'),
        ('Income between 1 and 5 Lakhs', 'Income between 1 and 5 Lakhs'),
    )
    fee_waiver = models.CharField(max_length=64, choices=waiver_choices)


class StudentFirstFeeStatus(models.Model):
    #default id is pk
    student = models.OneToOneField(
        StudentInfo, on_delete=models.CASCADE
    )
    fee_josaa_amount = models.PositiveIntegerField()
    fee_josaa_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NITH_amount = models.PositiveIntegerField()
    fee_nith_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_nith_receipt_no = models.CharField(max_length=32)
    fee_total = models.PositiveIntegerField()


class DocumentInfo(models.Model):
    #default id is pk
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)





class Result(models.Model):
    #default id is pk
    roll_no = models.OneToOneField(StudentInfo, to_field='roll_no', on_delete=models.CASCADE, unique=True, db_column='roll_no')
    semester_choice = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    semester = models.SmallIntegerField(choices=semester_choice, default=1)
    sgpi = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal(0.00))
    cgpi = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal(0.00))




class Due(models.Model):
    #defualt id is pk
    roll_no = models.OneToOneField(StudentInfo,to_field='roll_no',on_delete=models.CASCADE, unique=True, db_column='roll_no')
    library_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
    hostel_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
    academic_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))








# EXPIRED TABLES:
#
# class StudentMedicalInfo(models.Model):
#     #default id is pk
#     student = models.OneToOneField(
#         StudentInfo, on_delete=models.CASCADE, default=0
#     )
#     age = models.SmallIntegerField()
#     height = models.SmallIntegerField()     #(in cm)
#     # weight_kg = models.IntegerField()
#     blood_group = models.CharField(max_length=4)
#     id_mark = models.CharField(max_length=32, null=True, blank=True)
#     major_illness = models.CharField(max_length=64,null=True, blank=True)
#     past_mental_illness = models.CharField(max_length=64,null=True, blank=True)
#     vision = models.CharField(max_length=8,null=True, blank=True)
#     clour_blindness = models.CharField(max_length=32,null=True, blank=True)
#     other_defect = models.CharField(max_length=64,null=True, blank=True)