from pydantic import BaseModel, Field, EmailStr, model_validator, ValidationError


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., gt=0)


class User(BaseModel):
    name: str = Field(..., min_length=2, pattern=r"^[A-Za-z ]+$")
    age: int = Field(..., ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @model_validator(mode='after')
    def check_employed_age(self):
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError("Employed user must be between 18 and 65 years old")
        return self


def process_registration(json_input: str):
    try:
        user = User.model_validate_json(json_input)
        return user.model_dump_json(indent=4)
    except ValidationError as e:
        return f"Validation error:\n{e.json(indent=4)}"