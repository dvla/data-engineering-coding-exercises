class Brand:
    def __init__(self, record):
        self.Id = record[0]
        self.Name = record[1]
        self._registrations = [] 
        
    def __str__(self):
        return f"{self.Name} ({self.get_registrations_count()} registrations)"

    def get_registrations_count(self):
        return len(self._registrations)

    def add(self, registration):
        self._registrations.append(registration)
    

class Country:
    def __init__(self, record):
        self.Id = record[0]
        self.Name = record[1]
        self.ImportVolume = record[2]
        self._brands = {}

    def __str__(self):
        return f"{self.Name} (Import Volume: {self.ImportVolume})"

    def add(self, registration, brand_resolver):
        if not registration.Brand in self._brands.keys():
            self._brands[registration.Brand] = brand_resolver(registration.Brand)  
        self._brands[registration.Brand].add(registration)


class Registration:
    def __init__(self, record):
        self.Number = record[0]
        self.Country = record[1]
        self.Brand = record[2]