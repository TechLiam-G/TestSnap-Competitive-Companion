import argparse
import subprocess
import sys

def run():
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("--input", required=True)
    parser.add_argument("--expected", required=True)

    args = parser.parse_args()

    result = subprocess.run(
        [sys.executable, args.file],
        input=args.input + "\n",
        capture_output=True,
        text=True,
        timeout=5
    )

    output = result.stdout.strip()
    correct = result.returncode == 0 and output == args.expected.strip()

    if correct:
        s = f"""
CORRECT ANSWER!!!
=====================
Input: {args.input}

Output: {output}
Target output: {args.expected}
"""
    else:
        s = f"""
WRONG ANSWER :(
=====================
Input: {args.input}

Output: {output}
Target output: {args.expected}
"""
    print(s)

if __name__ == "__main__":
    run()
