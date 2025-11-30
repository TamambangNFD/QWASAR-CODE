NAME    = my_mastermind
CC      = gcc
CFLAGS  = -Wall -Wextra -Werror

SRC     = my_mastermind.c
OBJ     = $(SRC:.c=.o)
HEADER  = my_mastermind.h

all: $(NAME)

$(NAME): $(OBJ) $(HEADER)
	$(CC) $(CFLAGS) -o $(NAME) $(OBJ)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re