from redis import Redis
from redis.exceptions import ConnectionError, TimeoutError

class Cache:
  """
  Cache class to wrap redis providing interface to the redis python package
  """

  def __init__(self):
    self._redis = Redis(host="cache", decode_responses=True)
    self._redis.flushdb()

  def set(self, key: str, data, ttl: int) -> bool:
    """
    Sets data to the store

    Args:
    key(str): The key of the data to be stored
    data: The data to be stored
    ttl(int): The expiration time for the data

    Returns:
    bool: whether or not the data has been set successfully
    """
    try:
      self._redis.set(key, data, ttl)
      return True
    except TimeoutError:
      return False

  def get(self, key: str):
    """
    Gets data from the store

    Args:
    key(str): The key of the data to be stored

    Returns:
    The data saved with the given key
    """
    return self._redis.get(key)
  
  def delete(self, key: str) -> None:
    self._redis.delete(key)
  
  def health_check(self) -> bool:
    try:
      self._redis.ping()
      return True
    except ConnectionError:
      return False
