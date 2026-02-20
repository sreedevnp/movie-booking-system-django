from django.db import models
from django.utils import timezone

# Create your models here.

class language(models.Model):
    lang=models.CharField(max_length=30)

class add_genres(models.Model):
    genre=models.CharField(max_length=30)

class timer(models.Model):
    times=models.CharField(max_length=30)

class formats(models.Model):
    format=models.CharField(max_length=30)

class locations(models.Model):
    location=models.CharField(max_length=100)

class seats(models.Model):
    seat_name=models.CharField(max_length=10)
    rates=models.CharField(max_length=100)
    number=models.CharField(max_length=200,default="")
    theatre_name=models.CharField(max_length=500,default="")

class add_movie(models.Model):
    duration=models.CharField(max_length=30)
    movie_name=models.CharField(max_length=100)
    release_date=models.CharField(max_length=50)
    about=models.CharField(max_length=500)
    movie_poster=models.FileField(upload_to="file",default="")
    lang=models.CharField(max_length=50,default="")
    genre=models.CharField(max_length=50,default="")
    format=models.CharField(max_length=50,default="")
    time=models.CharField(max_length=100,default="")
    rating=models.CharField(max_length=10,default="")
    votes=models.CharField(max_length=50,default="")
    certificate=models.CharField(max_length=20,default="")
    date_from=models.CharField(max_length=50,default="")
    date_to=models.CharField(max_length=50,default="")

class theatres(models.Model):
    theatre_name=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    location=models.CharField(max_length=100,default="")

class assign_theatre(models.Model):
    movie=models.CharField(max_length=100)
    theatre=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    times=models.CharField(max_length=50)

class crew(models.Model):
    actor_1=models.CharField(max_length=60)
    actor_1_img=models.FileField(upload_to="file")

    actor_2=models.CharField(max_length=60)
    actor_2_img=models.FileField(upload_to="file")

    actor_3=models.CharField(max_length=60)
    actor_3_img=models.FileField(upload_to="file")

    actor_4=models.CharField(max_length=60)
    actor_4_img=models.FileField(upload_to="file")

    actor_5=models.FileField(max_length=60)
    actor_5_img=models.FileField(upload_to="file")

    crew_1=models.CharField(max_length=60)
    crew_1_desc=models.CharField(max_length=60)
    crew_1_img=models.FileField(upload_to="file")

    crew_2=models.CharField(max_length=60)
    crew_2_desc=models.CharField(max_length=60)
    crew_2_img=models.FileField(upload_to="file")

    crew_3=models.CharField(max_length=60)
    crew_3_desc=models.CharField(max_length=60)
    crew_3_img=models.FileField(upload_to="file")

    crew_4=models.CharField(max_length=60)
    crew_4_desc=models.CharField(max_length=60)
    crew_4_img=models.FileField(upload_to="file")

    crew_5=models.CharField(max_length=60)
    crew_5_desc=models.CharField(max_length=60)
    crew_5_img=models.FileField(upload_to="file")

    movie_name = models.CharField(max_length=100,default="")

class the(models.Model):
    theatre_name=models.CharField(max_length=100)

class shows(models.Model):
    show_date=models.CharField(max_length=100)
    show_day=models.CharField(max_length=100)

class up_coming(models.Model):
    upcoming_movie=models.CharField(max_length=100)
    poster=models.FileField(upload_to="file")

class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

class login_data(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    u_type = models.CharField(max_length=100)

class highlight(models.Model):
    h_movie_name = models.CharField(max_length=100)
    stars = models.CharField(max_length=50)
    votes = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    cast1 = models.FileField(upload_to="file",default="")
    cast2 = models.FileField(upload_to="file",default="")
    cast3 = models.FileField(upload_to="file",default="")
    cast4 = models.FileField(upload_to="file",default="")
    poster = models.FileField(upload_to="file",default="")

class verify(models.Model):
    c_name = models.CharField(max_length=100)
    acc_no = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    cvv = models.CharField(max_length=10)
    balance = models.CharField(max_length=100)
    user_email = models.EmailField(default="")

class Ticket(models.Model):
    user_email = models.EmailField()
    movie = models.CharField(max_length=100)
    theatre = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    seats = models.CharField(max_length=100)
    seat_count = models.IntegerField()
    amount = models.IntegerField()
    booked_on = models.DateTimeField(default=timezone.now)

class News(models.Model):
    news = models.CharField(max_length=10000)

class BookedSeat(models.Model):
    movie = models.ForeignKey(add_movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(theatres, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    seat_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.movie} | {self.theatre} | {self.date} | {self.time} | {self.seat_code}"


