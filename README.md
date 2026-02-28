# Deep Action Sniper - Monorepo

A cross-platform price monitoring application with Flutter frontend and Python FastAPI backend.

## 📁 Repository Structure

```
deep_action_sniper_monorepo/
├── frontend/                    # Flutter cross-platform application
│   ├── lib/                     # Dart source code
│   ├── android/                 # Android native code
│   ├── ios/                     # iOS native code
│   ├── web/                     # Web (Flutter Web)
│   ├── windows/                 # Windows desktop
│   ├── linux/                   # Linux desktop
│   ├── macos/                   # macOS desktop
│   ├── test/                    # Dart tests
│   ├── pubspec.yaml             # Flutter dependencies
│   └── README.md                # Frontend documentation
│
└── backend/                     # FastAPI Python backend
    ├── main.py                  # FastAPI application
    └── requirements.txt         # Python dependencies (if exists)
```

## 🎯 Project Overview

### Frontend (Flutter)
- **Platforms**: Android, iOS, Web, Windows, Linux, macOS
- **Language**: Dart
- **Framework**: Flutter
- **Key Dependencies**: 
  - `http` - HTTP client for API calls
  - `cupertino_icons` - iOS-style icons

**Location**: `frontend/`

**Setup**:
```bash
cd frontend
flutter pub get
flutter run
```

### Backend (FastAPI)
- **Language**: Python
- **Framework**: FastAPI with Uvicorn
- **Port**: 8000 (by default, configurable at `192.168.68.105:8000`)
- **Main Endpoints**:
  - `GET /get_snipes` - Fetch all price snipes
  - `POST /add_snipe` - Add new price snipe

**Location**: `backend/`

**Setup**:
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python main.py
```

---

## 🚀 Getting Started

### Prerequisites
- **Flutter SDK** (for frontend development) - https://flutter.dev/docs/get-started/install
- **Python 3.11+** (for backend) - https://www.python.org/downloads/
- **Git** - Version control

### Quick Start

1. **Clone/download this monorepo**
   ```bash
   cd deep_action_sniper_monorepo
   ```

2. **Start the Backend**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python main.py
   ```
   Backend will run on `http://192.168.68.105:8000`

3. **Start the Frontend**
   ```bash
   cd frontend
   flutter pub get
   flutter run
   ```

---

## 🔧 Configuration

### Frontend API URL
Edit `frontend/lib/main.dart` line 43:
```dart
static const String backendUrl = "http://192.168.68.105:8000";
```

Change `192.168.68.105` to your backend's IP address or hostname.

### Backend Port
Edit `backend/main.py` to change the port from default 8000.

---

## 📊 API Endpoints

### GET /get_snipes
Fetch all active snipes
- **Response**: 
  ```json
  {
    "snipes": [
      {
        "id": 1,
        "url": "https://example.com/product",
        "target_price": 29.99,
        "current_price": 34.99,
        "status": "Monitoring"
      }
    ]
  }
  ```

### POST /add_snipe
Add a new price snipe
- **Request Body**:
  ```json
  {
    "url": "https://example.com/product",
    "target_price": 29.99
  }
  ```
- **Response**: 
  ```json
  {
    "success": true,
    "message": "Snipe added successfully"
  }
  ```

---

## 🐛 Troubleshooting

### Frontend can't reach backend
1. Verify backend is running on the correct IP/port
2. Check `frontend/lib/main.dart` for correct backend URL
3. Ensure devices are on the same network
4. Check Flutter console logs for detailed error messages

**Frontend now includes detailed logging**:
- Look for `[SNIPER_APP]` messages in the Flutter console
- Logs show network requests, responses, timeouts, and validation errors

### Backend not responding
- Check if `python main.py` is running
- Verify port 8000 is not in use
- Check Python version (requires 3.11+)

---

## 📝 Development Notes

- **Original Frontend Location**: `c:\Users\Rida\deep_action_sniper`
- **Original Backend Location**: `c:\Users\Rida\deep_action_sniper_backend`
- **Monorepo Root**: `c:\Users\Rida\deep_action_sniper_monorepo`

This is a **copy-based monorepo**, not moved. Original project folders remain unchanged.

---

## 📚 References

- [Flutter Documentation](https://flutter.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Dart Language Guide](https://dart.dev/guides)
- [Python Guide](https://docs.python.org/3/)

---

## 📄 License

ISC

---

**Last Updated**: February 28, 2026
