// TLE
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // dictionary of result. the key is a vector of three numbers, the value is a boolean
        map<vector<int>, bool> results;

        
        for (int i = 0; i < nums.size() - 2; i++) {
            for (int j = i + 1; j < nums.size() - 1; j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        // add to results if it doesn't already exist. sort the num[i], num[j], num[k] first
                        vector<int> result = {nums[i], nums[j], nums[k]};
                        sort(result.begin(), result.end());
                        results[result] = true;
                    }
                }
            }
        }
        // convert the map to a vector
        vector<vector<int>> mapResults;

        for (auto it = results.begin(); it != results.end(); it++) {
            mapResults.push_back(it->first);
        }
        return mapResults;
    }
};