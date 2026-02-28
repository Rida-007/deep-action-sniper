<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Deep Action Sniper 🎯

## Basic Details

### Team Name: Cache & Cookie

### Team Members
- Member 1: Rida Waseem - [College of Engineering Vadakara]
- Member 2: Aswandha R J - [College of Engineering Vadakara]

### Hosted Project Link
https://drive.google.com/drive/folders/10l7oABCP4BEqehKNdDpa0T1_LfJIRsjN

### Project Description
Deep Action Sniper is a cross-platform price monitoring application that allows users to monitor product prices across multiple platforms and receive notifications when prices match their target criteria.

### The Problem statement
In today’s online shopping environment, product prices fluctuate frequently. Users often miss the best buying opportunity because they cannot continuously monitor price changes. Manually checking prices multiple times a day is inefficient, time-consuming, and unreliable.

There is a need for a smart system that can:
	•	Track product prices automatically
	•	Monitor market changes
	•	Alert users when their desired price is reached
	•	Help users make timely purchasing decisions

Without such a system, users risk either overpaying or missing limited-time deals.  

### The Solution
Deep Action Sniper provides a smart and automated price-tracking solution.

The application allows users to:
	•	Add product URLs
	•	Set a desired target price
	•	Monitor simulated market price changes
	•	Automatically detect when the price reaches or falls below the target

The backend handles dynamic price simulation and updates product status to “Target Hit” when conditions are met. The dashboard displays real-time information including current price, target price, and potential savings.

By combining Flutter (frontend), FastAPI (backend), and MySQL (database), the system demonstrates a complete full-stack solution that improves user decision-making through automation and precision.
---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Dart, Python
- Frameworks used: Flutter, FastAPI
- Libraries used: http, cupertino_icons, uvicorn
- Tools used: VS Code, Git, Flutter SDK, Python

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
```bash
# Frontend
cd frontend
flutter pub get

# Backend
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

#### Run
```bash
# Frontend (Development)
cd frontend
flutter run

# Backend
cd backend
python main.py
```

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

https://drive.google.com/file/d/1Eo1LsSldXi5Cu0_XTQQwAimUOyN-NSRP/view?usp=drivesdk Add screenshot 1 here with proper name
This screenshot shows our backend API endpoint for adding a new product to track in Deep Action Sniper.

https://drive.google.com/file/d/1oXhGTgRRfoIYDscGjChpEjvO7ZM7-vGP/view?usp=drivesdk(Add screenshot 2 here with proper name)
This screenshot shows the frontend UI where users view tracked products and add a new product to monitor with a target price.

https://drive.google.com/file/d/1Xn2GZCHw_ZiuazbeLL9WZyIga72ovVoF/view?usp=drivesdk![Screenshot3](Add screenshot 3 here with proper name)
This screenshot represents the product tracking list screen where users can monitor multiple snipes and check their status in real time.

#### Diagrams


**Application Workflow:**

https://drive.google.com/file/d/1M7zXbc3_rTz8DnH8ksQbQNYVpGElicda/view?usp=drivesdk(docs/workflow.png)
*Add caption explaining your workflow*

---


#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

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

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
https://drive.google.com/file/d/1baNxXrS0vpl5bRhfzeJri_j9afA0bnIU/view?usp=drivesdk

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
