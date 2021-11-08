package appendixB;

import java.util.*;

public class IsPrimeImproved {
	
	// 소수 판별함수 (2 이상의 자연수에 대하여)
	public static boolean isPrimeNumber(int x) {
		// 2부터 x의 제곱근 까지의 모든 수를 확인하며
		for (int i = 2; i <= Math.sqrt(x); i++) {
			// x가 해당 수로 나누어 떨어진다면
			if (x % i == 0) {
				return false;		// 소수가 아님
			}
		}
		
		return true;	// 소수임
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(isPrimeNumber(4));
		System.out.println(isPrimeNumber(7));

	}

}
