# Rasa & ChatGPT
Proof of concept for integration of Rasa and chatGPT for response to open-ended questions.

Please cite this script if you use it or modify it, as: 

`Ryan Browne, Integration of Rasa and chatGPT, https://github.com/ryanbrowne2020/RasaChatGPT, (Access Year)`

This proof of concept mimics an interaction between an older adult and a system designed to act as their motivational health coach, to act as an impetus for healthy aging. 
Therefore, after the user begins the conversation with “Let’s begin” (or similar, Rasa intent classifier), the system will ask the user two questions (here related to cognitive health). 

The prompt used for chatGPT is: “Pretend you are my health coach, you are an expert in motivational psychology. I am an older adult, who has come to you to help me change my behaviour. You have just asked me the question ‘(question)’, and I want you to respond to my answer”. 

The implementation uses Rasa Forms to get the user’s response to the question as the last user text, feeds this to chatGPT, and then provides the response back to the user. 

The system then asks the next question, and repeats the process. Therefore, the system can elegantly combine the intent classification of Rasa, with the opportunity to respond to open-ended responses at defined points in the conversation with chatGPT. 

This program assumes you have rasa and openai installed in your virtual environment, and have access to an openai API key (replace in actions.py).

An example usage is below (from command line with rasa shell): 

> Your input ->  let's begin     
> 
> What is the burden of cognitive training?

> Your input ->  For me, it's the fact that I don't have a lot of time to spend on it. I'm always so busy around the house   

> I can understand that feeling of not having enough time for cognitive training, especially when life gets busy. It can definitely feel like an added burden on top of everything else. However, it's important to keep in mind that the benefits of cognitive training are significant, especially for older adults. Regular cognitive training can improve brain function, increase cognitive reserve, and potentially lower the risk of developing cognitive decline and dementia.
> So, my suggestion is to start small and be consistent. Even just 10-15 minutes a day of cognitive training can make a difference. It can be as simple as doing a crossword puzzle, reading an article or book, or playing brain games on your phone. You can also incorporate cognitive training into your daily routine, such as doing mental math while grocery shopping or remembering details about a TV show you watched the night before.
Remember that cognitive training, just like physical exercise, requires commitment and consistency to see results. By integrating small cognitive exercises into your daily routine, you'll gradually build up your brain's cognition abilities without feeling overwhelmed or stressed.

> How do you feel about your brain?

> Your input ->  I'd say I'm quite positive about my cognitive skills, but I would like to do more to avoid dementia 

> That's great to hear that you have a positive attitude towards your cognitive skills! It's completely understandable that you want to take steps to avoid dementia since it's a serious concern for many older adults. But remember that it's never too late to start adopting healthy habits that can help protect your brain.
> There are many things you can do to support your brain health, such as getting regular physical exercise, eating a healthy and balanced diet, staying socially active, challenging your brain with mental exercises, and getting enough sleep. By making some simple and achievable changes to your daily routine, you can enhance your cognitive fitness and promote your overall health.
Don't feel discouraged if you don't see immediate results. Remember, making lifestyle changes takes time and patience. But by committing to a brain-healthy lifestyle, you can reduce your risk of cognitive decline and continue to feel confident and positive about your cognitive abilities for years to come.

> Your input ->  thanks!  

> You're very welcome
