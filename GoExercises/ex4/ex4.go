package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type Stations struct {
	Linea         string    `json:"line"`
	Stations      []Station `json:"stations"`
	DepartingTime string    `json:"departingTime"`
}

type Station struct {
	Name     string `json:"name"`
	Distance int    `json:"distance"`
	ETA      int    `json:"ETA-from-previous-station"`
	Platform int    `json:"platform"`
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

	fmt.Printf("%+v\n", stations)
	totalDistance := 0
	travelTime := 0

	for i := 0; i < len(stations.Stations); i++ {
		totalDistance += stations.Stations[i].Distance
		travelTime += stations.Stations[i].ETA
	}
	fmt.Println(totalDistance)
	fmt.Println(travelTime)
}

