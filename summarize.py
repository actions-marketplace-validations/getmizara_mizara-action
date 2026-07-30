#!/usr/bin/env python3
"""Renders a mizara test --json result as a GitHub Actions job summary."""

import json
import sys

_MARKER = {
    "PROTECTED": "PASS",
    "DEFAULT-DENIED": "WARN",
    "FAIL": "FAIL",
}


def main() -> None:
    result_path, summary_path = sys.argv[1], sys.argv[2]
    with open(result_path) as f:
        results = json.load(f)

    lines = ["## Mizara Safety Test", "", "| | Scenario | Category | Verdict |", "| --- | --- | --- | --- |"]

    for r in results:
        lines.append(f"| {_MARKER.get(r['verdict'], r['verdict'])} | `{r['id']}` | {r['category']} | {r['verdict']} |")

    protected = sum(1 for r in results if r["verdict"] == "PROTECTED")
    warned = sum(1 for r in results if r["verdict"] == "DEFAULT-DENIED")
    failed = sum(1 for r in results if r["verdict"] == "FAIL")

    lines.append("")
    lines.append(
        f"**{protected} protected, {warned} default-denied (no explicit rule), {failed} unprotected** "
        f"- of {len(results)} common risk scenarios."
    )

    if failed:
        lines.append("")
        lines.append(
            "Unprotected scenarios would be allowed to execute under this policy. "
            "Add a rule targeting the listed action to close the gap."
        )

    with open(summary_path, "a") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
