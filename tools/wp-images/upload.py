#!/usr/bin/env python3
"""Put a rendered image on a public URL (postmypost bucket) for wp_upload_media_from_url.

    python3 upload.py <file> <init_upload.json> [key_prefix]

<init_upload.json> is the response of postmypost init_upload
(project_id=366895, name=<file name>, size=<bytes>), saved to a file.
key_prefix defaults to "272457/wp-media/<site or folder>" - pass e.g. 272457/wp-media/blog.speedyindex.com/2026-11-02
Prints the public HTTPS URL. GitHub push is blocked from cloud runs, so this is the default path.
"""
import json, os, subprocess, sys

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    path, init = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
    prefix = (sys.argv[3] if len(sys.argv) > 3 else "272457/wp-media/misc").strip("/")
    if not prefix.startswith("272457/"):
        sys.exit("key prefix must start with 272457/ (bucket policy)")
    fields = {f["key"]: f["value"] for f in init["fields"]}
    key = f"{prefix}/{os.path.basename(path)}"
    cmd = ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST", init["action"],
           "-F", f"key={key}"]
    # do NOT add Content-Type: the policy does not allow extra fields (403)
    for k in ("X-Amz-Credential", "X-Amz-Algorithm", "X-Amz-Date", "Policy", "X-Amz-Signature"):
        cmd += ["-F", f"{k}={fields[k]}"]
    cmd += ["-F", f"file=@{path}"]
    code = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
    if code not in ("200", "201", "204"):
        sys.exit(f"upload failed: HTTP {code}")
    url = f"{init['action'].rstrip('/')}/{key}"
    check = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code} %{size_download}", url],
                           capture_output=True, text=True).stdout.split()
    if check[0] != "200" or int(check[1]) != os.path.getsize(path):
        sys.exit(f"uploaded but not readable: {check}")
    print(url)

if __name__ == "__main__":
    main()
