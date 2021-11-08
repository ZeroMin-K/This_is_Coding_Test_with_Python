package appendixB;

import java.util.*;

public class SieveOfEratosthenes {
	
	public static int n = 1000;		// 2부터 1,000까지의 모든 수에 대하여 소수 판별
	public static boolean[] arr = new boolean[n+1];

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Arrays.fill(arr, true);	// 처음엔 모든 수가 소수(Ture)인 것으로 초기화(0과 1은 제외)
		for(int i = 2; i <= Math.sqrt(n); i++) {	// 2부터 n의 제곱근까지의 모든 수를 확인하며
			if(arr[i] == true) {	// i가 소수인경우(남은 수인 경우)
				// i를 제외한 i의 모든 배수 지우기
				int j = 2;
				while (i * j <= n) {
					arr[i * j] = false;
					j += 1;
				}
			}
		}
		
		for(int i = 2; i <= n; i++) {	// 모든 소수 출력
			if(arr[i]) 
				System.out.print(i + " ");
		}

	}

}
