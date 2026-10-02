class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #students =   [0,0,1,1,1]
        #sandwiches = [0,0,0,1,1]
        #cnt = Counter({1: 3, 0: 2})
        #res = 5

        cnt = Counter(students)
        res = len(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                break
        
        return res

       
