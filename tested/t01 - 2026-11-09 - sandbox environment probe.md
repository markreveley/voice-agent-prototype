# T01 - Sandbox environment probe

**Date:** November 9, 2026 **Run by:** Claude, in a Claude app voice chat with Mark

## What was run

Two Python runs in the code execution sandbox:

1. Printed the Python version and platform, wrote a file to /tmp, requested <https://api.github.com>, and ran git --version.
2. In a separate run, checked whether the /tmp file still existed, and requested <https://pypi.org/simple/requests/>.

## Raw output

Run 1:

- Python 3.12.3, Linux 6.18 x86_64, glibc 2.39. Working directory: /
- GitHub API: HTTPError 403 Forbidden
- git version 2.43.0

Run 2:

- /tmp/persist_test.txt exists: True
- PyPI: status 200

## Observations

- Files persist between separate code runs within the same chat.
- PyPI is reachable; GitHub's API is refused. The 403 may come from a network proxy rather than GitHub itself.

## Not tested

- Whether files survive into a new chat.
- Whether pip install actually completes.
- Whether git clone over HTTPS from GitHub fails the same way.
