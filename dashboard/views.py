from orders.models import Deliver, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from gigs.models import Comment, Gig
from django.contrib.auth import get_user_model
from users.forms import UserEditForm, ProfileEditForm
from django.views.decorators.csrf import csrf_exempt


@login_required
def get_dashboard_mygigs(request):
    user_gig = request.user.gig_set.all()
    context = {"user_gig": user_gig}
    return render(request, "dashboard/mygigs.html", context=context)


@login_required
def get_dashboard_orders(request):
    gigs = request.user.gig_set.all()
    orders = Order.objects.filter(gig__in=gigs)
    context = {"orders": orders}
    return render(request, "dashboard/orders.html", context=context)


@csrf_exempt
def set_order_status(request):
    if request.method == "POST":
        if request.is_ajax:
            order_id = request.POST["id"]
            order = Order.objects.get(id=order_id)
            if request.POST["act"] == "Accept":
                order.state = 1
                order.save()
                print("accepted")
            elif request.POST["act"] == "Decline":
                order.state = 3
                order.save()
                print("declined")
            else:
                print("Choose an option")
                pass
            return redirect("dashboard-orders")
        return redirect("dashboard-orders")


@login_required
def get_dashboard_profile_edit(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {"u_form": user_form, "p_form": profile_form}

    return render(request, "dashboard/profile_edit.html", context)


@login_required
def get_dashboard_comments(request):
    gigs = request.user.gig_set.all()
    comments = Comment.objects.filter(gig__in=gigs)
    context = {"comments": comments}
    return render(request, "dashboard/comments.html", context=context)


@login_required
def get_dashboard_myorders(request):
    orders = request.user.order_set.all()
    delivers = Deliver.objects.filter(order__in=orders)
    context = {"orders": orders,"delivers":delivers}
    return render(request, "dashboard/myorders.html", context=context)