OPTS=-Wall -Werror -pedantic -fno-pie -no-pie

all: demo1.elf demo2.elf

demo1.elf: demo1.o main1.o
	gcc -o $@ $^ $(OPTS)

demo1.o: demo1.s
	gcc -o $@ -c $^ $(OPTS)

main1.o: main1.c
	gcc -o $@ -c $^ $(OPTS)

demo2.elf: demo2.o main2.o
	gcc -o $@ $^ $(OPTS)

demo2.o: demo2.s
	gcc -o $@ -c $^ $(OPTS)

main2.o: main2.c
	gcc -o $@ -c $^ $(OPTS)

demo1_run: demo1.elf
	./demo1.ef

demo2_run: demo2.elf
	./demo2.elf

demo1_nc:
	nc -l -p 1337 | xxd | grep -v -e "0000 0000 0000 0000 0000 0000 0000 0000"

demo2_nc:
	nc -l -p 1337

demo1_segments: demo1.elf
	readelf demo1.elf -l

clean:
	rm -f main1.o main2.o demo1.o demo2.o demo1.elf demo2.elf
