#  SmartSeason – Agricultural Field Monitoring System

SmartSeason is a full-stack web application designed to help agricultural organizations monitor field activities, track crop progress, and manage field agents efficiently.

---

##  Live Demo

* **Frontend (Netlify):** https://shambamonitor.netlify.app/
* **Backend (PythonAnywhere):** https://okemwabrian.pythonanywhere.com/

---

##  Demo Credentials

###  Admin

* **Username:** Okemwa
* **Password:** 123456

###  Agent

* **Username:** kevin
* **Password:** 123456

---

##  Features

###  Authentication

* JWT-based authentication
* Role-based access (Admin & Agent)

###  Field Management

* Create and assign fields to agents
* Track:

  * Field name
  * Crop type
  * Planting date
  * Current stage

###  Field Updates

* Agents can update:

  * Crop stage
  * Notes
* Admin can view all updates

###  Field Status Logic

Field status is computed dynamically:

| Status    | Condition                                           |
| --------- | --------------------------------------------------- |
| Active    | Field progressing normally                          |
| At Risk   | More than 120 days since planting and not harvested |
| Completed | Field is harvested                                  |

---

###  Dashboard

* Summary cards:

  * Total fields
  * Active
  * At Risk
  * Completed
* Charts:

  * Bar chart (status overview)
  * Pie chart (distribution)
* Role-based views:

  * Admin → sees all fields
  * Agent → sees assigned fields only

---

##  Tech Stack

### Backend

* Django
* Django REST Framework
* SimpleJWT (Authentication)

### Frontend

* React
* Axios
* Recharts (charts)
* React Icons

### Deployment

* Frontend → Netlify
* Backend → PythonAnywhere

---

##  Installation (Local Setup)

### 🔹 Backend

```bash
git clone https://github.com/okemwabrian/shamba-backend.git
cd shamba-backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

### 🔹 Frontend

```bash
git clone https://github.com/okemwabrian/smartseason-frontend.git
cd smartseason-frontend

npm install
npm start
```

---

##  API Endpoints

| Endpoint                  | Description      |
| ------------------------- | ---------------- |
| `/api/token/`             | Login (JWT)      |
| `/api/fields/`            | Field management |
| `/api/updates/`           | Field updates    |
| `/api/dashboard/summary/` | Dashboard data   |

---

##  Design Decisions

* **JWT Authentication** chosen for stateless and scalable auth
* **Role-based filtering** ensures data security
* **Computed field status** avoids redundant database storage
* **Responsive UI** for mobile and desktop usability
* **Charts added** for better data visualization (bonus feature)

---

##  Responsiveness

* Mobile-friendly layout
* Sidebar collapses on small screens
* Charts and tables adapt to screen size

---

##  Future Improvements

* Password reset functionality
* Field images upload
* Notifications for “At Risk” fields
* Map-based field visualization

---

##  Author

**Okemwa Brian**

---

##  Conclusion

SmartSeason is a production-ready agricultural monitoring system demonstrating:

* Full-stack development
* Authentication & authorization
* Data visualization
* Responsive UI design
* Real-world deployment

---
