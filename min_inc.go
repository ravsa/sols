package main

import "fmt"

func main() {
	var arr = []int{1, 3, 3, 2}
	var ans int = 0
	var x int = 2
	minMoves(arr, &ans, x)
	fmt.Printf("%d\n", ans)
}

func minMoves(arr []int, ans *int, x int) {
	for i := 1; i < len(arr); i++ {
		if arr[i] <= arr[i-1] {
			p := ((arr[i-1] - arr[i]) / x) + 1
			*ans += p
			arr[i] = arr[i] + (p * x)
			// fmt.Printf("%d\n", p)
		}
	}
}
