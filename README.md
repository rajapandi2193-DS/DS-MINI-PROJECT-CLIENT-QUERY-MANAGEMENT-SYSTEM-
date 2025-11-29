# **Client Query Management System**
### *Organizing, Tracking, and Closing Support Queries*

A complete end-to-end system for managing client queries using **Python, MySQL, Pandas, Streamlit**, and **CSV-based dataset ingestion**.  
The project simulates real-time client query submission, management, and tracking with a fully functional dashboard.

---

## 🚀 **Project Features**
### **1. Client Interface**
- Submit new queries  
- Inputs: Email, Mobile Number, Query Heading, Description  
- Automatically generates:
  - `query_created_time`
  - `status = "Open"`

### **2. Support Team Dashboard**
- View all queries (Open/Closed)
- Filter by status / category / date
- Close queries with timestamp auto-update
- Real-time monitoring & KPI tracking

### **3. Login System (with Roles)**
- Secure registration & login  
- SHA-256 password hashing  
- Role-based access:
  - **Client → Submission Page**
  - **Support → Dashboard Page**

---

## 🧠 **Skills Gained**
- Python Programming  
- MySQL CRUD Operations  
- Streamlit Web App Development  
- Data Cleaning & Processing using Pandas  
- Statistics & KPI Measurement  
- Data Engineering Fundamentals  
- Real-time Dashboard Building  

---

## 📂 **Project Architecture**
```
CSV Dataset → Pandas → MySQL DB → Streamlit UI
```

---

## 🏗️ **Tech Stack**
**Languages:** Python  
**Database:** MySQL / SQLite  
**Frontend:** Streamlit  
**Libraries:** Pandas, mysql-connector-python, datetime  
**Version Control:** Git & GitHub  

---

## 📝 **Dataset Columns**
| Column Name | Description |
|------------|-------------|
| query_id | Unique ID |
| mail_id | Client email |
| mobile_number | Client phone |
| query_heading | Short title |
| query_description | Full query text |
| status | Open / Closed |
| query_created_time | Timestamp |
| query_closed_time | Timestamp |

---

## 🔐 **Login Workflow**
### **Registration**
- User enters username, password, role
- Password hashed using:
```python
hashlib.sha256(password.encode()).hexdigest()
```
- Data stored in SQL table:
  - username  
  - hashed_password  
  - role  

### **Login**
- User enters username & password → hash → match in DB  
- Redirect:
  - Client → Query Submission  
  - Support → Management Dashboard  

---

## 🛠️ **Functional Flow**

### **1️⃣ Client Submission Page**
- Fill form → Insert to MySQL  
- Auto-set:
```
status = "Open"
query_created_time = datetime.now()
```

### **2️⃣ Support Dashboard**
- View tables  
- Filter queries  
- Close query (updates status & time)  

---

## 📊 **KPIs & Analysis**
- Query resolution time  
- Open vs Closed query ratio  
- Daily query volume  
- Most common query categories  
- Support team workload  

---

## 📦 **Folder Structure**
```
/project-root
│── app.py               
│── client_page.py       
│── support_page.py      
│── database.py          
│── dataset.csv          
│── README.md            
│── requirements.txt
│── /images              
```

---

## 📝 **How to Run the Project**
### **1️⃣ Install Dependencies**
```
pip install -r requirements.txt
```

### **2️⃣ Set up MySQL Database**
```
CREATE DATABASE client_queries;
USE client_queries;

CREATE TABLE users (
    username VARCHAR(255),
    hashed_password TEXT,
    role VARCHAR(50)
);

CREATE TABLE queries (
    query_id INT PRIMARY KEY AUTO_INCREMENT,
    mail_id TEXT,
    mobile_number TEXT,
    query_heading TEXT,
    query_description TEXT,
    status TEXT,
    query_created_time DATETIME,
    query_closed_time DATETIME
);
```

### **3️⃣ Run Streamlit App**
```
streamlit run app.py
```

---

## ✔️ **Project Evaluation Checklist**
- [x] Maintainable Python Code  
- [x] MySQL DB Integrated  
- [x] Clean Streamlit UI  
- [x] Login & Role-Based Routing  
- [x] Real-Time Query Updates  
- [x] Complete README Documentation  
- [x] GitHub-Friendly Folder Structure  

---

## 📬 **Author**
**Rajapandi**  
*Client Query Management System — Complete Project*

