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

To compare the generated stories from each of the models, we will employ two methods: after randomly selecting a number of prompts, we will be evaluating the grammar correctness on Grammarly, and creativity through human evaluation on Amazon Mechanical Turk.

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

The BLEU score is calculated by comparing each generated story with it's original counterpart. These scores are averaged out and reported as Avg. BLEU.

Coherence, Fluency, Interesting and Relevant correspond to scores from Amazon Mechanical Turk. Users were asked asked to rank the coherence, fluency, how interesting a sample was as well as how relevant the sample was to the prompt on a scale from 1 - 4, where 1 was least favorable and 4 was most favorable.

Lastly, we ran the generated samples through Grammarly and averaged the resulting scores over 100 random samples.

## Observations
### Brevity

T5 had a 128 token cut-off whereas GPT-2 had 300
This might have caused the poor performance of GPT-2 even with 6x the run time
 
### Grammarly Scores
The difference in Grammarly scores were caused due to different reasons. For example, the original human-written stories’ poor Grammarly score can be attributed to intentional data punctuations:
  
Eg.1 (the spaces between the commas and words): He then looks down at his race torn by religion , hate , racism .
  
Eg.2 (the spaces between do and n't): `` Why do n't you have a seat ? '' Asked Christopher .

GPT-2’s comparatively better Grammarly score is because Grammarly focuses on sentences more than sentence flow([References from Grammarly Blog](https://www.grammarly.com/blog/how-grammarly-uses-ai/)).

Meanwhile, T5 has an overwhelming superior Grammarly score mostly due to shorter sentences generated, leading to less chances of grammer mistakes.
  
### T5 Repetitive starts
Another point we noticed specifically with T5 story generations was about 3/4ths of the T5 stories start with the same phrases, in which we are unsure as to why. This requires additional research and would be a good direction for future work.
<img width="303" alt="Screen Shot 2022-12-08 at 11 36 13 PM" src="https://user-images.githubusercontent.com/72052259/206631829-112f034a-388c-4763-8842-e0793a5a16c4.png">

## Examples
### Prompt
You are a serial killer. Each murder you commit adds a new voice to your head.

**Original**
  
“Oh God, please don’t, please don’t” wailed the voices in my head. I wished they would shut up for a moment. They made it hard to hear if the girl in my trunk was waking up. 

“Don’t do it, you sick bastard”. There was old man McAvoy, shouting over the rest. I was pretty sure he yelled so loud because he was deaf . After all, he really should have heard me in the alley behind him. It had been a cloudy night and I’d tripped over a rusty trashcan, but that old coot had kept on fumbling with his keys and stopping to rummage around in his pockets like he had all the time in the world, instead of four hours.

I pulled into the parking lot of the motel where I was staying and cut the engine. As I approached the trunk of the car, the wailing crescendoed. “Cut it out”, I grumbled, rubbing the bridge of my nose, “Or I’ll take it out of her skin”.

About half the voices fell silent. The other half were too crazy to listen or too angry to care, but the volume in my head was manageable at least. “You sick motherfucker ”, McAvoy railed. “I can’t wait til the cops catch ya. They’re gonna beat your sorry ass and stick you in the chair faster than… ” 

“Faster than I can kill this girl? ” I muttered, lifting her

**GPT2-small**

Tyler Roberts was a man like nobody else. He was a serial killer.
  
**T5-small**

I'm not sure what to do. It's just me, it's my job. I've been doing this for years now, and I've never seen anything like that before. I've always wanted to be a killer, but I wasn't the only one who would ever get into this world. But I didn't want to be a murderer, or even a murderer.

I'm going to die.

### Prompt
"Some days , I think I am dying . Other days , I hope I am ..."
  
**Original**
  
Some days, I think I am dying. Other days, I hope I am. But i'm here.Unfortunately , I am still here. A shell of a human being. A painting of modest beauty but exquisite detail. Inside, however, lies a drawing soaked in black ink and torn to shreds. There's no beauty in such a world anymore. Just emptiness. Days upon days of gut wrentching emptiness and the sharp teeth of loneliness tearing away at your heels.

Torment ; noun
  
1 . Severe physical or mental suffering.
  
And then you're presented with it. An escape. The smallest glint of light. You can practically feel the relief, the though of it making you happier than anything perhaps ever has. Your whole body tingles at the idea, fear and excitement clouding your desperate mind. If you had a cavity, you would want a dentist to remove it, would you not? It's been bothering you for weeks now, your teeth in more pain than they've ever been before. You can't eat you favorite things, you can't do any sports, you can hardly talk its so incredibly sore. The only thing on your mind is the pain. The constant never ending pain. How are you supposed to focus on anything with your jaw throbbing like this? It's impossible. But lucky you , there's a solution. A silver dentist with a loud booming voice, promising you to completely rid yourself of your nasty toothache.

**GPT2-small**
  
 You 're killing yourself ? '' <newline> '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' , '' <newline> `` <newline> '' , '' , '' <newline> `` <newline> '' , '' , '' <newline> `` <newline> '' , '' , '' <newline> `` <newline> '' , '' <newline> `` <newline> '' , '' <newline> `` <newline> '' , '' <newline> `` <newline> '' <newline> `` <newline> '' <newline> `` <newline> '' <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> `` <newline> ``
  
**T5-small**

Some days, I think I am dying. Other days, I hope I am.''
  
What do you mean? ''
  
No, no, it's just me. ''
  
It's not my fault. ''
  
Yes, that's what I want. ''
  
### Prompt
An army approached the pass. Only one being stood in there way. They did not plan to survive, just survive long enough.

**Original**

The march had been long and arduous but they had reached the pass. Tomorrow would be the final day of life for most of the army. The soldiers though had made their peace with God, and knew that what they were about to sacrifice gave the chance of hope for their families to survive.
  
The pass in front of them was the only link with the outside world , the only way for food to come and enter to the valley. That was until the beast appeared. It killed anything that entered the past and the valley had been slowly starving to death due to a drought that killed the harvest. Their only hope was to send messengers to the outside to gain the assistance of a legendary warrior.
  
The army sat around their campfires sharing one last round of somber laughs before tomorrow. The five fastest runners were already asleep ready to prepare for the mad dash they would attempt through the chaos. They carried the hope of all the valley. As the fires died that evening and the stars faded to the morning lights the men awoke ready for death.
  
The men stood , at arms just on the edge of the pass staring at their foe and death. It sat among a pile of bones at the center of the valley at his narrowest point. Its white fur glistened clean a pure, a contrast to the blood of those around it whom it had slain. Its red eyes stared at them glinting of chaos and death. Its nose twitched as if beckoning them to try and kill it. To most it

**GPT2-small**

I 'm not alone.
  
Not in a sense. I'm not the handiwork of a random assassin. I'm not a hero.
  
And I 'm not the man I 'm facing right now.
  
I 'm not a hero.
  
And I 'm not the man I 'm facing right now.
  
Not at all .
  
Not as the hero I am .

**T5-small**

I don't know what to expect, '' the army said.
  
What is it? ''
  
It's not like we are going to be here for long enough. ''
  
No, no, that's just me. ''
  
Well, this isn't my fault
