package chapter08;

public class fibo_recursive {
	
	// 피보나치 함수를  재귀함수로 호출
	public static int fibo(int x) {
		if ( x == 1 || x == 2) {
			return 1;
		}
		return fibo(x-1) + fibo(x-2);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(fibo(4));

	}

}
