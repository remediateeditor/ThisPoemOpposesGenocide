import random
from random import choice				#######       this poem opposes genocide        #######
def memory(year):
	random.seed(year)
	while(1): 																	#yesterday i needed three things 
		politeness = choice(["generous", "civil", "neutral?!", "angry", "sad"]) #to get through the day: a new pillowcase,
		if(politeness != "generous"): 											#a stamp, a giant cappuccino
			break																#i wield need without metaphor,
	return politeness 															#as if i really mean it
																				#it is good to send birthday cards,
print("What is your name?")														#nice to slurp foam, leaking like static
name = input() + "\n"															
BritsOut = ["BRITISH", "UK", "BRIT", "SCOTTISH", "WELSH", "NORTHERN IRISH"]		
USAUSA = ["AMERICAN", "USA", "US", "UNITED STATES OF AMERICA", "THE STATES", "KISSINGER'S"] 
geo = 2 																		
while(1): 																		
	print("Which spellings match your politicians' expectations: British or American?") 
	spelling = input().upper()													#i set aside my phone and the news is
	for x in enumerate(BritsOut):												#very far away
		if(spelling == x[1]):													
			geo = 0 															#how do you regulate your emotions?
			break																#are you taking baths? aromatherapy?																		
	for x in enumerate(USAUSA):													#my sister grows tomatoes and squash
		if(spelling == x[1]):												
			geo = 1																#personal tragedy is supposed to make you
			break																#sympathetic, so you're meant to feel bad
	if(geo <= 1): ##no spelling set 											#for me if i talk about my scars, mea culpa,
		break																	#you should hold open doors, walk slower,
	else:																		#or at least chitchat while we wait for
		print("Sorry I did not understand. Please try again.")					#the lift — nice weather, finally,
print("What is the name of the place where you live?\nBe specific.")				#some rain, we needed it, 
community = input().title()																#after you, please —

print("\nPlease use a government website to find your representative's contact info.\n") 
#Find your representative's email: house.gov/representatives/find-your-representative 
#or members.parliament.uk/members/commons
print("How would you like to address your politician?")   #you cannot pretend 
print("For example, 'Lord Hain' or 'Congresswoman Tlaib'")#that you'll do it later
CivilServant = input()
print("\n\033[1mTo:\033[0m [Figure it Out]\n")
print("\033[1mSubject:\033[0m", end=" ")
mood = memory(1948)																#keep photo albums to protect
match mood:																		#the good times, they've all been good
	case "civil" | "neutral?!":													#so far probably — or at least simpler
		print("Constituent Concerned About Gaza\n")								
	case "angry":					
		print("Gaza — How Many Deaths Until You Act?\n")
	case "sad":																	#preserve peaches to remember the sun
		print("They are starving — Constituent Pleading for Action\n")			#practice your deep breathing
																				
print("\033[1mBody:\033[0m\n")													
print("Dear " + CivilServant + ",\n")
intro = "I am a constituent of your district in " + community + " and am writing to you today in order to "
mood = memory(1987)
match mood:
	case "civil":
		intro += "entreat you to "												#oh please
	case "neutral?!":
		intro += "request that you "												#give me a break
	case "angry":
		intro += "demand that you "														#cry me a river
	case "sad":
		intro += "beg you to "																#what do you care
intro += ("take action regarding the humanitarian crisis in Gaza. "				
	"The ongoing bombings, assassinations of journalists, starvation, and blockade of humanitarian aid are a crisis "
	"that cannot be ignored. We must act now.\n")
print(intro)

clarify = "I’d hope you would listen to a concerned constituent, but you don’t have to take my word for it. "
if(geo == 0):
	clarify += ("The 18 July 2025 report from the Foreign Affairs Committee on The Israeli-Palestinian Conflict states that"
		" ‘The UK’s actions in this conflict, and in the years preceding, have often been too little, too late.’ "
		"The report includes calls for a ‘redoubling of effort’ towards immediate ceasefire supplemented "
		"with explicit measures to support humanitarian efforts before, during, and after the ceasefire is implemented.\n")
elif (geo == 1):
	clarify += ( "Doctors without Borders has repeatedly called for Israel to restore the ceasefire "
		"in order to provide necessary medical aid to injured civilians in Gaza. This war is impacting the most vulnerable."
		" On September 3, 2025, the UN Committee on the Rights of Persons with Disabilities reported that of the over "
		"40,000 children injured in Gaza, more than half of them have been left disabled, profoundly impacting their life"
		" and making it difficult for them to comply with Israel's frequent relocation orders.\n")
else:
	clarify += ("You should overcome your narcisistic apathy and decide whether you want your children to be able to "
		"look you in the eyes when they grow up and realize that your inaction in the face of overwhelming evidence "
		"let death and destruction reign unchecked. You were supposed to have learned from the past and be better.\n")
print(clarify)

def mourn(capacity):															#how do you mourn at scale?
	x = 0 																		#badly: my black clothes are all dirty
	while(x < capacity):      													#this grief needs letting out at the seams
		print(infants[x], end=", ")
		x += 1 																	#here are the names of one hundred infants
	print("and many others under the age of one.\n")							#who should be fat and happy
																				#there are hundreds more

infants = ["Adam Hana", "Izz Sweilem", "Yazan Shaafout", "Dalaa Khella", "Aseed Abu Hamad",
	"Celine Al-Yaziji", "Bilal Jnena", "Reem Abu Seido", "Abdel Hathut", "Alma Al-Zahrani",
	"Hayla Abu Tuaima", "Maria Rayan", "Norsin Faliona", "Abdullah Kul", "Louay Al-Ajrami",
	"Sham Al-Ghurabli", "Teem Salman", "Asali Daghmash", "Sara Al-Ilmi", "Mohammed Baroud",
	"Rafiq Al-Kahlout", "Bakr Tafesh", "Hamza Al-Nabih", "Ahmed Nasiyo", "Wafaa Al-Zmaili",
	"Ibrahim Shalayel", "Jinan Al-Ghurra", "Muath Saad", "Bisan Qandil", "Ahmed Abu Daqqa",
	"Malak Awad Allah", "Sharif Al-Hindi", "Yazan Radi", "Zain Al-Zard", "Ibrahim Al-Qara",
	"Sayyaf Abu Salah", "Hamed Abu Khati", "Dalal Ouda", "Muath Miqdad", "Eileen Al-Assar",
	"Mohammed Darwish", "Muath Al-Bayouk", "Sama Muqat", "Wesam Wishah", "Siwar Abu Atiwi",
	"Ibrahim Al-Shaer", "Yousef Abu Nimr", "Rital Nasr", "Sham Muharib", "Banan Al-Saloul",
	"Mira Abu Muammar", "Samir Al-Zinati", "Amal Alyan", "Raed Al-Dawawsa", "Nawal Ghaben",
	"Abdullah Al-Ghaz", "Mohammed Salama", "Asia Breis", "Salim Al-Zinati", "Tamer Mohsen",
	"Mohammed Al-Ghaz", "Yahya Al-Sinwar", "Rafat Anan", "Ahmed Al-Shrafi", "Bayan Ghanim",
	"Malak Al-Fayoumi", "Mohammed Khella", "Hind Ajour", "Bisan Al-Malaha", "Fatima Daher",
	"Yousef Al-Ghafri", "Mariam Al-Sousi", "Hour Habib", "Hour Al-Madhoun", "Tariq Kuhail",
	"Mohammed Shaaban", "Mai Al-Dalo", "Al-Amira Zarab", "Hanan Al-Ashqar", "Salman Manun",
	"Shorouq Al-Atout", "Adam Ashour", "Hamza Abu Jabr", "Fadl Abu Hasira", "Atef Darwish", 
	"Alaa Al-Maghribi", "Yamen Muqat", "Yaqeen Isbelta", "Amir Al-Shobaki", "Suhaib Eliwa",
	"Asaad Al-Fayoumi", "Kanari Aqel", "Asir Abu Salah", "Talaat Shamlakh", "Wateen Jaber", 
	"Lynn Abu Khattab", "Ziyad Habib", "Alma Abu Ayada", "Mahmoud Al-Baba", "Omar Sharaf",] 					
																				
print("I urge you to use your voice and your vote as our elected representative to:")
print("\t• Support the protection and provision of humanitarian aid in Gaza without bureaucratic", end=" ") 
print("or military barriers to prevent further loss of life.", end="")			#what are you going to do with that?
if(geo == 1):																	#there are hundreds more-
	print(", and support House Resolution 473.")
else:
	print("")
print("\t• Place diplomatic and political pressure on Israel to resume the ceasefire agreement", end=" ") 
print("and issue work visas to humanitarian workers.")
mood = memory(2000)																#i set aside my phone and the news is
match mood:																		#very far away
	case "civil" | "neutral?!":
		print("\t• Press your Israeli counterparts to restore access for journalists to report from Gaza,", end="")
		print(" the West Bank, and Israel, and lift the ban on media outlets that the Israeli Government", end="")
		print("does not agree with.")
	case "angry":
		if(geo == 0):
			print("\t• Lessen the barriers to entry for the forty students from Gaza who have funded places at", end=" ")
			print("British Universities and speak up regarding the Israeli restrictions preventing their departure", end="")
			print(" from the region to take up their studies.")
			print("\t• Support admitted students without funding and their", end=" ")
			print("swift departure from the region so that they can begin their studies safely should funding be secured.")
		if(geo == 1):
			print("\t• Do not support legislation such as the unconstitutional Israel Anti-Boycott Act which", end=" ")
			print("attempts to criminalize constitutionally protected free speech.")
	case "sad":
		print("\t• Urgently support the evacuation of children from Gaza to receive medical aid.", end=" ")
		print("• Remember the dead: ", end="")
		mourn(20) #hold them

conclusion = ("\nYour action is needed now to prevent further loss of life and destruction. Please act with haste. " 
	"Hindsight is 20/20 and history will remember your actions. " 
	"Furthermore, I will be voting in the next election entirely based on your actions on this issue now.\n\n")
mood = memory(2023)
match mood:
	case "civil" | "neutral?!":
		conclusion += "Sincerely,\n" 											#(this will never be read)
	case "angry":																#this is probably a waste of time
		conclusion += "With Deep Frustration,\n"								#but so is everything, id imagine
	case "sad":																	#except growing tomatoes and squash
		conclusion += "Yours in Grief,\n"										#and perhaps holding you
conclusion += name																#as the sky opens up
print(conclusion)																#the clouds painted on fresh each morning
		






