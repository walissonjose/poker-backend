from pydantic import BaseModel


def snake_to_camel(snake_str: str | None = None):
    if snake_str is None:
        return None
    components = snake_str.split('_')
    return components[0] + ''.join(s.title() for s in components[1:])


class GenericSchema(BaseModel):
    class Config:
        alias_generator = snake_to_camel
        populate_by_name = True
