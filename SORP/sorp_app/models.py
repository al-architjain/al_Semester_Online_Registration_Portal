from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


from datetime import datetime
## Function to calculate current year :)
def currYear():
    now = datetime.now()
    return now.year
##


class Board(models.Model):
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=12)
    full_name = models.CharField(max_length=100)

class Category(models.Model):
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=12)
    full_name = models.CharField(max_length=60)

class UGClass(models.Model):
    id = models.PositiveIntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=25)
    full_name = models.CharField(max_length=60)

class UGBranch(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    full_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    section = models.CharField(max_length=5)

class Subjects(models.Model):
    classname = models.ForeignKey(UGClass, on_delete=models.CASCADE)
    branch = models.ForeignKey(UGBranch, on_delete=models.CASCADE)
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


class Documents(models.Model):
    doc_name = models.CharField(max_length=500)
    doc_imp = models.CharField(max_length=2, default = 'M', choices=(('M', 'Mandatory'), ('O', 'Optional'),('NA', 'Not Applicable')))


class StudentInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, default=0
    )
    #
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
    category_main = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='main')
    contact = models.CharField(max_length=20, null=True)
    aadhar_no = models.CharField(max_length=16, unique='True', null=True)
    area_choice = (
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    )
    area = models.CharField(max_length=10, choices=area_choice)
    bonafide_country = models.CharField(max_length=30)
    bonafide_state = models.CharField(max_length=30)
    nearest_railway_st = models.CharField(max_length=70)
    correspondence_add = models.CharField(max_length=1000)
    permanent_add = models.CharField(max_length=1000)
    #
    # Academics Details
    year_of_admission = models.IntegerField(default=currYear)
    jee_roll_no = models.BigIntegerField()
    jee_score = models.PositiveIntegerField()
    jee_AI_rank = models.PositiveIntegerField()
    jee_category_rank = models.PositiveIntegerField(null=True)
    category_admission = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='admission')
    intermediate_country = models.CharField(max_length=30)
    intermediate_state = models.CharField(max_length=30)
    intermediate_percentage = models.DecimalField(max_digits=5, decimal_places=3)
    intermediate_pass_year = models.IntegerField(default=currYear)
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
    ug_sem = models.SmallIntegerField(choices=semester_choice, default=1)
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
    active_status = models.BooleanField(default=True)   # (1 is active) and (0 is inactive)
    #
    # Guardian Details
    father_name = models.CharField(max_length=60)
    father_contact = models.CharField(max_length=20)
    father_email = models.EmailField()
    mother_name = models.CharField(max_length=60)
    mother_contact = models.CharField(max_length=20)
    mother_email = models.EmailField()
    guardian_name = models.CharField(max_length=60)
    guardian_contact = models.CharField(max_length=20)
    guardian_email = models.EmailField()
    family_income = models.PositiveIntegerField(default=0)
    fee_waiver_claim = models.CharField(max_length=60)

class StudentMedicalInfo(models.Model):
    student_id = models.OneToOneField(
        StudentInfo, on_delete=models.CASCADE, default=0
    )
    age = models.IntegerField()
    identification_mark = models.CharField(max_length=40)
    major_illness = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=5)
    vision = models.CharField(max_length=3)
    height_in_cm = models.SmallIntegerField()
    # weight_kg = models.IntegerField()
    past_mental_illness = models.CharField(max_length=30)
    clour_blindness = models.CharField(max_length=10)
    any_other_defect = models.CharField(max_length=30)


class StudentFirstFeeStatus(models.Model):
    student_id = models.OneToOneField(
        StudentInfo, on_delete=models.CASCADE
    )
    fee_josaa_amount = models.PositiveIntegerField()
    fee_josaa_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NITH_amount = models.PositiveIntegerField()
    fee_nith_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    fee_NIT_receipt_no = models.CharField(max_length=25)
    fee_total = models.PositiveIntegerField()


class DocumentInfo(models.Model):
    stud_id = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Documents, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)


class Result(models.Model):
    roll_no = models.OneToOneField(StudentInfo, to_field='roll_no', on_delete=models.CASCADE, unique=True)
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
    roll_no = models.OneToOneField(StudentInfo,to_field='roll_no',on_delete=models.CASCADE, unique=True)
    library_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
    hostel_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
    academic_due = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal(0.00))
