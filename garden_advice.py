"""
Garden Advice Program

Provides simple gardening advice based on the season
and the type of plant entered by the user.
"""


def get_season_advice(season: str) -> str:
    """
    Return gardening advice based on the season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type: str) -> str:
    """
    Return gardening advice based on the plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """
    Main program execution.
    """
    # Get user input
    season = input("Enter the season (e.g. summer or winter): ").strip().lower()
    plant_type = input("Enter the plant type (e.g. flower or vegetable): ").strip().lower()

    # Build advice using helper functions
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Display the advice
    print(advice)


# Run the program
if __name__ == "__main__":
    main()
