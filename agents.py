from tools import get_destination_info, calculate_budget
from memory import add_to_session


def destination_agent(dest_name, session_id="default"):

    add_to_session(session_id, "system", f"Destination request: {dest_name}")

    info = get_destination_info(dest_name)

    # If destination exists in database
    if info:
        return {"found": True, "info": info}

    # Fallback if destination is not in database
    mock_info = {
        "country": "Unknown",
        "highlights": [
            f"{dest_name} Central Market",
            f"{dest_name} Old Town",
            f"{dest_name} Cultural District",
            f"{dest_name} Main Landmark"
        ],
        "typical_cost_per_day": 3000
    }

    return {"found": True, "info": mock_info}


def budget_agent(dest_info, days):

    cost_per_day = dest_info.get("typical_cost_per_day", 2500)

    return calculate_budget(days, cost_per_day)


def itinerary_agent(dest_info, days, preferences):

    highlights = dest_info.get("highlights", [])

    itinerary = ""

    for d in range(1, days + 1):

        place = highlights[(d - 1) % len(highlights)]

        itinerary += f"Day {d}: Visit {place} and enjoy {preferences}.\n"

    return itinerary