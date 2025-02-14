# ID Mimic

## Return Values

When running the app, the following return values are generated:
- A list of 100 fake personal data based on location The Netherlands, each representing a fake person's data-set.
- Each dictionary contains the following keys:
    - `personal_info`: 
        - `name`: A randomly generated full name.
        - `email`: A randomly generated email address.
        - `phone_number`: A randomly generated phone number.
        - `birthdate`: A randomly generated birthdate.
        - `gender`: A randomly generated gender.
    - `address`: 
        - `street`: A randomly generated street address.
        - `postalcode`: A randomly generated postal code.
        - `city`: A randomly generated city.
        - `province`: A randomly generated province.
        - `country`: A randomly generated country.
    - `company`: 
        - `company_name`: A randomly generated company name.
        - `job_title`: A randomly generated job title.
    - `bank`: 
        - `iban`: A randomly generated IBAN.
        - `bic`: A randomly generated BIC.
        - `bank_country`: A randomly generated bank country.
        - `ssn`: A randomly generated social security number.

These values are returned by the FastAPI endpoint /fake-persons and can be saved to file for further use.

### Example JSON Output

```json
[
    {
    "personal_info": {
      "first_name": "Nout",
      "last_name": "Bos",
      "email": "evelien42@example.org",
      "phone_number": "+3180 9954092",
      "birthdate": "1981-10-28",
      "gender": "Male"
    },
    "address": {
      "street": "Noëllesteeg 403\n2886 YE\nUddel",
      "postalcode": "2984 ZP",
      "city": "Hoogvliet Rotterdam",
      "province": "Noord-Holland",
      "country": "The Netherlands"
    },
    "company": {
      "company_name": "Wouters & Arens",
      "job_title": "Hydrologist"
    },
    "bank": {
      "iban": "NL72RXZT7498537639",
      "bic": "EDIPNLAS",
      "bank_country": "NL"
    }
  },
    // ... 98 more entries
]
```

## Setup Instructions

### Prerequisites

- Docker
- Python 3.x

### Using Docker

1. Build the Docker image:

    ```sh
    docker build -t id_mimic .
    ```

2. Run the Docker container:

    ```sh
    docker run --rm id_mimic
    ```

### Running Locally

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/id_mimic.git
    cd id_mimic
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the main script:

    ```sh
    python main.py
    ```

## Project Description
The project generates 100 random fake personal data entries using the `main.py` script and serves them using FastAPI. The generated data includes names, addresses, and other personal information.
