#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:

    def __init__(self):
        self.alphabet = string.ascii_letters
        self.long_short = {} # 長網址到短網址的對應 
        self.short_long = {} # 短網址到長網址的對應，短網址只記末6碼

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.long_short:
            return "http://tinyurl.com/" + self.long_short[longUrl]
        
        short_url = ''.join(random.choices(self.alphabet, k = 6))
        while short_url in self.short_long:
            short_url = ''.join(random.choices(self.alphabet, k = 6))
        
        self.short_long[short_url] = longUrl
        self.long_short[longUrl] = short_url

        return "http://tinyurl.com/" + short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_long[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

