# Notes for linkedin article 'Harnessing LLMs for Streamlined Requirements Discovery Interviews'

Source [here](./Sources/Harnessing%20LLMs%20for%20Streamlined%20Requirements%20Discovery%20Interviews%20|%20LinkedIn.pdf):

#### Background:
Complicated projects require a 'discovery' phase which involves numerous interviews and meetings between business analysys, consultants, project managers, etc.

#### Problem:
Accomplishing all the tasks in the background section is time-consuming, riddled with misunderstandings and misinterpretations leading to unstructured data that's not incredibly useful to analyze and act upon.  

#### LLM Involvement:
Author speaks on how LLMs can operate across various platforms. I see a few issues with this as far as actually providing a solution. 

1. **Non-Deterministic Responses** LLMs are not deterministic. While they can be made to feel more deterministic via things like 'temperature' settings they very rarely, if ever, provide the exact same output response from an input query. So if a business analyst, a consultant, and a project manager all use it to ask the same questions about the same data they're all going to get varying responses, even if they are all utilizing the same model. This just shifts the blame of misunderstanding and misinterpretation it does not alleviate it.
2. The author provides this example: 

> A stakeholder sends an email stating, "We need a system that can handle our growing inventory more efficiently." The LLM can follow up with targeted questions to clarify requirements, such as, "Could you specify the average number of inventory items handled daily?" or "What specific challenges are you facing with the current system?"

This is an ideal scenario where an LLM effectively utilizes targeted questions in order to gain more context. However, even the best, and most expensive to use, LLMs often struggle significantly with deep contextual understanding, especially as the conversation grows in size. This leads to the LLM frequently hallucinating resulting in irrelevant responses or repetitive questions. 

3. **Privacy**: Integrating LLMs into business processes where sensitive information is handled introduces significant privacy and ethical concerns. This is part of what my other research aims to touch on via local deployment of quantized LLMs.

#### End of article section 'Case in Point: A Real-World Application'  
The author suggests an LLM capable of being used by numerous different team members across a company, then from the interactions building a taxonomy of requirements and categorizing them into things like 'user management', 'sales tracking', etc. The author then states "It learns that when sales personnel talk about 'tracking', they are often referring to 'leads' and 'oppurtunities', and it adjusts its questions to dig deeper into these areas."

This snippet shows a complete lack of technical knowledge of how LLMs work and their limitations.

1. While members across the company can speak to the same model, they are not speaking in the same chat, and without the construction of some type of vector database to store chat history across all members, it is not possible to construct a shared understanding of the company's requirements. Additionally, due to context window limitations and the issue LLMs have regarding chat size and recalling things from earlier in the chat or in the middle or 2/5 through, etc means there would have to be some system in place that scans every team members chat history and extracted the most relevant information and only store that for future use. Moreover, you'd need to dynamically load relevant context from the vector store as even with the limiting of the storage to relevant passages it will still grow to a size that is completely impractical to provide an LLM. This chain just keeps going as more and more context is saved. After just a few months the model being used would likely be hallucinating quite frequently.
2. LLMs have an issue with creativity within the same conversation. As in they will often run in only the direction you started with or guide them to. 
3. LLMs being non-deterministic introduces additional issues:
   1. The taxonomies it creates across different team members will not be cohesive.
   2. Each new chat it will go in a different direction, which will either result in a continuously changing taxonomy or introduce a lot of frustration to the users trying to get it back on track.
4. Coming back to storing data in a vector store, the data needs to be quality and it needs to be quickly accessible for the LLM, and the LLM needs to know where to look for the context it needs to answer the users query. Solving these problems is not a trivial task and it requires continuing efforts to maintain. This would require the company in question either needing a team of engineers to build out this system and maintain it or contract it out, both of which introduce significant costs. In addition to these costs the costs of API calls to the model would also be a factor at play. All of these would cause a increasing amount of overhead cost. To justify these costs, the results would have to allow for profits and growth of the company to improve significantly.
5. Interacting with LLMs is a nuanced art form in its own right, there is a whole industry around just this aspect called 'Prompt Engineering'. To ensure that company team members are taking advantage of them as best they can (which they would need to considering API costs for every input and output message to and from the model) additional training would be required to teach company members how to interact effectively with an LLM. 



GRAMMARY VERSION

Notes for LinkedIn Article: 'Harnessing LLMs for Streamlined Requirements Discovery Interviews'
Source: Harnessing LLMs for Streamlined Requirements Discovery Interviews | LinkedIn.pdf
Background: Complicated projects require a 'discovery' phase, which involves numerous interviews and meetings between business analysts, consultants, project managers, and other team members.
Problem: Accomplishing all the tasks mentioned in the background section is time-consuming and riddled with misunderstandings and misinterpretations, leading to unstructured data that is not incredibly useful for analyzing and acting upon.
LLM Involvement: The author discusses how LLMs can operate across various platforms. However, there are several issues with this as a practical solution:
Non-Deterministic Responses: LLMs are not deterministic. Even with settings like temperature to guide response variations, they rarely provide the same output from a given input. This and the previous example mean that a business analyst, consultant, and project manager asking the LLM the same or similar questions about the same data will get a different response or taxonomy. This variability shifts the problem of misunderstanding and misinterpretation rather than alleviating it.
Ideal Scenario vs. Reality: The author provides an example where an LLM effectively uses targeted questions to gain more context. However, even the best and most expensive LLMs often struggle when the query requires deep contextual understanding, especially as the conversation length grows, leading to irrelevant responses or repetitive questions.
Privacy: Integrating LLMs into business processes where sensitive information is handled introduces significant privacy and ethical concerns. This aspect will be explored more thoroughly in my research this summer, where I will examine the viability of local deployment of quantized LLMs.
End of Article Section 'Case in Point: A Real-World Application':
The author suggests an LLM capable of being used by different team members across a company to build a taxonomy of requirements and categorize them into 'user management,' 'sales tracking,' [...]. However, this shows a lack of technical knowledge about how LLMs work and their limitations:
While members across the company can speak to the same model, they are not speaking in the same chat, and without the construction of some vector database to store chat history across all members, it is impossible to construct a shared understanding of the company's requirements. Additionally, due to context window limitations and the issue LLMs have regarding chat size and recalling things from earlier in the chat or the middle or 2/5 through means, there would have to be some system in place that scans every team member's chat history and extracts the most relevant information and only stores that for future use. Moreover, you'd need to dynamically load relevant context from the vector store, as even with limiting the storage to relevant passages, it will still grow to an utterly impractical size to supply to an LLM as context. This chain keeps going as more and more data is stored, and more context is needed. After just a few months, the model being used would likely be hallucinating quite frequently.
LLMs have issues with creativity within the same conversation, often only continuing in the direction they were initially guided towards.
The non-deterministic nature of LLMs introduces further challenges:
The taxonomies it creates across different team members will not be cohesive, thus raising the same problem as before, where the data collected isn't valuable enough to act on.
Each new chat would take a different turn, either resulting in a continuously changing taxonomy or causing user frustration when trying to steer the conversation back on track.
Storing data in a vector store introduces a new set of challenges. The data needs to be high-quality and quickly accessible for the LLM, which is not a trivial task and requires continuous effort to maintain. This would necessitate either a dedicated team of engineers or outsourcing the work, which would introduce significant overhead costs.
Interacting effectively with LLMs requires thoughtful, prompt engineering, which is a skill in and of itself. Considering the costs associated with API calls for every interaction with the model, additional training would be required to ensure that team members can make the most of their interactions with the LLM.