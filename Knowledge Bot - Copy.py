import telegram.ext
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '5421270850:AAGr1klJqXvRlSO8GiQDpI7ekpbdAQQp-nk'

#########################################################################################################################################################################################

def start(update, context, reply_markup=None):
    user = update.message.from_user
    print('•{} used the /start Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'], ))
    keyboard = [[InlineKeyboardButton("Developer", url='https://t.me/SachinduChamika'), InlineKeyboardButton("Channel", url='https://t.me/MasterMindsInc')],
                [InlineKeyboardButton("Help", callback_data='Help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("""
<b>👋Hello {}, I am a telegram bot developed to enhance the knowledge of my users.</b>
""".format(user['first_name']), parse_mode= telegram.ParseMode.HTML, reply_markup=reply_markup)

#########################################################################################################################################################################################

def start_reply(update, context):
    query = update.callback_query
    if query.data == 'Help':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      text="""
<b>Welcome to the Help Menu!</b>

Here you will find a detailed overview of every command.

Send /help to open the detailed Menu.
        """, parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=0)

#########################################################################################################################################################################################

def help(update, context):
    user = update.message.from_user
    print('•{} used the /help Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'], ))
    keyboard = [[InlineKeyboardButton("☎️Ask for Help", url='https://t.me/SachinduChamika')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("""<b>👇Available Commands👇</b>

/start - Start the bot
/fact - Get a random fact
/quote - Get a random quote
/help - Show this guide
/more - See all my hidden Features.""",
                              parse_mode=telegram.ParseMode.HTML, )

#########################################################################################################################################################################################

def notices(update, context):
    user = update.message.from_user
    print('•{} used the /notices Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'],  ))
    update.message.reply_text("""
🤖 <b>Knowledge Bot - V2.1</b>

🥳 <i>Knowledge Bot has been successfully updated to V2.1.</i>

- 52 truths have been added to the /truth command.

<b>NOTE:</b> We will continue adding more updates will come in the upcoming weeks. 🎉

Report Bugs To @SachinduChamika""", parse_mode=telegram.ParseMode.HTML)

#########################################################################################################################################################################################

def details(update, context):
    user = update.message.from_user
    print('•{} used the /details Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'],  ))
    update.message.reply_text("""
<b>Bot Developer</b> - @SachinduChamika
<b>Bot Ownership</b> - @MasterMindsInc
<b>Bot Language</b> - Python
<b>Bot Server</b> - PythonAnywhere
<b>Bot Online Since</b> - 10/10/2022
<b>Last Updated on</b> - 28/10/2022
    """, parse_mode=telegram.ParseMode.HTML)

#########################################################################################################################################################################################

def myinfo(update, context):
    user = update.message.from_user
    print('•{} used the /myinfo Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id']))
    update.message.reply_text("""
    <b>ID:</b> {}
<b>First Name:</b> {}
<b>Last Name:</b> {}
<b>Username:</b> @{}
<b>Language:</b> {}""".format(user['id'], user['first_name'], user['last_name'], user['username'], user['language_code']), parse_mode=telegram.ParseMode.HTML)

#########################################################################################################################################################################################

def generate_truth():
    replies = """
After you've dropped a piece of food, what's the longest time you've left it on the ground?
Are you scared of the dark?
Describe the strangest dream you've ever had. 
Do you cover your eyes during a scary part in a movie?
Do you dance when you’re by yourself?
Do you ever talk to yourself in the mirror?
Do you have an imaginary friend?
Do you have any silly nicknames? 
Do you hide secrets from your bestie?
Do you keep secrets from your mother or father?
Do you still watch cartoons meant for children?
Do you talk in your sleep?
Do you want to change your first name? 
Do you write in a diary?
Does your best friend call you their best friend?
Has your sibling ever embarrassed you?
Have you ever been caught for checking someone’s bag?
Have you ever been late to school?
Have you ever been part of a protest or riot?
Have you ever cheated in an exam?
Have you ever cheated on your Best Friend?
Have you ever cheated your sibling?
Have you ever climbed a tree?
Have you ever cried because you missed your parents so much?
Have you ever got detention or been suspended?
Have you ever got into a fight in school?
Have you ever got less than 75 marks for your favorite subject?
Have you ever lied to a teacher?
Have you ever pretended to be sick to get out of something?
Have you ever spread a false rumor on purpose?
Have you ever stolen anything?
Have you ever stuck chewing gum under a desk?
Have you ever told a lie during a game of Truth or Dare? 
Have you ever told one of your best friend’s secrets, even if you said you wouldn’t?
Have you ever witnessed a crime?
Have you ever worn the same clothes for more than three days?
How many hours would you spend online if you didn't have school or homework?
How many selfies do you take a day?
If someone offered you $1 million to hitting your sibling, would you do it?
If there was no such thing as money, what would you do with your life?
If you could change one thing about your past, what would it be?
If you could go back in time in erase one thing you said or did, what would it be?
If you could go invisible, what would you do?
If you could only hear one song for the rest of your life, what would it be?
If you could put one person in your family on mute for a day, who would it be?
If you could suddenly become invisible, what would you do?
If you had a million dollars, what would you do with all of your money?
If you had a time machine, to which time period would you go?
If you had only 24 hours left to live, what would you do?
If you had only three wishes, what would they be?
If you had the power to fire one teacher, who would it be?
If you had the power to hypnotize someone, who would it be?
If you had to delete one app from your phone, which one would it be?
If you lost one day of your life every time you said a bad word, would you try not to tell it?
If you were reborn, what decade would you want to be born in?
Name a time when you used somebody for your personal gain.
Name the animal that you least like.
Name your favorite movie.
Pick one: money, fame or power.
Tell the craziest thing that you did this year.
What animal most resembles your personality?
What app on your phone do you waste the most time on?
What are the silly nicknames that you have? 
What are you most excited about?
What are you really really good at?
What are you thinking about at the moment?
What are your worst habits?
What children’s movie could you watch over and over again?
What do you think is better: tests or essays?
What is something that no one else knows about you?
What is something you’ve done to try to be ‘cooler’?
What is the funniest dream that you have ever had?
What is the longest you have gone without sleep?
What is the meanest thing you have done?
What is the most childish thing that you still do?
What is the nastiest thing you ever did?
What is the worst advice anyone has ever given you?
What is the worst fact I should know about you?
What is your biggest fear?
What is your favorite sport in the Olympics?
What is your favorite TV show?
What is your special talent?
What is your worst habit?
What was the last thing you searched for in google?
What was the worst score you’ve ever got on a test?
What would be in your web history that you’d be embarrassed if someone saw?
What's the best meal you've ever had?
What's the best meal you've ever had?
What's the last lie you told?
What's the most embarrassing thing that has ever happened to you in public?
What's the most embarrassing thing you've ever done in a school?
What's the weirdest dream you've ever had?
What's your biggest fear about your school?
What's your favorite joke?
What's your favorite music genre?
What's your most awkward experience?
When have you had to walk away in shame?
When was the last time you cried? 
When was the last time you googled your own name?
Where do you want to be right now?
Who is one person you pretend to like, but actually don’t?
Who is the most annoying person you know?
Who is your favorite person and why?
Who is your personal hero?
Who is your worst enemy?
Who were you last in a fight with?
Who would you never ever want to sit next to in school?
Who's the most annoying person in your class?
Why did you cry for the last time?
Will you cry if the person you hate the most dies one day right in front of your eyes?
Would you choose to save 100 people without anyone knowing about it or not save them but have everyone praise you for it?
Would you trade your sibling for a million dollars?
Would you wear your shirt inside out for a whole day if someone paid you $100?
You have to delete five people from your contacts. What are their names?
              """.splitlines()
    r = random.choice(replies).strip()
    return r

#########################################################################################################################################################################################

def truth(update, context):
    user = update.message.from_user
    print('•{} used the /truth Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'],  ))
    update.message.reply_text(generate_truth())

#########################################################################################################################################################################################

def generate_dare():
    replies = """
Act like a pig for another 5 minutes.
Call a random number and ask if they have sushi.
Call a random number and scold with the person who picks up.
Call a random number and sing "Happy Birthday."
Call a random number and tell them a secret.
Call a random number, and when someone picks up ask if you can return a pizza.
Call a random number, and when someone picks up ask them ask if they sell Whoppers.
Call a random number, and when someone picks up ask them if they deliver popcorn.
Call a random number, and when someone picks up, immediately start singing the national anthem.
Call the pizza hut and order 300 sardine pizzas.
Call your best friend and tell him/her that he's/she’s the ugliest person you've ever met.
Call your mom and tell her that you have signed up for an audition on American Idol next year.
Cry like a baby for one minute.
Do a headstand for 2 mins.
Draw on your face with permanent marker.
Eat a pinch of pepper.
Eat as much hot sauce as you can.
Fake cry for till the next round ends.
Get into a debate with a wall.
Get on all fours and act like a dog for another 5 minutes.
Give compliment to five members of this group.
Go 10 minutes without saying the words: but, a, the, or.
Go and send "I hate you" to your best friend.
Go and stab your sibling.
Go and tell your sibling that he/she is the best sibling in the whole world.
Go and tell your sibling that he's/she’s the best sibling in the whole world and that you love him/her so much and that you think you are the luckiest brother/sister to have him/her as your sibling.
Go next door with a measuring cup and ask for a cup of sugar.
Go outside and act like you are crazy until at least three passersby have seen you.
Go outside and pretend you're cutting the grass with an invisible mower.
Go outside the house and dance without music.
Go to WhatsApp and write "How do you spell "WhatsApp"?" as your status and keep it for another 24 hours.
Hold your breath for 10 seconds.
Hold your breath for 15 seconds.
Hop on one foot wherever you have to go for another 5 minutes.
Hop on one leg whenever you need to walk somewhere for another 10 minutes.
Imitate a celebrity and imagine yourself on a red carpet in front of your sibling.
Imitate a witch laugh.
Imitate Superman saving somebody.
Imitate your favorite Pokémon.
Kneel down for another 7 minutes.
Knock on the door of your neighbor, and say, "Welcome to the neighborhood" as if you've never met them before.
Knock on your neighbor's door and tell that you are sick.
Make a round of the house in someone else's shoes.
Make a round of the room on your knees.
Make a silly face and go and show it to your sibling.
Make up a poem about the colour blue.
Make up a rap about koalas and send it to your best friend
Moo like a cow as loud as you can.
Open WhatsApp, go to the account of the first person you see, and send them telling asking how to spell your name.
Open your front door and howl like a wolf for 30 seconds.
Open your front door and loudly tell “Yes, I am crazy!”
Post a really long and serious WhatsApp status confessing your love for chocolate.
Prank call a local restaurant and order one of everything on the menu.
Prank call someone and make them talk for 2 minutes. If they hang up, keep trying.
Pretend that you are in an invisible wheelchair.
Put a WhatsApp status as “I’m coming . . . I’m coming . . . “Then, one minute later, put another one as "I just came.” And keep it for another 24 hours. 
Recite the multiplication table of 2.
Run around the house imitating a monkey.
Run around your house yelling, “I have lice!” for one minute.
Say 'banana’ after everything you say for another 10 minutes.
Say the alphabet in a different language.
Say 'ya heard meh” after everything you say for the next 5 minutes.
Scream to you neighbors: 'Keep it down, dammit!”.
Send a message to your best friend telling “I just found out I am adopted.”
Send a message to your best friend telling how excited you are about eating grass.
Send a screenshot of your google/browser history.
Send a screenshot of your telegram inbox.
Send a screenshot of your YouTube history.
Show your tongue to the sibling.
Sing everything you say for the next 10 minutes.
Sing your favorite song like a rap.
Slap the person nearest to you.
Smell pepper and try not to sneeze.
Spin around 10 times. When you're done, try to walk in a straight line.
Spin around 30 times and try to walk straight.
Stand in the middle of your house and yell at the top of your lungs, “Nooooo! I was adopted!”
Take a selfie with your sibling, and post it as WhatsApp status and type ‘With my beloved sibling. He/She is the best sibling(s) in the world.” And post it for another 24 hours. 
Tell you sibling: “Your majesty I would like to serve you for the rest of the day.”
Text someone “hey.” Every time they respond, say “hey.” Do this 10 times. For the 11th time, reply with “hi.”
The next time your phone rings, answer 'Papa Pepe's Pizza Place, may I take your order...?”.
Turn around yourself 10 times.
Walk around the house like a crab for another 2 minutes.
Walk around the house like a duck.
Whistle your favorite song.
You are now invisible! Steal the first thing that comes to your mind.
You cannot speak until your sibling says your name.
You can't say 'yes' or 'no' for another 3 minutes.
              """.splitlines()
    r = random.choice(replies).strip()
    return r

#########################################################################################################################################################################################

def dare(update, context):
    user = update.message.from_user
    print('•{} used the /dare Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'],  ))
    update.message.reply_text(generate_dare())

#########################################################################################################################################################################################

def generate_fact():
    replies = """
100 million years ago, crocodiles had long legs and could gallop after their prey.
46% of all the Earth’s water is in the Pacific Ocean; Atlantic Ocean 23.9%; Indian Ocean 20.3; Arctic Ocean 3.7%.
5,840 people with pillow related injuries checked into U.S. emergency rooms in 1992.
718 Celsius is the temperature of the hell.
A cat has 32 muscles in each ear.
A crocodile cannot stick its tongue out.
A day on Venus lasts almost 243 Earth days.
A dime has 118 ridges around the edge.
A family of 26 could go to the movies in Mexico City for the price of one in Tokyo.
A flea can accelerate faster than a space shuttle. Fleas are very nimble: during the jump, they are able to reach a speech of 8 centimeters per millisecond.
A full-loaded supertanker traveling at normal speed takes at least 20 minutes to stop.
A raccoon always rinses its food in water before eating, even if it’s clean and doesn’t need it.
About 15% of people in the world are left-handed.
About 800 types of drinking water are sold in USA,
About 85% of the world’s population is right-handed.
Africa and Asia are home to nearly 90 percent of the world's rural population.
Al Capone's business card said he was a used furniture dealer.
Albatross can sleep while flying. It sleeps at 25 miles per hour.
All US Presidents have worn glasses; some just didn't like being seen wearing them in public.
All zebras have a unique pattern of stripes and they recognize each other by it.
An octopus has 3 hearts, 9 brains & blue blood.
Annual growth of WWW traffic is 314,000%
Ants can lift 20 times their own body weight.
Apollo 8 astronauts were the first to celebrate Christmas in space.
Apples are really good for cleaning and strengthening the teeth.
At the time of Google’s creation, its owners were going to sell it for just 1 million dollars. But a buyer was never found.
Bats are the only mammal that can actually fly.
Beavers’ teeth never stop growing, so in order to control their length, the animals have to constantly gnaw on trees.
Between 25% and 33% of the population sneeze when exposed to light.
Blood in human body travels 97,000 kilometers per day.
Brown eggs are healthier than weight eggs.
Cancer is a genetic disease because calls contain mutated, fused genes, or the wrong copies of genes or their components.
Captain cook was the first man to set foot on every continent on Earth except, of course, Antarctica. 
Cats see perfectly well in low light, but they cannot see in total darkness.
Cats should not drink salty water often because it can cause urolithiasis.
Certain species of turtles can cry.
Climate change is causing flowers to change color.
Cold water weighs less than hot water.
Copenhagen is the capital of the kingdom of Denmark and the country’s largest city.
Dentistry is the oldest profession in the world.
Despite their enormous size, hippos are great swimmers and can hold their breath do up two five minutes underwater. When completely submerged, their ears and nostrils fold shut to keep water out.
Did you know that some dinosaurs were as small as a hen.
Did you know that you share your birthday with at least nine million people in the world?
Dolphins sleep with one eye open.
Dr. Jack Kevorkian first patient has Alzheimer's disease.
During a hurricane the wind can blow at 250kmph. It was reported that during typhoon the sustained wind speed reached 346kmph.
Elephant is one of the few mammals that can't jump.
Emus and kangaroos cannot walk backwards, and are on the Australian coat of arms for that reason.
Every 2 minutes we take more photographs than all of humanity in the 19th century.
Every acre of American crops harvested contains 100 pounds of insects.
Every day on planet Earth 250,000 newborn babies are born. Every second approximately 2-3 newborn babies.
Facetious and abstemious contain all the vowels in the correct order, as does arsenious, meaning 'containing arsenic.'
Fictional/horror writer Stephen King sleeps with a nearby light on to calm his fear of the dark.
Four babies are born every second.
French has been the official language of England for over 600 years.
Frogs never drink water.
Giraffes, like all mammals, have only seven cervical vertebrae.
Glaciers and ice sheets hold about 69 percent of the world's freshwater.
Glaciers cover about 10% of the land area and contain about 25 million cubic kilometers of ice.
Half of the world population has never seen snow.
Hawaiian alphabet only has 12 letters: A, E, I, O, U, H, K, L, M, N, P, W
High reading speed helps you to concentrate better and comprehend the text. The comprehension level in traditional reading is 60% while in fast reading it is 80%.
Honey is the only natural food that is made without destroying any kind of life. What about milk you say? A cow has to eat grass to produce milk and grass are living.
Honeybees have a type of hair on their eyes!
Human brain is 80% water, lungs are 83% water and skin is 64% water.
If baby geese are hatched in the absence of their mother, they will follow the first moving object that they see.
If sun stops shining, people will really won’t realize it right away, but only after 8 minutes and 20 seconds.
If two identical twins have children with another pair of identical twins, then their children will genetically be full siblings.
If you yelled for 8 years, 7 months and 6 days, you will have produced enough sound energy to heat one cup of coffee.
In every episode of Seinfeld there is a Superman somewhere.
In France prisoners do not wear uniforms, they dress in regular clothes.
In the average lifetime a person will walk the equivalent of five times around the equator.
In The Empire Strikes Back there is a potato hidden in the asteroid field
In the last 4000 years, no new animals have been domesticated.
In the Mariana Trench an iron ball will sink for more than an hour because its depth is 11km.
Indonesia is home to some of the shortest people in the world.
Ingrown toenails are hereditary.
Intelligent people have more zinc and copper in their hair.
Istanbul is the only city in the world located on two continents
It is estimated that the world’s oceans contain 10 billion tons of gold.
It is illegal to hunt camels in the state of Arizona.
It is proven by a study of the University of Chicago that your decisions will be more rational if you think about them in a foreign language.
It takes 17 muscles to smile and 43 to frown.
It takes 60 to 80 minutes to boil an ostrich egg.
It takes an interaction of 72 muscles to produce human speech.
Japan is the world's most earthquake-prone country.
John Lennon's first girlfriend was named Thelma Pickles.
Larry Lewis ran the 100-yard dash in 17.8 seconds in 1969, thereby setting a new world's record for runners in the 100-years-or-older class. He was 101.
Lightning strikes in the same place with a probability of about 45%.
Los Angeles is the most automobile city in the world with 1.8 million more registered cars than drivers.
Male lions sleep up to 20 hours a day. They spend the rest of their time eating and walking, during which they hunt.
Mammoths lived at the same time as the architects of the Egyptian pyramids, but in different parts of the planet.
Mobile communications and high-speed internet appeared on Everest in 2010.
Moose are excellent swimmers; they swim well and like to stay in the water for a long time.
More people visit France than any other country.
More than 52% of the world's population is under 30 years old.
Morns horns are very sensitive. They sense when insects land on their antlers.
Mosquito repellents don't repel. They hide you. The spray blocks the mosquito's sensors so they don't know you're there.
Mount Everest is bigger now than the last time it was measured.
Mountains on Mars reach heights of 20 to 25 kilometers.
Muhammad is thought to be the most popular name in the world.
NBA superstar Michael Jordan was originally cut from his high school basketball team.
Nearly half of the world's population watched both the 2010 and 2014 FIFA World Cup games.
New creatures have been found in deep-sea volcanoes.
North Korea and Cuba are the only places you can't buy Coca-Cola.
One bee family produces up to 150 kilograms of honey per summer.
Only two countries use purple in their national flags. That is Dominica and Nicaragua.
Ostriches live about 75 years and can reproduce for 50 years.
Peanuts is one of the components of dynamite. Peanut butter can be processed to make glycerin and thus become an ingredient in dynamite.
Pearls melt in vinegar
People 60 years and older make up 12.3% of the global population.
People can’t breathe and swallow at the same time because of the special structure of the larynx.
Pigs can communicate with each other.
Port Louis is the largest city, main port and capital of Mauritius. 
Rhode Island is the only state which the hammer throw is a legal high school sport.
Schools in ancient Rome were attended only by boys. Girls were educated at home.
Scientists have found that goats, like us, have an accent, depending on where they live.
Scissors as they are known today were invented by Leonardo da Vinci.
Scorpions can eat nothing for almost two years.
Since sharks do not have an air bubble, they must swim continuously, otherwise they will drown.
Smart people underestimate themselves, stupid people overestimate themselves.  This is called the Dunning Krueger effect.
South Sudan is the youngest country in the world.
Stress is contagious. If you socialize with depressed people, you will become one of them soon.
Telly Savalas and Louis Armstrong died on their birthdays.
Termites are the main food of anteaters.
The 3 most valuable brand names on earth are Marlboro, Coca-Cola, and Budweiser (in that order).
The alternation of black and white stripes helps zebras with thermoregulation.
The amount of computer Memory required to run WordPerfect for Win95 is 8 times the amount needed aboard the space shuttle.
The ant always falls over on its right side when intoxicated.
The Apple Macintosh had the signatures Of its design team engraved inside its case.
The Barbie doll’s full name is Barbara Millicent Roberts, from Willows, Wisconsin. Her birthday is March 9, 1959, when she was first displayed at the New York Toy Fair.
The Basenji is the only dog that can’t bark.
The Berlin Wall was built in 1961.
The best place in the world to see rainbows is in Hawaii.
The Canary Islands are named after dogs, not birds.
The coldest temperature ever recorded was -144 degrees Fahrenheit.
The common idea that only 10% of the brain is used it not true as it is impossible to determine the actual percentage because of the complexity of the brain.
The earth’s circumference is 24,900 miles.
The Earth's ozone layer will make a full recovery in 50 years. 
The Eiffel Tower gets 15 centimeters taller in summer. When steel is heated, it begins to expand and takes up more volume.
The entire world's population could fit inside Los Angeles
The fasted creature is the peregrine falcon. It can reach speeds of over 322 km/h.
The fastest growing plant in the world is bamboo.
The fastest gust of wind ever recorded on Earth was 253 miles per hour.
The first cultural plantings of carrots appeared in the 10th century. These first cultivated carrots were purple and yellow.
The first paper money appeared in China.
The first product to have a bar code was Wrigley’s gum.
The footprints of humans will remain forever because there is no wind on the moon.
The great lakes are the largest group of freshwater lakes in the world.  Their total area is 94,230 square miles which is more than the states of New York, New Jersey and Connecticut combined.
The growth rate of pearls is about 0.1mm per year.
The heart of a blue whale is so huge that a person can easily swim through the arteries. Its heart is size of a small car and weights 600-700kg.
The heart of the shrimp is in the head, in the back of the head.
The hippos use self-made sub cream to keep from getting sunburned. Their skin exudes a thick red substance, which is released in the open sun.
The hottest chili pepper in the world is so hot it could kill you.
The human heart creates enough pressure to squirt blood 30ft.
The inscription on the tomb of the great Russian commander Alexander Vasilievich Surorov is very short, just three words: “Here lies Surorov”.
The inventors of paper are the Chinese.
The KGB is headquartered at No. 2 Felix Dzerzhinsky Square, Moscow
The largest chamber in the world is Sarawak in Gunung Mulu National Park in Malaysia. It has a 700m length, 70m height and average width of 300m.
The largest hailstorm recorded by humans fell on the site of Coffeyville Kansas in USA. It weighed almost 700 grams.
The largest natural pearl is the Laozi pearl. Its weight is 6.37kg.
The largest pyramid in the world was built in Mexico and is called Cholula.
The length of the intestine of an adult is about 12 meters.
The longest jellyfish measured by humans was about 50 meters long which is almost the length of a soccer field.
The longest one-syllable word in the English language is 'screeched.'
The longest place name on the planet is 85 letters long.
The mantis us the only insect that can turn its head. It has its head on its neck and it turns it in different directions just like humans.
The most expensive coin in the world was sold for more than $7 million.
The octopus has three hearts, nine brains, eight tentacles and blue blood.
The oldest flag which is found on Iranian territory was made mainly of copper.
The only part of the body that has no blood supply is the cornea of the eye. It gets oxygen directly from the air.
The ostrich has the largest eyes among birds. The eyes of an ostrich are the largest in the world among birds and together weight more than a brain.
The Paris Agreement on climate change was signed by the largest number of countries ever in one day.
The reticulated python is the longest snake in the world. Its length is 9 meters.
The Russian alphabet has six vowel sounds.
The San Francisco Cable cars are the only mobile National Monuments.
The shortest war in history lasted 38 minutes. It was a war between Great Britain and Zanzibar. IT began and ended on August 27, 1896.
The surface area of a human lung is about the same as a tennis court.  If you lay out all the lung bubbles in one plane, their area is more than 150 square meters.
The tallest TV tower in the world is the Tokyo Skytree, 634 meters tall.
The Tokyo Zoo closes for two months every year so the animals can get a break from visitors.
The total length of all blood vessels is 100,00km.
The typical laboratory mouse runs 2.5 miles per night on its treadmill.
The unicorn is the national symbol of Scotland. A pair of unicorns are the holders of the shield in the coat of arms of Scotland.
The United States ranks first in the world in terms of the number of prisoners which is more than 2,000,000 people.
The widest street in the world is monumental axis street located in the city of Brasilia with a width of 250 meters.
The world's largest man-made oyster reef was created in Maryland.
The world's most densely populated island is the size of two soccer fields.
The world's quietest room is located at Microsoft's headquarters in Washington state.
There are fossilized plants in Greenland under 1.4 km of ice.
There are more French restaurants in New York City than in Paris.
There are more than 100 types of rhinoviruses that causes runny nose are known.
There are more than 24 time zones around the world.
There are more than 7 million millionaires in the world.
There are more twins now than ever before.
There are over 4 billion people worldwide using the internet now. And the number of these people are growing every year by about 4%.
There is a restaurant in Stockholm that only offers all-garlic products. They even have a garlic cheesecake.
There were always 56 curls in Shirley Temple's hair.
There's a systematic lull in conversation every 7 minutes.
There's only one country in the world that doesn't use the metric system.
Walt Disney originally suggested to use the name Mortimer Mouse instead of Mickey Mouse.
Water in the Dead Sea is 7 to 8 times saltier than in the oceans.
Whale songs can be used to map out the ocean floor.
Who’s that playing the piano on the 'Mad About You' theme? Paul Reiser himself.
Women in France did not have the right to vote in elections until 29th of April, 1945.
Worms have 5 pairs of pulsating tubes, which are essentially hearts.
Yogurt got its name from the Turkish word which means long life.
You blink over 10,000,000 times a year.
You burn more calories sleeping than you do watching TV.
You spend 7 years of your life in the bathroom.
Your fingers swell because of narrowing of blood vessels.
              """.splitlines()
    r = random.choice(replies).strip()
    return r

#########################################################################################################################################################################################

def fact(update, context):
    user = update.message.from_user
    print('•{} used the /fact Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'],  ))
    update.message.reply_text(generate_fact())

#########################################################################################################################################################################################

def generate_quote():
    replies = """
3 Tips to Staying Positive:  Look back and be grateful… Look ahead and be hopeful… Look around and be helpful…
6+3=9 but so does 5+4. The way you do things isn't always the only way to do them. Respect other people's way of thinking.
A champion is someone who gets up when he can't.
A foreign language is like a frail, delicate muscle. If you don't use it, it weakens.
A lion never roars after a kill.
A seed grows with no sound but a tree falls with huge noise. Destruction has noise, but creation is quite. This is the power of silence... Grow silently.
An idiot with plan can beat a genius without plan.
Be happy. Be who you want to be. If others don't like it, then let them be. Happiness is a choice. Life isn't about pleasing everybody.
Be like a tree. Stay grounded. Connect with your roots. Turn over a new leaf. Bend before you break. Enjoy your unique beauty. Keep growing.
Be patient, sometimes you have to go through the worst to get to the best.
Be very careful with people whose words do not match their actions.
Because there is a law such as gravity, the universe can and will create itself from nothing.
Chase your dreams before it gets steered by others.
Clean out a carrier you mind and creativity will instantly fill it.
Confidence isn't walking into a room thinking you are better than everyone, it's walking in not having to compare yourself to anyone at all.
Creativity is allowing yourself to make mistakes. Art is knowing which ones to keep.
Do not follow the majority, follow the right way.
Don't discuss your personal life or close, funny habits of yours to anyone. One day they will make fun out of it Infront of others and you will not have a single penny idea of that...
Don't expect too much. It's always better to feel surprised than to feel disappointed.
Don't feel bad if people remember you only when they need you. Feel privileged that you are like a candle that comes to their mind when there is darkness.
Don't stop when you are tired. Stop when you are done.
Don't wait for the opportunity, create it.
Don't waste your time with explanation people only hear what they want to hear.
Enjoy the little things, for one day you may look back and realize they were the big things.
Every artist dips his brush in his soul and paints his own nature into his paintings.
Everything is beautiful, but not everyone can see it.
Falling down is how we grow. Staying down is how we die. Always get back up.
Focus believe and achieve.
Forget past mistakes. Forget failures. Forget everything except what you’re going to do now and do it.
God doesn't give the hardest battles to his toughest soldiers; he creates the toughest soldiers through life's hardest battles.
Hard work is directly proportional to success.
Hope - Hold on Pain Ends.
However difficult life may seem, there is always something you can do and succeed at.  It matters that you don't give up.
Hurting someone can be as easy as throwing a stone in a sea, but do you have any idea how deep that stone can go?
I am not what happened to me, I am what I choose to become.
I am strong because I know I've been weak. I am beautiful because I know my flaws. I am fearless because I've been afraid. I am wise because I've been foolish. I can laugh because I've known sadness... We all should have this mentality.
I don't care who is doing better than me, I'm doing better than I was last year.
I hope you will never see yourself as unworthy just because you couldn't become what someone else wanted you to be.
If aliens visit us, the outcome would be much as when Columbus landed in America, which didn't turn out well for the Native Americans.
If an egg is broken by an outside force, life ends. But if it’s broken by an inside force, life begins. Great things always begin form the inside.
If God is making you wait, then be prepared to receive more than you asked for.
If God is not answering you, remember teacher does not speak during test.
If words control you, then anyone can control you.
If you don't ask, you don't get.
If you want to be original, be ready to be copied.
Inspiration exists but it has to find you working.
Intelligence is the ability to change.
It's human nature to stretch, to go, to see, to understand. Exploration is not a choice. Really, it's an imperative.
It's time to surprise all those who doubt you.
Learn from your past and be better because of your past, but don't cry about your past. Life is full of pain. Let the pain sharpen you, but don't hold on to it. Don't be bitter.
Life has no remote. Get up and change it yourself.
Life is like a notebook. Two pages are already written by God. First page is birth and last page is death. Center page are empty. Fill them with smile and memories.
Life is short. Time is fast. No replay, no rewind. So, enjoy every moment as it comes
Life is the most difficult exam. Many people fail because they try to copy others, not realizing that everyone has a difficult question paper.
Like the moon, we must go through phases of emptiness to feel full again.
Magical things happen when you surrounded yourself with people with beautiful hearts.
Mistakes are proof that you are trying.
Musicians must make music, artists must paint, poets must write if they are to be ultimately at peace with themselves. What human beings can be, they must be. They must be true to their own nature. This needs we may call self-actualization.
My silence doesn't mean I agree with you, it means your level of stupidity left me speechless.
Never be afraid to start over again. This time you won't be starting from scratch, you'll be starting from Experience.
Never feel sad on losing anything in life because whenever a tree loses its leaf a new leaf is ready to take its place.
No matter how strong of a person you are, there’s always someone who can make you weak.
No matter what, expect the unexpected. And whenever possible, be the unexpected.
No one in the world is pure and perfect. If you avoid people for their mistakes, you will be alone in this world. So, judge less and love more.
Nobody is coming to save you. Get up and be your own hero.
One bad chapter doesn't mean your story is over, turn the page.
Opportunities do not happen, you create them.
Patience is power.
Patience, persistence and perspiration make and unbeatable combination for success.
People say, find good people and leave the bad ones. But I say, find the good in people and ignore the bad in them. Because no one is perfect.
Respect your choices, stop lowering your standards. They will push you, test you and tease you. Stay rooted to who you truly are.
Run after your dreams like a lion runs after a deer.
Satisfy your soul not the society.
Science is like magic but real.
Smile hides so many secrets.
Smiling is the best way to face every problem, to crush every fear, to hide every pain.
Some days I am the sun, other days I am the rain. Without either, the garden will not grow.
Some people just act like they are trying to help you...
Some people will only love you as much as they can use you. Their loyalty ends where the benefit stops.
Sometimes it takes 10 years to get that one year that will change your life. So, keep going.
Sometimes the smallest step in the right direction ends up being the biggest step of your life.
Sometimes you don't get what you want because you deserve better.
Sometimes you have to go up really high to understand how small you really are.
Space is an inspirational concept that allows you to dream big.
Strong people fall down... they don't stay down. Strong people break... they don't stay broken. They mend. They piece themselves back together and they come back stronger. Strong people feel like quitting... but they don't. Strong people aren't free from challenges. They're strong because of challenges.
Study now. Be proud later.
Sunsets are proof that endings can be beautiful too.
Talk too much and people will think you're a fool. Stay silent, and you'll make them curious.
The aim of art is not to represent the outward appearance of things but their inward significance.
The artist sees what others only catch a glimpse of.
The expert in anything was once a beginner.
The greatest enemy of knowledge is not ignorance it is illusion of knowledge.
The hardest walk you can make is alone. But it's the walk that will make you stronger.
The man who does more than he is paid for will soon be paid for more than he does.
The moment you start acting like life is a blessing, it starts feeling like one.
The only time you should look back in life is to see how far you've come.
There are no limits to success.
There's always light after dark.
To accomplish great things, we must not only act, but also dream, not only plan, but also believe.
To improve your mood, exercise. To think more clearly, meditate. To understand the world, read. To understand yourself, write. To help people, help yourself. To learn faster, have fun.
TRUST- It takes years to build, seconds to break and forever to repair.
Trying leaI don't care who is doing better than me, I'm doing better than I was last year.d you to mistakes. Mistakes will lead you to the right way.
Unsuccessful people make decisions based on their current situations, Successful people make decisions based on where they want to be.
Vision without action is a daydream.
We don't know the true value of a moment, until it becomes a memory.
Weak people revenge. Strong people forgive. Intelligent people Ignore.
We'll all die, the goal isn't to live forever, it's to create something that will.
What makes you happy that doesn't need approval from anyone else.
When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.
When you need motivation, remind yourself the progress you've already made, recognizing what you have overcome will help you realize what you can overcome.
Without imperfection, you or I would not exist.
Work hard in silence. Let success make the noise.
Work hard. Stay disciplined and be patient. Your time will come.
Yesterday you said "I'll do it tomorrow".
You have to fight through some bad days to earn the best days to your life.
Your struggle may go unnoticed but your results won't.
              """.splitlines()
    r = random.choice(replies).strip()
    return r

#########################################################################################################################################################################################

def quote(update, context):
    user = update.message.from_user
    print('•{} used the /quote Command. His/Her Username is @{} and User ID is {}'.format(user['first_name'], user['username'], user['id'],  ))
    update.message.reply_text(generate_quote())

#########################################################################################################################################################################################

def handle_message(update, context):
    update.message.reply_text("Please train the bot and upload a picture")

#########################################################################################################################################################################################

def handle_photo(update, context):
    pass

#########################################################################################################################################################################################

updater = telegram.ext.Updater('5421270850:AAGr1klJqXvRlSO8GiQDpI7ekpbdAQQp-nk', use_context=True)
dp = updater.dispatcher

dp.add_handler(telegram.ext.CommandHandler("start", start))
dp.add_handler(telegram.ext.CallbackQueryHandler(start_reply))
dp.add_handler(telegram.ext.CommandHandler("help", help))
dp.add_handler(telegram.ext.CommandHandler("notices", notices))
dp.add_handler(telegram.ext.CommandHandler("fact", fact))
dp.add_handler(telegram.ext.CommandHandler("quote", quote))
dp.add_handler(telegram.ext.CommandHandler("details", details))
dp.add_handler(telegram.ext.CommandHandler("truth", truth))
dp.add_handler(telegram.ext.CommandHandler("dare", dare))
dp.add_handler(telegram.ext.CommandHandler("myinfo", myinfo))
updater.start_polling()
updater.idle()