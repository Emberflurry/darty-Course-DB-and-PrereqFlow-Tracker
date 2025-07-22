import requests
from bs4 import BeautifulSoup

# List of athlete names
athlete_names = [
    "AARON ROYLE",
    "SAM LAIDLOW",
    "JOSH AMBERGER",
    # Add the remaining athlete names here
]

# Iterate over each athlete name
for name in athlete_names:
    # Format the name to be used in the URL
    formatted_name = name.lower().replace(" ", "-")

    # Construct the URL for the athlete's page
    url = f"https://stats.protriathletes.org/athlete/{formatted_name}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing height and weight information
    height_element = soup.find("div", text="Height")
    weight_element = soup.find("div", text="Weight")

    # Extract the height and weight values
    height = height_element.find_next("div").text.strip()
    weight = weight_element.find_next("div").text.strip()

    # Print the results
    print(f"Athlete: {name}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print("----------")
