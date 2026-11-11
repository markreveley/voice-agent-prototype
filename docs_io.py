"""docs_io.py - move Python code between Google Docs and the sandbox.


Workflow (Claude performs the Drive tool calls; this module handles the text):
  LOAD: Drive download_file_content(fileId, exportMimeType="text/plain")
        returns base64 -> decode_export(b64) -> clean source -> write_program()
  SAVE: read_program() -> prepare_upload(src) -> Drive create_file
        (contentMimeType="text/plain", textContent=...) for a new Doc.
Never load code with read_file_content: it returns Markdown with
backslash escapes and doubled blank lines, which breaks code.
"""
import base64, re, subprocess, sys


def decode_export(b64: str) -> str:
    """Turn a plain-text Docs export (base64) into clean Python source."""
    text = base64.b64decode(b64).decode("utf-8-sig")   # strips byte order mark
    text = text.replace("\r\n", "\n").replace("\r", "\n")  # Windows endings
    text = re.sub(r"\n{4,}", "\n\n\n", text)            # cap blank-line growth
    return text.rstrip() + "\n"


def prepare_upload(src: str) -> str:
    """Normalize source before saving it to a Doc."""
    return src.replace("\r\n", "\n").rstrip() + "\n"


def write_program(name: str, src: str, folder: str = "/tmp/programs") -> str:
    import os
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, name)
    with open(path, "w") as f:
        f.write(src)
    return path


def read_program(path: str) -> str:
    with open(path) as f:
        return f.read()


def run_program(path: str, *args: str, timeout: int = 60):
    """Run a program and return (exit code, stdout, stderr)."""
    r = subprocess.run([sys.executable, path, *args],
                       capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr
