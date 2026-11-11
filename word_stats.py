"""word_stats.py - tiny test program for the voice agent prototype."""
import sys
from collections import Counter


def stats(text):
    words = [w.strip('.,!?;:"()').lower() for w in text.split()]
    words = [w for w in words if w]
    return len(words), Counter(words).most_common(3)


if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "the voice agent reads the doc and the doc holds the code"
    n, top = stats(text)
    print(f"{n} words; top: {top}")
