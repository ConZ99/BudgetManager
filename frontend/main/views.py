import json
import requests
from django.shortcuts import redirect, render


def fetch_data(request):
    response = requests.get(
        "http://127.0.0.1:8001/api/data", timeout=3
    )  # FastAPI endpoint
    data = (
        response.json()
        if response.status_code == 200
        else {"error": "Failed to fetch data"}
    )

    return render(request, "data_page.html", {"data": data})


def post_data(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        my_obj = {"key": key, "value": value}

        response = requests.post(
            "http://127.0.0.1:8001/api/data", data=json.dumps(my_obj), timeout=3
        )
        if response.status_code == 200:
            print("Data added successfully")
        else:
            print("Failed to add data")

    # Redirect to `fetch_data` after processing the form
    return redirect("fetch_data")
