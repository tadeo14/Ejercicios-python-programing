import subprocess



p = subprocess.run(["ping","lanacion.com"], capture_output=True, encoding="cp850")

