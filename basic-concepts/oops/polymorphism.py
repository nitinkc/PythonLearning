
class Wizard:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def cast_spell(self):
        print(f"{self.name} casts a spell with power {self.power}! PARENT")


class ArchWizard(Wizard):
    def __init__(self, name, power, realm):
        super().__init__(name, power)
        self.realm = realm

    def summon_familiar(self):
        print(f"{self.name} summons a familiar from the {self.realm} realm.")


class Sorcerer(Wizard):
    def cast_spell(self):# Overridden method
        print(f"{self.name} casts a powerful dark spell! CHILD")


def unleash_magic(wizard):# Taking an object as a paraameter, object can be of Polymorphic type
    wizard.cast_spell()

def unleash_magic(wizard):
    wizard.cast_spell()

if __name__ == "__main__":
    unleash_magic(Wizard("Merlin", 100))
    unleash_magic(Sorcerer("Voldemort", 90))  # Sorcerer is Child of Wizard


