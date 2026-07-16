import json
from pathlib import Path

def test_total_requests():
    """1. `total_requests`: the total number of non-blank lines in the log (integer)."""
    report = json.loads(Path("/app/report.json").read_text())
    assert report.get("total_requests") == 6, f"Expected 6 total requests, got {report.get('total_requests')}"

def test_unique_ips():
    """2. `unique_ips`: the number of distinct client IP addresses, taken from the first field of each log line (integer)."""
    report = json.loads(Path("/app/report.json").read_text())
    assert report.get("unique_ips") == 3, f"Expected 3 unique IPs, got {report.get('unique_ips')}"

def test_top_path():
    """3. `top_path`: the request path (e.g. `/index.html`) that was requested more often than any other path across the whole log (string)."""
    report = json.loads(Path("/app/report.json").read_text())
    assert report.get("top_path") == "/index.html", f"Expected /index.html as top path, got {report.get('top_path')}"
