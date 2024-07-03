func _insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
    var intervals = intervals
    var results = Array<[Int]>()
    var currentInterval = newInterval
    while !intervals.isEmpty {
        let interval = intervals.first!
        intervals = Array(intervals.dropFirst())
        if currentInterval[1] < interval[0] {
            return results + [currentInterval] + [interval] + intervals
        }
        if currentInterval[0] > interval[1] {
            results = results + [interval]
            continue
        }
        currentInterval[0] = min(currentInterval[0], interval[0])
        currentInterval[1] = max(currentInterval[1], interval[1])
    }
    
    return results + [currentInterval]
}

class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        return _insert(intervals, newInterval)
    }
}

let intervals = [[1,3],[6,9]]
let newInterval = [2,5]
let result = Solution().insert(intervals, newInterval)
print(result)
