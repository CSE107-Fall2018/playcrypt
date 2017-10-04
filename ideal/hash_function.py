from crypto.primitives import *

class HashFunction():
    """
    This class simulates a hash function. It can emulate a hash function with
    or without a key and with any key or output length (in bytes).

    Example Usage:

    .. testcode::

        from crypto.ideal.hash_function import HashFunction

        h = HashFunction(16)

        h1 = h.hash("Hello World!")
        h2 = h.hash("H3110 W0r1d!")

        print str(h1 != h2 and len(h1) == h.out_len and len(h1) == len(h2))

    .. testoutput::

        True
    """
    def __init__(self, out_len, key_len=0):
        """
        :param out_len: Output length for the hash function in bytes.
        :param key_len: Key length for the hash function in bytes, defaults
                        to 0.
        """
        self.key_len, self.out_len = key_len, out_len
        self.hashes = {}

    def hash(self, message, key=None):
        """
        This is a simulated hashing function. If a key is used then it must have
        the correct key length.

        :param message: Must be a string of length > 0
        :param key: Key used for simulated hashing, must have length
                    ``self.key_len``.
        :return: Hash of message if all parameters are met, ``None`` otherwise.
        """
        if (key is not None and len(key) is not self.key_len):
            raise ValueError("Invalid key length, key length was: " + \
                    str(len(key)) + " should be: " + str(self.key_len) + ".")


        if not (key, message) in self.hashes:
            self.hashes[(key, message)] = random_string(self.out_len)

        return self.hashes[(key, message)]
