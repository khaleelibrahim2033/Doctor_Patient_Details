**Doctor and Patient API**
A simple REST API built using **Python and FastAPI** to manage doctors and patients.

**Technologies Used**

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn
* In-memory storage

**Features**

 **Doctor APIs**

| Method | Endpoint               | Description      |
| ------ | ---------------------- | ---------------- |
| POST   | `/doctors`             | Create a doctor  |
| GET    | `/doctors`             | List all doctors |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID |

Doctor fields:

* `name`
* `specialization`
* `email`
* `is_active`

`is_active` is `true` by default.

**Patient APIs**

| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| POST   | `/patients` | Create a patient  |
| GET    | `/patients` | List all patients |

Patient fields:

* `name`
* `age`
* `phone`

**Validation**

The application includes the following validation:

* Email must be valid.
* Patient age must be greater than 0.
* Pydantic models are used for request validation.
* `HTTPException` is used for proper error handling.
* A `404` error is returned when a requested doctor does not exist.

**Installation**

**Step 1: Open the project folder**

```bash
cd fastapi_doctor_patient
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Run the application**

```bash
uvicorn main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

**API Documentation**

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test all the API endpoints using Swagger UI.

**Example Doctor Request**

```json
{
    "name": "Dr. Ravi",
    "specialization": "Cardiologist",
    "email": "ravi@gmail.com",
    "is_active": true
}
```

**Example Patient Request**

```json
{
    "name": "Rahul",
    "age": 25,
    "phone": "9876543210"
}

```
