# 最长上升（递增）子序列
# 位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
# 所以：if (nums[i] > nums[j]) dp[i] = max(dp[i], dp[j] + 1);

# 最长连续递增子序列
# 只需要和前一个比较，而不用和前面所有比较。即dp[i + 1] = dp[i] + 1

# 最长重复子数组
# 由于要求的是连续的数组，也就是说遍历到s[i]位置时，所求结果是包含s[i]的最长公共子数组
# 所以当遇到s[i]!=s[j]时，不需要进行操作，也就是说不需要将dp[i][j]置为前面的最大值。
# 而相等时，dp[i][j]=dp[i-1][j-1]+1

# 最长公共子序列，包括1035不想交的线
# 子序列是不连续的，所以遍历到s[i]位置时，所求结果是可包含可不包含s[i]的最长公共子数组
# 所以当遇到s[i]!=s[j]时，需要将dp[i][j]置为前面的最大值，dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# 而相等时，dp[i][j]=dp[i-1][j-1]+1

# 最大子数组和
# 数组是连续的，所以dp[i]只有两个方向可以推出来：dp[i - 1] + nums[i]，即：nums[i]加入当前连续子序列
# 和，nums[i]，即：从头开始计算当前连续子序列和

# 判断子序列
# 序列可以不连续，以s为行，t为列，当s[i]!=t[j]时，由于判断的是s是否在t中，因此要看没有t[j]时s是否在t中，
# 即dp[i][j] = dp[i][j - 1]，而相等时，仍然有dp[i - 1][j - 1]+1

# 不同的子序列
# 由于是用s去构造t，所以s为行，t为列。dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]。
# s[i - 1] 与 t[j - 1]相等
# s[i - 1] 与 t[j - 1] 不相等
# 当s[i - 1] 与 t[j - 1]相等时，dp[i][j]可以有两部分组成。
# 一部分是用s[i - 1]来匹配，那么个数为dp[i - 1][j - 1]。一部分是不用s[i - 1]来匹配，个数为dp[i - 1][j]。
# s[i - 1] 与 t[j - 1] 不相等，dp[i][j]只有一部分组成，不用s[i - 1]来匹配，即：dp[i - 1][j]

# 两个字符串的删除操作
# 当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];
# 当word1[i - 1] 与 word2[j - 1]不相同的时候，要么删除word1[i - 1]，最少操作次数为dp[i - 1][j] + 1，
# 要么删除word2[j - 1]，最少操作次数为dp[i][j - 1] + 1，
# 要么同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2

# 编辑距离
# 当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];
# 当word1[i - 1] 与 word2[j - 1]不相同的时候，要么删除word1[i - 1]，最少操作次数为dp[i - 1][j] + 1，
# 要么添加word2[j - 1]在word1[i - 1]后，最少操作次数为dp[i][j - 1] + 1，
# 要么替换word1[i - 1]为word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 1

# 回文子串
# i正序，j逆序
# 当s[i]与s[j]不相等，dp[i][j]一定是false。
# 当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
# 情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
# 情况二：下标i 与 j相差为1，例如aa，也是回文子串
# 情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
# 我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，
# 这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

# 最长回文子串
# 子串是连续的，s[i] == s[j]，同时要求j - i <= 1或者i+1到j-1也是回文串，则dp[i][j] = dp[i + 1][j - 1] + 2，否则0

# 最长回文子序列
# 子序列是不连续的，不需要j - i <= 1或者i+1到j-1也是回文串的条件，
# 也就是当s[i] == s[j]，直接有dp[i][j] = dp[i + 1][j - 1] + 2
# 同时，由于子序列可以不连续，则需要记录s[i] != s[j]，记录为dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
# 总而言之，子数组和子串要求连续，除了相等的位置其他都为0，也就是不需要记录不相等的位置
# 子序列不要求连续，当不相等时，需要把dp[i][j]记为周围的最大值