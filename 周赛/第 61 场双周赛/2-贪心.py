import collections

class Solution:
    def run(self, changed):
        cnt = collections.Counter(changed)
        keys = sorted(cnt.keys())
        ans = []
        for key in keys:
            if key == 0:
                if cnt[key] % 2 != 0:
                    return []
                else:
                    ans += [0] * (cnt[key]//2) # 可以把float 2.0变为int 2
            else:
                if cnt[key*2] < cnt[key]:
                    return []
                else:
                    cnt[key*2] -= cnt[key]
                    ans += [key] * cnt[key]
        return ans


if __name__ == "__main__":
    changed = [1,3,4,2,6,8]
    res = Solution().run(changed)
    print(res)