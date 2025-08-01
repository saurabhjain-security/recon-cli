# 🌐 Subdomain Intelligence Mapper
# recon-cli

A Python CLI tool that takes a list of subdomains and returns enriched metadata including:

- 🔍 IP address lookup
- 🔁 Reverse DNS (domain pointer)
- 🏢 WHOIS organization data

This is useful for **OSINT**, **infrastructure mapping**, or **reconnaissance** in security assessments.

---

## 📦 Features

- Resolve subdomains to IP addresses
- Get reverse DNS pointers for IPs
- Parse WHOIS data for OrgName and Organization
- Display results in a **color-coded tabulated format**

---

## 🛠️ Requirements

- Python 3.6+
- The following tools installed and available in `PATH`:
  - `host`
  - `whois`

Install required Python packages:

```bash
pip install termcolor tabulate
````

## 🚀 Usage
```bash
python3 script.py subdomain_list.txt
````

## 📄 Example Input (subdomain_list.txt)

````txt
www.google.com
api.github.com
aws.amazon.com
````

## ✅ Example Output


<img width="2444" height="1070" alt="image" src="https://github.com/user-attachments/assets/d485e3c4-55e8-429c-b69b-ce192938b017" />



