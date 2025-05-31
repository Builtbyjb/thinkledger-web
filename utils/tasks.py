from enum import Enum
from database.redis.redis import get_redis
from utils.logger import log


class Tasks(Enum):
  setup_spreadsheet = "setup_spreadsheet"
  sync_transaction = "sync_transaction"


class TaskPriority(Enum):
  """
    HIGH priority tasks are tasks that require immediate user feedback.
    LOW priority tasks are tasks that go on in the background without direct user input.
  """
  HIGH = "HIGH"
  LOW = "LOW"


def add_task(user_id: str, priority: str, value: str) -> bool:
  """
    The value argument contains the action to perform and the variables needed to complete
    action.
  """
  redis = get_redis()
  if redis is None: return False
  with redis as r:
    # Add tasks to the list head
    try: r.lpush(f"task:{priority}:{user_id}", value)
    except Exception as e:
      log.error(f"Error adding task to queue: {e}")
      return False
  return True