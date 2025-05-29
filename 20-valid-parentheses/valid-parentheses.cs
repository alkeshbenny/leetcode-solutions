public class Solution {
    public bool IsValid(string s) {
        Stack<char> stacks = new Stack<char>();
        foreach(char c in s){
            if(c=='(' || c=='{' || c=='['){
                stacks.Push(c);
            }
            else{
                if(stacks.Count==0) return false;
                char top = stacks.Pop();

                if(c==')'&& top!='(' ||
                c=='}'&& top!='{' ||
                c==']'&& top!='['){
                    return false;
                }
            }
        }
        return stacks.Count==0;
    }
}