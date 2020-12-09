#!/usr/bin/python3
def remove_char_at(str, n):
    #  return (str[0:n] + str[n+1:] if n >= 0 else str)
    if n >= 0:
        return str[0:n] + str[n+1:]
    else:
        return str

    #  str[0:n] - get string up until n
    #  str[n+1] adds/concatenates string after n
    #  if n is negative, just print the whole string
