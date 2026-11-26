import os

# Honest tab count, digits only, no words or punctuation.
ENTRY = "63"

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "wb") as f:
    f.write(ENTRY.encode("utf-8"))
