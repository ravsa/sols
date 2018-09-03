package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }

func handleNegative(num int) (int, int) {
	if num < 0 {
		return num * -1, -1
	}
	return num, 1
}

func main() {
	defer writer.Flush()
	var num, sum, isNegative int
	scanf("%d\n", &num)
	printf("%d", int(math.Pow(-2, 31)))
	num, isNegative = handleNegative(num)
	for num > 0 {
		sum = (sum * 10) + num%10
		num /= 10
	}
	print("%d\n", sum*isNegative)
}
