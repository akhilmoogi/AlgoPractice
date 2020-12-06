package main

import (
	"fmt"
	"strings"
)

func main() {}

func Ceaser(str string, key int) string {
	runes := []rune(str)
	alphabet := "abcdefghijklmnopqrstuvwxyz"
	for i, char := range runes {
		index := strings.Index(alphabet, string(char))
		if index == -1 {
			return "" //Bad Input
		}
		newindex := (index + key) % 26
		runes[i] = rune(alphabet[newindex])
	}

	fmt.Printf("%d  \n", runes)
	return string(runes)
}
