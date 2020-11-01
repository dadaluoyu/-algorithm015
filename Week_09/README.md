学习笔记


最长回文子串
一个是初始化长度为1的区间
一个是初始化长度为0的区间


动态规划方法实现

最关键的这句话很重要
is_palindrome[i][j]= (s[i]==s[j]) and is_palindrome[i+1][j-1]
这个s[i]==s[j]是一个判断条件，如果两个相等，那个is_palindrome[i][j]就是true
然后is_palindrome[i+1][j-1]就是内部的子串是不是true
如果都符合，长度+1
如果是最长的，就记录下来

然后长度可以是1到n
对于每个长度，搜索对应的范围
由于是不是回文子串都记录在二维数组is_palindrome里面了，所以不会重复到O（n^3）这样

一开始把is_palindrome改成全false
然后自己单个字符是true

  for i in range(1,n):
            is_palindrome[i][i-1]=True
            #only works when length==1, that i+1 will bigger than j-1
这个就很好理解了，length为1时，检测回文子串比如“aa”时，由于is_palindrome[i][j]的下一级is_palindrome[i+1][j-1]会没有东西，出现i+1>j-1的情况，但是形如“aa”是可行的回文子串，所以在初始化的时候考虑这个条件