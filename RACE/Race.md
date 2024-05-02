# RACE.txt

prompt using the RACE approach

## ROLE: gives LLM instruction to use a subset of its training persona

Psychology, human behavior, and language analysis: gives LLM a way to analyze the complex convo data

have knowledge of jargons: makes sure LLM are aware that the transcripts contain car sales jargon

## CONTEXT: giving LLM the context for the car dealer representitive convo

We gave series of comments cusing on making sure the LLM knows a conversation should be enjoyable and helpful
We also laid out the difference to ASK and OBTAIN with 1-shot prompting techniques

## ACTION: gives LLM a expectation of the structure of the conversation transcripts. Also layout the structure of the questions asked.

upon testing, we can write structures in square brackets and use "replace" to represent a variable
We choose the structure 

\[NUMBER]. [QUESTION (DETAILS)]

where details gives additonal details the LLM might need to determine the answer for that question

## EXECUTE: gives LLM a concrete output format

We chose the output format to be JSON formatted for readability and easy manipulation.
when testing with the automatic grading, we can separate the comments easily
