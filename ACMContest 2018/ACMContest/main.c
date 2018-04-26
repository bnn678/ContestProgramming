#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma warning(disable:4996)

void CopyString(int start_c, int length, char* input_str, char* output_str )
{
	for (int i = 0; i < length; i++)
	{
		output_str[i] = input_str[start_c + i];
	}
}

void SubStr(char* destination, char* input, int start_c, char delimiter)
{
	char substring[20] = { 0 };
	int count = 0;
	char c;
	while (1)
	{
		c = input[count + start_c];
		if (c != delimiter && c != '\0')
		{
			substring[count] = c;
			count++;
		}
		else
		{
			strcpy(destination, substring);
			return;
		}
	}
}

void Swap(int* heights, int num_to_swap)
{
	int temp;
	int a = heights[num_to_swap];
	int b = heights[num_to_swap + 1];

	temp = a;
	heights[num_to_swap] = b;
	heights[num_to_swap+1] = temp;
}


int main()
{
	/*
	test for SubStr
	char test[] = "1 1000 900";

	char my_test1[20];
	strcpy(my_test1, SubStr(test, 0, ' '));
	printf("%s\n", my_test1);

	char my_test2[20];
	strcpy(my_test2, SubStr(test, 2, ' '));
	printf("%s\n", my_test2);

	char my_test3[20];
	strcpy(my_test3, SubStr(test, 7, ' '));
	printf("%s\n", my_test3);
	*/


	char p[5] = { 0 };
	fgets(p, 4, stdin);

	char input_line[150] = { 0 };	

	//FILE* f_in = fopen("input.txt", "r");

	int outputs[1000];
	char inputs[1000][150];
	char dumb[100];

	for (int i = 0; i < atoi(p); i++)
	{
		/*
		fgets(inputs[i], 150, f_in);
		fgets(dumb, 2, f_in);
		/**/
		fgets(inputs[i], 150, stdin);
		fgets(dumb, 2, stdin);
		
	}

	for (int i = 0; i < atoi(p); i++)
	{
		strcpy(input_line, inputs[i]);

		char heights_str[20][6] = { 0 };

		
		int char_pos;
		SubStr(dumb, input_line, 0, ' ');
		char_pos = strlen(dumb) + 1;
		for (int j = 0; j < 20; j++)
		{
			SubStr(heights_str[j], input_line, char_pos, ' ');
			char_pos += strlen(heights_str[j]) + 1;
		}

		int heights[20] = { 0 };
		for (int j = 0; j < 20; j++)
		{
			heights[j] = atoi(heights_str[j]);
		}

		int steps = 0;

		for (int j = 0; j < 20; j++)
		{
			for (int k = 0; k < 19; k++)
			{
				if (heights[k] > heights[k + 1])
				{
					Swap(heights, k);
					steps += 1;
				}
			}
		}

		outputs[i] = steps;
	}

	for (int i = 0; i < atoi(p); i++)
	{
		printf("%d %d\n", i + 1, outputs[i]);
	}

	//fclose(f_in);
}