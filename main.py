from fastapi import FastAPI, HTTPException
 
from app.models import (
    DoctorCreate,
    DoctorResponse,
    PatientCreate,
    PatientResponse
)
 
from app.database import doctors, patients
 
 
app = FastAPI(
    title="Doctor and Patient Management API",
    description="A simple FastAPI project for managing doctors and patients",
    version="1.0.0"
)
 
 
# =========================================================
# DOCTOR APIs
# =========================================================
 
@app.post("/doctors", response_model=DoctorResponse, status_code=201)
def create_doctor(doctor: DoctorCreate):
 
    doctor_id = len(doctors) + 1
 
    new_doctor = {
        "id": doctor_id,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }
 
    doctors.append(new_doctor)
 
    return new_doctor
 
 
@app.get("/doctors", response_model=list[DoctorResponse])
def get_doctors():
 
    return doctors
 
 
@app.get("/doctors/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int):
 
    for doctor in doctors:
 
        if doctor["id"] == doctor_id:
            return doctor
 
    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )
 
 
# =========================================================
# PATIENT APIs
# =========================================================
 
@app.post("/patients", response_model=PatientResponse, status_code=201)
def create_patient(patient: PatientCreate):
 
    patient_id = len(patients) + 1
 
    new_patient = {
        "id": patient_id,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }
 
    patients.append(new_patient)
 
    return new_patient
 
 
@app.get("/patients", response_model=list[PatientResponse])
def get_patients():
 
    return patients