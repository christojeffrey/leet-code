class Solution {
public:
    int romanToInt(string s) {
        // dictionary
        map<char, int> dict;
        dict['I'] = 1;
        dict['V'] = 5;
        dict['X'] = 10;
        dict['L'] = 50;
        dict['C'] = 100;
        dict['D'] = 500;
        dict['M'] = 1000;

        int n = 0;
        int previousNumber = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentNumber = dict[s[i]];
            if (currentNumber < previousNumber) {
                n -= currentNumber;
            } else {
                n += currentNumber;
            }
            previousNumber = currentNumber;
        }
        return n;
    }
};