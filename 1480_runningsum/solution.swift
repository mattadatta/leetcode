func _runningSum(_ nums: [Int]) -> [Int] {
    return nums.enumerated().reduce([]) { result, next in
        var result = result
        let (index, number) = next
        if index == 0 {
            result.append(number)
        } else {
            result.append(result[index - 1] + number)
        }
        return result
    }
}

class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        return _runningSum(nums)
    }
}

let nums = [3,1,2,10,1]
let result = Solution().runningSum(nums)
print(result)
