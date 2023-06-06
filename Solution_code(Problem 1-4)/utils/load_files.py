from pathlib import Path
import numpy as np

def load_file(n, path_file, file_format, press='*.'):
    n = int(n)
    ls_1 = list(Path(path_file).glob(press+file_format)) 
    return list(map(list,np.array_split(ls_1, n)))


def save_ml_file(path, file_name):
    pass