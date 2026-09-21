class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        low = 1
        high = position[-1] - position[0]
        ans = 0

        def canPlace(distance):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= distance:
                    count += 1
                    last = position[i]

                    if count == m:
                        return True

            return False

        while low <= high:
            mid = (low + high) // 2

            if canPlace(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
