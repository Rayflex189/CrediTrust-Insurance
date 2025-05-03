from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from django.db import transaction
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

from .decorators import *
from .forms import *
from .models import *
from .utilis import *


# Create your views here.

def home(request):
    return render(request, 'axis_app/index.html')

@login_required(login_url='loginview')
def analytics(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'axis_app/analytics.html', context)

@login_required(login_url='loginview')
def bank_transfer(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user
    # Handle the deposit form submission
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            try:
                deposit_amount = form.cleaned_data['amount']
                if deposit_amount <= 0:
                    form.add_error('amount', "Deposit amount must be greater than zero.")
                else:
                    # Create a transaction record without updating the balance
                    Transaction.objects.create(
                        user=user_profile.user,
                        amount=deposit_amount,
                        balance_after=user_profile.balance,  # Keeping the existing balance
                        description='Pending'
                    )

                    return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm()


    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'axis_app/bank_transfer.html', context)
    
@login_required
def Upgrade_Account(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    # Account upgrade status message
    if user_profile.is_upgraded:
        message = 'Account upgraded successfully'
    else:
        message = 'Account upgrade processing. Contact support for more information.'

    # Months and years for dropdowns
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    current_year = datetime.now().year
    years = [str(year) for year in range(current_year, current_year + 10)]

    # If the form is submitted via POST
    if request.method == "POST":
        # Get form data
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        expiry_date = request.POST.get('expiry_date')

        # Validate inputs
        if user_profile.card_number != card_number:
            messages.error(request, 'Invalid card number. Please check and try again.')
            return redirect('Upgrade_Account')

        if user_profile.cvv != cvv:
            messages.error(request, 'Invalid CVV. Please check and try again.')
            return redirect('Upgrade_Account')

        if user_profile.expiry_date != expiry_date:
            messages.error(request, 'Invalid expiration date. Please check and try again.')
            return redirect('Upgrade_Account')

        # Update profile
        user_profile.is_upgraded = True
        user_profile.save()

        messages.success(request, 'Account upgraded successfully!')
        return redirect('pendingPro')

    # Context to render on the page (only runs if not redirected above)
    context = {
        'user_profile': user_profile,
        'message': message,
        'months': months,
        'years': years,
    }
    return render(request, 'axis_app/account_upgrade.html', context)
        

@login_required(login_url='loginview')
def skrill(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with the current user

    # Handle the deposit form submission
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            try:
                deposit_amount = form.cleaned_data['amount']
                if deposit_amount <= 0:
                    form.add_error('amount', "Deposit amount must be greater than zero.")
                else:
                    # Create a transaction record without updating the balance
                    Transaction.objects.create(
                        user=user_profile.user,
                        amount=deposit_amount,
                        balance_after=user_profile.balance,  # Keeping the existing balance
                        description='Pending'
                    )

                    return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm()


    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'axis_app/skrill.html', context)

@unauthenticated_user
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('loginview')

    context = {'form': form}
    return render(request, 'axis_app/register.html', context)

@unauthenticated_user
def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('reset_profile')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'axis_app/login.html')

@login_required(login_url='loginview')
def dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Log out the user and redirect to login page
        logout(request)
        return redirect('loginview')

    # Fetch the last 10 transactions
    transactions = Transaction.objects.filter(user=user_profile.user).order_by('-timestamp')[:10]

    # Calculate doubled balance
    doubled_balance = user_profile.balance * 2

    # Check if account is linked
    if not user_profile.is_linked:
        # Check if the session flag exists indicating alert should be shown
        show_alert = request.session.get('show_alert', True)

        if show_alert:
            # Retrieve last refresh time from session and convert to datetime
            last_refresh_str = request.session.get('last_refresh', None)
            if last_refresh_str:
                last_refresh = timezone.datetime.fromisoformat(last_refresh_str)
            else:
                last_refresh = None

            # Check if enough time has passed since last refresh to show the alert
            if last_refresh is None or (timezone.now() - last_refresh) > timedelta(minutes=5):
                request.session['last_refresh'] = timezone.now().isoformat()
                request.session['show_alert'] = True  # Set the flag to show alert
                alert_message = "Activate account with the payment system for secure transfer"
            else:
                alert_message = None
        else:
            alert_message = None
    else:
        # If account is linked, no alert message needed
        alert_message = None
        request.session['show_alert'] = False  # Ensure flag is False if account is linked

   # Handle the deposit form submission
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            try:
                deposit_amount = form.cleaned_data['amount']
                if deposit_amount <= 0:
                    form.add_error('amount', "Deposit amount must be greater than zero.")
                else:
                    # Create a transaction record without updating the balance
                    Transaction.objects.create(
                        user=user_profile.user,
                        amount=deposit_amount,
                        balance_after=user_profile.balance,  # Keeping the existing balance
                        description='Pending'
                    )

                    return redirect('imf')  # Redirect to dashboard view after processing the deposit
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = DepositForm()

    context = {
        'user_profile': user_profile,
        'alert_message': alert_message,
        'doubled_balance': doubled_balance,
        'transactions': transactions,
        'form': form,
    }
    return render(request, 'axis_app/dashboard.html', context)

@login_required(login_url='loginview')
@transaction.atomic
def reset_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the same page after successful update
        else:
            form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'form': form
    }
    return render(request, 'axis_app/reset_profile.html', context)

@login_required(login_url='loginview')
def imf(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = IMFForm(request.POST)
        if form.is_valid():
            imf_code_input = form.cleaned_data['imf']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_imf(imf_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('vat')
            else:
                form.add_error(None, 'Invalid IMF code')
    else:
        form = IMFForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'axis_app/imf.html', context)

@login_required(login_url='loginview')
def tac(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = TACForm(request.POST)
        if form.is_valid():
            tac_code_input = form.cleaned_data['tac']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_tac(tac_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('vat')
            else:
                # Handle invalid OTP case
                form.add_error(None, 'Invalid TAC code')
    else:
        form = TACForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'axis_app/tac.html', context)

@login_required(login_url='loginview')
def loans(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'axis_app/loans.html', context)

@login_required(login_url='loginview')
def vat(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = VATForm(request.POST)
        if form.is_valid():
            vat_code_input = form.cleaned_data['vat']
            # Validate the OTP here (e.g., check if it matches the expected value)
            if validate_vat(vat_code_input, user_profile):  # Define this function based on your validation logic
                # Redirect to success page or dashboard
                return redirect('pending')
            else:
                # Handle invalid OTP case
                form.add_error(None, 'Invalid VAT code')
    else:
        form = VATForm()

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'axis_app/vat.html', context)

@login_required(login_url='loginview')
def pending(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'axis_app/pending.html', context)

@login_required(login_url='loginview')
def pendingPro(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        user_profile = UserProfile.objects.create(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'axis_app/pendingPro.html', context)
    

@login_required(login_url='loginview')
@transaction.atomic
def linking_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = LinkingCodeForm(request.POST)
        if form.is_valid():
            # Check if the linking code matches
            entered_code = form.cleaned_data['linking_code']
            if entered_code == profile.linking_code:
                messages.success(request, 'Account successfully Activated.')
                # Handle linking logic here, e.g., set a flag in UserProfile
                profile.is_linked = True
                profile.save()
                return redirect('dashboard')  # Redirect to dashboard or another view
            else:
                messages.error(request, 'Invalid activation code. Please try again.')
        else:
            messages.error(request, 'Form validation failed. Please check the input.')

    else:
        form = LinkingCodeForm()

    context = {
        'form': form,
        'user_profile': profile
    }
    return render(request, 'axis_app/linking_page.html', context)

@login_required(login_url='loginview')
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'axis_app/profile.html', context)

@login_required(login_url='loginview')
def kyc(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'axis_app/kyc.html', context)

@login_required(login_url='loginview')
def coming_soon(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'axis_app/coming_soon.html')

@login_required(login_url='loginview')
def LogOut(request):
    logout(request)
    return redirect('loginview')
