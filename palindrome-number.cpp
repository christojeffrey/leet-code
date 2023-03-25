class Solution {
public:
    bool isPalindrome(int x) {
        // parse x to string
        string s = to_string(x);
        // reverse string
        string r = s;
        reverse(r.begin(), r.end());
        // compare
        return s == r;
        
    }
};