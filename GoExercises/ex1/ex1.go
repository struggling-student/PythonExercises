package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"time"
)

func evenRandomNumber(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	var p = rand.Int()
	if p%2 == 0 {
		fmt.Fprintf(w, "%d is even", p)
	} else {
		fmt.Fprintf(w, "%d is odd", p)
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())

	http.HandleFunc("/", evenRandomNumber)

	fmt.Println("Starting web server at http://localhost:8080")
	http.ListenAndServe(":8090", nil)
}

