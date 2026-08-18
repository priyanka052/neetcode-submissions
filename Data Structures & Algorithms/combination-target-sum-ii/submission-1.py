class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtracking(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            
            for j in range(start, len(candidates)):
                
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > remaining:
                    break

                path.append(candidates[j])
                backtracking(j+1, remaining-candidates[j], path)
                path.pop()

        backtracking(0,target, [] )
        return result