package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

var nonAlphanumericRegex = regexp.MustCompile("[^a-zA-Z0-9 ]+")

func clearString(str string) string {
	return nonAlphanumericRegex.ReplaceAllString(str, "")
}

func main() {
	filename := "test1.txt"
	fmt.Println(filename)

	fh, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Could not open file '%v': %v", filename, err)
		os.Exit(1)
	}

	reader := bufio.NewReader(fh)
	counter := make(map[string]int)
	for {
		line, _ := reader.ReadString('\n')
		fields := strings.Fields(line)
		for _, word := range fields {
			word = clearString(word)
			word = strings.ToLower(word)
			counter[word]++
		}
		if line == "" {
			break
		}
	}
	for word, cnt := range counter {
		fmt.Printf("%v %v\n", word, cnt)
	}
}

