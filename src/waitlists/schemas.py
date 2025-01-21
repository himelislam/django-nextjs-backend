from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistsEntryIn
    email: EmailStr

class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistsEntryOut
    email: EmailStr
    timestamp: datetime