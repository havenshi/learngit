# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
# Note:
# The read function may be called multiple times.
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
    def __init__(self):
        self.remain = ''

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        start = 0
        buffer = [''] * 4
        copyn = n
        if self.remain: # read remain part from the last call
            length = len(self.remain)
            if copyn > length:  # append remain firstly
                buf[start:start + length] = self.remain
                start += length
                copyn -= length
            else:
                buf[start:start + length] = self.remain # append add remain, no file left
                start += length
                return min(start, n)
        while copyn > 0:  # if any group left
            size = read4(buffer)
            if copyn >= 4:
                buf[start:start + size] = buffer
                start += 4
                copyn -= 4
            else:             # if remain group length is 1-3
                buffer = buffer[:size] # only slice with size length from 4
                gap = min(copyn, size) # get the minimum of copyn and size
                buf[start:start + gap] = buffer[:gap]
                self.remain = buffer[gap:]  # remain part
                start += gap
                break
        return min(start, n)


if __name__ == "__main__":
    global file_content
    answer = Solution()
    buf = ['' for i in range(100)]
    file_content = "abcdefg"
    print buf[:answer.read(buf, 5)]
    print buf[:answer.read(buf, 3)]