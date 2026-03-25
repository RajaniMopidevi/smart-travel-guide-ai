from tools import get_destination_info, calculate_budget
from memory import add_to_session
import ollama
import re


def generate_destination_info(dest_name):
    prompt = f"""
    Give travel details for {dest_name}.
    Return in this format:
    country: <country>
    highlights: <5 famous places separated by comma>
    typical_cost_per_day: (only one number like 2500, no ranges, no text)
    """
    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response["message"]["content"]

    # Parsing
    lines = text.split("\n")
    country = "Unknown"
    highlights = []
    cost = 3000
    for line in lines:
        line_lower = line.lower()
        if "country" in line_lower:
            country = line.split(":")[-1].strip()
        elif "highlights" in line_lower:
            highlights = [h.strip() for h in line.split(":")[-1].split(",")]
        elif "cost" in line_lower:
            numbers = re.findall(r'\d+', line)
            if numbers:
                cost = int(numbers[0])  # take only first number
    return {
        "country": country,
        "highlights": highlights,
        "typical_cost_per_day": cost
    }
def destination_agent(dest_name, session_id="default"):

    add_to_session(session_id, "system", f"Destination request: {dest_name}")

    info = get_destination_info(dest_name)

    # If destination exists in dataset
    if info:
        return {"found": True, "info": info}

    #  AI fallback
    ai_info = generate_destination_info(dest_name)

    return {"found": False, "info": ai_info}
def budget_agent(dest_info, days):

    cost_per_day = dest_info.get("typical_cost_per_day", 2500)

    return calculate_budget(days, cost_per_day)


def itinerary_agent(dest_info, days, preferences):

    destination = dest_info.get("country", "")  # fallback safety
    highlights = dest_info.get("highlights", [])

    places = ", ".join(highlights)

    prompt = f"""
    Create a detailed {days}-day travel itinerary.

    Destination: {places}
    Preferences: {preferences}

    Instructions:
    - For each day, give a full plan (morning, afternoon, evening)
    - Include:
        - Places to visit
        - Food suggestions (local dishes or cafes)
        - Activities to do
    - Make it realistic and structured
    - Format clearly like:

    Day 1:
    Morning: ...
    Afternoon: ...
    Evening: ...
    Food: ...

    Keep it clean and readable.
    """

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": prompt}]
    )

    itinerary = response["message"]["content"]

    return itinerary