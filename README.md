# Cloud S3 Bucket Scanner
**Name:** Sumitha A
**Roll Number:** 727823TUCY048
**Subject:** Hacker Techniques, Tools and Incident Handling
**Category:** Cloud Security / Reconnaissance

## Tool Description
Python-based scanner to detect misconfigured AWS S3 buckets.
Identifies public access, ACL misconfigurations, and exposed objects.

## Lab Environment
- OS: Windows/Kali Linux
- Python 3.11
- AWS Free Tier (isolated test buckets)

## Setup
```bash
pip install -r requirements.txt
aws configure
```

## Usage
```bash
python code/setup_lab.py
python code/tool_main.py
python code/analyze_results.py
```

## Test Cases
| TC | Target | Result |
|---|---|---|
| TC-01 | public bucket | 200 PUBLIC |
| TC-02 | private bucket | 403 PRIVATE |
| TC-03 | wordlist scan | 2/8 found |
| TC-04 | dev bucket ACL | CRITICAL |
| TC-05 | empty bucket | 200 empty |

## Tools Used
boto3, requests, pyyaml, pandas, jupyter
```
