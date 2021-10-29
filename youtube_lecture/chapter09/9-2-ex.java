package chapter09;
import java.util.*;

public class ex_9_2 {
	
	public static final int INF = (int) 1e9;	// 무한을 의미하는 값으로 10억 설정
	// 노드의 개수(N), 간선의 개수(M), 거쳐갈 노드(K), 최종 목적지 노드(X)
	public static int n, m, x, k;
	// 2차원 배열(그래프 표현)만들기
	public static int[][] graph = new int[101][101];

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		// 최단 거리 테이블을 모두 무한으로 초기화
		for (int i = 0; i < 101; i++) {
			Arrays.fill(graph[i],  INF);
		}
		
		// 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
		for(int a = 1; a <= n; a++) {
			for(int b = 1; b <= n; b++) {
				if (a == b) 
					graph[a][b] = 0;
			}
		}
		
		// 각 간선에 대한 정보를 입력 받아, 그값으로 초기화
		for (int i = 0; i < m; i++) {
			// A와 B가 서로에게 가는 비용은 1
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			graph[a][b] = 1;
			graph[b][a] = 1;
		}
		
		x = sc.nextInt();
		k = sc.nextInt();
		
		// 점화식에 따라 플로이드 워셜 알고리즘수행
		for(int k = 1; k <= n; k++) {
			for (int a = 1; a <= n; a++) {
				for (int b = 1; b <= n; b++) {
					graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
				}
			}
		}
		
		// 수행된 결과 출력
		int distance = graph[1][k] + graph[k][x];
		
		// 도달할 수 없는 경우 -1 출력
		if (distance >= INF) {
			System.out.println(-1);
		}
		// 도달할 수 있다면 최단 거리 출력
		else {
			System.out.println(distance);
		}
	}
}
