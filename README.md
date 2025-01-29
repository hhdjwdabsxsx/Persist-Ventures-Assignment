# FastAPI + OAuth2.0 FatSecret API Integration

This assignment demonstrates how to integrate **FastAPI** with the **FatSecret API** for food search using **OAuth 2.0 Client Credentials Flow**.

## 🚀 Features
- ✅ **FastAPI** for building APIs
- ✅ **OAuth 2.0 Authentication** (Client Credentials Flow)
- ✅ **Search for foods** using FatSecret API
- ✅ **Error handling & debugging** for API responses
- ✅ **Easy deployment** using Uvicorn

## 📌 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/hhdjwdabsxsx/Persist-Ventures-Assignment.git
cd Persist-Ventures-Assignment
```

### **2️⃣ Install Dependencies**
```bash
pip install fastapi uvicorn requests 
```

### **3️⃣ Run the FastAPI Server**
```bash
uvicorn main:app --reload
```

## 📌 API Endpoints

### **🔹 Get Access Token (Handled Automatically)**
- **Method:** `POST`
- **URL:** `https://oauth.fatsecret.com/connect/token`
- **Headers:** `{ "Content-Type": "application/x-www-form-urlencoded" }`

### **🔹 Search for Foods**
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/search_food?query=apple`
- **Response Format:** JSON

#### **Example Response:**
```json
{
  "foods": {
    "food": [
      {
        "food_id": "12345",
        "food_name": "Apple",
        "food_type": "Generic",
        "food_url": "https://www.fatsecret.com/foods/apple"
      }
    ]
  }
}
```



