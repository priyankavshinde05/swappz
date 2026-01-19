import subprocess
import sys

def test_swapp():
    result = subprocess.run(
        [sys.executable, "swapp.py", "10", "20"],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    assert "a = 20" in output
    assert "b = 10" in output
    print("Test passed")

if __name__ == "__main__":
    test_swapp()
