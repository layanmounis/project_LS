import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

with open("data/jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

df = pd.DataFrame(jobs)

print("Total jobs:", len(df))
print("\nFirst 5 titles:")
print(df["job_title"].head())

# sklearn preprocessing: encode job titles
le = LabelEncoder()
df["job_title_encoded"] = le.fit_transform(df["job_title"].astype(str))

df.to_json("data/clean_jobs.json", orient="records", force_ascii=False, indent=2)
print("\nSaved clean data to data/clean_jobs.json")