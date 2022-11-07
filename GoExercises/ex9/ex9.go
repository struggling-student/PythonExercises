package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Esami struct {
	Esami []Esame `json:"esami"`
}

type Esame struct {
	Voto int `json:"voto"`
	Cfu  int `json:"cfu`
}

func process(w http.ResponseWriter, r *http.Request) {
	var esami Esami

	err := json.NewDecoder(r.Body).Decode(&esami)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var total_cfu float64
	var total_voti float64
	var risultato float64

	for i := 0; i < len(esami.Esami); i++ {
		total_voti = total_voti + (float64(esami.Esami[i].Voto) * float64(esami.Esami[i].Cfu))
		total_cfu = total_cfu + float64(esami.Esami[i].Cfu)
	}

	risultato = total_voti / total_cfu
	w.Header().Set("Content-Type", "text/plain")
	fmt.Fprintf(w, " %v!", risultato)
}

func main() {
	http.HandleFunc("/", process)
	fmt.Println("Starting web server")
	http.ListenAndServe(":8090", nil)
}

// USE curl -X POST -H "Content-Type: application/json" -d @PATH_OF_JSON_FILE http://localhost:8090/process
