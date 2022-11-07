package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var somma_cfu float64
	var somma_voti float64

	for x := 1; x <= 40; x++ {
		fmt.Println("inserisci voto:")
		voto, _ := reader.ReadString('\n')
		voto = strings.Replace(voto, "\n", "", -1)

		fmt.Println("inserisci CFU:")
		cfu, _ := reader.ReadString('\n')
		cfu = strings.Replace(cfu, "\n", "", -1)

		if strings.Compare("stop", voto) == 0 {
			break
		} else {
			int_voto, err := strconv.ParseFloat(voto, 32)
			int_cfu, err := strconv.ParseFloat(cfu, 32)

			if err == nil {
				somma_voti = somma_voti + (int_voto * int_cfu)
				somma_cfu = somma_cfu + int_cfu
			}
		}
	}
	var risultato float64
	risultato = somma_voti / somma_cfu
	fmt.Println(risultato)
}
