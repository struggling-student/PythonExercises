package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
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

func main() {
	jsonFile, err := os.Open("data.json")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("Successfully opened the file")
	defer jsonFile.Close()

	byteRead, _ := ioutil.ReadAll(jsonFile)

	var stations Stations

	json.Unmarshal(byteRead, &stations)

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

	file, _ := json.MarshalIndent(response, "", " ")
	_ = ioutil.WriteFile("test.json", file, 0644)
}
