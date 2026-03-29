# student_name: Sumitha A
# roll_number: 727823TUCY048
# project_name: Cloud S3 Bucket Scanner
# date: 2026-03-29

import boto3
import requests
import datetime
import json
from botocore.exceptions import ClientError, NoCredentialsError

ROLL_NUMBER = "727823TUCY048"
TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[*] Roll Number: {ROLL_NUMBER}")
print(f"[*] Timestamp  : {TIMESTAMP}")
print("=" * 55)

SUFFIXES = ["-public", "-private", "-dev", "-backup",
            "-logs", "-staging", "-data", "-test"]

def check_bucket_public(bucket_name):
    url = f"https://{bucket_name}.s3.amazonaws.com/"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return "PUBLIC", r.status_code
        elif r.status_code == 403:
            return "PRIVATE/FORBIDDEN", r.status_code
        elif r.status_code == 404:
            return "NOT FOUND", r.status_code
        else:
            return "UNKNOWN", r.status_code
    except Exception as e:
        return f"ERROR: {e}", 0

def audit_bucket_acl(bucket_name):
    s3 = boto3.client("s3", region_name="us-east-1")
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        grants = acl.get("Grants", [])
        for grant in grants:
            grantee = grant.get("Grantee", {})
            permission = grant.get("Permission", "")
            uri = grantee.get("URI", "")
            if "AllUsers" in uri:
                if permission == "READ":
                    return "PUBLIC-READ (Medium)"
                elif permission == "WRITE":
                    return "PUBLIC-WRITE (CRITICAL)"
                elif permission == "FULL_CONTROL":
                    return "FULL CONTROL (CRITICAL)"
        return "PRIVATE (Safe)"
    except ClientError as e:
        code = e.response["Error"]["Code"]
        if code == "AccessDenied":
            return "ACCESS DENIED - cannot read ACL"
        elif code == "NoSuchBucket":
            return "BUCKET DOES NOT EXIST"
        return f"ClientError: {code}"
    except NoCredentialsError:
        return "NO AWS CREDENTIALS FOUND"

def list_objects(bucket_name):
    s3 = boto3.client("s3", region_name="us-east-1")
    try:
        resp = s3.list_objects_v2(Bucket=bucket_name)
        contents = resp.get("Contents", [])
        if not contents:
            return []
        return [obj["Key"] for obj in contents]
    except ClientError:
        return []

def wordlist_scan(keyword):
    print(f"\n[TC-03] Wordlist Enumeration — keyword: '{keyword}'")
    print("-" * 55)
    found = []
    for suffix in SUFFIXES:
        name = keyword + suffix
        status, code = check_bucket_public(name)
        print(f"  {name:<45} [{code}] {status}")
        if code == 200:
            found.append(name)
    print(f"\n  >> {len(found)} bucket(s) found out of {len(SUFFIXES)} tested")
    return found

def run_test_case(tc_id, bucket_name, mode="probe"):
    print(f"\n[{tc_id}] Target: {bucket_name} | Mode: {mode.upper()}")
    print("-" * 55)
    status, code = check_bucket_public(bucket_name)
    print(f"  HTTP Status : {code}")
    print(f"  Access      : {status}")
    if mode == "audit":
        acl_result = audit_bucket_acl(bucket_name)
        print(f"  ACL Audit   : {acl_result}")
    objects = list_objects(bucket_name)
    if objects:
        print(f"  Objects     : {objects}")
    else:
        print(f"  Objects     : None found / not accessible")
    print(f"  Timestamp   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ── Run all test cases ──────────────────────────────────
print("\n>>> TEST CASE 1: Single Probe — Public Bucket")
run_test_case("TC-01", "skct-727823tucy048-public", mode="probe")

print("\n>>> TEST CASE 2: Single Probe — Private Bucket")
run_test_case("TC-02", "skct-727823tucy048-private", mode="probe")

print("\n>>> TEST CASE 3: Wordlist Enumeration")
wordlist_scan("skct-727823tucy048")

print("\n>>> TEST CASE 4: ACL Permission Audit")
run_test_case("TC-04", "skct-727823tucy048-dev", mode="audit")

print("\n>>> TEST CASE 5: Empty Bucket Probe")
run_test_case("TC-05", "skct-727823tucy048-backup", mode="probe")

print("\n" + "=" * 55)
print("[*] Scan complete.")
print(f"[*] Roll Number : {ROLL_NUMBER}")
print(f"[*] Finished at : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")