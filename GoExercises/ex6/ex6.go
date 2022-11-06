package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
)

type Stations struct {
	Linea         string    `json:"line"`
	Stations      []Station `json:"stations"`
	DepartingTime time.Time `json:"departingTime"`
}

type Station struct {
	Name     string `json:"name"`
	Distance int    `json:"distance"`
	ETA      int    `json:"ETA-from-previous-station"`
	Platform int    `json:"platform"`
}

type Response struct {
	TotalDistance int       `json:"totalDistance"`
	TravelTime    int       `json:"travelTime"`
	ArrivalTime   time.Time `json:"arrivalTime"`
}

func calcolo(w http.ResponseWriter, r *http.Request) {

	var stations Stations

	err := json.NewDecoder(r.Body).Decode(&stations)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	totalDistance := 0
	travelTime := 0
	for i := 0; i < len(stations.Stations); i++ {
		totalDistance += stations.Stations[i].Distance
		travelTime += stations.Stations[i].ETA
	}
	arrival := time.Date(stations.DepartingTime.Year(), stations.DepartingTime.Month(), stations.DepartingTime.Day(), stations.DepartingTime.Hour(), travelTime, stations.DepartingTime.Second(), 0, time.Local)
	var response Response
	response.TotalDistance = totalDistance
	response.TravelTime = travelTime
	response.ArrivalTime = arrival

	w.Header().Set("Content-Type", "application/json")
	jsonResp, err := json.Marshal(response)
	if err != nil {
		log.Fatalf("Error happened in JSON marshal. Err: %s", err)
	}
	w.Write(jsonResp)
}

func main() {
	http.HandleFunc("/", calcolo)

	fmt.Println("Starting web server")
	http.ListenAndServe(":8090", nil)
}
