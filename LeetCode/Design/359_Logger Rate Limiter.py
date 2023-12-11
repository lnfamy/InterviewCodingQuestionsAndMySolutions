"""
https://leetcode.com/problems/logger-rate-limiter/description/
"""
import collections


class Logger:
    # this is a sliding window problem basically
    def __init__(self):
        # make a set for the messages (for no duplicates)
        # and make a double ended queue for out sliding window implementation
        self._msg_set = set()
        self._msg_queue = collections.deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # returns True if the message should be printed on the given timestamp, False otherwise
        while self._msg_queue:
            # getting rid of all "expired" messages, i/e messages whose timestamp is 10 secs ago or more
            msg, timest = self._msg_queue[0]
            if timestamp - timest >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                # since all the messages are stored in chronological order, once we found
                # a message that isn't expired, that means everything after it isn't expired either
                # therefore there is no need to continue checking at all
                break

        # if the message isn't in the set, then we add it to our queue and set with the current
        # timestamp, and then return True because now it's meant to be printed on this timestamp
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class Logger:
    # in this approach we use a dictionary, and we don't actually delete any items.
    # this saves us some runtime and runs smoother.
    def __init__(self):
        self._dct = collections.defaultdict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # if the message wasn't in the dictionary to begin with, add it with the current
        # timestamp and return True because it is to be printed now
        if message not in self._dct:
            self._dct[message] = timestamp
            return True
        # if the messsage we got is a duplicate of an expired message, 'update' its timestamp
        if timestamp - self._dct[message] >= 10:
            self._dct[message] = timestamp
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
