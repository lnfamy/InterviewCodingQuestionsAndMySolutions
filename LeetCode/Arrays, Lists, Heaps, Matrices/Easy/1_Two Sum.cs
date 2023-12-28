/*
https://leetcode.com/problems/two-sum/
*/

/*
public class Solution {
        //first solution is brute force
        //for every element in the array 'x', loop thru the entire array and look for
        //an element that equals 'target - x'
        //if found: return, end program.
        //else: finish looping through the entire array for a time complexity of O(n^2)

    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++) {
            for (int j = i+1; j < nums.Length; j++) {
                if(nums[j] + nums[i] == target){
                    return new int[] {i, j};
                }
            }
        }
        //if we reached here, there's no match
        throw new ArgumentException("A two sum doesn't exist in this array for the selected target.");
    }
}
*/

public class Solution{
    public int[] TwoSum(int[] nums, int target){
        // more efficient solution: we can use the C# equivalent of a hashmap, a dictionary
        // to find if the target has a 2-sum in the array using just one pass
        // for a time complexity of O(n)
        // explanation: we map each number in the array to its index, access by value

        Dictionary <int, int> numToIndex = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++){
            int complement = target - nums[i];
            if(numToIndex.ContainsKey(complement)){
                return new int[] {numToIndex[complement], i};
            }

            //we store the current number in the dictionary last because we check back on each number
            numToIndex[nums[i]] = i;
        }
        throw new ArgumentException("A two sum doesn't exist in this array for the selected target.");
    }
}