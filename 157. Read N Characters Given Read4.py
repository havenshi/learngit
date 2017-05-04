# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
# Note:
# The read function will only be called once for each test case.
#

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer

def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        start = 0
        buffer = [''] * 4
        for i in range(n / 4 + 1):  # how many groups (size == 4 or size < 4)
            size = read4(buffer)
            if size:
                buf[start:start + size] = buffer
                start += size
            else:
                break
        return min(start, n)


if __name__ == "__main__":
    answer = Solution()
    buf = ['' for i in range(100)]
    file_content = "abcdefghijklmnop"
    print buf[:answer.read(buf, 5)]
    print buf[:answer.read(buf, 3)]