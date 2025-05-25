from redis import Redis
import os
import sys
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


def get_redis() -> Optional[Redis]:
  redis_url = os.getenv("REDIS_URL")
  if redis_url is None: sys.exit("REDIS_URL environment variable is not set")
  try:
    redis_client = Redis.from_url(redis_url, decode_responses=True)
    assert isinstance(redis_client, Redis)
    return redis_client
  except Exception:
    return None