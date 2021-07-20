import os
for dirName, subDirList, fnames in os.walk('C:\\Windows\\debug'):
    for fname in fnames:
        os.path.join(dirName, fname)
