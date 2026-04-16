
## 📌 Telegram Group Members Scraper

A Python script that uses the Telegram API to fetch and extract usernames or full names of members from a specified Telegram group.

---

## 🚀 Features

* Extracts member usernames or names from a Telegram group
* Supports public and private groups (depending on access permissions)
* Option to save results to a file
* Simple and easy to modify

---

## 🛠️ Requirements

* Python 3.x
* Telethon library

Install dependencies:

```bash
pip install telethon
```

---

## 🔑 Telegram API Setup

To use this script, you need Telegram API credentials:

1. Go to: [https://my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Click on **API Development Tools**
4. Copy your:

   * `api_id`
   * `api_hash`

---

## ⚙️ Usage

Update the following variables in the script:

```python
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
group_username = "GROUP_USERNAME"
```

Run the script:

```bash
python script.py
```

---

## 📂 Example Output

```
user1
user2
user3
```

---

## ⚠️ Notes

* You must have access to the target group
* Some groups restrict member visibility
* Excessive or improper use may result in Telegram account limitations or bans

