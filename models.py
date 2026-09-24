from pydantic import BaseModel, EmailStr, Field
 
 
class DoctorCreate(BaseModel):

    name: str = Field(..., min_length=1)

    specialization: str = Field(..., min_length=1)

    email: EmailStr

    is_active: bool = True
 
 
class DoctorResponse(BaseModel):

    id: int

    name: str

    specialization: str

    email: EmailStr

    is_active: bool
 
 
class PatientCreate(BaseModel):

    name: str = Field(..., min_length=1)

    age: int = Field(..., gt=0)

    phone: str = Field(..., min_length=1)
 
 
class PatientResponse(BaseModel):

    id: int

    name: str

    age: int

    phone: str
 