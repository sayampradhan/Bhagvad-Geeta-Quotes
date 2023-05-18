import random

import requests

# Generate random chapter and verse numbers
chapter = random.randint(1, 18)
verses = 0

# Determine the number of verses in the selected chapter
if chapter == 1:
    verses = random.randint(1, 47)

elif chapter == 2:
    verses = random.randint(1, 72)

elif chapter == 3:
    verses = random.randint(1, 43)

elif chapter == 4:
    verses = random.randint(1, 42)

elif chapter == 5:
    verses = random.randint(1, 29)

elif chapter == 6:
    verses = random.randint(1, 47)

elif chapter == 7:
    verses = random.randint(1, 30)

elif chapter == 8:
    verses = random.randint(1, 28)

elif chapter == 9:
    verses = random.randint(1, 34)

elif chapter == 10:
    verses = random.randint(1, 42)

elif chapter == 11:
    verses = random.randint(1, 55)

elif chapter == 12:
    verses = random.randint(1, 20)

elif chapter == 13:
    verses = random.randint(1, 35)

elif chapter == 14:
    verses = random.randint(1, 27)

elif chapter == 15:
    verses = random.randint(1, 20)

elif chapter == 16:
    verses = random.randint(1, 24)

elif chapter == 17:
    verses = random.randint(1, 28)

elif chapter == 18:
    verses = random.randint(1, 78)

try:
    # Construct the URL for the Bhagavad Gita API
    url = f"https://bhagavad-gita3.p.rapidapi.com/v2/chapters/{chapter}/verses/{verses}/"

    headers = {
        "X-RapidAPI-Key": "14c1a49a87mshfce8345f77f3c8dp1339bbjsn8ebe0f5af81d",
        "X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
    }

    # Make a GET request to the API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Extract the verse text from the response
        verse_data = response.json()
        verse = verse_data["text"]
        # Print the selected verse
        print(f"Bhagavad Gita Chapter {chapter}, Verse {verses}:")
        print(verse)
    else:
        # Display an error message if the request was unsuccessful
        print("Failed to fetch verse. Error:", response.status_code)

except requests.exceptions.RequestException as e:
    # Handle any exceptions that occur during the API request
    print("Error occurred:", e)
