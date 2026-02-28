# Setup Checklist

Use this checklist to ensure both frontend and backend are properly configured and ready to run.

## ✅ Backend Setup (Python/FastAPI)

- [ ] Navigate to `backend/` folder
- [ ] Create Python virtual environment: `python -m venv venv`
- [ ] Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
- [ ] Install dependencies: `pip install -r requirements.txt`
  - ⚠️ If `requirements.txt` is missing, you'll need to create one or ask the user to add it
- [ ] Verify backend can start: `python main.py`
- [ ] Backend should be accessible at: `http://192.168.68.105:8000`
- [ ] Test endpoint: Open browser and navigate to `http://192.168.68.105:8000/get_snipes`
  - Expected response: JSON with snipes data or empty list

**Status**: ⚠️ **ACTION NEEDED** - Backend folder only contains `main.py`. Missing:
- `requirements.txt` file (Python dependencies list)
- Any other Python modules or configuration files

---

## ✅ Frontend Setup (Flutter)

- [ ] Navigate to `frontend/` folder
- [ ] Install Flutter if not already installed: https://flutter.dev/docs/get-started/install
- [ ] Verify Flutter installation: `flutter --version`
- [ ] Get Flutter dependencies: `flutter pub get`
- [ ] **IMPORTANT**: Verify backend URL in `frontend/lib/main.dart`
  - Line 43: `static const String backendUrl = "http://192.168.68.105:8000";`
  - ⚠️ Change IP address if backend is running on different machine/IP
- [ ] List available devices: `flutter devices`
- [ ] Choose a device and run: `flutter run`

**Frontend Changes Applied**:
- ✅ Added comprehensive error handling
- ✅ Added input validation (URL format, price validation)
- ✅ Added 10-second request timeout
- ✅ Added detailed logging (look for `[SNIPER_APP]` in console)
- ✅ Better error messages for debugging

---

## 🔍 Verification Steps

### Check Backend is Working

```bash
cd backend
python main.py
```

Expected output should show the server is running. Then in another terminal:

```bash
curl http://192.168.68.105:8000/get_snipes
```

Should return JSON response.

### Check Frontend Can Reach Backend

1. Open Flutter console while running the app
2. Try to add a snipe with valid data (real URL + numeric price)
3. Look for `[SNIPER_APP]` log messages showing:
   - `Adding snipe: url=...`
   - `Sending POST request to...`
   - `Response received: status=...`

If you see **"Network error: Cannot reach backend"** or **"Request timed out"**:
- Verify backend IP in `frontend/lib/main.dart` is correct
- Ensure backend is actually running
- Check firewall isn't blocking port 8000

---

## ⚠️ Missing Files to Address

### Backend Issues
**Status**: Missing Python dependencies file

The backend folder only contains:
- `main.py` - The FastAPI application
- `.git/` - Version control

**NEED**: 
- [ ] `requirements.txt` - List of Python packages (FastAPI, Uvicorn, Pydantic, etc.)
- [ ] Any additional Python modules the backend uses
- [ ] Configuration files (if any)

**Action**: Please provide or create `backend/requirements.txt` with the Python dependencies.

Example format:
```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
```

---

## 🔧 Configuration Files Status

| File | Location | Status | Notes |
|------|----------|--------|-------|
| Frontend pubspec.yaml | `frontend/pubspec.yaml` | ✅ Present | Flutter dependencies configured |
| Backend requirements.txt | `backend/requirements.txt` | ⚠️ Missing | Need to configure Python dependencies |
| Backend main.py | `backend/main.py` | ✅ Present | FastAPI application |
| Frontend main.dart | `frontend/lib/main.dart` | ✅ Present | Updated with error handling |

---

## 📋 Next Steps

1. **Provide backend requirements** or run: `pip freeze > backend/requirements.txt` in the backend venv
2. **Update frontend URL** if backend IP/port differs
3. **Test both services** separately before testing integration
4. **Check logs** - Frontend logging will help diagnose connection issues

---

**Date**: February 28, 2026  
**Monorepo Root**: `c:\Users\Rida\deep_action_sniper_monorepo`
