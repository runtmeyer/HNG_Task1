# 📊 FastAPI Number Classifier

A simple **FastAPI** application that classifies numbers based on properties such as **prime, perfect, even, and odd**. It also provides **digit sum** and a fun fact about the number.

---

## 🚀 Features
- ✅ Checks if a number is **prime**
- ✅ Checks if a number is **perfect**
- ✅ Identifies if a number is **even** or **odd**
- ✅ Computes the **sum of digits**
- ✅ Provides a **fun fact** about the number

---

## 🛠️ Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone <your-repo-url>
cd <your-repo-folder>
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install fastapi uvicorn
```

---

## ▶️ Running the Application
Start the FastAPI server using **Uvicorn**:
```sh
uvicorn main:app --reload
```
- The API will be available at: **`http://127.0.0.1:8000`**
- Interactive API docs: **`http://127.0.0.1:8000/docs`**

---

## 💼 API Usage

### **Endpoint:**  
```http
GET /api/classify-number?number=<integer>
```

### **Example Request:**
```http
GET http://127.0.0.1:8000/api/classify-number?number=28
```

### **Example Response (JSON):**
```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["perfect", "even"],
  "digit_sum": 10,
  "fun_fact": "Second perfect number."
}
```

---

