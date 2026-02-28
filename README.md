<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Deep Action Sniper 🎯

## Basic Details

### Team Name: 

### Team Members
- Member 1:  - 
- Member 2:  - 

### Hosted Project Link


### Project Description
Deep Action Sniper is a cross-platform price monitoring application that allows users to monitor product prices across multiple platforms and receive notifications when prices match their target criteria.

### The Problem statement


### The Solution


---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Dart, Python
- Frameworks used: Flutter, FastAPI
- Libraries used: http, cupertino_icons, uvicorn
- Tools used: VS Code, Git, Flutter SDK, Python

---

## Features

List the key features of your project:
- Feature 1: Cross-platform compatibility (Android, iOS, Web, Windows, Linux, macOS)
- Feature 2: Real-time price monitoring and tracking
- Feature 3: Add and manage price snipes with target URLs and prices
- Feature 4: RESTful API backend with FastAPI

---

## Implementation

### For Software:

#### Installation

**Frontend:**
```bash
cd frontend
flutter pub get
```

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

#### Run

**Frontend (Development):**
```bash
cd frontend
flutter run
```

**Backend:**
```bash
cd backend
python main.py
```

---

## Project Documentation

### For Mobile Apps:

#### Installation Guide

**For Android (APK):**
1. Build APK from source:
   ```bash
   cd frontend
   flutter build apk --release
   ```
2. APK will be generated at: `frontend\build\app\outputs\flutter-apk\app-release.apk`
3. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
4. Open the downloaded APK file
5. Follow the installation prompts
6. Open the app and enjoy!

**For iOS:**
1. Build iOS app from source:
   ```bash
   cd frontend
   flutter build ios --release
   ```
2. Follow Apple's distribution guidelines for app store submission

**Building from Source:**
```bash
# For Android
flutter build apk --release

# For iOS
flutter build ios --release

# For Web
flutter build web

# For Windows Desktop
flutter build windows

# For Linux Desktop
flutter build linux

# For macOS Desktop
flutter build macos
```

---

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `http://localhost:8000` (local development)

##### Endpoints

**GET /get_snipes**
- **Description:** Fetch all active price snipes
- **Parameters:** None
- **Response:**
```json
{
  "status": "success",
  "data": []
}
```

**POST /add_snipe**
- **Description:** Add a new price snipe to monitor
- **Request Body:**
```json
{
  "url": "https://example.com/product",
  "target_price": 99.99
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Snipe added successfully"
}
```

---

## Architecture

### System Components

- **Frontend**: Flutter application handling UI, user input, and API communication
- **Backend**: FastAPI REST API managing price data and snipe records
- **Database**: 

### Technologies Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Flutter (Dart) |
| Backend | FastAPI (Python) |
| Server | Uvicorn |

---

## Project Demo

### Video


*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos


---

## Team Contributions

- [Name 1]: 
- [Name 2]: 

---

## License

This project is licensed under the  License - see the LICENSE file for details.

---

Made with ❤️ at TinkerHub

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
