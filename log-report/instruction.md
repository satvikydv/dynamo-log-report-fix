There is an Apache-style access log at `/app/access.log`.

Parse the log and write a JSON summary report to `/app/report.json` containing exactly these three keys:

1. `total_requests`: the total number of non-blank lines in the log (integer).
2. `unique_ips`: the number of distinct client IP addresses, taken from the first field of each log line (integer).
3. `top_path`: the request path (e.g. `/index.html`) that was requested more often than any other path across the whole log (string). If multiple paths are tied for the highest count, use whichever of the tied paths appears first in the log file.

`/app/report.json` must contain a single JSON object with only these three keys - no extra keys, no wrapper structure.
