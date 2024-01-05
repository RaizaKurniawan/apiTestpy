import requests

def test_api(endpoint): 
    base_url = "https://reqres.in/api/users?page=2"
    url = f"{base_url}/{endpoint}"

    # Make a Get Request
    response = requests.get(url)

    # Check the http status code 
    if response.status_code == 200:
        print(f"Success! Response 200 for {endpoint}")
        print(response.json())
        return True
        # You can also print or manipulate the response content if needed
    elif response.status_code == 400:
        print("Bad Request! Response 400 for {endpoint}")
    elif response.status_code == 404:
        print("Not Found! Response 404 for {endpoint}")
    else:
        print(f"Unexpected response: {response.status_code} for {endpoint}")

    return False

# Example usage
result_200 = test_api("endpoint-for-200")
result_400 = test_api("endpoint-for-400")
result_404 = test_api("non-existent-endpoint")

print("\n Test Results: ")
print(f"Test for endpoint-for-200: {'Passed' if result_200 else 'Failed'}")
print(f"Test for endpoint-for-400: {'Passed' if not result_400 else 'Failed'}")
print(f"Test for non-existent-endpoint: {'Passed' if not result_404 else 'Failed'}")