# Guildlines for Don't Starve Together by ChatGPT

### Motivation:

When playing the game, once you are sufficient enough skill-wise, you want to make it more interesting by trying different things, which I hope to achieve by playing in different roles. 

With that in mind, to argue that switching roles is one good way, there are also two other assumptions:
- I want to play on a public server, where it brings more uncertain surprises and I don’t have to spend most of the time on surviving but can focus on exploration.
- I just want to play for a short period of time, e.g. a few hours, which means I only play for about 20 days in the game. Given how the public server is constructed, the things can happen is quite predictable. 

However, each character in Don’t starve together is designed to have lots of special strengths and weakness, even tools that can only be made by them, BUT, vaguely described and remaining to be  discovered by player. On one hand, it is the nature of a sandbox game. On the other hand, it requires lots of effort from a player to diverge from what they usually do even in different roles, which limits the fun they can have. 

Thus, I want to provide a general to-dos provided by someone knowledgeable in the game to help users to start with. Here I consider our large language model, ChatGPT, as the knowledgeable guide. 

Some general strategies I have:

- I kept a clean version of prompt for each character, once I identify a working template. Basically, I worry about having every thing in the one long thread, will hurts the goal of making distinct timelines serving the best of different characters. 
- The same strategy is used in the separation of the coding and content generation. 

**Prompts I used:**

#### Background

> Don’t starve together has many characters. I have to make a webpage hosted on GitHub pages in Jekyll, where the homepage include the introduction and the lists of characters, each can be clicked by user and leads to a subpage showing the suggested actions the first 20 days. 
> I have the following assumptions about the timeline generated per character:
> Assuming we have an experienced player but don't have much experience with the specific character, such as Wigfrid. The user is playing on one of the Klei's public servers. The goal is to survive for 20 days and unlock as many different things as possible, especially about the specific character. 
> Would you please give a nice introduction to include on the homepage? 

#### Character-wise content
> Don’t starve together has many characters.  Do you know “NAME”? How is he/she different from other roles, especially when it comes to playing strategies?

> Assuming I am a experienced player but don't have much experience with the character, NAME. I play on one of the Klei's public servers. The goal is to survive for 20 days and unlock as many different things as possible, especially about the specific character.  Could you give me a timeline in detail, with actions to take listed, including the resources to collect, the feasts to hunt, the food to eat, as deta
ils as possible.

> Use exactly what you proposed but format the timeline in a YAML file as:
` - "Day 1##Collect grass, twigs, and flint---Build a campfire before nightfall" `
each action per day is seperated by `---`

- 

#### Roadmap

Todos:
- [Nan] formalize the content generation prompts for: 

    * Homepage: Background and basic introduction per character.
    * Character page

- [] formalize the prompts supporting data pipelne:
    * format the generated contents as `YAML` and `markdown` files.

- [] webpage improvement 
    * add a theme 
    * better designed timeline presentation 
    * 