package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }

func main() {
	defer writer.Flush()
	var T, A, B int
	scanf("%d\n", &T)
	for i := 0; i < T; i++ {
		scanf("%d %d\n", &A, &B)
		if A > B {
			printf(">\n")
		} else if A < B {
			printf("<\n")
		} else {
			printf("=\n")
		}
	}
}
