class Solution {
    public void moveZeroes(int[] nums) {
        int length = nums.length;
        int lastValidLocation = -1;

        for(int i = 0; i < length; i++){
            int current = nums[i];
            if(current != 0){
                // move the number forward, to the last validLocation + 1
                nums[lastValidLocation + 1] = current;
                lastValidLocation++;
            }
        } 
        // change the back part to 0
        for(int i = lastValidLocation + 1; i < length; i++){
            nums[i] = 0;
        }
    }

    public static void main(String[] args){
        int[] nums = {1,2,3,0,4};
        int length = nums.length;
        
        Solution sol = new Solution();
        for(int i = 0; i < length; i++){
            System.out.print(nums[i]);
        }
        System.out.println();
        
        sol.moveZeroes(nums);


        for(int i = 0; i < length; i++){
            System.out.print(nums[i]);
        }
        System.out.println();


    }
}