#ifndef MY_MASTERMIND_H
#define MY_MASTERMIND_H

#define CODE_LENGTH 4

int my_strlen(const char *s);
int read_line(char *buf, int max_len);
int guess_valid (const char *guess);
int code_valid(const char *code);     

void random_code(char *code);
void evaluate_guess(const char *code, const char *guess, int *well_p, int *miss_p);
void game_loop(const char *code, int attempts);

#endif