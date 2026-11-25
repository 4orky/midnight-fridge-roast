# midnight-fridge-roast: one-line roast generator.
#
# The joke below was picked from eleven hand-written candidates by scoring
# each one against the brief (midnight lockout, one punchline, spoken
# aloud, under 200 characters). This script only assembles the winning
# line, checks it against the entry gate, and saves it.

from pathlib import Path
import sys

HEADLINE_BITS = [
    "Midnight hits and my fridge goes full Fort Knox",
    "guarding food I bought from me, the burglar who paid for it.",
]
DASH = " — "
OUT_PATH = Path("/output/entry.txt")
LOWER_LIMIT = 1
UPPER_LIMIT = 200


def assemble_roast():
    return DASH.join(HEADLINE_BITS)


def gate_failures(roast):
    problems = []
    if not roast:
        problems.append("empty line")
    if not LOWER_LIMIT <= len(roast) <= UPPER_LIMIT:
        problems.append(f"length {len(roast)} outside 1-200")
    if roast != roast.strip():
        problems.append("leading or trailing whitespace")
    if roast.count("\n") > 0 or roast.count("\r") > 0:
        problems.append("more than one line")
    return problems


def save_roast(roast):
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(roast, encoding="utf-8")
    if OUT_PATH.read_text(encoding="utf-8") != roast:
        raise RuntimeError("round-trip check failed: file differs from roast")
    return OUT_PATH


def run():
    roast = assemble_roast()
    problems = gate_failures(roast)
    if problems:
        print("entry failed the gate: " + "; ".join(problems), file=sys.stderr)
        raise SystemExit(1)
    saved = save_roast(roast)
    print(f"saved {len(roast)} characters to {saved}")


run()
