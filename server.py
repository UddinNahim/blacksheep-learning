from blacksheep import Application
from blacksheep.server.controllers import Controller , get, post, put, delete
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info
from uuid import UUID
from dataclasses import dataclass


app = Application()

docs = OpenAPIHandler(info=Info(title="Pet store api", version = "1.0.0"))
docs.bind_app(app)

@dataclass
class Pet:
    id: UUID
    name: str
    category: str

# class Pet:
#     def __init__(self,id: UUID,name: str, category: str):
#         self.id = id
#         self.name = name
#         self.category = name


@dataclass
class CreatePetInput:
    name: str
    category: str

@docs.tags("Pets")
class PetsController(Controller):

    @classmethod
    def route(cls) -> str:
        return "/api/pets"

    @get()
    async def get_pets(self) -> list[Pet]:
        return []
    
    @get("/{pet_id}")
    async def get_pet(self,pet_id: UUID) -> Pet:
        pass

    @post()
    async def create_pet(self, input: CreatePetInput) -> Pet:
        pass
    


