# File `requirements.txt` explanation

---
## 📌 What is `requirements.txt` in Python?
`requirements.txt` is a file that lists all dependencies (libraries/packages) your Python project needs. It allows others (or your future self) to quickly install the same dependencies using pip.

## 🚀 How to Create `requirements.txt`

### 1️⃣ Manually
You can create `requirements.txt` and list your dependencies:

```
fastapi
uvicorn
oracledb
python-dotenv
```

2️⃣ Automatically (Recommended) If you've already installed libraries in your virtual environment, run:

```
pip freeze > requirements.txt
```

This saves all installed packages into `requirements.txt`.

## 📥 Installing Dependencies from `requirements.txt`
To install all dependencies from `requirements.txt`, run:

```
pip install -r requirements.txt
```

This ensures everyone working on the project has the same libraries.

## 📌 Example `requirements.txt` for a FastAPI Project

```
fastapi==0.109.0
uvicorn==0.27.0
oracledb==1.4.1
python-dotenv==1.0.1
```

## 🌟 Why Use `requirements.txt`?
- ✅ **Ensures consistency in dependencies**
- ✅ **Makes deployment easier**
- ✅ **Helps with virtual environments**
- ✅ **Saves time when setting up a project**