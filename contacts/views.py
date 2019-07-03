from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(req):
    if req.method ==  'POST':
        listing_id = req.POST['listing_id']
        listing = req.POST['listing']
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        user_id = req.POST['user_id']
        realtor_email = req.POST['realtor_email']
        # check if user already made inquiry
        if req.user.is_authenticated:
                user_id = req.user.id
                has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id )
                if has_contacted:
                        messages.error(req, 'you have already made an inquire for this listing')
                        return redirect('/listings/'+listing_id)



        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, 
        phone=phone, message=message, user_id=user_id)

        contact.save()

        #send mail

        send_mail(
                'property listing enquiry',
                'there has been enquiry for'+ listing + '. Sign into the admin panel for more info ' ,
                'gnanavelv27@gmail.com',
                [realtor_email, 'gnanav63@gmail.com'],
                fail_silently=False
        )

        messages.success(req, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/'+listing_id)
