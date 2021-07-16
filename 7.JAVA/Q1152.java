package algorithm;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Q1152 {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String str;
		str = scan.nextLine();
		System.out.println(new StringTokenizer(str," ").countTokens());
	}
}

/*
 * import java.util.Scanner;
 * 
 * public class Main { public static void main(String[] args) { Scanner scan =
 * new Scanner(System.in); String str; str = scan.nextLine(); String[] result =
 * str.split(" "); if(result.length>0) { if(result[0].length()==0)
 * System.out.println(result.length-1); else System.out.println(result.length);
 * }else System.out.println(0); } }
 */