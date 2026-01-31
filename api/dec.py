import requests
import os
from datetime import datetime
from upstash_redis import Redis

redis = Redis(
    url=os.environ["KV_REST_API_URL"],
    token=os.environ["KV_REST_API_TOKEN"]
)

def handler(request):
    url = "https://taokey567.c25tool.net/src/srctoolvip.php"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)

    key = f"dec:{datetime.utcnow().isoformat()}"
    redis.set(key, r.text)

    return {
        "statusCode": 200,
        "body": f"Saved OK | key={key} | length={len(r.text)}"
    }
