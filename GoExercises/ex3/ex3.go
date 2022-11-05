package main

import (
	"fmt"
	"io"
	"net/http"
)

func hi(w http.ResponseWriter, r *http.Request) {
	body, _ := io.ReadAll(r.Body)

	// We assume that the body contains the raw string
	// In a real server, you want to check this before proceeding
	name := string(body)

	w.Header().Set("Content-Type", "text/plain")
	fmt.Fprintf(w, "Hi %s!", name)
}

func main() {
	http.HandleFunc("/", hi)

	fmt.Println("Starting web server")
	http.ListenAndServe(":8090", nil)
}

