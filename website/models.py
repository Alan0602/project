from django.db import models

# Create your models here.

class CseDepartment(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=300)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title
  
class CseNewsImage(models.Model):
	cseDepartment = models.ForeignKey(CseDepartment, on_delete=models.CASCADE, related_name="images")
	image = models.CharField(max_length=300)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.image[0:50]

class CseEvent(models.Model):
  title = models.CharField(max_length=200)
  poster = models.CharField(max_length=300)
  description = models.TextField(max_length=300)
  last_date = models.CharField(max_length=50)
  google_form = models.CharField(max_length=300)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title

class CseTeacher(models.Model):
  name = models.CharField(max_length=200)
  profile_picture = models.CharField(max_length=300)
  email = models.CharField(max_length=100)
  qualification = models.TextField(max_length=200)
  FACULTY = "F"
  TECHNICAL_STAFF = "T"
  ROLE_CHOICES = [
		(FACULTY, "Faculty"),
		(TECHNICAL_STAFF, "Technical Staff"),
	]
  role = models.CharField(
		max_length = 1,
		choices = ROLE_CHOICES,
		default=FACULTY,
	)
  experience = models.TextField(max_length=400)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.name