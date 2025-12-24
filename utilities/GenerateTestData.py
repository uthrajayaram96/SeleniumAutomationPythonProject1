from faker import Faker
import random


class GenerateTestData:
    fake = Faker()

    @classmethod
    def generate_email(cls):
        return cls.fake.email()

    @classmethod
    def generate_password(cls):
        return cls.fake.password()

    @classmethod
    def generate_first_name(cls):
        first_name = cls.fake.first_name()
        print('\n' + first_name, end=' ')
        return first_name

    @classmethod
    def generate_last_name(cls):
        last_name = cls.fake.last_name()
        print(last_name)
        return last_name

    @classmethod
    def generate_company_name(cls):
        return cls.fake.company()

    @classmethod
    def generate_comments(cls):
        return cls.fake.text(max_nb_chars=100)

    @classmethod
    def generate_gender(cls):
        gender = ['Male', 'Female']
        random_number = random.randint(0, 1)
        # print(gender[random_number])
        return gender[random_number]

    @classmethod
    def generate_manager_of_vendor(cls):
        vendors = ['Not a vendor', 'Vendor 1', 'Vendor 2']
        random_number = random.randint(0, 2)
        return vendors[random_number]

    @classmethod
    def generate_customer_roles(cls):
        roles = ['Guests', 'Registered', 'Administrators', 'Forum Moderators', 'Vendors']
        random_number = random.randint(0, 4)
        return roles[random_number]
