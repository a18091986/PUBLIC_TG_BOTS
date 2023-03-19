FLAGS = -Wall -Werror -Wextra -std=c11

all: clean_before main clean_after

main: main.o
		gcc $(FLAGS) main.o -o c_func

main.o:
		gcc -c $(FLAGS) main.c -o main.o

# git:
# 		git add .
# 		git commit -am "from make"
# 		git push

clean_before: 
		del *.o *.exe

clean_after: 
		del *.o