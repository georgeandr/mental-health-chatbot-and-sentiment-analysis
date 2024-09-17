from pydantic import BaseModel

# Define the input structure
class TextData(BaseModel):
    cleaned_statement: str