package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)
	scanner.Scan()
	T := scanner.Text()
	scanner.Scan()
	T2 := scanner.Text()

	var res []string

	for i := 0; i < len(T2); i++ {
		if string(T[i]) == "1" || string(T2[i]) == "1" {
			res = append(res, "1")
		} else {
			res = append(res, "0")
		}
	}
	fmt.Println(strings.Join(res, ""))
}
