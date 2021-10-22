package chapter08;
import java.util.*;

public class ex8_3_ex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[] arr = new int[n];
		for ( int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		int[] d = new int[m+1];
		Arrays.fill(d,  10001);
		
		d[0] = 0;
		for ( int i = 0; i < n; i++) {
			for (int j = arr[i]; j <= m; j++) {
				if (d[j-arr[i]] != 10001 ) {
					d[j] = Math.min(d[j], d[j-arr[i]] + 1);
				}
			}
		}
		if (d[m] == 10001) 
			System.out.print(-1);
		else
			System.out.print(d[m]);
		

	}

}
