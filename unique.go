package main

import "fmt"

func main() {
	var arr = []int{1, 3, 3, 1, 2, 4}
	var dict = make(map[int]int)
	for _, i := range arr {
		dict[i]++
	}
	for i, j := range dict {
		if j%2 != 0 {
			fmt.Println(i)
		}
	}
}

func print(a []int) {
	for i := 0; i < len(a); i++ {
		fmt.Println(a[i])
	}
}
