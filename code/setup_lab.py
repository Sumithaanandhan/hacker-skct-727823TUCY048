# student_name: SUMITHA A | roll_number: 727823TUCY048
import datetime, subprocess, sys

ROLL_NUMBER = "727823TUCY048"
print(f"[SETUP] Roll Number : {ROLL_NUMBER}")
print(f"[SETUP] Timestamp   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("[SETUP] Installing required packages...")

packages = ["boto3", "requests", "pyyaml", "pandas", "jupyter"]
for pkg in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])
    print(f"  [OK] {pkg}")

print("[SETUP] All dependencies installed successfully.")
print(f"[SETUP] Environment ready for 727823TUCY048 S3 Scanner.")