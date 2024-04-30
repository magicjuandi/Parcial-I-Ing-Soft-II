import Persona

class PersonaService:
    def __init__(self):
        self.persona = []

    def edit(self, id: int,new_user: Persona):
        self.persona[id] = new_user

    def List(self):
        for i, persona in enumerate(self.persona):
            print(f"User {i}: {persona.name}, {persona.phone}, {persona.email}")
    def Add(self, persona: Persona):
        self.persona.append(persona)