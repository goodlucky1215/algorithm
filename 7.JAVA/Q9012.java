package algorithm;

import java.util.Scanner;
import java.util.Stack;

public class Q9012 {
	Scanner scan = new Scanner(System.in);
	public void result() {
		Stack<Character> stack = new Stack<>();
		String test = scan.next();
		for(int i=0;i<test.length();i++) {
			if(')'==test.charAt(i)&&!stack.empty()&&'('==stack.peek()) {
				stack.pop();
			}else {
				stack.push(test.charAt(i));
			}
		}
		System.out.println(stack.empty() ? "YES" : "NO");
	}
	public void input() {
		int num = scan.nextInt();
		for(int i=0;i<num;i++) {
			result();
		}
	}
	public static void main(String[] args) {
		Q9012 input = new Q9012();
		input.input();
	}
}
