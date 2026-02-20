from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.template.context_processors import request
from django.template.defaultfilters import title
from.models import language
from.models import add_genres
from.models import timer
from.models import formats
from.models import locations
from.models import assign_theatre
from.models import crew
from.models import the
from.models import shows
from.models import up_coming
from datetime import datetime, timedelta
from.models import register
from django.core.mail import send_mail
import random
from.models import highlight
from.models import login_data
from django.shortcuts import render, get_object_or_404
from.models import seats, theatres, add_movie
from.models import verify,Ticket,News,BookedSeat
# Create your views here.

def adminhm(request):
    context = {}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))

def user(request):
    movies = add_movie.objects.all()
    crew_data = crew.objects.all()
    highlights_data = highlight.objects.all().order_by("-id")[:5]

    return render(request, "userp.html", {
        "key": movies,
        "key2": crew_data,
        "highlights": highlights_data
    })

def addlang(request):
    if request.method == 'POST':
        a=language()
        lang=request.POST.get("lang")
        a.lang=lang
        a.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/adminhm'</script>")
    else:
        context = {}
        template = loader.get_template("addlang.html")
        return HttpResponse(template.render(context, request))

def genres(request):
    if request.method == 'POST':
        b=add_genres()
        genre=request.POST.get("genre")
        b.genre=genre
        b.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/adminhm'</script>")
    else:
        c=language.objects.all()
        context = {"key":c}
        template = loader.get_template("genres.html")
        return HttpResponse(template.render(context, request))

def time(request):
    if request.method == "POST":
        d=timer()
        time_s=request.POST.get("time")
        d.times=time_s
        d.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/time'</script>")
    else:
        context = {}
        template = loader.get_template("time.html")
        return HttpResponse(template.render(context, request))

def format(request):
    if request.method == "POST":
        e=formats()
        form=request.POST.get("format")
        e.format=form
        e.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/adminhm'</script>")
    else:
        context = {}
        template = loader.get_template("format.html")
        return HttpResponse(template.render(context, request))

def location(request):
    if request.method == "POST":
        f=locations()
        location=request.POST.get("location")
        f.location=location
        f.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/adminhm'</script>")
    else:
        context = {}
        template = loader.get_template("location.html")
        return HttpResponse(template.render(context, request))

def seat(request):
    if request.method == "POST":
        g=seats()
        seat_name=request.POST.get("seat_name")
        rate=request.POST.get("rate")
        number=request.POST.get("number")
        theatre_name=request.POST.get("theatre_name")
        g.theatre_name=theatre_name
        g.seat_name=seat_name
        g.rates=rate
        g.number=number
        g.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/seat'</script>")
    else:
        i=theatres.objects.all()
        context = {"key":i}
        template = loader.get_template("seat.html")
        return HttpResponse(template.render(context, request))

def movie_add(request):
    if request.method == 'POST':
        h=add_movie()
        duration=request.POST.get("duration")
        movie_name=request.POST.get("movie_name")
        release_date=request.POST.get("release_date")
        about=request.POST.get("about")
        movie_poster=request.FILES["movie_poster"]
        lang=request.POST.get("lang")
        genre = request.POST.get("genre")
        format = request.POST.get("format")
        # time = request.POST.getlist("time")
        time_list = request.POST.getlist("time")

        rating = request.POST.get("rating")
        votes = request.POST.get("votes")
        certificate = request.POST.get("certificate")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        h.date_from = date_from
        h.date_to = date_to
        h.duration=duration
        h.movie_name=movie_name
        h.release_date=release_date
        h.about=about
        h.movie_poster=movie_poster
        h.lang=lang
        h.genre=genre
        h.format=format
        h.time = ",".join(time_list)
        h.rating=rating
        h.votes=votes
        h.certificate=certificate
        h.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/movie_add'</script>")
    else:
        c = language.objects.all()
        d = add_genres.objects.all()
        e = formats.objects.all()
        f = timer.objects.all()
        context = {"key":c,"key2":d,"key3":e,"key4":f}
        template = loader.get_template("addmovie.html")
        return HttpResponse(template.render(context, request))

def theatre(request):
    if request.method == "POST":
        i = theatres()
        theatre_name=request.POST.get("theatre_name")
        contact=request.POST.get("contact")
        location=request.POST.get("location")
        i.theatre_name=theatre_name
        i.contact=contact
        i.location=location
        i.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/adminhm'</script>")
    else:
        f=locations.objects.all()
        context = {"key":f}
        template = loader.get_template("theatre.html")
        return HttpResponse(template.render(context, request))

def assign_theatres(request):
    if request.method == "POST":
        j = assign_theatre()
        movie=request.POST.get("movie_name")
        theatre=request.POST.get("theatre_name")
        j.movie=movie
        j.theatre=theatre
        j.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/assign_theatres'</script>")
    else:
        h=add_movie.objects.all()
        i=theatres.objects.all()
        context = {"key":h,"key2":i}
        template = loader.get_template("assign theatre.html")
        return HttpResponse(template.render(context, request))

def cast_crew(request):
    if request.method == "POST":
        l=crew()
        actor_1=request.POST.get("actor_1")
        actor_1_img=request.FILES["actor_1_img"]

        actor_2 = request.POST.get("actor_2")
        actor_2_img = request.FILES["actor_2_img"]

        actor_3 = request.POST.get("actor_3")
        actor_3_img = request.FILES["actor_3_img"]

        actor_4 = request.POST.get("actor_4")
        actor_4_img = request.FILES["actor_4_img"]

        actor_5 = request.POST.get("actor_5")
        actor_5_img = request.FILES["actor_5_img"]

        crew_1 = request.POST.get("crew_1")
        crew_1_desc=request.POST.get("crew_1_desc")
        crew_1_img=request.FILES["crew_1_img"]

        crew_2 = request.POST.get("crew_2")
        crew_2_desc = request.POST.get("crew_2_desc")
        crew_2_img = request.FILES["crew_2_img"]

        crew_3 = request.POST.get("crew_3")
        crew_3_desc = request.POST.get("crew_3_desc")
        crew_3_img = request.FILES["crew_3_img"]

        crew_4 = request.POST.get("crew_4")
        crew_4_desc = request.POST.get("crew_4_desc")
        crew_4_img = request.FILES["crew_4_img"]

        crew_5 = request.POST.get("crew_5")
        crew_5_desc = request.POST.get("crew_5_desc")
        crew_5_img = request.FILES["crew_5_img"]

        movie_name = request.POST.get("movie_name")

        l.movie_name = movie_name

        l.actor_1=actor_1
        l.actor_1_img=actor_1_img

        l.actor_2=actor_2
        l.actor_2_img=actor_2_img

        l.actor_3=actor_3
        l.actor_3_img=actor_3_img

        l.actor_4=actor_4
        l.actor_4_img=actor_4_img

        l.actor_5=actor_5
        l.actor_5_img=actor_5_img

        l.crew_1=crew_1
        l.crew_1_desc=crew_1_desc
        l.crew_1_img=crew_1_img

        l.crew_2=crew_2
        l.crew_2_desc=crew_2_desc
        l.crew_2_img=crew_2_img

        l.crew_3=crew_3
        l.crew_3_desc=crew_3_desc
        l.crew_3_img=crew_3_img

        l.crew_4=crew_4
        l.crew_4_desc=crew_4_desc
        l.crew_4_img=crew_4_img

        l.crew_5=crew_5
        l.crew_5_desc=crew_5_desc
        l.crew_5_img=crew_5_img

        l.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/adminhm'</script>")
    else:
        h = add_movie.objects.all()
        context = {"key": h}
        template = loader.get_template("castcrew.html")
        return HttpResponse(template.render(context, request))

def view(request,id):
    h = add_movie.objects.get(id=id)
    context = {"key":h}
    template = loader.get_template("view.html")
    return HttpResponse(template.render(context, request))

from django.db.models import Q

def book(request, id):
    # load movie object
    h = add_movie.objects.get(id=id)

    # all locations for the location buttons
    locations_list = locations.objects.all()

    # Try to find assignments robustly: sometimes you stored movie as id (string/int), sometimes name.
    movie_id_str = str(id)
    movie_name = h.movie_name

    # fetch any assign_theatre row where movie matches either movie id (as string) or movie name
    assigned_entries = assign_theatre.objects.filter(Q(movie=movie_id_str) | Q(movie=movie_name))

    # If still empty, try numeric comparison if DB stored numeric type unusually (defensive)
    if not assigned_entries.exists():
        try:
            assigned_entries = assign_theatre.objects.filter(movie=int(id))
        except Exception:
            pass

    # Extract theatre IDs from assignments (handle string / int)
    assigned_theatre_ids = []
    for a in assigned_entries:
        raw = a.theatre
        # try numeric conversion, fallback to str if not numeric
        try:
            assigned_theatre_ids.append(int(raw))
        except Exception:
            # if theatre stored as name, try to find its id by name
            try:
                t_obj = theatres.objects.filter(theatre_name=str(raw)).first()
                if t_obj:
                    assigned_theatre_ids.append(t_obj.id)
            except Exception:
                pass

    # ensure unique and non-empty
    assigned_theatre_ids = list({x for x in assigned_theatre_ids if isinstance(x, int)})

    # load only theatres assigned to this movie
    if assigned_theatre_ids:
        theatres_list = theatres.objects.filter(id__in=assigned_theatre_ids)
    else:
        theatres_list = theatres.objects.none()

    # date range
    start = datetime.strptime(h.date_from, "%Y-%m-%d")
    end = datetime.strptime(h.date_to, "%Y-%m-%d")
    date_list = []
    current = start
    while current <= end:
        date_list.append({
            "day": current.strftime("%a").upper(),
            "date": current.strftime("%d"),
            "month": current.strftime("%b").upper()
        })
        current += timedelta(days=1)

    times = h.time.split(",") if h.time else []

    return render(request, "booktickets.html", {
        "key": h,
        "dates": date_list,
        "times": times,
        "locations": locations_list,
        "theatres": theatres_list,
        "assigned": assigned_entries,
    })



def show(request):
    if request.method == "POST":
        n = shows()
        show_date = request.POST.get("show_date")
        n.show_date=show_date
        n.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/show'</script>")
    else:
        context = {}
        template = loader.get_template("show.html")
        return HttpResponse(template.render(context, request))

def upcoming_movies(request):
    if request.method == "POST":
        o = up_coming()
        upcoming_movie=request.POST.get("upcoming_movie")
        poster=request.FILES["poster"]
        o.upcoming_movie=upcoming_movie
        o.poster = poster
        o.save()
        return HttpResponse("<script>alert('Inserted successfully');window.location='/upcoming_movies'</script>")
    else:
        context = {}
        template = loader.get_template("upcoming.html")
        return HttpResponse(template.render(context, request))

def highlights(request):
    if request.method == "POST":
        p = highlight()
        name = request.POST.get("h_movie_name")
        stars = request.POST.get("stars")
        votes = request.POST.get("votes")
        about = request.POST.get("about")
        cast1 = request.FILES["cast1"]
        cast2 = request.FILES["cast2"]
        cast3 = request.FILES["cast3"]
        cast4 = request.FILES["cast4"]
        poster = request.FILES["poster"]
        # if not poster:
        #     return HttpResponse(
        #         "<script>alert('Poster is required');history.back();</script>"
        #     )

            # ✅ validate poster BEFORE saving
        # if poster.content_type not in ["image/jpeg", "image/png"]:
        #     return HttpResponse(
        #         "<script>alert('Only JPG or PNG images allowed');history.back();</script>"
        #     )
        #
        # if poster.size > 2 * 1024 * 1024:
        #     return HttpResponse(
        #         "<script>alert('Poster must be less than 2MB');history.back();</script>"
        #     )

            # ✅ assign files AFTER validation
        p.h_movie_name = name
        p.about = about
        p.stars = stars
        p.votes = votes
        p.cast1 = cast1
        p.cast2 = cast2
        p.cast3 = cast3
        p.cast4 = cast4
        p.poster = poster

        p.save()

        return HttpResponse(
            "<script>alert('Inserted successfully');window.location='/user'</script>"
        )

    return render(request, "highlights.html")

def up_display(request):
    o = up_coming.objects.all()
    context = {"key":o}
    template = loader.get_template("view upcoming.html")
    return HttpResponse(template.render(context, request))

# def seat_booking(request):
#     movie_id = request.GET.get("movie")
#     theatre_id = request.GET.get("theatre")
#     date = request.GET.get("date")
#     time = request.GET.get("time")
#
#     # Fetch DB objects
#     movie = get_object_or_404(add_movie, id=movie_id)
#     theatre = get_object_or_404(theatres, id=theatre_id)
#
#     context = {
#         "movie": movie,
#         "theatre": theatre,
#         "date": date,
#         "time": time,
#     }
#
#     return render(request, "seatbooking.html", context)s

def seat_booking(request):
    movie_id = request.GET.get("movie")
    theatre_id = request.GET.get("theatre")
    date = request.GET.get("date")
    time = request.GET.get("time")

    movie = get_object_or_404(add_movie, id=movie_id)
    theatre = get_object_or_404(theatres, id=theatre_id)

    # ✅ FETCH SEATS FOR THIS THEATRE
    seat_categories = seats.objects.filter(theatre_name=str(theatre_id))

    # 🔒 FETCH ALREADY BOOKED SEATS
    booked_seats = BookedSeat.objects.filter(
        movie=movie,
        theatre=theatre,
        date=date,
        time=time
    ).values_list("seat_code", flat=True)

    context = {
        "movie": movie,
        "theatre": theatre,
        "date": date,
        "time": time,
        "seat_categories": seat_categories,
        "booked_seats": list(booked_seats),
    }

    return render(request, "seatbooking.html", context)



# def seat_booking(request):
#     movie_id = request.GET.get("movie")
#     theatre_id = request.GET.get("theatre")
#     date = request.GET.get("date")
#     time = request.GET.get("time")
#
#     # Fetch DB objects
#     movie = get_object_or_404(add_movie, id=movie_id)
#     theatre = get_object_or_404(theatres, id=theatre_id)
#
#     context = {
#         "movie": movie,
#         "theatre": theatre,
#         "date": date,
#         "time": time,
#     }
#
#     return render(request, "seatbooking.html", context)



def registration(request):
    if request.method == "POST":
        aa = register()
        log = login_data()
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        # Check password match
        if password != confirm:
            return HttpResponse("<script>alert('Passwords do not match');window.location='/registration'</script>")

        # Check email exists
        if register.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('Email already registered');window.location='/registration'</script>")

        # Save data
        aa.name = name
        aa.email = email
        aa.password = password
        aa.save()
        log.name = name
        log.password = password
        log.u_type = 'user'
        log.save()
        # Redirect to login page after success
        return HttpResponse("<script>alert('Account created successfully!');window.location='/login'</script>")
    else:
        context = {}
        template = loader.get_template("registration.html")
        return HttpResponse(template.render(context, request))


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # 🔐 Admin Login (Hardcoded or DB-based)
        if email == "flickzya0@gmail.com" and password == "admin123":
            return redirect("adminhm")

        # 👤 Normal User Login
        user = register.objects.filter(email=email, password=password).first()

        if user:
            request.session["user_id"] = user.id
            request.session["user_email"] = user.email
            request.session["user_name"] = user.name
            return redirect("user")

        else:
            return HttpResponse(
                "<script>alert('Invalid email or password');window.location='/login'</script>"
            )

    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect("user")


def forgot_password(request):
    if request.method == "POST":

        # SEND OTP
        if "send_otp" in request.POST:
            email = request.POST.get("email")

            # Check if user exists
            if not register.objects.filter(email=email).exists():
                return HttpResponse("<script>alert('Email not found');window.location='/forgot'</script>")

            otp = random.randint(100000, 999999)

            # store OTP temporarily in session
            request.session["reset_email"] = email
            request.session["reset_otp"] = otp

            # send otp email
            send_mail(
                subject="Flickzy Password Reset Code",
                message=f"Your OTP code is: {otp}",
                from_email="noreply@flickzy.com",
                recipient_list=[email],
                fail_silently=True,
            )

            template = loader.get_template("forgot_pass.html")
            return HttpResponse(template.render({"otp_sent": True}, request))


        # VERIFY OTP
        if "verify_otp" in request.POST:
            user_input = request.POST.get("otp")
            original_otp = str(request.session.get("reset_otp"))

            if user_input == original_otp:
                return HttpResponse("<script>alert('OTP Verified');window.location='/reset_password'</script>")
            else:
                return HttpResponse("<script>alert('Invalid OTP');window.location='/forgot'</script>")

    return render(request, "forgot_pass.html")

def reset_password(request):
    if request.method == "POST":
        new = request.POST.get("new_password")
        confirm = request.POST.get("confirm_password")
        email = request.session.get("reset_email")

        if new != confirm:
            return HttpResponse("<script>alert('Passwords do not match');window.location='/reset_password'</script>")

        user = register.objects.get(email=email)
        user.password = new
        user.save()

        del request.session["reset_email"]
        del request.session["reset_otp"]

        return HttpResponse("<script>alert('Password updated successfully');window.location='/login'</script>")

    return render(request, "reset_password.html")

def payment(request):
    if "user_email" not in request.session:
        return redirect("login")

    movie_id = request.GET.get("movie")
    theatre_id = request.GET.get("theatre")
    date = request.GET.get("date")
    time = request.GET.get("time")
    seats = request.GET.get("seats")
    seat_count = request.GET.get("count")
    total_price = request.GET.get("total", 0)

    movie = get_object_or_404(add_movie, id=movie_id)
    theatre = get_object_or_404(theatres, id=theatre_id)

    request.session["movie_name"] = movie.movie_name
    request.session["theatre_name"] = theatre.theatre_name
    request.session["date"] = date
    request.session["time"] = time
    request.session["seats"] = seats
    request.session["seat_count"] = seat_count
    request.session["total_price"] = int(total_price)

    return render(request, "payment.html", {
        "movie": movie,
        "theatre": theatre,
        "date": date,
        "time": time,
        "seats": seats,
        "seat_count": seat_count,
        "total_price": total_price,
    })

def payment_start(request):
    total_price = request.POST.get("total_price")

    if not total_price:
        return HttpResponse(
            "<script>alert('Payment amount missing');window.location='/user';</script>"
        )

    request.session["total_price"] = int(total_price)

    # 🔑 CHECK IF ACCOUNT EXISTS FOR THIS USER
    acc = verify.objects.filter(
        user_email=request.session.get("user_email")
    ).first()

    if acc:
        # ✅ EXISTING USER → VERIFY DETAILS
        request.session["acc_id"] = acc.id
        return redirect("account_verify2")
    else:
        # ✅ NEW USER → CREATE ACCOUNT
        return redirect("account_verify")

def account_verify(request):
    if request.method == "POST":
        ver = verify()
        c_name = request.POST.get("c_name")
        ifsc = request.POST.get("ifsc")
        cvv = request.POST.get("cvv")
        acc_no = request.POST.get("acc_no")
        balance = request.POST.get("balance")
        ver.user_email = request.session.get("user_email")
        ver.c_name = c_name
        ver.ifsc = ifsc
        ver.cvv = cvv
        ver.acc_no = acc_no
        ver.balance = balance
        ver.save()
        # ✅ VERY IMPORTANT
        request.session["acc_id"] = ver.id
        if acc_no is None:
            return HttpResponse(
                "<script>alert('Verification Failed');"
                "window.location='/verify_process';</script>"
            )
        return HttpResponse("<script>alert('Account created successfully!');window.location='/account_verify2'</script>")
    else:
        context = {}
        template = loader.get_template("account_verify.html")
        return HttpResponse(template.render(context, request))

def account_verify2(request):
    acc_id = request.session.get("acc_id")
    total_price = int(request.session.get("total_price", 0))

    acc = verify.objects.filter(id=acc_id).first()
    if not acc:
        return redirect("account_verify")

    if request.method == "POST":
        if (
            acc.c_name == request.POST.get("c_name")
            and acc.acc_no == request.POST.get("acc_no")
            and acc.ifsc == request.POST.get("ifsc")
            and acc.cvv == request.POST.get("cvv")
        ):
            balance = int(acc.balance)

            if balance < total_price:
                request.session["recharge_acc_id"] = acc.id
                return redirect("recharge")
            else:
                return redirect("pay")

        return HttpResponse(
            "<script>alert('Details mismatch');history.back();</script>"
        )

    return render(request, "account_verify2.html", {"acc": acc})




def pay(request):
    acc_id = request.session.get("acc_id")
    total = int(request.session.get("total_price", 0))

    # ✅ SAVE BOOKED SEATS (ADD ONLY)
    selected_seats = request.session.get("seats", "").split(",")

    movie = add_movie.objects.get(movie_name=request.session["movie_name"])
    theatre = theatres.objects.get(theatre_name=request.session["theatre_name"])

    for seat in selected_seats:
        BookedSeat.objects.create(
            movie=movie,
            theatre=theatre,
            date=request.session["date"],
            time=request.session["time"],
            seat_code=seat
        )

    # Safety check
    if not acc_id:
        return redirect("payment_start")

    acc = verify.objects.get(id=acc_id)

    # Convert balance to int
    balance = int(acc.balance)

    if request.method == "POST":
        # 🔐 Double-check balance before deducting
        if balance < total:
            return redirect("recharge")

        # Deduct and save
        acc.balance = balance - total
        acc.save()

        return redirect("tick")

        # ✅ SAVE TICKET
    Ticket.objects.create(
        user_email=request.session.get("user_email"),
        movie=request.session.get("movie_name"),
        theatre=request.session.get("theatre_name"),
        date=request.session.get("date"),
        time=request.session.get("time"),
        seats=request.session.get("seats"),
        seat_count=request.session.get("seat_count"),
        amount=request.session.get("total_price"),
        )

    return render(request, "pay.html", {
        "amount": total,
        "balance": balance
    })


def recharge(request):
    acc_id = request.session.get("acc_id")

    if not acc_id:
        return redirect("payment_start")

    acc = verify.objects.get(id=acc_id)
    total = int(request.session.get("total_price", 0))

    if request.method == "POST":
        recharge_amt = request.POST.get("recharge")

        if not recharge_amt:
            return HttpResponse(
                "<script>alert('Enter recharge amount');history.back();</script>"
            )

        recharge_amt = int(recharge_amt)
        acc.balance = int(acc.balance) + recharge_amt
        acc.save()

        return redirect("pay")

    # ✅ PASS DATA TO TEMPLATE
    return render(request, "recharge.html", {
        "balance": acc.balance,
        "amount": total
    })


def tick(request):
    if "user_email" not in request.session:
        return redirect("login")

    context = {
        "email": request.session.get("user_email"),
        "movie": request.session.get("movie_name"),
        "theatre": request.session.get("theatre_name"),
        "date": request.session.get("date"),
        "time": request.session.get("time"),
        "seats": request.session.get("seats"),
        "count": request.session.get("seat_count"),
        "amount": request.session.get("total_price"),
    }

    return render(request, "tick.html", context)

def view_tickets(request):
    if "user_email" not in request.session:
        return redirect("login")

    tickets = Ticket.objects.filter(
        user_email=request.session["user_email"]
    ).order_by("-booked_on")

    return render(request, "view ticket details.html", {"tickets": tickets})

def profile(request):
    if "user_id" not in request.session:
        return redirect("login")

    user = register.objects.get(id=request.session["user_id"])

    return render(request, "profile.html", {
        "name": user.name,
        "email": user.email,
        "password": user.password,  # ⚠️ plain text (see note below)
    })

def edit_profile(request):
    if "user_id" not in request.session:
        return redirect("login")

    user = register.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()

        # update session values
        request.session["user_name"] = user.name
        request.session["user_email"] = user.email

        return HttpResponse(
            "<script>alert('Profile updated successfully');window.location='/profile';</script>"
        )

    return render(request, "edit profile.html", {"user": user})

def news(request):
    if request.method == "POST":
        new = News()
        news = request.POST.get("news")
        new.news = news
        new.save()
        return HttpResponse(
            "<script>alert('News Added successfully');window.location='/news';</script>"
        )
    else:
        context={}
        template = loader.get_template("news.html")
        return HttpResponse(template.render(context, request))








