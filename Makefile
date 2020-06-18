jobs:
	for jobs in Jobs/*; do if [ -d ${job} ]; then mkdir -p docs/${job} && cp ${job}/README.md docs/${job}; fi; done
	for doc in docs/Jobs/*; do if [ -d ${doc} ]; then echo 'collapse: true' > ${doc}/.pages; fi; done
