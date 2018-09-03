package main

import (
	"fmt"
)

func main() {
	var S string = "aaAAAbdd"
	var J string = "aA"
	var count int = 0
	dict := make(map[string]int)
	for _, chr := range S {
		var temp string = string(chr)
		_, ok := dict[temp]
		if !ok {
			dict[temp] = 1
		} else {
			dict[temp] += 1
		}
	}
	for _, chr := range J {
		var temp string = string(chr)
		i, ok := dict[temp]
		if ok {
			count += i
		}

	}
	fmt.Printf("%v\n", count)
}
