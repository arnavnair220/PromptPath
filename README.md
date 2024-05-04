Repo Link: https://github.com/arnavnair220/PromptPath

# Python Scripts
## automatedGrading.py
automatedGrading.py and automatedAssitantFeeder.py work in conjunction in order to validate OpenAI assistant efficacy.
Run the script by inputting "python .\automatedGrading.py" in the terminal. Requires "UW Chat Transcripts.xlsx" and "Manual Real Chat Grading [Confidential].xlsx"
Outputs a visualization with each point from the grading rubric and a corresponding score
The assistant called on can be changed by changing the assistant_id
Requires OpenAI secret key
If I were to continue working on this, I would add the functionality for just testing one row from the rubric to save time of grading

## CustomerDealerSimulator.py
CustomerDealerSimulator.py simulates a chat of user specified length between PromptPath's dealer assistant and a custom made customer assistant.
Run the script by inputting "python .\CustomerDealerSimulator.py" in the terminal.
The assistant called on can be changed by changing the assistant_id.
Requires OpenAI secret key
If I were to continue working on this, I would add a UI to make the program more appealing, intuitive, and easier to use

# COSTAR readme
## Summary
2/12-3/30: Summary of COSTAR prompt changes so far (instructed to make summary file on 3/18)

The first week (2/12-2/19) was understanding what prompt engineering is. In order to do this for COSTAR, we read some articles shared by PromptPath that dived deep into prompt engineering and the COSTAR model specifically. After that, we started getting our hands dirty by just trying prompt engineering out for ourselves by making some basic prompts for some of the questions on the rubric.

The second week (2/19-2/26) we continued working on the easier parts of the rubric and started fleshing out our prompts. I worked on the COSTAR model, and had answered most of the 'easy' questions on the rubric by now with relatively decent accuracy (around 10-12 questions on the rubric and therefore the prompt).

The third week (2/26-03/04) was when we really started getting the gears moving. I made significant changes to most of the easier questions to ensure higher accuracy, and then proceeded to start working on some more questions from the rubric. While doing this, I kept on running into problems with inconsistent results, and therefore had to keep tweaking my prompts to make them more consistent.

The next couple of weeks (03/04-03/20) saw a lot of changes. We received an amended rubric, which changed things from a point based system with weightage to each prompt to an atomic rubric. Because of this, I changed all my prompts to match the new output specification. I also ended up making quite a few changes to the prompts over the course of these weeks as they seemed to work more consistently with every small change I made. Most of the rubric has now been answered pretty accurately and consistently by the model (~88% overall accuracy). There are however a few questions left to tackle from the rubric, and that will be my focus for the next week or so.

3/20 - 3/30 was focused on solving the last few parts of the rubric (6 or so questions). This was done with testing multiple different examples, as the example (multishot prompting) given to the prompt changed results every time. Finding the right example might be a longer process, and once we test the current complete COSTAR prompt against the chats, we'll know exactly which parts of the rubric need more work. I continued working on grading some manual chats over this week, along with refining the prompt. 

3/30-04/05: worked on refining costar prompt by adding examples and redifining structures. Also worked on grading more manual chats. 

4/05 - 4/17: continued working on refining costar prompt. We are no longer grading manual chats, as we had to change our focus to part 2 and 3 of the project, which was essentially about creating assistants that act as customers (good/bad) and then creating a software harness to simulate chats between the customer(s) and the dealer (PromptPath's Assistant). After these chats were created, they were then ran by our COSTAR model to grade them based on the rubric. We are now essentially done with the project, apart from trying to combine the COSTAR and RACE grading models/choosing which one works better.

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
