package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Sorts ints using insertion sort
func Sort(unsorted []int) []int {
	fmt.Printf("Sorting %v items...", len(unsorted))
	start := time.Now()
	// Copy the unsorted slice for sorting
	sorted := make([]int, len(unsorted))
	copy(sorted, unsorted)
	for i := 1; i < len(sorted); i++ {
		// Pluck next number to sort
		unum := sorted[i]
		// Slide all numbers up the sorted aspect until we arrive where our unsorted number should be
		j := i - 1
		for ; j >= 0 && sorted[j] > unum; j-- {
			sorted[j+1] = sorted[j]
		}
		// PLace the unsorted number in it's position
		sorted[j+1] = unum
	}
	fmt.Printf("took %s number of seconds: %d\n", time.Since(start), time.Since(start))
	return sorted
}

func main() {
	// Here we add an extra 1,000 random numbers to the list to sort
	// each time it goes in
	var unsorted []int
	for range 1000 {
		new_unsorted := make([]int, 1000)
		for i, _ := range new_unsorted {
			new_unsorted[i] = rand.Intn(32_000)
		}
		unsorted = append(unsorted, new_unsorted...)
		Sort(unsorted)
	}
}
