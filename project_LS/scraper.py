import requests
from bs4 import BeautifulSoup
import json

URL = "https://wuzzuf.net/a/Python-Jobs-in-Egypt"
HEADERS = {"User-Agent": "Mozilla/5.0"}

r = requests.get(URL, headers=HEADERS, timeout=20)
print("Status code:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

# Try to collect job titles from any h2 links
titles = [a.get_text(strip=True) for a in soup.select("h2 a") if a.get_text(strip=True)]
print("Titles found:", len(titles))

jobs = [{"job_title": t} for t in titles]

with open("data/jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print("Saved to data/jobs.json")