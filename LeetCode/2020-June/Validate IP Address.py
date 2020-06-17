from ipaddress import ip_address, IPv6Address

# This question mainly requires us to know the lib named ipaddress which can help us directly figure out whether the str
# is a IP or not and it can even give us which IP type it belongs to.
# By the way, there are some other functions I learn from the question, like str.zfill(), str.isdecimal() and so on.

class Solution(object):
    # consider the blank, prefix 0 (ipv4), length. Note: 'G' is bigger than 'FFFF' while '000G' is smaller.
    def validIPAddress1(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        list_ip = IP.split('.')
        if len(list_ip) == 4:
            for i in list_ip:
                if not i.isdecimal(): # Check whether it is a Decimal number or not.
                    return 'Neither'
                i_int = int(i)
                if i_int < 0 or i_int > 255:
                    return 'Neither'
                i_new = str(int(i))
                if i_new != i:
                    return 'Neither'
            return 'IPv4'
        IP = IP.upper() # rewritten to the upper case
        list_ip = IP.split(':')
        if len(list_ip) == 8:
            for i in list_ip:
                if not i.isalnum(): # Check whether it consists of numbers or letters and there is no ''.
                    return 'Neither'
                if len(i) > 4 or i > 'FFFF' or i < '0':
                    return 'Neither'
            return 'IPv6'
        return 'Neither'

    def validIPAddress(self, IP):
        try:
            return 'IPv6' if type(ip_address(IP)) is IPv6Address else 'IPv4'
        except ValueError:
            return 'Neither'
        # if ip_address(IP):
        #     if IPv6Address(IP):
        #         return 'IPv6'
        #     else:
        #         return 'IPv4'
        #

s1 = Solution()
s1.validIPAddress('172.16.254.1')
#
# if i > 'FFFF' or i < '0':
#     return 'Neither'
# if len(i) < 4:
#     i = i.zfill(4) # add prefix 0.

