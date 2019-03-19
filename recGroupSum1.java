public boolean sum(int[] nums, int target)
{
  int n = nums.length;
  boolean dp[][] = new boolean[n+1][target+1];
  for(int i = 0 ; i<=n;i++)
  {
    dp[i][0] = true;
  }
  for(int i = 1 ;i<=target;i++)
  {
    dp[0][i] = false;
  }

  for(int i =1;i<=n;i++)
  {
    for(int j = 1;j<=target;j++)
    {
      if(j<nums[i-1])
      {
        dp[i][j] = dp[i-1][j];
      }
      else
      {
        dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]];
      }
    }
  }

  return dp[n][target];
}

public boolean groupSum(int start, int[] nums, int target) {

  int l = nums.length - start;
  int num2[] = new int[l];
  for(int i = start;i<nums.length;i++)
  {
    num2[i-start] = nums[i];
  }

  return sum(num2,target);
}
