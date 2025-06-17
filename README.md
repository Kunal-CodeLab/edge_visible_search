# 🔍 Edge Visible Search

**Edge Visible Search** is a Python automation tool that performs 30 Bing searches using Microsoft Edge in visible mode. It simulates user-like activity like typing and scrolling using Selenium.

---

## 🧰 Requirements

- Python 3.x installed  
- Microsoft Edge browser installed  
- Selenium library  
- Edge WebDriver (`msedgedriver.exe`) — placed in same folder as script

---

## 📥 Step-by-Step Setup

### ✅ Step 1: Install Python (if not installed)
Download from: https://www.python.org/downloads/

Make sure you tick **"Add to PATH"** during installation.

---

### ✅ Step 2: Download Edge WebDriver

1. Open this link: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. Check your Edge browser version  
   - Open Edge → go to `edge://settings/help`
3. Download the **matching version** of `msedgedriver`
4. Extract `msedgedriver.exe` and **place it in the same folder** as this script.

> 🔁 Final folder should look like:
```
📁 edge_visible_search/
├── edge_visible_search.py
├── msedgedriver.exe ✅
├── requirements.txt
├── run.bat
└── README.md
```

---

### ✅ Step 3: Install Required Packages

Open Command Prompt in the folder and run:

```bash
pip install -r requirements.txt
```

---

### ✅ Step 4: Run the Script

🔹 **Option 1:** Just double-click `run.bat`  
🔹 **Option 2:** Or manually run:

```bash
python edge_visible_search.py
```

It will:
- Open Edge
- Perform 30 Bing searches automatically
- Scroll each page
- Close browser at the end

---

## 💬 FAQs

**Q: What is msedgedriver.exe?**  
A: It’s a bridge between Selenium and Microsoft Edge — required to control the browser.

**Q: Is this safe to use?**  
A: Yes! It just opens your Edge browser, searches 30 terms on Bing, and scrolls.

---

## 👨‍💻 Author

**Kunal Choudhary**  
📧 kunal.codes5@gmail.com  
🎓 BCA Cyber Security – JNU Jaipur

---

## ⚖️ License

MIT License – Free to use and modify.---

## 🔐 Safety & Trust

✅ **Microsoft Edge Required**  
This script requires Microsoft Edge to be installed on your system.  
Make sure you're **logged in with your Microsoft account** inside Edge to earn Bing Rewards automatically.

✅ **100% Safe & Secure**  
This script:
- Does **not collect any personal data**
- Does **not interfere** with system files or browser settings
- Does **not break any Microsoft or browser policy**

We have carefully created this automation to respect:
- Bing and Edge's **Terms of Service**
- Ethical use of browser automation
- Educational/demo usage only

🔒 **This tool is completely local** – all actions happen inside your computer only.

✅ Verified safe for automation tasks like:
- Educational demos
- Showcasing browser automation
- Simulating searches with scrolling behavior

---

Use responsibly. We respect all platform rules and expect the same from all users.