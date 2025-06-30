## Čtení na doma: Knihovna pydantic

Knihovna `pydantic` může hodně pomoci především v případě, že potřebujeme provést validaci dat.

```py
from pydantic import BaseModel, PositiveInt, field_validator

class Employee(BaseModel):
    name: str
    position: str
    holiday_entitlement: int
```


```py
from typing import Literal
from pydantic import BaseModel, PositiveInt, field_validator
class Employee(BaseModel):
    name: str
    position: Literal["vývojář/ka", "tester/ka", "manažer/ka"]
    holiday_entitlement: PositiveInt
    # PRA1234 , LON0012, neplatné: NEW5
    personal_number: str

    @field_validator("personal_number", mode="before")
    @classmethod
    def check_personal_number(cls, v):
        # v nezačíná řetězcem PRA nebo LON
        v = v.upper()
        if "PRA"[:3] not in ["PRA", "LON"]:
            raise ValueError(f"{v} nezačíná PRA nebo LON")
        return v
```
