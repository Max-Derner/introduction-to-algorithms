package main

import (
	"slices"
	"testing"
)

func TestSort(t *testing.T) {
	unsorted := []int{3, 7, 6, 4, 8, 2, 9, 1, 10, 5}
	sorted := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	result := Sort(unsorted)
	if !slices.Equal(result, sorted) {
		t.Errorf("Expected %v, got %v", sorted, result)
	}
}