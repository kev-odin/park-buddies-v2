import requests

base_url = f"https://developer.nps.gov/api/v1/"
params = {"api_key": "rRScznr5cMqmr00eoeO61Xmc3FL9fB6o499OJqbf"}


def _address_string(addresses: dict):
    return f"{addresses[0]['line1']}, {addresses[0]['city']}, {addresses[0]['stateCode']} {addresses[0]['postalCode']}"


def activities():
    """
    Returns dictionary of all activities codified by NPS
    {activity_name : json}
    """
    request_url = base_url + "activities"
    response = requests.get(request_url, params=params)
    data = response.json()["data"]
    activites = {x["name"]:x for x in data}
    return activites


def activities_parks():
    """
    Returns dictionary of all activities that can be enjoyed at each park
    {activity_name : json}
    """
    request_url = base_url + "activities/parks"
    response = requests.get(request_url, params=params)
    data = response.json()["data"]
    activities_parks = {x["name"]:x for x in data}
    return activities_parks


def parks(state_code: str = None):
    """
    Returns a dictionary of parks in a provided state
    {park_code : json}
    """
    request_url = base_url + "parks"
    params["stateCode"] = state_code
    response = requests.get(request_url, params=params)
    data = response.json()["data"]
    parks = {x["parkCode"]:x for x in data}
    return parks


def webcams():
    """
    Returns dict of active webcams at each park
    {park_code : json}
    """
    params["limit"] = 500
    request_url = base_url + "webcams"
    response = requests.get(request_url, params=params)
    data = response.json()["data"]
    webcams = {
        x["relatedParks"][0]["parkCode"]:x
        for x in data
        if x["status"] == "Active" and x["relatedParks"]
    }
    return webcams


if __name__ == "__main__":
    test0 = activities()
    test1 = activities_parks()
    test2 = webcams() 
    test3 = parks()
    x = 0
