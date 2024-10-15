import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/liam/CS460_HW1/fall2024-cs460-indoor-env/install/myenv'
