package main

import (
	"fmt"
	"net/http"
)

func hi(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")

	w.Header().Set("Content-Type", "text/plain")
	fmt.Fprintf(w, "Hi %s", name)
}

func main() {
	http.HandleFunc("/", hi)

	fmt.Println("Starting web server")
	http.ListenAndServe(":8090", nil)
}

