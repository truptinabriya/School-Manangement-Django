from django.db import models

# Create your models here.

class Student(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    # Contact Information
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    # Parent/Guardian Information
    guardian_name = models.CharField(max_length=100)
    guardian_phone_number = models.CharField(max_length=15)
    guardian_email = models.EmailField(max_length=100)

    # Academic Information
    roll_number = models.CharField(max_length=15)
    admission_date = models.DateField()
    current_class = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Class {self.current_class})"
    
    

    
# Student Admission model:

class StudentAdmission(models.Model):
    ADMISSION_CHOICES = (
        ('Class1', 'Class 1'),
        ('Class2', 'Class 2'),
    )
    
    ADMISSION_GROUP_CHOICES = (
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Commerce', 'Commerce'),
        ('General', 'General'),
    )
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    RELIGION_CHOICES = (
        ('Hindu', 'Hindu'),
        ('Christianity', 'Christianity'),
        ('Buddhism', 'Buddhism'),
        ('Hinduism', 'Hinduism'),
    )
    
    NATIONALITY_CHOICES = (
        ('Indian', 'Indian'),
    )
    
    admissionFor = models.CharField(max_length=7, choices=ADMISSION_CHOICES, default='Class1')
    admissionGroup = models.CharField(max_length=9, choices=ADMISSION_GROUP_CHOICES, default='Science')
    studentFirstName = models.CharField(max_length=100)
    studentLastName = models.CharField(max_length=100)
    studentEmail = models.EmailField()
    studentPhoneNumber = models.CharField(max_length=15)
    studentImage = models.ImageField(upload_to='student_images/')
    studentSignature = models.ImageField(upload_to='student_signatures/')
    studentGender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='Female')
    studentReligion = models.CharField(max_length=15, choices=RELIGION_CHOICES,default='Hindu')
    studentNationality = models.CharField(max_length=15, choices=NATIONALITY_CHOICES,default='India')
    birthDate = models.DateField()
    birthCertificateNumber = models.PositiveIntegerField()
    fatherName = models.CharField(max_length=100)
    fatherNID = models.PositiveIntegerField()
    fatherPhoneNumber = models.CharField(max_length=15)
    fatherOccupation = models.CharField(max_length=100)
    fatherReligion = models.CharField(max_length=15, choices=RELIGION_CHOICES,default='Hindu')
    fatherMonthlyIncome = models.PositiveIntegerField()
    fatherNationality = models.CharField(max_length=15, choices=NATIONALITY_CHOICES,default='India')
    motherName = models.CharField(max_length=100)
    motherNID = models.PositiveIntegerField()
    motherPhoneNumber = models.CharField(max_length=15)
    motherOccupation = models.CharField(max_length=100)
    motherReligion = models.CharField(max_length=15, choices=RELIGION_CHOICES,default='Hindu')
    motherMonthlyIncome = models.PositiveIntegerField()
    motherNationality = models.CharField(max_length=15, choices=NATIONALITY_CHOICES,default='India')
    presentAddressLine1 = models.CharField(max_length=100)
    presentAddressLine2 = models.CharField(max_length=100, blank=True, null=True)
    presentZila = models.CharField(max_length=100)
    presentThana = models.CharField(max_length=100, blank=True, null=True)
    presentPostalCode = models.PositiveIntegerField()
    permanentAddressLine1 = models.CharField(max_length=100)
    permanentAddressLine2 = models.CharField(max_length=100, blank=True, null=True)
    permanentZila = models.CharField(max_length=100)
    permanentThana = models.CharField(max_length=100, blank=True, null=True)
    permanentPostalCode = models.PositiveIntegerField()
    previousClass = models.CharField(max_length=100, blank=True, null=True)
    previousClassGroup = models.CharField(max_length=15, choices=ADMISSION_GROUP_CHOICES, default='Science', blank=True, null=True)
    previousClassResultTotalMark = models.PositiveIntegerField(blank=True, null=True)
    previousClassResultGPA = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    previousSchoolName = models.CharField(max_length=100, blank=True, null=True)
    previousSchoolClassRoll = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.studentFirstName} {self.studentLastName} - {self.admissionFor}'



class ClassRoutineModel(models.Model):
    classDay = models.CharField(max_length=100)
    teacherName = models.TextField(max_length=100)
    subjectData = models.TextField()
    
    def __str__(self):
        return self.classDay
    



class Video(models.Model):
    playlist = models.CharField(max_length=50,default='undefined')
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/', max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
