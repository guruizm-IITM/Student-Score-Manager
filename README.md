# 🧮 Student Score Manager

**Student Score Manager** is a simple Flask web application that helps display student or course-level performance data.  
Users can enter either a **Student ID** or **Course ID** and get detailed marks information or statistics, respectively.

---

## 🚀 Features

- 🔹 Displays individual **student details** with marks and total score.  
- 🔹 Displays **course statistics** including average, maximum marks, and histogram visualization.  
- 🔹 Generates a **histogram plot** of marks dynamically using `matplotlib`.  
- 🔹 Organized project structure using Flask templates and static folders.  

---

## 🧩 Project Structure

```
Student_Score_Manager/
│
├── app.py                 # Main Flask application
├── data.csv               # Dataset containing student_id, course_id, marks
│
├── templates/             # HTML templates for rendering views
│   ├── index.html
│   ├── student_details.html
│   ├── course_details.html
│   ├── error.html
│
├── static/                # Stores static assets (e.g., generated image.png)
│   └── image.png
│
├── .venv/                 # Virtual environment (local only, not pushed to repo)
└── README.md
```

---

## ⚙️ How It Works

1. On the home page (`index.html`), users can:
   - Search by **Student ID** → see student details and total marks.  
   - Search by **Course ID** → see course statistics and histogram.

2. When a **Course ID** is entered:
   - The app calculates average and maximum marks.
   - Generates a histogram image (`image.png`) saved inside the `static/` folder.

3. When a **Student ID** is entered:
   - The app lists all courses taken by that student.
   - Computes the total marks and displays them.

---

## 🧠 Technologies Used

- **Python 3**
- **Flask**
- **Matplotlib**
- **HTML / CSS (Jinja Templates)**

---

## 🖥️ Running Locally

```bash
# 1️⃣ Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)

# 2️⃣ Install dependencies
pip install flask matplotlib

# 3️⃣ Run the app
python app.py

# 4️⃣ Open the link shown in the terminal (e.g., http://127.0.0.1:5000/)
```

---

## 📊 Example Dataset Format

```
student_id, course_id, marks
S01, C01, 85
S01, C02, 78
S02, C01, 92
S02, C03, 74
S03, C02, 88
```

---

## 🧾 License

This project is open-source and free to use for educational purposes.
