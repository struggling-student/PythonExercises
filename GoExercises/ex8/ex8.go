package main

import (
	"fmt"
	"io"
	"net/http"
	"regexp"
	"strings"
)

var nonAlphanumericRegex = regexp.MustCompile("[^a-zA-Z0-9 ]+")

func clearString(str string) string {
	return nonAlphanumericRegex.ReplaceAllString(str, "")
}
func repetition(st string) map[string]int {
	input := strings.Fields(st)

	wc := make(map[string]int)
	for _, word := range input {
		_, matched := wc[word]
		if matched {
			wc[word] += 1
		} else {
			wc[word] = 1
		}
	}
	return wc
}

func wordCount(w http.ResponseWriter, r *http.Request) {
	body, _ := io.ReadAll(r.Body)
	name := clearString(string(body))

	for index, element := range repetition(name) {
		w.Header().Set("Content-Type", "text/plain")
		fmt.Fprintf(w, "%v %v\n", index, element)
	}
}

func main() {
	http.HandleFunc("/", wordCount)
	fmt.Println("Starting web server")
	http.ListenAndServe(":8090", nil)
}
