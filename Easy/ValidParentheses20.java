import java.util.Stack;

public class ValidParentheses20 {
    public boolean isValid(String s) {
        Stack<String> bracketStack = new Stack<String>();
        for (int i = 0; i < s.length(); i++) {
            String charChecking = s.substring(i, i + 1);
            if (charChecking.equals("(") || charChecking.equals("[") || charChecking.equals("{")) {
                bracketStack.push(charChecking);
            } else {
                if (bracketStack.size() != 0) {
                    if (charChecking.equals(")") && bracketStack.peek().equals("(")) {
                        bracketStack.pop();
                    } else if (charChecking.equals("]") && bracketStack.peek().equals("[")) {
                        bracketStack.pop();
                    } else if (charChecking.equals("}") && bracketStack.peek().equals("{")) {
                        bracketStack.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }

        }
        return bracketStack.size() == 0;
    }
}
