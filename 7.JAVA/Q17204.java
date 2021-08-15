package algorithm;

import java.util.Scanner;

public class Q17204 {
	
	private int findBosung(int person, int bosung, int[] death) {
		int[] checkPerson = new int[person];
		int result = 0;
		int start = death[0];
		checkPerson[0]=1;
		while(true) {
			if(checkPerson[start]==0) {
				result++;
				if(start==bosung) break;
				checkPerson[start]=1;
				start = death[start];
			}else if(checkPerson[start]==1) {
				result = -1;
				break;
			}
		}
		return result;
	}
	
	public void input() {
		Scanner scan = new Scanner(System.in);
		int person = scan.nextInt();
		int bosung = scan.nextInt();
		int[] death= new int[person];
		for(int i=0;i<person;i++) {
			death[i] = scan.nextInt();
		}
		System.out.println(findBosung(person,bosung,death));
	}
	
	public static void main(String[] args) {
		Q17204 input = new Q17204();
		input.input();
	}
}
