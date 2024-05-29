class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self) -> str:
        return f'{self.name} - {self.pet_type} - {self.owner.name}'

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, type):
        if type in Pet.PET_TYPES:
            self._pet_type = type
        else:
            raise Exception('Pet must be in list of approved PET_TYPES')

class Owner:
    def __init__(self, name) :
        self.name = name

    def pets(self):
        result = []
        for pet in Pet.all:
            if pet.owner is self:
                result.append(pet)
        return result

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception('Pet must be a instance of <Pet> object!')

    def get_sorted_pets(self):


        return sorted([pet for pet in self.pets()], key = lambda pet: pet.name)

james = Owner('mike')
cat1 = Pet('Suzzy', 'cat', james)
cat2 = Pet('Rose', 'cat', james)

print(f'pets: {james.pets()}')
print(f'sorted: {james.get_sorted_pets()}')