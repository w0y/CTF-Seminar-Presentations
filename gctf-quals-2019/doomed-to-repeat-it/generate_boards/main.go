package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"./random"
)

const (
	BoardWidth  = 7
	BoardHeight = 8
	BoardSize   = BoardWidth * BoardHeight // even
)

func init() {
	if BoardSize%2 != 0 {
		panic("BoardSize must be even")
	}
}

func main() {
	file, err := os.OpenFile("board_layouts.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		log.Printf("couldn't open file: %v", err)
		return
	}
	defer file.Close()
	var i uint64
	for i = 0; i < 1<<17; i++ {
		rand, err := random.New(i << 47) // use custom seed
		if err != nil {
			log.Printf("couldn't create random: %v", err)
			return
		}
		boardLayout := make([]int, BoardSize)
		for i, _ := range boardLayout {
			boardLayout[i] = i / 2
		}
		for i := BoardSize - 1; i > 0; i-- {
			j := rand.UInt64n(uint64(i) + 1)
			boardLayout[i], boardLayout[j] = boardLayout[j], boardLayout[i]
		}
		board := strings.Trim(strings.Join(strings.Fields(fmt.Sprint(boardLayout)), " "), "[]")
		if _, err = file.WriteString(board + "\n"); err != nil {
			log.Printf("couldn't write to file: %v", err)
			return
		}
	}
}
