package chapter10;
import java.util.*;

public class Disjoint_sets_cycle {
	
	// 노드의 개수(v)와 간선(Union연산)의 개수(e)
	// 노드의 개수는 최대 100,000개라고 가정
	public static int v, e;
	public static int[] parent = new int[100001];	// 부모 테이블 초기화
	
	// 특정 원소가 속한 집합 찾기
	public static int findParent(int x) {
		// 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
		if (x == parent[x])
			return x;
		return parent[x] = findParent(parent[x]);
	}
	
	// 두 원소가 속한 집합 합치기
	public static void unionParent(int a, int b) {
		a = findParent(a);
		b = findParent(b);
		if (a < b)
			parent[b] = a;
		else
			parent[a] = b;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		v = sc.nextInt();
		e = sc.nextInt();
		
		// 부모 테이블상에서 부모를 자기자신으로 초기화
		for(int i = 1; i <= v; i++) {
			parent[i] = i;
		}
		
		boolean cycle = false; 	// 사이크 발생여부
		
		for (int i = 0; i < e; i++ ) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			// 사이클이 발생한 경우 종료
			if (findParent(a) == findParent(b)) {
				cycle = true;
				break;
			}
			// 사이클이 발생하지 않았다면 합집합(Union)연산수행
			else {
				unionParent(a, b);
			}
		}
		
		if (cycle) {
			System.out.println("사이클 발생");
		}
		else {
			System.out.println("사이클 발생 안함");
		}

	}

}
