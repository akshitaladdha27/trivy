import requests

def main():
    print("Fetching data from external API...")

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    if response.status_code == 200:
        print("Success!")
        print("Response:", response.json())
    else:
        print("Failed with status:", response.status_code)

if __name__ == "__main__":
    main()
# test workflow trigger
