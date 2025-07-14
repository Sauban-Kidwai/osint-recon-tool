# 🔎 OSINT Recon Tool

A lightweight Python-based reconnaissance tool designed for red teamers, bug bounty hunters, and penetration testers. It detects CMS types, finds usernames, identifies login portals, and generates clean HTML reports for your targets. The future plan is for this to become the main reconnaissance tool that can help people

---

## 🚀 Features

- ✅ CMS Detection via WhatWeb (e.g. WordPress, Joomla, Drupal)
- ✅ Username Enumeration (CMS-aware: WordPress, Generic)
- ✅ Login Portal Discovery (40+ endpoint patterns from top CMS platforms)
- ✅ Clean HTML Report Output (styled and timestamped)
- ✅ Usernames saved to `output/usernames.txt`
- ✅ CLI arguments and verbose mode

---

## 📂 Project Structure

```
osint_tool/
├── cms_detector.py
├── login_finder.py
├── main.py
├── report_generator.py
├── username_enum.py
├── templates/               # Jinja2 templates for HTML report
├── output/                  # Generated reports and usernames (auto-created)
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/osint-recon-tool.git
cd osint-recon-tool
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Install WhatWeb** (required for CMS detection)
```bash
sudo apt install whatweb
```

> If that doesn't work, install manually:
```bash
git clone https://github.com/urbanadventurer/WhatWeb.git
cd WhatWeb
sudo gem install bundler
bundle install
```

---

## ⚙️ Usage

```bash
python3 main.py https://example.com -v
```

### Options:
- `-v` / `--verbose`: Enable verbose output
- `-o` / `--output`: Set output directory (default: `output/`)
- `--no-report`: Skip HTML report generation

---

## 📄 Output

- `report.html`: Visual summary of CMS, usernames, and login endpoints
- `usernames.txt`: Extracted usernames (WordPress / generic scraping)

---

## 🌐 Supported CMS-Specific Features

| CMS        | CMS Detection | User Enumeration | Login Paths Detected      |
|------------|----------------|------------------|----------------------------|
| WordPress  | ✅ WhatWeb     | ✅ /?author=X     | ✅ wp-login, wp-admin       |
| Joomla     | ✅ WhatWeb     | ⏳ Planned        | ✅ /administrator          |
| Drupal     | ✅ WhatWeb     | ⏳ Planned        | ✅ /user/login             |
| Magento    | ✅ WhatWeb     | ⏳ Planned        | ✅ /admin                  |
| Ghost, Wix, etc. | ✅ Partial | ⏳ Planned      | ✅ /ghost/, /login, etc.   |

---

## 📌 TODO Roadmap

- [ ] Add Joomla/Drupal-specific enumeration
- [ ] Add subdomain + DNS recon modules
- [ ] Export to JSON for possible future integrations

---

## 🧑‍💻 Author

Built by Sauban Kidwai for educational and ethical testing purposes only.

---

## Inspired By:

- Course: [Hands-On Phishing](https://academy.simplycyber.io/l/pdp/hands-on-phishing)
- Author: [Tyler Rambsbey](https://www.linkedin.com/in/tyler-ramsbey-86221643/)

---

## 📜 License

MIT License — Free to use, modify, and distribute.

---
