# Solutions

Solutions have now been uploaded for this assessment.

For HSMA Students: these solutions are intended to provide an example of how to approach a question. They are far from the only way to tackle these questions! If you have provided a solution that works, your solution will not be marked down from being different from the code and approaches in the solutions file.

In some cases, the solutions may go slightly beyond the standard expected to achieve full marks, but showcase some 'best practice' that would be recommended. Instances of this include

- filtering the dataframe in the streamlit question to hide some columns (this would be nicer for your end user, but wasn't requested)
- using a random state when initialising the XGBoost model (it is very good practice to do so, but the question only requested it in the train test split) 

In the event we think something is missing from your solution, we will carefully cross-reference with the question wording to ensure that the question was worded fairly and made it explicit what was expected. 

---

## Web version of the assessment

If you wish to try out the assessment using a web environment, head to [this repository](https://github.com/hsma-programme/hsma6_assessment_WEB) and click on the button at the beginning of the readme.

---

# Assessment Information

The assessment is provided as a Jupyter Notebook, along with some csv data files that are required to answer some of the optional questions.

You will have from 10:30 - 12 to complete the assessment, and submit it to us (instructions for submission will be provided on the day).  Late submissions will be disqualified.

You will not be required to stay on the Zoom call whilst undertaking the assessment.

As a reminder, the assessment is open book

- You can use any material, lecture notes, videos, code snippets, books etc. (HSMA or otherwise) and package documentation to help you write your answers
- The standard built-in code completion via Intellisense - a default feature installed when adding the Python extension to VSCode - is fine to use. It looks something like this and will give you help with things like the names of parameters.
  - However, you cannot use LLMs/AI like ChatGPT, Github Copilot, or Intellicode (different to intellisense!) to write or assist in writing or debugging your answer in this assessment.
  -Instructions on how to check you don’t have any disallowed extensions enabled can be found in this video: https://youtu.be/1vbc1_CPG4k
- Remember - you can easily access the books, slides and repositories via our website.
  - https://hsma-programme.github.io/hsma_site/hsma_content/books/books.html
  - https://hsma-programme.github.io/hsma_site/hsma_content/modules/modules.html

Once the examination has been released, neither Dan nor myself will answer any Python questions from anyone within the HSMA community for the duration of the assessment.  An announcement will be made on Slack that no Python questions will be answered during this time.

Plagiarism will result in immediate disqualification.  You are not permitted to ask other HSMAs for help during the assessment, or to take their work (or part of their work) as your own.

# Assessment Structure
There will be several mandatory questions in the notebook using core Python skills. You should attempt all of these questions.

You will then choose two of the remaining questions to answer from the notebook.

There is no benefit to answering more than two of these questions, and if you start answering a question and then choose a different one, we’d recommend removing your code before submitting it (to ensure we don’t mark the wrong question)

# Passing the assessment

The pass mark for the assessment is 50%. Any instances where people fail to reach this mark will be moderated by both Dan and me.

If you do not pass the assessment, you can choose to submit project work to be certified by the project assessment route instead.  You can also submit as many projects for certification as you like, but be aware that once you have been successfully certified once (whether via completing the assessment or by having a project assessed), you cannot be certified again.

# Environments for the Assessment

The assessment will make use of the environments we have been using throughout the course.

Note that while running the code is likely to help you write your solution, it is not an essential requirement, and code that fails to run due to small typos or other minor errors will not automatically receive zero marks - rather, you will receive an amount of marks up to the maximum depending on how close to a working solution you are.

## For those of you who have used Anaconda throughout the HSMA course

As long as you have the environments from the course already installed, you will not need to do anything with the exception of:

- installing one extra package into the nlp_basics environment
	1. Open an Anaconda Prompt
  2. Run conda activate nlp_basics
  3. Run pip install requests

- Installing one extra package into the abs environment
	1.Open an Anaconda Prompt (or use the one from the previous step)
  2. Run conda activate abs
  3. Run pip install ipykernel

This is demonstrated in this video:  https://youtu.be/yQnbfaCM5es

This video demonstrates how you can activate different environments for different questions throughout the assessment:  https://youtu.be/QLqoKGqxoV0

However - we know some of you may have moved computers, or will be doing this on a personal laptop on which the environments were never installed. Therefore, we have also provided an optional environment.yml file in Slack that will create a ‘hsma_assessment’ environment. You may even wish to install this as a backup option in case of any issues with your existing environments on the day!

## For those of you who have been using venv for environment management

I have provided some requirements.txt files on Slack. These have been tested with Python

- 3.9.13, 3.10.11, 3.11.9 (one file)
- 3.12.2 (the other file)

This should work with other minor versions (other numbers after the final dot - e.g. 3.9.12 or 3.10.13 would also most likely work).

However, neither will work with 3.13 due to an essential package not being supported in 3.13 yet. Therefore, it is not possible to use 3.13 for the assessment.

I would recommend that you set up a folder that you will store the assessment notebook and data files in, and then create the virtual environment in there.

This video demonstrates how you can do this: https://youtu.be/XaJggpYw4AE

## If you are unable to install or use those environments for any reason

A web-based option will be made available on the day of the assessment.
