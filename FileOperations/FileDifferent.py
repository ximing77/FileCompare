
def isFileDifferent(file0Path, file1Path):
    pass

def isFileDifferentInBytes(file0Path, file1Path):
    readBuffSize = 50000
    try:
        with open(file0Path, 'rb') as file0:
            with open(file1Path, 'rb') as file1:
                buff0 = file0.read(readBuffSize)
                buff1 = file1.read(readBuffSize)
                while buff0 != None and len(buff0) != 0 and buff1 != None and len(buff1) != 0:
                    if len(buff0) != len(buff1):
                        return True
                    actualLen = len(buff0)
                    for i in range(actualLen):
                        b0 = buff0[i]
                        b1 = buff1[i]
                        if b0 != b1:
                            return True
                    buff0 = file0.read(readBuffSize)
                    buff1 = file1.read(readBuffSize)

                state0 = buff0 == None or len(buff0) == 0
                state1 = buff1 == None or len(buff1) == 0
                if state0 and state1:
                    return False
                else:
                    return True
    except:
        print('exception')
        return None

