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
	ME := scanner.Text()
	myhobbies := strings.Fields(ME)
	var N int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &N)

	var match string
	base_incommon := 0

	for i := 0; i < N; i++ {
		var incommon int
		scanner.Scan()
		DATE := scanner.Text()
		herhobbies := strings.Fields(DATE)
		for _, herhobby := range herhobbies {
			for _, myhobby := range myhobbies {
				if herhobby == myhobby {
					incommon++
				}
			}
		}
		if incommon >= base_incommon {
			match = herhobbies[0]
			base_incommon = incommon
		}
	}
	fmt.Println(match)
}
