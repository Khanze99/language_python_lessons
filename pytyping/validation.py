from pydantic import BaseModel, ValidationError, validator


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        print(cls, v)
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v


if __name__ == '__main__':

    user = UserModel(
        name='anvar khamidov',
        username='khanze',
        password1='gggggg',
        password2='gggggg'
    )
