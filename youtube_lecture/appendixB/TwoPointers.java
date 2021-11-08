package appendixB;

import java.util.*;

public class TwoPointers {
	
	public static int n = 5; 	// 데이터의 개수n
	public static int m = 5;	// 찾고자 하는 부분합m
	public static int[] arr = {1, 2, 3, 2, 5};	// 전체 수열

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int cnt = 0, intervalSum = 0, end = 0;
		for(int start = 0; start < n; start++) {	// start를 차례대로 증가시키며 반복
			while (intervalSum < m && end < n) {	// end를 가능한 만큼 이동
				intervalSum += arr[end];
				end += 1;
			}
			if(intervalSum == m ) {	// 부분합이 m일때 카운트 증가
				cnt += 1;
			}
			intervalSum -= arr[start];
		}
		System.out.println(cnt);
	}
}
