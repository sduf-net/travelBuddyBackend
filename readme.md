# 📡 Mobile App Backend – Powered by SDUF  

A lightweight **Python backend** designed to handle all user requests and dynamically send UI configurations using [SDUF.net](https://sduf.net/) – a **Server-Driven UI platform**.  

---

## 🚀 Features  

✅ **User Request Handling** – Efficiently process and respond to mobile app requests.  
✅ **Dynamic UI Configuration** – Send UI updates in real time using SDUF.  
✅ **Fast & Lightweight** – Built with **FastAPI** and powered by **Uvicorn**.  
✅ **Easy Deployment** – Simple to set up and run locally.  

---

## 🛠️ Installation  

1️⃣ **Clone the repository**  
```sh
git clone git@github.com:Dimakoua/travel_buddy_api.git
cd travel_buddy_api
```

2️⃣ **Create a virtual environment**  
```sh
python -m venv .venv
```

3️⃣ **Activate the virtual environment**  
- **Linux/macOS:**  
  ```sh
  source .venv/bin/activate
  ```
- **Windows (PowerShell):**  
  ```sh
  .venv\Scripts\Activate
  ```

4️⃣ **Install dependencies**  
```sh
pip install -r requirements.txt
```

---

## ▶️ Running the Server  

Once dependencies are installed, start the backend server:  

```sh
source .venv/bin/activate
uvicorn main:app --reload
deactivate
```

> **Note:** The \`--reload\` flag enables auto-reloading for development.

---

## 🧪 Running Tests  

Run the test suite in a **test environment**:  

```sh
ENV=test pytest
```

---

## 📜 License  

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

