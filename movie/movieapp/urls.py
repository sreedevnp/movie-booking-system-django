from django.urls import path
import movieapp.views

urlpatterns = [
    path('adminhm/',movieapp.views.adminhm,name="adminhm"),

    path('login/',movieapp.views.login,name="login"),

    path("logout/",movieapp.views.logout, name="logout"),

    path('registration/',movieapp.views.registration,name="registration"),

    path('forgot_password/',movieapp.views.forgot_password,name="forgot_password"),

    path('reset_password/', movieapp.views.reset_password, name="reset_password"),

    path('user/',movieapp.views.user,name="user"),

    path('addlang/',movieapp.views.addlang,name="addlang"),

    path('genres/',movieapp.views.genres,name="genres"),

    path('time/',movieapp.views.time,name="time"),

    path('format/',movieapp.views.format,name="format"),

    path('location/',movieapp.views.location,name="location"),

    path('seat/',movieapp.views.seat,name="seat"),

    path('movie_add/',movieapp.views.movie_add,name="movie_add"),

    path('theatre/',movieapp.views.theatre,name="theatre"),

    path('assign_theatres/',movieapp.views.assign_theatres,name="assign_theatres"),

    path('cast_crew/',movieapp.views.cast_crew,name="cast_crew"),

    path('view/<int:id>',movieapp.views.view,name="view"),

    path('book/<int:id>',movieapp.views.book,name="book"),

    path('show/',movieapp.views.show,name="show"),

    path('upcoming_movies/',movieapp.views.upcoming_movies,name="upcoming_movies"),

    path('highlights/',movieapp.views.highlights,name="highlights"),

    path('up_display/',movieapp.views.up_display,name="up_display"),

    path('seat_booking/',movieapp.views.seat_booking,name="seat_booking"),

    path("payment/",movieapp.views.payment,name="payment"),

    path("account_verify/",movieapp.views.account_verify,name="account_verify"),

    path("payment_start/", movieapp.views.payment_start, name="payment_start"),

    path("account_verify2/", movieapp.views.account_verify2, name="account_verify2"),

    path("pay/", movieapp.views.pay, name="pay"),

    path("recharge/", movieapp.views.recharge, name="recharge"),

    path("tick/", movieapp.views.tick, name="tick"),

    path("view_tickets/",movieapp.views.view_tickets,name="view_tickets"),

    path("profile/",movieapp.views.profile, name="profile"),

    path("edit-profile/",movieapp.views.edit_profile, name="edit_profile"),

    path("news/",movieapp.views.news,name="news")

]