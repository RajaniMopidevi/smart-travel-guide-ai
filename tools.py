from data import DESTINATIONS

def get_destination_info(dest_name):

    key = dest_name.strip().lower()
    return DESTINATIONS.get(key, None)


def calculate_budget(days, cost_per_day, flights_estimate=8000):

    total = days * cost_per_day + flights_estimate

    return {
        "approx_total_inr": int(total),
        "breakdown": {
            "days_cost": days * cost_per_day,
            "flights_estimate": flights_estimate
        }
    }