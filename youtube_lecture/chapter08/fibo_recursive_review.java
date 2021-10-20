package chapter08;

public class fibo_recursive_review {
	
	public static int fibo(int x) {
		if ( x== 1 || x == 2) {
			return 1;
		}
		return fibo(x-1) + fibo(x-2);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(fibo(4));

	}

}
