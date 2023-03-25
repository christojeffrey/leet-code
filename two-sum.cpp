class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // iterate through the array again
            for (int j = i + 1; j < nums.size(); j++) {
                // if the sum of the two numbers is equal to the target
                if (nums[i] + nums[j] == target) {
                    // return the indices of the two numbers as array
                    return {i, j};
                }
            }
        }
        // if no two numbers sum to the target, return an empty array
        return {};
    }
};