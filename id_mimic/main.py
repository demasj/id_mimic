from fastapi import FastAPI
from faker import Faker
from faker.providers import bank, phone_number, address, person

app = FastAPI()
fake = Faker('nl_NL')
fake.add_provider(bank)
fake.add_provider(phone_number)
fake.add_provider(address)
fake.add_provider(person)

@app.get("/fake-persons")
def get_fake_data():
    results = []
    for _ in range(100):
        results.append({
            "personal_info": {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "phone_number": fake.unique.phone_number(),
                "birthdate": fake.date_of_birth().isoformat(),
                "gender": fake.random_element(elements=('Male', 'Female'))
            },
            "address": {
                "street": fake.address(),
                "postalcode": fake.postcode(),
                "city": fake.city(),
                "province": fake.province(),           
                "country": "The Netherlands",
            },
            "company": {
                "company_name": fake.company(),
                "job_title": fake.job()
            },
            "bank": {
                "iban": fake.unique.iban(),
                "bic": fake.swift(),
                "bank_country": fake.bank_country()
            }
        })
    return results