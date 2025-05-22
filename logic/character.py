# Class will be created for characters
class Character: 
    def __init__(self, name: str, metatype: str):
        # Stores the name and metatype in following dictionary
        self.name = name
        self.metatype = metatype
        self.attributes = {
            "Body": 1,
            "Agility": 1,
            "Reaction": 1,
            "Strength": 1,
            "Charisma": 1,
            "Intuition": 1,
            "Logic": 1,
            "Willpower": 1,
            "Edge": 1,
            "Essence": 1,
            "Magic": 1
        }
    
    # Adding __str__ for readable debug
    def __str__(self):
        return f"{self.name} the {self.metatype}"