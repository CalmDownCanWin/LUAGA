import os

from ESXi_config import create_directory

def create_esx_tmp():
    tmp_folder = {
        os.path.join(os.path.expanduser("~"), "ESXI 7", "tmp", "vmware-root"),  # Thực hiện hàm os.path.join
        os.path.join(os.path.expanduser("~"), "ESXI 7", "tmp", "vmware-root_68260-1619746241"),
        os.path.join(os.path.expanduser("~"), "ESXI 7", "tmp", "vmware-uid_0"),
        os.path.join(os.path.expanduser("~"), "ESXI 7", "tmp", "vmware-root_85464_5645446546"),
        os.path.join(os.path.expanduser("~"), "ESXI 7", "tmp", "vmware-root_54545_8454548451"),
    }
    for path in tmp_folder:
        create_directory(path)
