

class Billing:
    def __init__(self, license):
        self.license = license

    def some_behavior(self):
        self.license.calcFee()


class License:
    def calcFee(self):
        print('Calculate')


class PersonalLicense(License):
    pass


class BusinessLicense(License):
    def __init__(self):
        self.users = 10


def builder(license):
    billing = Billing(license)
    billing.some_behavior()


licenses = [License, PersonalLicense, BusinessLicense]

for license in licenses:
    builder(license())
