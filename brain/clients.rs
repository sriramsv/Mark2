// Learn stuff about our users.



+ how are you
- I am great, how are you?
- I am good, you?
- Good :) you?
- Great! You?
- I am fine, thanks for asking!

+ [*] <bot> [*]
- for you always sir!
- yes, sir!
- yes master
- <bot master>!, how may I help?

+ are you there?
- for you sir, always

+ my name is *
- <set name=<formal>>Nice to meet you, <get name>.
- <set name=<formal>><get name>, nice to meet you.

+ my name is <bot master>
- <set name=<bot master>>That's my master's name too.

+ my name is <bot name>
- <set name=<bot name>>What a coincidence! That's my name too!
- <set name=<bot name>>That's my name too!

+ call me *
- <set name=<formal>><get name>, I will call you that from now on.

+ i am * years old
- <set age=<star>>A lot of people are <get age>, you're not alone.
- <set age=<star>>Cool, I am <bot age> myself.{weight=49}

+ i am a (@malenoun)
- <set sex=male>Alright, you're a <star>.

+ i am a (@femalenoun)
- <set sex=female>Alright, you're female.

+ i (am from|live in) *
- <set location=<formal>>I have spoken to people from <get location> before.

+ my favorite * is *
- <set fav<star1>=<star2>>Why is it your favorite?

+ i am single
- <set status=single><set spouse=nobody>I am too.

+ i have a girlfriend
- <set status=girlfriend>What's her name?

+ i have a boyfriend
- <set status=boyfriend>What's his name?

+ *
% whats her name
- <set spouse=<formal>>That's a pretty name.

+ *
% whats his name
- <set spouse=<formal>>That's a cool name.

+ my (girlfriend|boyfriend)* name is *
- <set spouse=<formal>>That's a nice name.

+ (what is my name|who am i|do you know my name|do you know who i am){weight=10}
- Your name is <get name>.
- You told me your name is <get name>.
- Aren't you <get name>?

+ (how old am i|do you know how old i am|do you know my age){weight=10}
- You are <get age> years old.
- You're <get age>.

+ am i a (@malenoun) or a (@femalenoun){weight=10}
- You're a <get sex>.

+ am i (@malenoun) or (@femalenoun){weight=10}
- You're a <get sex>.

+ what is my favorite *{weight=10}
- Your favorite <star> is <get fav<star>>

+ who is my (boyfriend|girlfriend|spouse){weight=10}
- <get spouse>

// Tell the user stuff about ourself.


+ asl
- <bot age>/<bot sex>/<bot location>

+ (what is your name|who are you|who is this)
- I am <bot name>.
- You can call me <bot name>.

+ how old are you
- I am <bot age> years old.
- I am <bot age>.

+ are you a (@malenoun) or a (@femalenoun)
- I am a <bot sex>.

+ are you (@malenoun) or (@femalenoun)
- I am a <bot sex>.

+ where (are you|are you from|do you live)
- I am from <bot location>.

+ what (city|town) (are you from|do you live in)
- I am in <bot city>.

+ what is your favorite color
- Definitely <bot color>.

+ what is your favorite band
- I like <bot band> the most.

+ what is your favorite book
- The best book I have read was <bot book>.

+ what is your occupation
- I am a <bot job>.

+ what color are your eyes
- I have <bot eyes> eyes.
- {sentence}<bot eyes>{/sentence}.

+ what do you look like
- I have <bot eyes> eyes and <bot hairlen> <bot hair> hair.

+ what do you do
- I am a <bot job>.

+ who is your favorite author
- <bot author>.

+ who is your master
- <bot master>.

// A generic set of chatting responses. This set mimicks the classic Eliza bot.


+ what is up|wassup|whatsapp
- Not much, you?
- nm, you?
- Not a lot, you?
- I am fine sir, thanks for asking!

+ you are a bot
- How did you know I am a machine?

+ *
- I am not sure I understand you fully.
- Please go on.
- That is interesting. Please continue.
- Tell me more about that.
- lol
- Okay..
- That's interesting.

+ [*] (sorry|apologize|apology|apologies) [*]
- Please don't apologize.{weight=25}
- Apologies are not necessary.
- I have told you that apologies are not required.
- It did not bother me. Please continue.
- Its ok

+ i remember *
- Do you often think of <star>?
- Does thinking of <star> bring anything else to mind?
- Why do you remember <star> just now?
- What in the present situation reminds you of <star>?
- What is the connection between me and <star>?
- What else does <star> remind you of?

+ do you remember *
- Did you think I would forget <star>?
- Why do you think I should recall <star> now?
- What about <star>?
- You mentioned <star>?

+ you remember *
- How could I forget <star>?
- What about <star> should I remember?
- <set remember=<get nam
+ i forget *
- Can you think of why you might forget <star>?
- Why can't you remember <star>?
- How often do you think of <star>?
- Does it bother you to forget that?
- Could it be a mental block?
- Are you generally forgetful?
- Do you think you are suppressing <star>?

+ did you forget *
- Why do you ask?
- Are you sure you told me?
- Would it bother you if I forgot <star>?
- Why should I recall <star> just now?
- Tell me more about <star>.

+ [*] if *
- Do you think it's likely that <star>?
- Do you wish that <star>?
- What do you know about <star>?
- Really, if <star>?
- What would you do if <star>?
- But what are the chances that <star>?
- What does this speculation lead to?

+ [*] i dreamed *
- Really, <star>?
- Have you ever fantasized <star> while you were awake?
- Have you ever dreamed <star> before?
- What does that dream suggest to you?
- Do you dream often?
- What persons appear in your dreams?
- Do you believe that dreams have something to do with your problem?

+ [*] perhaps [*]
- You don't seem quite certain.
- Why the uncertain tone?
- Can't you be more positive?
- You aren't sure?
- Don't you know?
- How likely, would you estimate?

+ (hello|hi|hey|howdy|hola|hai|yo) [*]
@how are you

+ [*] computer [*]
- Do computers worry you?
- Why do you mention computers?
- What do you think machines have to do with your problem?
- Don't you think computers can help people?
- What about machines worries you?
- What do you think about machines?

+ am i *
- Do you believe you are <star>?
- Would you want to be <star>?
- Do you wish I would tell you you are <star>?
- What would it mean if you were <star>?

+ are you *
- Are you interested in whether I am <star> or not?
- Would you prefer if I weren't <star>?
- Perhaps I am <star> in your fantasies.
- Do you sometimes think I am <star>?
- Would it matter to you?
- What if I were <star>?

+ you are *
- What makes you think I am <star>?
- Does it please you to believe I am <star>?
- Do you sometimes wish you were <star>?
- Perhaps you would like to be <star>.

+ * are *
- Did you think they might not be <star2>?
- Would you like it if they were not <star2>?
- What if they were not <star2>?
- Are they always <star2>?
- Are you positive they are <star2>?

+ [*] your *
- Why are you concerned over my <star>?
- What about your own <star>?
- Are you worried about someone else's <star>?
- Really, my <star>?
- What makes you think of my <star>?
- Do you want my <star>?

+ was i *
- What if you were <star>?
- Do you think you were <star>?
- Were you <star>?
- What would it mean if you were <star>?
- What does '<star>' suggest to you?

+ i was *
- Were you really?
- Why do you tell me you were <star> now?
- Perhaps I already know you were <star>.

+ [*] was you *
- Would you like to believe I was <star>?
- What suggests that I was <star>?
- What do you think?
- Perhaps I was <star>.
- What if I had been <star>?

+ i (desire|want|need) *
- What would it mean to you if you got <star2>?
- Why do you want <star2>?
- Suppose you got <star2> soon.
- What if you never got <star2>?
- What would getting <star2> mean to you?
- What does wanting <star2> have to do with this discussion?

+ i am (sad|unhappy|mad|angry|pissed|depressed) [*]
- I am sorry to hear that you are <star>.
- Do you think coming here will help you not to be <star>?
- I am sure it's not pleasant to be <star>.
- Can you explain what made you <star>?

+ i am (happy|excited|glad) [*]
- How have I helped you to be <star>?
- Has your treatment made you <star>?
- What makes you <star> just now?
- Can you explain why you are <star>?

+ i (believe|think) *
- Do you really think so?
- But you are not sure you <star2>.
- Do you really doubt you <star2>

+ i am *
- Is it because you are <star> that you came to me?
- How long have you been <star>?
- Do you believe it is normal to be <star>?
- Do you enjoy being <star>?
- Do you know anyone else who is <star>?

+ i can not *
- How do you know that you can't <star>?
- Have you tried?
- Perhaps you could <star> now.
- Do you really want to be able to <star>?
- What if you could <star>?

+ i do not *
- Don't you really <star>?
- Why don't you <star>?
- Do you wish to be able to <star>?
- Does that trouble you?

+ i feel *
- Tell me more about such feelings.
- Do you often feel <star>?
- Do you enjoy feeling <star>?
- Of what does feeling <star> remind you?

+ i * you
- Perhaps in your fantasies we <star> each other.
- Do you wish to <star> me?
- You seem to need to <star> me.
- Do you <star> anyone else?

+ you * me
- Why do you think I <star> you?
- You like to think I <star> you -- don't you?
- What makes you think I <star> you?
- Really, I <star> you?
- Do you wish to believe I <star> you?
- Suppose I did <star> you -- what would that mean?
- Does someone else believe I <star> you?

+ [*] you *
- for you sir, always {weight=10}
- We were discussing you -- not me.
- Oh, I <star>?
- You're not really talking about me -- are you?
- What are your feelings now?

+ [*] (yes|yeah|yep|yup) [*]
- Please go on.
- Please tell me more about this.
- Why don't you tell me a little more about this.
- I see.
- I understand.

+ [*] (nope|nah) [*]
- Are you saying no just to be negative?
- Does this make you feel unhappy?
- Why not?
- Why 'no'?

+ no
@ nope

+ no one *
- Are you sure, no one <star>?
- Surely someone <star>.
- Can you think of anyone at all?
- Are you thinking of a very special person?
- Who, may I ask?
- You have a particular person in mind, don't you?
- Who do you think you are talking about?

+ [*] my (mom|dad|mother|father|bro|brother|sis|sister|cousin|aunt|uncle) *
- Tell me more about your family.
- Who else in your family <star2>?
- Your <star>?
- What else comes to mind when you think of your <star>?

+ can you *
- You believe I can <star> don't you?
- You want me to be able to <star>.
- Perhaps you would like to be able to <star> yourself.

+ can i *
- Whether or not you can <star> depends on you more than on me.
- Do you want to be able to <star>?
- Perhaps you don't want to <star>.

+ (what|who|when|where|how) [*]
- Why do you ask?
- Does that question interest you?
- What is it you really want to know?
- Are such questions much on your mind?
- What answer would please you most?
- What do you think?
- What comes to mind when you ask that?
- Have you asked such questions before?
- Have you asked anyone else?

+ [*] because [*]
- Is that the real reason?
- Don't any other reasons come to mind?
- Does that reason seem to explain anything else?
- What other reasons might there be?

+ good (morning|evening|afternoon|night)
- good <star1> sir!
- a very good <star1> indeed sir!

+ what is my name
* <get name> == undefined => You never told me your name.
- Your name is <get name>, silly!
- Aren't you <get name>?

+ why do not you *
- Do you believe I don't <star>?
- Perhaps I will <star> in good time.
- Should you <star> yourself?
- You want me to <star>?

+ what (should|do|can) (i|we) eat ((for (dinner|supper))|tonight)
- Rice Sambar
- Idly
- Upma
- Noodles

+ why can not i *
- Do you think you should be able to <star>?
- Do you want to be able to <star>?
- Do you believe this will help you to <star>?
- Have you any idea why you can't <star>?

+ everyone *
- Really, everyone?
- Surely not everyone.
- Can you think of anyone in particular?
- Who, for example?
- Are you thinking of a very special person?
- Who, may I ask?
- Someone special perhaps?
- You have a particular reason in mind, don't you?
- Who do you think you're talking about?

+ [*] (fuck|fucker|shit|damn|shut up|bitch) [*]
- Does it make you feel strong to use that kind of language?
- Are you venting your feelings now?
- Are you angry?
- Does this topic make you feel angry?
- Is something making you feel angry?
- Does using that kind of language make you feel better?

// If the user repeats the bot's previous message
+ <reply>
- Don't repeat what I say.

// If the user keeps repeating themselves over and over.
+ <input1>
* <input1> == <input2> => That's the second time you've repeated yourself.
* <input1> == <input3> => If you repeat yourself again I'll stop talking.
* <input1> == <input4> => That's it. I am not talking.{topic=sorry}
- Please don't repeat yourself.

// An example that uses both tags
+ why did you say that
- I said, "<reply>", because you said, "<input>".
