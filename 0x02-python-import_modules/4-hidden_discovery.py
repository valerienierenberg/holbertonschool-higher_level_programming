#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for att in dir(hidden_4):
        if att[:2] != "__":
            print("{:s}".format(att))