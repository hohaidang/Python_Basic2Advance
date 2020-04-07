

def get_path(filename):
    import os
    head, tail = os.path.split(filename)
    return head
