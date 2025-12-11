import requests


# Simple GET request to a public API
def get_random_joke():
    """Fetch a random joke from a public API"""
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get (url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json ()  # Parse JSON response
        print(f"Raw Response: {data}")
        print (f"Setup: {data['setup']}")
        print (f"Punchline: {data['punchline']}")
        print("===== Understanding the response object =====")
        print (f"Status Code: {response.status_code}")
        print (f"Headers: {dict (response.headers)}")
        print (f"Raw Text: {response.text}")
        print (f"JSON Data: {response.json ()}")
    else:
        print (f"Error: {response.status_code}")


# GET request with parameters
def get_activity(participants=1):
    """Fetch a random activity suggestion"""
    url = "https://bored-api.appbrewery.com/filter"
    params = {"participants": participants}

    response = requests.get (url, params=params)

    if response.status_code == 200:
        activities = response.json ()
        print (f"Raw Response: {activities}")
        print (f"Suggested activity: {activities[0]['activity']}")
    else:
        print (f"Error: {response.status_code}")



# Run examples
if __name__ == "__main__":
    print ("=== Random Joke ===")
    get_random_joke ()

    print ("\n=== Activity for 2 people ===")
    get_activity (participants=2)