skill: /bootstrap

Trigger: Mark says "slash bootstrap", or another skill (start-dev) calls it, or the sandbox has lost /tmp/docs_io.py mid-session. Moved from agents.md in run 03 (2026-11-10).

What it does: loads docs_io.py, the helper that moves code between Google Docs and the sandbox. Do this before any code work.

Steps

1. Find docs_io.py in root (confirm its parent is root) and download it with download_file_content and exportMimeType text/plain. It returns base64.
2. In the sandbox, paste the base64 into this and run it:

   import base64, importlib.util
   b = "<paste base64 here>"
   src = base64.b64decode(b).decode("utf-8-sig").replace("\r\n", "\n")
   open("/tmp/docs_io.py", "w").write(src)
   spec = importlib.util.spec_from_file_location("docs_io", "/tmp/docs_io.py")
   docs_io = importlib.util.module_from_spec(spec); spec.loader.exec_module(docs_io)

3. From then on use docs_io.decode_export(b64) to load any program (file format rule fmt-03).
4. Installing packages: pip install --break-system-packages NAME

Notes

- A new chat starts with an empty sandbox (test record t08), so run this in every new development chat.
- Status: tested in run 02 (t08) and run 03, as part of start-dev.
