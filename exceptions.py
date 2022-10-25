class NoOptionError(Exception):
    def __str__(self):
        return "Option doesn't exist"

class WrongCredentials(Exception):
    def __str__(self):
        return "You entered wrong credentials"

class WrongID(Exception):
    def __str__(self):
        return "You entered wrong Food ID"

class SimilarID(Exception):
    def __str__(self):
        return "This ID is already used, please use another ID"
    
class TryAgain(Exception):
    def __str__(self):
        return f"\nTry again!\n"