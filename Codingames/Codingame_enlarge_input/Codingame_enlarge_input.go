package main

import (
	"fmt"
	"strings"
)

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	var N int
	fmt.Scan(&N)

	for i := 0; i < N; i++ {
		var M string
		fmt.Scan(&M)
		split := strings.Split(M, "")
		double := []string{}
		for i := 0; i < len(split); i++ {
			double = append(double, split[i], split[i])
		}
		for i := 0; i < 2; i++ {
			fmt.Println(strings.Join(double, ""))
		}
	}

}
