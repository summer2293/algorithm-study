class Solution {
    public int[] twoSum(int[] nums, int target) {
    	if (nums.length == 2)
    		return new int[] {0,1};
    	int[] answer = {0,0};
    	int index = 0;
    	for (int i = index; i < nums.length; i++) {
    		for (int j = i + 1; j < nums.length; j++) {
    			if (nums[i] + nums[j] == target) {
    				answer[0] = i;
    				answer[1] = j;
    				return answer;
    				
    			}
    		}
    		index ++;
    	}
    	return answer;
    }
}