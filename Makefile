run:
	python src/assistant.py prompts/Atomic.txt data/chats/17.txt > results/Atomic.out
	cat results/Atomic.out

clean:
	rm results/Atomic.out