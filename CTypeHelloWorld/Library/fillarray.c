#include <Windows.h>

#include <stdio.h>
__declspec(dllexport) void fill_array_with_ones(int* arr, int size) {
	for (int i = 0; i < size; i++)
	{
		arr[i] = 1; 
	}
}
