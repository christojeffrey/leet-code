class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string answer = "";
        if (strs.size() == 0) {
            return answer;
        }
        // take the first, compare with the rest
        string first = strs[0];
        for (int i = 0; i < first.length(); i++) {
            char c = first[i];
            for (int j = 1; j < strs.size(); j++) {
                if (i >= strs[j].length() || strs[j][i] != c) {
                    return answer;
                }
            }
            answer += c;
        }
        return answer;

    }
};