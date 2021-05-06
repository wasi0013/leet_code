from hashlib import sha256
class Codec:
    hash_map = dict()
    base_url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash = sha256(bytes(longUrl, 'utf-8')).hexdigest()[:7]
        self.hash_map[hash] = longUrl
        return self.base_url+hash

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_map[shortUrl.rsplit("/", 1)[1]]
        

