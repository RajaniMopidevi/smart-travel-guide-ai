from agents import destination_agent, budget_agent, itinerary_agent
from memory import create_session

def travel_advisor(request):

    dest = request["destination"]
    days = request["days"]
    budget = request.get("budget_inr", None)
    preferences = request.get("preferences", "")

    dest_resp = destination_agent(dest)

    dest_info = dest_resp["info"]

    budget_resp = budget_agent(dest_info, days)

    itinerary = itinerary_agent(dest_info, days, preferences)

    return {
        "destination": dest,
        "country": dest_info["country"],
        "budget": budget_resp,
        "itinerary": itinerary
    }


if __name__ == "__main__":

    create_session("demo")

    destination = input("Enter destination: ")
    days = int(input("Enter number of days: "))
    preferences = input("Enter travel preference: ")
    budget = int(input("Enter your budget (INR): "))

    req = {
        "destination": destination,
        "days": days,
        "budget_inr": budget,
        "preferences": preferences
    }

    result = travel_advisor(req)

    print("\nDestination:", result["destination"])
    print("Country:", result["country"])
    print(" Budget:", result["budget"])
    print("\nItinerary:\n")
    print(result["itinerary"])