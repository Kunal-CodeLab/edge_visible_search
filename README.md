# Edge Visible Search

**Edge Visible Search** is a Python automation tool that performs 30 Bing searches using Microsoft Edge in visible mode. It simulates user-like activity like typing and scrolling using Selenium.

---

## Table of Contents
- [What Was Built](#what-was-built)
- [Challenges & Problems Faced](#challenges--problems-faced)
- [How Problems Were Solved](#how-problems-were-solved)
- [Requirements](#requirements)
- [Step-by-Step Setup](#step-by-step-setup)
- [FAQs](#faqs)
- [Author](#author)
- [License](#license)
- [Safety & Trust](#safety--trust)

---

## What Was Built

Edge Visible Search is a Python browser automation utility using Selenium and Microsoft Edge (`msedgedriver.exe`). It automates 30 sequential Bing web searches in visible browser mode, simulating human typing delays, random page interactions, and smooth viewport scrolling to showcase browser automation workflows.

### Core Modules:
- **Selenium Edge WebDriver Controller (`edge_visible_search.py`)**: Manages browser instance lifecycle, URL navigation, and DOM element interactions using `msedgedriver.exe`.
- **Human Activity Simulator Engine**: Simulates realistic human search behaviors with character-by-character typing delays, random pause intervals, and smooth page scrolling.
- **One-Click Batch Execution Launcher (`run.bat`)**: Windows batch script automating Python environment verification and script execution.

---

## Challenges & Problems Faced

1. **WebDriver Version Mismatch & Launch Failures**: Incompatibilities between installed Microsoft Edge browser versions and `msedgedriver.exe` cause `SessionNotCreatedException` during browser initialization.
2. **Bot Detection & Fast Search Flagging**: Executing rapid automated search requests without human-like typing delays or viewport interactions causes search engines to trigger bot CAPTCHAs or rate limits.
3. **DOM Element Loading Timeouts**: Attempting to locate and interact with search input elements before Bing's dynamic page assets fully load results in `NoSuchElementException` or `ElementNotInteractableException`.

---

## How Problems Were Solved

1. **WebDriver Matching & Pre-flight Diagnostics**: Provided step-by-step version verification instructions in setup guides and error-handling checks for `msedgedriver.exe` path resolution.
2. **Humanized Typing Delays & Page Scrolling**: Integrated randomized sleep intervals (`random.uniform`) between keystrokes and JavaScript-driven page scrolling (`window.scrollTo`) to mirror natural human browsing.
3. **Explicit Selenium Web Driver Waits (`WebDriverWait`)**: Replaced hardcoded sleep pauses with Selenium `WebDriverWait` and `EC.element_to_be_clickable` conditions to wait for DOM elements to load reliably.

---

## Requirements

- Python 3.x installed  
- Microsoft Edge browser installed  
- Selenium library  
- Edge WebDriver (`msedgedriver.exe`) — placed in same folder as script

---

## Step-by-Step Setup

### Step 1: Install Python (if not installed)
Download from: https://www.python.org/downloads/

Make sure you tick **"Add to PATH"** during installation.

---

### Step 2: Download Edge WebDriver

1. Open this link: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. Check your Edge browser version  
   - Open Edge -> go to `edge://settings/help`
3. Download the **matching version** of `msedgedriver`
4. Extract `msedgedriver.exe` and **place it in the same folder** as this script.

Final folder structure should look like:
```
edge_visible_search/
├── edge_visible_search.py
├── msedgedriver.exe
├── requirements.txt
├── run.bat
└── README.md
```

---

### Step 3: Install Required Packages

Open Command Prompt in the folder and run:

```bash
pip install selenium
```

---

### Step 4: Run the Script

- **Option 1:** Double-click `run.bat`  
- **Option 2:** Or manually run:

```bash
python edge_visible_search.py
```

It will:
- Open Edge
- Perform 30 Bing searches automatically
- Scroll each page
- Close browser at the end

---

## FAQs

**Q: What is msedgedriver.exe?**  
A: It's a bridge between Selenium and Microsoft Edge — required to control the browser.

**Q: Is this safe to use?**  
A: Yes! It just opens your Edge browser, searches 30 terms on Bing, and scrolls.

---

## Author

**Kunal Choudhary**  
Email: kunal.codes5@gmail.com  
Degree: BCA Cyber Security – JNU Jaipur

---

## License

MIT License – Free to use and modify.

---

## Safety & Trust

**Microsoft Edge Required**  
This script requires Microsoft Edge to be installed on your system.  
Make sure you're **logged in with your Microsoft account** inside Edge to earn Bing Rewards automatically.

**100% Safe & Secure**  
This script:
- Does **not collect any personal data**
- Does **not interfere** with system files or browser settings
- Does **not break any Microsoft or browser policy**

We have carefully created this automation to respect:
- Bing and Edge's **Terms of Service**
- Ethical use of browser automation
- Educational/demo usage only

**This tool is completely local** – all actions happen inside your computer only.

Verified safe for automation tasks like:
- Educational demos
- Showcasing browser automation
- Simulating searches with scrolling behavior

---

Use responsibly. We respect all platform rules and expect the same from all users.
