# AgriScan 🌾

**AI-powered mobile crop-health scanner for smallholder farmers.**  
Detect diseases, get treatment recommendations, and track farm health in real-time.

---

## 🚀 Mission
Empower farmers with **affordable, instant crop diagnostics** – using only a smartphone camera.

---

## 🛠️ Tech Stack (Target Architecture)
- **Flutter** – Mobile App  
- **FastAPI / Python** – Backend (AI API)  
- **Supabase / PostgreSQL** – Database + Auth  
- **TensorFlow / PyTorch** – Model Training  
- **Docker & CI/CD** – Production pipeline

---

## 📌 Core Features (MVP: 90 Days)
- [x] Scan leaf → AI disease detection
- [ ] Treatment recommendations
- [x] Farm logbook + image history
- [x] SMS/Offline support (for rural areas)
- [ ] Admin dashboard (later phase)

---

## 🌱 Public Roadmap (Build in Public)
- **Q1** – Research + UI + Data Collection
- **Q2** – AI Inference + MVP App
- **Q3** – Pilot with Kenyan Farmers
- **Q4** – Monetize (B2B + Co-ops)

---

## 📍 Status
**Current Version: v0.1 MVP**

✅ **Completed:**
- TensorFlow Lite model integration for cassava leaf disease classification
- FastAPI backend with `/api/v1/predict` endpoint
- Flutter mobile app with camera integration
- Hive database for offline history and queueing
- Material 3 UI with clean, modern design
- CI/CD pipeline with GitHub Actions
- Automated tests for API and Flutter app

🚧 **In Progress:**
- Treatment recommendations
- SMS integration
- Admin dashboard

---

## 🚀 Demo

### Screenshots

| Screen | Description |
|--------|-------------|
| Scan Screen | Camera interface for capturing leaf images |
| History Screen | View all past scans with sync status |

> 📸 Screenshots coming soon! Add them to `/docs/` folder.

### Quick Start

**Backend:**
```bash
cd api
pip install -r requirements.txt
python models/convert_to_tflite.py  # If needed
uvicorn app.main:app --reload
```

**Mobile App:**
```bash
cd app
flutter pub get
flutter packages pub run build_runner build  # Generate Hive adapters
flutter run
```

**Run Tests:**
```bash
# API tests
cd api
pytest tests/ -v

# Flutter tests
cd app
flutter test
```

---

## 📄 License
MIT
