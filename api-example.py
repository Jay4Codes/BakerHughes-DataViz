from assets.datathon_api import get_embedding

# Define your API key here 
API_KEY = "YOUR API KEY HERE"
TEXT = "Some piece of text other than \"Hello World!\" because it's way cliche."

# Call the get_embedding function located in ./assets
embedding = get_embedding(TEXT, API_KEY)

# Print stuff out and be prepared for a ton of numbers
print(embedding)

