package api

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/julienschmidt/httprouter"
)

type Fountains struct {
	Fountains []Fountain
}

type Fountain struct {
	Id        int
	status    string
	latitude  float64
	longitude float64
}

// liveness is an HTTP handler that checks the API server status. If the server cannot serve requests (e.g., some
// resources are not ready), this should reply with HTTP Status 500. Otherwise, with HTTP Status 200
func (rt *_router) fountains(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	var fountains Fountains

	w.Header().Set("Content-Type", "application/json")
	jsonResp, err := json.Marshal(fountains)
	if err != nil {
		log.Fatalf("Error happened in JSON marshal. Err: %s", err)
	}
	w.Write(jsonResp)
}
