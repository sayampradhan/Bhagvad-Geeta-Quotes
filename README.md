# Bhagvad-Geeta-Quotes

This Python script generates a random verse from the Bhagavad Gita using the Bhagavad Gita API. It selects a random chapter and verse number, makes a GET request to the API, and displays the verse text.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your_username/your_repository.git```

2. Change to the project directory:
```cd your_repository```

3. Install the required `requests` library:
```pip install requests
```

## Usage
Run the Python script using the following command:
```python random_verse.py
```

The script will generate a random chapter and verse number, make a request to the Bhagavad Gita API, and display the selected verse.

## API Key
To use the Bhagavad Gita API, you need an API key. Follow the steps below to obtain one:

1. Visit the RapidAPI Bhagavad Gita API page.
2. Sign up for a RapidAPI account (if you don't have one).
3. Subscribe to the Bhagavad Gita API and obtain your API key.
4. Replace the placeholder API key in the Python script with your actual API key.

```headers = {
    "X-RapidAPI-Key": "your_api_key",
    "X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
}
```
Make sure to keep your API key secure and avoid committing it to version control.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## [License](/LICENSE)
This project is licensed under the MIT License. 

