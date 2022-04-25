import requests, json
response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)
print(response.json())

# Formats the response as a JSON object
def jprint(obj):
    return json.dumps(obj, sort_keys=True, indent=4)

response_json = jprint(response.json())
print(response_json)

# Make API queries with parameters
parameters = {
    'lat':6.675356,
    'lon':-1.079543
}
r = requests.get("http://api.open-notify.org/astrosis", params=parameters)
r_json = jprint(r.json())
