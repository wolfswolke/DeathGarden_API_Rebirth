import hashlib
import mmap

class HashHandler:
    def __init__(self):
        self.pak = ""
        self.sig = ""
        self.pak_path = "files/TheExitRebirthBackendAPI-WindowsNoEditor_P.pak"
        self.sig_path = "files/TheExitRebirthBackendAPI-WindowsNoEditor_P.sig"

    def setup(self):
        self.pak = self.get_256_sum(self.pak_path)
        self.sig = self.get_256_sum(self.sig_path)

    def get_256_sum(self, filename):
        h = hashlib.sha256()
        with open(filename, 'rb') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                h.update(mm)
        return h.hexdigest()

    def get_hash(self):
        return str(self.pak), str(self.sig)

hash_handler = HashHandler()