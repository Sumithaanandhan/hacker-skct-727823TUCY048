# student_name: [YOUR NAME] | roll_number: 727823TUCY048
import datetime, subprocess, sys

ROLL_NUMBER = "727823TUCY048"
print(f"[RUN] Roll Number : {ROLL_NUMBER}")
print(f"[RUN] Timestamp   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("[RUN] Launching Cloud S3 Bucket Scanner...\n")

result = subprocess.run(
    [sys.executable, "tool_main.py"],
    capture_output=False
)

print(f"\n[RUN] Tool exited with code: {result.returncode}")
print(f"[RUN] Completed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")