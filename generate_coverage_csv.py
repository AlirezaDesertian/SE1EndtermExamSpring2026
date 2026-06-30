import json
import csv
from pathlib import Path

coverage_file = Path("coverage.json")
csv_file = Path("coverage_report_40231035.csv")

with coverage_file.open("r", encoding="utf-8") as f:
    data = json.load(f)

with csv_file.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["file", "statements", "covered_lines", "missing_lines", "coverage_percent"])

    for file_path, info in sorted(data["files"].items()):
        summary = info["summary"]
        writer.writerow([
            file_path,
            summary.get("num_statements", 0),
            summary.get("covered_lines", 0),
            summary.get("missing_lines", 0),
            summary.get("percent_covered_display", summary.get("percent_covered", 0)),
        ])

    totals = data["totals"]
    writer.writerow([])
    writer.writerow([
        "TOTAL",
        totals.get("num_statements", 0),
        totals.get("covered_lines", 0),
        totals.get("missing_lines", 0),
        totals.get("percent_covered_display", totals.get("percent_covered", 0)),
    ])

print(f"CSV report generated at {csv_file}")