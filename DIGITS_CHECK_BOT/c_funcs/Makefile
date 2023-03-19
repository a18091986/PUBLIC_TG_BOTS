FLAGS = -Wall -Werror -Wextra -std=c11

all: clean_before main clean_after

main: main.o
		gcc $(FLAGS) main.o -o c_func.exe

main.o:
		gcc -c $(FLAGS) main.c -o main.o

# git:
# 		git add .
# 		git commit -am "from make"
# 		git push

clean_before: 
		rm -rf *.o *.exe

clean_after: 
		rm -rf *.o
