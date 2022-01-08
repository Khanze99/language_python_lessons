

def singleton(aClass):
    instance = None

    def onCall(*args, **kwargs):
        nonlocal instance

        if instance == None:
            instance = aClass(*args, **kwargs)

        return instance
    return onCall

