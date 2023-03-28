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
	var B string
	fmt.Scan(&B)
	myslice := strings.Split(B, "")
	var notslice []string
	for _, number := range myslice {
		if number == "1" {
			notslice = append(notslice, "0")
		} else {
			notslice = append(notslice, "1")
		}
	}
	fmt.Println(strings.Join(notslice, ""))
}
