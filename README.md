# AIStoryGeneration

## Our Motivation
Automated story generation is an exciting field of AI research that aims to generate good stories using technology. The quality of stories can be subjective and difficult to define, so there are multiple ways to evaluate them. In this blog, we will review and compare various Large Language Models (LLMs) for their ability to generate stories.

We will use the WritingPrompts dataset, which includes 300,000 writing prompts and corresponding stories, to train the models and evaluate the resulting stories. Story generation has many potential applications, from interactive storytelling to automated news article generation.

It also raises important research questions about the capabilities of generative models and their understanding of the world. By comparing different models, we hope to gain insights into the capabilities and limitations of automated story generation.

## Introduction to AI Story Generation
AI story generation is a field within artificial intelligence that focuses on developing algorithms and models that can generate written narratives or stories.

This technology has the potential to be used in a variety of applications, such as creating personalized content for social media, improving language learning and education, and helping to automate the writing process in journalism and other fields.

Fictional storytelling can be used in multiple scenarios, some of which are computer games(generating new scenarios based on user gameplay) and education(generating personalized "stories" based on various inquiries from teachers and students). These would have multiple qualitative and quantitative dimensions to look at, such as narrative styles, story/universe building, knowledge utilization or creation, etc.

Apart from the aforementioned, story generation also highlights some of the important research questions within generative models. To generate a story, a system would need to know how to tell a story as well as knowledge of how the world works. Story generation is also a possible way of finding out if a system "understands" something; generating a story demonstrating a concept correctly would show that it understood the concept.

## Our Task
### Build 2 LLM(Large Language Models) to generate stories given a promopt and evaluate them grammatically and qualitatively.

## Dataset: Writing Prompts
The dataset that we used to train our models is the **WritingPrompts** dataset. The WritingPrompts dataset contains 300,000 writing prompts and written stories spanning 3 years that have been scraped with Reddit's official API and cleaned from Reddit's WritingPrompts forum, where users can posts prompts to inspire other users within the community. Each prompt in the WritingPrompts dataset may contain more than one corresponding story response. Stories in this dataset are more than 30 words.

Our training dataset contained 272,600 stories mapped to about 104,000 prompts. Our validation and test datasets each contained about 15,000-16,000 story-prompt pairs. There are a total of 7.7M words and 200M words respectively for prompts and stories. The average token length is 28.4 for prompts and 734.8 for stories.

### Preprocessing
Due to a lack of time, we restricted the story token size to 300 tokens to encourage faster model building, as training on 735 tokens would take a long time. Additionally, we preprocced data with the <CLS> tag to separate prompts from stories and removed whitespaces. We decided to keep the <new line> tags, however, as some of the stories where written in the form of poetry or otherwise had paragraph structure that was essential to the story.

## Our Models
### GPT2-small

### T5-small

<img width="657" alt="Screen Shot 2022-12-08 at 1 14 46 PM" src="https://user-images.githubusercontent.com/72052259/206546682-b708a96c-52e8-49a1-a7dd-96c851f48d9c.png">

## Our Results

The average BLEU score corresponds to
Coherence, Fluency, Interesting and Relevant correspond to scores from Amazon Mechanical Turk. Users were asked asked to rank the coherence, fluency, how interesting a sample was as well as how relevant the sample was to the prompt on a scale from 1 - 4, where 1 was least favorable and 4 was most favorable.
Lastly, we ran the generated samples through Grammarly and averaged the resulting scores over 100 random samples.

## Observations

## Examples
