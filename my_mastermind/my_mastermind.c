#include "my_mastermind.h"
#include <stdio.h>      // printf 
#include <unistd.h>     // read 
#include <stdlib.h>     // atoi, rand, srand 
#include <time.h>       // time 
#include <string.h>     // strcmp 


int my_strlen(const char *s) //Counts the lenght of a string
{
    int i = 0;

    while (s[i] != '\0')
        i++;
    return i;

}

int read_line(char *buf, int max_len)
{
    int i = 0;
    char c;
    ssize_t r;

    while (1)
    {
        r = read(0, &c, 1);
        if (r <= 0)
        {
            if (i == 0)
                return -1;
            break;
        
        }
        if (c == '\n')
            break;
        if (i < max_len -1)
        {
            buf[i] = c;
            i++;
        }    
    }
    buf[i] = '\0';
    return i;    
}

int guess_valid (const char *guess) //Checks if length is correct and contents are from 0 to 8
{
    int len = my_strlen(guess);
    int i = 0;

    if (len != CODE_LENGTH)
        return 0;

    while (i < CODE_LENGTH)
    {
        if (guess[i] < '0' || guess[i] > '8')
            return 0;
        i++;
    }
    return 1;
}


int code_valid(const char *code) //Checks if the CODE is correct - length, numbers 0-8, don't repeat
{
    int used[9] = {0}; //Makes 9 "solts" for items, each slot is set to 0.
    int i = 0;
    int d;

    if (!guess_valid(code)) //Checks length and content
        return 0;
    while (i < CODE_LENGTH) //Checks if there's no repetitions
    {
        d = code[i] - '0';
        if (used[d] == 1)
            return 0;
        used[d] = 1;
        i++;
    }
    return 1;
}

void random_code(char *code)
{
    int used[9] = {0};
    int i = 0;
    int d;

    srand((unsigned int)time(NULL));
    while (i < CODE_LENGTH)
    {
        d = rand() % 9;
        if (used[d] == 0)
        {
            used[d] = 1;
            code[i] = (char)('0' + d);
            i++;
        }
    }
}

void evaluate_guess(const char *code, const char *guess, int *well_p, int *miss_p)
{
    int i;
    int count_code[9] = {0};
    int count_guess[9] = {0};
    int total_matches = 0;

    *well_p = 0;
    *miss_p = 0;

    i = 0;
    while (i < CODE_LENGTH)
    {
        if (guess[i] == code[i])
            (*well_p)++;
        count_code[code[i] - '0']++;
        count_guess[guess[i] - '0']++;
        i++;
    }
    i = 0;
    while (i < 9)
    {
        if (count_code[i] < count_guess[i])
            total_matches = total_matches + count_code[i];
        else 
            total_matches = total_matches + count_guess[i];
        i++;
    }
    *miss_p = total_matches - *well_p;
}

void game_loop(const char *code, int attempts)
{
    int round_num = 0;
    char buf[64];
    int len;
    int well_p;
    int miss_p;

    printf("Will you find the secret code?\n");
    printf("Please enter a valid guess\n");

    while (round_num < attempts)
    {
        printf("Round %d\n", round_num);
        while (1)
        {
            printf(">");
            len = read_line(buf, (int)sizeof(buf)); //Reads the input and stores it in the buffer after pressing enter or crtl+D
            if (len < 0)
                return;

            if (!guess_valid(buf)) //Checks if the lenght and the contents of the input are valid
            {
                printf("Wrong input!\n");
                continue; //Returns to the begining of the loop to ask for input again
            }
            break; //If check passed, the loop breaks
        }
    

    if (strcmp(buf, code) == 0)//Vicroty
    {
        printf("Congratz! You did it!\n");
        return;
    }

    evaluate_guess(code, buf, &well_p, &miss_p);
    printf("Well placed pieces: %d\n", well_p);
    printf("Misplaced pieces: %d\n", miss_p);
    printf("-----\n");
    round_num++;
    }
}


int main(int argc, char **argv)
{
    char code[CODE_LENGTH + 1];
    int attempts = 10;
    int i = 1;
    int have_code = 0;

    while (i < argc){
        //Loop checking if the code is valid 
        if ((strcmp(argv[i], "-c") == 0) && i + 1 < argc) //Checking if the input is "-c" and there is more content in next string
        {
            if (code_valid(argv[i + 1]))
            {
                    int j = 0;
                    while (j < CODE_LENGTH)
                    {
                        code[j] = argv[i + 1][j];
                        j++;
                    }
                    code[CODE_LENGTH] = '\0';
                    have_code = 1;
            }
            i += 2;
        }
        else if ((strcmp(argv[i], "-t") == 0) && i + 1 < argc)  //Checking if the input is "-t" and there is more content in next string
        {
            attempts = atoi(argv[i + 1]); //Change attempts
            if (attempts <= 0) 
                attempts = 10; //If invalid, less then 0, attepmts back to default 10
            i += 2;
        }
        else {
            i++;
        }
    }
    //If incorrect code, generate random code
    if (!have_code)
        random_code(code);
    //Run game
    game_loop(code, attempts);
    return 0;
}
