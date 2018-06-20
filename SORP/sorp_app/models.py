from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


from datetime import datetime
## Function to calculate current year :)
def currYear():
    now = datetime.now()
    return now.year
##
## For profile picture
import os
def get_image_path(instance, filename):
    return os.path.join(str(instance.id), 'profile_pic.jpg')
##

class Board(models.Model):
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=12)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=12)
    full_name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class UGClass(models.Model):
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=25)
    full_name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class UGBranch(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    full_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    section = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Subjects(models.Model):
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
    sub_code = models.CharField(primary_key=True,max_length=20)
    sub_name = models.CharField(max_length=200)


    def __str__(self):
        return self.classname


class Documents(models.Model):
    doc_name = models.CharField(max_length=500)
    doc_imp_choice=(
        ('M' , 'Mandatory'),
        ('O' , 'Optional'),
        ('NA', 'Not Applicable')
    )
    doc_imp = models.CharField(max_length=2, default = 'M', choices=doc_imp_choice)


class StudentInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT
    )
    #
    #Student Image
    img = models.ImageField(upload_to=get_image_path, default = 'def_profile_pic.jpg')
    year_of_admission = models.IntegerField(default=currYear)
    active_status = models.BooleanField(default=True)  # (1 is active) and (0 is inactive)
    ug_sem = models.SmallIntegerField(default=1)
    # Documents
    stud_doc = models.ManyToManyField(Documents, through='DocumentInfo')
    #
    # Personal Details
    name_eng = models.CharField(max_length=60)
    name_hindi = models.CharField(max_length=60, null=True)
    email = models.EmailField()
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    dob = models.DateField()
    religion = models.CharField(max_length=20)
    category_main = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='main', db_column='Main Category')
    contact = models.CharField(max_length=20, null=True)
    aadhar_no = models.CharField(max_length=16, unique='True', null=True)
    area_choice = (
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    )
    area = models.CharField(max_length=10, choices=area_choice)
    b_country = models.CharField(max_length=30)
    b_state = models.CharField(max_length=30)
    nearest_rs = models.CharField(max_length=70)
    corr_addr = models.CharField(max_length=1000)
    perm_addr = models.CharField(max_length=1000)
    #
    #
    # Academics Details
    #
    #
    jee_roll_no = models.BigIntegerField()
    jee_score = models.PositiveIntegerField()
    jee_ai_rank = models.PositiveIntegerField()
    jee_cat_rank = models.PositiveIntegerField(null=True)
    category_admission = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='admission', db_column='Admitted Category')
    int_country = models.CharField(max_length=30)
    int_state = models.CharField(max_length=30)
    int_percentage = models.DecimalField(max_digits=5, decimal_places=3, db_column='12th Percentage')
    int_pass_year = models.IntegerField(default=currYear, db_column='10+2 Pass Year')
    school_type_choices = (
        ('Government', 'Government School'),
        ('Private', 'Private School')
    )
    int_school_type = models.CharField(max_length=20, choices=school_type_choices, db_column='12th School type')
    int_school_area = models.CharField(max_length=10, choices=area_choice,db_column='12th School Area')
    int_school_name = models.CharField(max_length=60, db_column='12th School name')
    int_school_board = models.ForeignKey(Board, on_delete=models.PROTECT, db_column='12th Board')
    ug_class = models.ForeignKey(UGClass, on_delete=models.PROTECT, db_column='UGClass')
    ug_branch = models.ForeignKey(UGBranch, on_delete=models.PROTECT, db_column='UGBranch')
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
    hostel_name = models.CharField(max_length=50, choices=hostel_choices, null=True)
    entry_no = models.PositiveIntegerField(unique=True,default=None)
    reg_no = models.CharField(unique=True,max_length=50)
    roll_no = models.CharField(unique=True, max_length=10)
    #
    #
    # Guardian Details
    #
    #
    father_name = models.CharField(max_length=60)
    father_contact = models.CharField(max_length=20,null=True,blank=True)
    father_email = models.EmailField(null=True,blank=True)
    mother_name = models.CharField(max_length=60)
    mother_contact = models.CharField(max_length=20,null=True,blank=True)
    mother_email = models.EmailField(null=True,blank=True)
    guardian_name = models.CharField(max_length=60,null=True,blank=True)
    guardian_contact = models.CharField(max_length=20,null=True,blank=True)
    guardian_email = models.EmailField(null=True,blank=True)
    family_income = models.PositiveIntegerField(default=0)
    fee_waiver = models.CharField(max_length=60)


class StudentMedicalInfo(models.Model):
    student = models.OneToOneField(
        StudentInfo, on_delete=models.CASCADE, default=0
    )
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()     #(in cm)
    # weight_kg = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    id_mark = models.CharField(max_length=30, null=True)
    major_illness = models.CharField(max_length=40,null=True)
    past_mental_illness = models.CharField(max_length=30,null=True)
    vision = models.CharField(max_length=3,null=True)
    clour_blindness = models.CharField(max_length=10,null=True)
    other_defect = models.CharField(max_length=50,null=True)


class StudentFirstFeeStatus(models.Model):
    student = models.OneToOneField(
        StudentInfo, on_delete=models.CASCADE
    )
    fee_josaa_amount = models.PositiveIntegerField()
    fee_josaa_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NITH_amount = models.PositiveIntegerField()
    fee_nith_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_nith_receipt_no = models.CharField(max_length=25)
    fee_total = models.PositiveIntegerField()


class DocumentInfo(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)


class Result(models.Model):
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
    roll_no = models.OneToOneField(StudentInfo,to_field='roll_no',on_delete=models.CASCADE, unique=True, db_column='roll_no')
    library_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
    hostel_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
    academic_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
