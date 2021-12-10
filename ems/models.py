from django.db import models

# Create your models here.

# Event model here 
class Event(models.Model):

    Event_name=models.CharField(max_length=100)
    Event_category=models.ForeignKey("ems.Category", on_delete=models.CASCADE, blank=True)
    Event_Desc=models.CharField(max_length=500)
    Event_sponsor=models.ForeignKey("ems.Sponsor", on_delete=models.CASCADE, blank=True)
    Event_price=models.IntegerField(default=0)
    Event_venue=models.CharField(max_length=300,default="")
    Event_datetime=models.DateTimeField(default="")
    Event_image=models.ImageField(upload_to="static/media/event_img",default="")
    
    def __str__(self):
        return self.Event_name


# sponser model here 
class Sponsor(models.Model):
   
    Sponser_name=models.CharField(max_length=100)
    Sponser_image=models.ImageField(upload_to="static/media/sponser_img",default="")
    Sponser_desc=models.CharField(max_length=300,default="")
    
    def __str__(self):
        return self.Sponser_name

class Category(models.Model):
   
    Category_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Category_name


# new model here 
class News(models.Model):
    News_title=models.CharField(max_length=200)
    News_desc=models.TextField(default="")
    
    def __str__(self):
        return self.News_title

    
# booking and Payement model here
class Booking(models.Model):
    
    Booking_username=models.CharField(max_length=50,default="")
    Booking_event=models.CharField(max_length=100,default="")
    Register_fees=models.IntegerField(default=0)
    Your_name=models.CharField(max_length=50,default="")
    Your_phone=models.IntegerField(default=0)
    Date_created=models.DateTimeField(auto_now_add=True,null=True)
    Your_Email=models.CharField(max_length=100,default="")
    # Gender_choices
    # MALE='M'
    # FEMALE='F'
    # OTHER='O'
    # Gender_choices=[(MALE,'Male'),(FEMALE,'Female'),(OTHER,'Other')]
    # Gender=models.CharField(max_length=1,choices=Gender_choices,default="")
    # end 
    def __str__(self):
        
        return self.Booking_username
 