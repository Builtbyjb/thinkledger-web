import redis
import os
import sys
from dotenv import load_dotenv
from typing import Generator, Any, Callable, Optional

load_dotenv()


def get_redis() -> Any:
  redis_url = os.getenv("REDIS_URL")
  if redis_url is None: sys.exit("REDIS_URL environment variable is not set")
  redis_client = redis.Redis.from_url(redis_url, decode_responses=True)
  try: yield redis_client
  finally: redis_client.close()


def gen_redis(
    redis_gen: Callable[..., Generator[redis.Redis, Any, None]] = get_redis
    ) -> Optional[redis.Redis]:
  """
    Takes in a redis generator function any redis a Redis instance or None.
    The Depends function from fastapi does not handle generators well, if it not called
    within a route.
  """
  for v in redis_gen():
    if isinstance(v, redis.Redis): return v
  return None
