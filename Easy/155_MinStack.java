import java.util.Stack;

class MinStack {
    private Stack<Integer> stack = new Stack<Integer>();
    private Stack<Integer> min_stack = new Stack<>();


    public void push(int x) {
        if (min_stack.isEmpty() || x <= min_stack.peek()) {
            min_stack.push(x);
        }
        stack.push(x);
    }

    public void pop() {
        if (stack.peek().equals(min_stack.peek())) {
            min_stack.pop();
        }
        stack.pop();

    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return min_stack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
