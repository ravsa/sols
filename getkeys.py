#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import getopt
import sys

Phone = None
Country_code = None
help_message = """
            getkeys -c <country-Code> -p <Phone-Number>

            -c,--country        Country Code without prefix(+)
            -p,--phone          Phone Number without Country code
            -h,--help           Show this message
            """


class NetworkError(RuntimeError):
    """docstring for NetworkError"""

    def __init__(self, arg):
        super(NetworkError, self).__init__()
        self.arg = arg


def run_command(Phone, Country_code):
    """run commands and store their stdout and stderr of commands in a variable

    :Phone: phone
    :Country_code: Country_code
    :returns: output

    """
    print Country_code, Country_code + Phone
    data = Popen(['yowsup-cli', 'registration', '-C', Country_code, '-r',
                  'sms', '-p', Country_code + Phone], stderr=PIPE, stdout=PIPE)
    output, error = data.communicate()
    if error.find('socket.gaierror') != -1:
        raise NetworkError(
            "Unable to connect to servers.Check your network connection")
    else:
        return error


try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:p:", [
                               "country=", "phone=", "help"])

except getopt.GetoptError, err:
    # Print debug info
    print(str(err))
    print(help_message)

for option, argument in opts:
    if option in ("-h", "--help"):
        print(help_message)
        sys.exit()
    elif option in ("-p", "--phone"):
        Phone = argument
    elif option in ("-c", "--country"):
        Country_code = argument
if __name__ == '__main__':
    try:
        print(run_command(Phone, Country_code))
    except NetworkError, err:
        print "n/w", err.arg
