import functools
from utils.logger import Logger

def ejra_konande(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:

            Logger.info(f"Start {func.__name__} : inputs : {args[1:]}, {kwargs}")
            result = func(*args, **kwargs)
            Logger.info(f"End {func.__name__} : Success -> {result}")
            return True, result
        except Exception as e:
            Logger.error(f"Error in {func.__name__}: {e}")
            return False, str(e)
    return inner