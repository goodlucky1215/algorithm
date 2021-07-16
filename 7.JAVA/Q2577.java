package algorithm;

import java.util.Scanner;

public class Q2577 {
	int a = 1;
	public void result(int a) {
		int[] num = new int[10];
		while(a>0) {
			num[a%10]+=1;
			a/=10;
		}
		for(int e : num) {
			System.out.println(e);
		}
	}
	public void input() {
		Scanner sc = new Scanner(System.in);
		for(int i=0;i<3;i++) {
			a*=sc.nextInt();
		}
		result(a);
	}
	public static void main(String[] args) {
		Q2577 quest = new Q2577();
		quest.input();
	}

}
