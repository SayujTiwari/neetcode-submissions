class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, count_t = {}, {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        need, have = len(count_t), 0
        min_len, res = float("inf"), [-1, -1]
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1
            if ch in count_t and count_t[ch] == window[ch]:
                have += 1
            while need==have:
                if min_len > r-l+1:
                    min_len = r-l+1
                    res = [l, r]
                l_ch = s[l]
                window[l_ch] = window[l_ch] - 1
                if l_ch in count_t and count_t[l_ch] > window[l_ch]:
                    have -= 1
                l+=1
        l, r = res
        return "" if min_len == float("inf") else s[l:r+1]

