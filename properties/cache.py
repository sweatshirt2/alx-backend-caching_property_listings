from redis import Redis
from redis.exceptions import ConnectionError, TimeoutError

class Cache:
  def __init__(self):
    self._redis = Redis(host="cache", decode_responses=True)
    self._redis.flushdb()

  def set(self, key: str, data) -> bool:
    try:
      self._redis.set(key, data)
      return True
    except TimeoutError:
      return False

  def get(self, key: str):
    return self._redis.get(key)
  
  def health_check(self) -> bool:
    try:
      self._redis.ping()
      return True
    except ConnectionError:
      return False
