#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        tmp = path.replace("//", "/")
        folder_name_list = tmp.strip('/').split('/')
        for folder in folder_name_list:
            if folder == "..":
                if stack:
                    stack.pop()
            elif folder == "" or folder == ".":
                continue
            else:
                stack.append(folder)

        if not stack:
            return "/"

        return "/" + "/".join(stack)
        

# @lc code=end

