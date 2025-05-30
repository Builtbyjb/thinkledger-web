from enum import Enum
from database.redis.redis import get_redis


class Tasks(Enum):
  setup_spreadsheet = "setup_spreadsheet"
  sync_transaction = "sync_transaction"


class TaskPriority(Enum):
  """
    HIGH priority tasks are tasks that require immediate user feedback.
    LOW priority tasks are tasks that go on in the background without direct user input
  """
  HIGH = "HIGH"
  LOW = "LOW"


# Ideas:
# I could manage complexity by creating a class and having custom functions for different tasks
# takes in a task, a list of arguments, and user_id
def add_tasks(value: str, user_id: str, priority: str) -> bool:
  """
    Adds a task to the core task queue.
    Value is a string containing the task function signature, and its arguments,
    separated by a colon e.g "func:arg1:arg2"
  """
  redis = get_redis()
  if redis is None: return False
  with redis as r:
    # Add tasks to list head (LPUSH)
    try: r.lpush(f"tasks:{priority}:{user_id}", value)
    except Exception as e:
      print(f"Error adding task to queue: {e}")
      return False

  return True