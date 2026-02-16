from pydantic import BaseModel, ConfigDict
from sqlalchemy import DECIMAL


class MineralOut(BaseModel):
    model_config = ConfigDict(  # эта настройка помогает задать дополнительные конфигурации модели
        from_attributes=True,  # поможет пайдантик работать с классами и их аттрибутами
        str_strip_whitespace=True,  # для всех строковых полей убирает пробелы
        extra="forbid"  # запрещает создание полей, которых нет в модели
    )

    id: int
    name: str
    color: str
    hardness: DECIMAL

