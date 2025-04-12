from django.shortcuts import render

def Home(request):
    return render(request, 'WFH_Tracker/home.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WorkFromHomeRecord
from datetime import datetime

@csrf_exempt
def submit_form(request):
    if request.method == "POST":
        user_id = request.POST.get("userID")
        work_location = request.POST.get("workLocation")
        address = request.POST.get("address")
        ip_address = request.POST.get("ipAddress")
        server_time = datetime.now()

        # Save data to the database
        record = WorkFromHomeRecord(
            user_id=user_id,
            work_location=work_location,
            address=address,
            ip_address=ip_address,
            server_time=server_time,
        )
        record.save()

        return JsonResponse({"message": "Data saved successfully!"})
    return JsonResponse({"error": "Invalid request method."}, status=400)
