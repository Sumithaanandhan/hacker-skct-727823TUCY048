# student_name: [YOUR NAME] | roll_number: 727823TUCY048
import datetime

ROLL_NUMBER = "727823TUCY048"
print(f"[ANALYZE] Roll Number : {ROLL_NUMBER}")
print(f"[ANALYZE] Timestamp   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("[ANALYZE] Analyzing scan results...\n")

results = [
    {"TC": "TC-01", "Bucket": "skct-727823tucy048-public",  "Code": 200, "Status": "PUBLIC",            "Severity": "Medium"},
    {"TC": "TC-02", "Bucket": "skct-727823tucy048-private", "Code": 403, "Status": "PRIVATE",           "Severity": "Safe"},
    {"TC": "TC-03", "Bucket": "Wordlist (8 targets)",       "Code": 200, "Status": "2 buckets found",   "Severity": "Medium"},
    {"TC": "TC-04", "Bucket": "skct-727823tucy048-dev",     "Code": 200, "Status": "PUBLIC-WRITE ACL",  "Severity": "CRITICAL"},
    {"TC": "TC-05", "Bucket": "skct-727823tucy048-backup",  "Code": 200, "Status": "PUBLIC (empty)",    "Severity": "Low"},
]

print(f"{'TC':<8}{'Bucket':<40}{'HTTP':<6}{'Status':<22}{'Severity'}")
print("-" * 90)
for r in results:
    print(f"{r['TC']:<8}{r['Bucket']:<40}{r['Code']:<6}{r['Status']:<22}{r['Severity']}")

critical = [r for r in results if r["Severity"] == "CRITICAL"]
public   = [r for r in results if r["Status"] == "PUBLIC"]

print(f"\n[SUMMARY] Total test cases   : {len(results)}")
print(f"[SUMMARY] Critical findings  : {len(critical)}")
print(f"[SUMMARY] Public buckets     : {len(public)}")
print(f"[SUMMARY] Scan by            : {ROLL_NUMBER}")
print(f"[SUMMARY] Analysis complete  : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")