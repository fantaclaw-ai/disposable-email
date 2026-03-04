#!/usr/bin/env python3
import json
import random
import string
import time
from urllib import request

API = "https://api.mail.tm"


def http_json(url, method="GET", data=None, headers=None):
    req = request.Request(url=url, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    with request.urlopen(req, body, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    domains = http_json(f"{API}/domains").get("hydra:member", [])
    if not domains:
        raise SystemExit("No Mail.tm domains available")

    domain = domains[0]["domain"]
    local = "tmp" + str(int(time.time())) + "".join(random.choices(string.ascii_lowercase, k=4))
    address = f"{local}@{domain}"
    password = "Tmp!" + "".join(random.choices(string.ascii_letters + string.digits, k=12))

    account = http_json(f"{API}/accounts", method="POST", data={"address": address, "password": password})
    token_resp = http_json(f"{API}/token", method="POST", data={"address": address, "password": password})

    print(json.dumps({
        "address": address,
        "password": password,
        "token": token_resp.get("token"),
        "accountId": account.get("id"),
        "domain": domain,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
