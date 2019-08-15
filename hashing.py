import zlib

#the function takes the file path as the input, and returns its hash
def genHash(filepath):

    file = open(filepath, 'r')

    buffer = ""

    for line in file.readlines():
        buffer += line

    checksum = zlib.adler32(buffer.encode('utf-8')) & 0xfffffff

    return checksum

#checkign for equality, but im guessing this is not useful.
def isEqual(filepath1, filepath2):
    file1 = open(filepath1, 'r')
    file2 = open(filepath2, 'r')

    buffer1 = ""
    buffer2 = ""

    for line in file1.readlines():
        buffer1 += line

    for line in file2.readlines():
        buffer2 += line

    checksum1 = zlib.adler32(buffer1.encode('utf-8')) & 0xfffffff
    checksum2 = zlib.adler32(buffer2.encode('utf-8')) & 0xfffffff

    return checksum1 == checksum2

if __name__ == '__main__':
    print(genHash('app.py'))
    # print(genHash('testFile.txt'))
    # print(isEqual("textFile1.txt", "testFile.txt"))
