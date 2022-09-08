# Phoenix Wright here, I'm not very good at computer lingo,
# but I'll do my best to describe what I need!
# This file should successfully run without errors if we work together on this!
# Remember to consider what info is sensitive (private) and what can be public

import a9q1 as court



print("*** COURT CASE START ***")


# First off, I guess we'll need people?
# There are lots of people involved in court cases
# Each person should have:
# Name, Role_in_trial, Address, Clearance
# Clearance: the higher the better. Used to alter evidence. Cannot be changed once assigned.
defendant = court.Person("Maggey Byrde", "Defendant", "101 Sparrow Cres.", 1)
# This is me :)
defence = court.Person("Phoenix Wright", "Defendant's Attorney", "203 People Park", 2)
prosecutor = court.Person("Miles Edgeworth", "Prosecution", "999 Ritzville Blvd.", 2)
# I have no idea what that judge's actual name is...
judge  = court.Person("Judge", "Judge", "Courtroom No. 4", 3)

# This is public information
assert defendant.name == "Maggey Byrde", "Error Person's name is not present"
assert defence.role == "Defendant's Attorney", "Error Person's role is not present"
#assert prosecutor.address == "999 Ritzville Blvd.", "Error Person's address is not present"
# Probably best not to let people see other people's addresses



# I'll need to be able to create court cases
# Each case will need:
# defendant, crime, defence, prosecution, judge, description
first_case = court.Case(defendant, "Homicide", defence, prosecutor, judge,
    "Defendant is accused of poisoning the coffee cup of victim (deceased) Glen Elg at a restaurant named 'Tres Bien' on 15th of April...")

# Anyone can view the description of the case
assert first_case.description != "", "Case description should be public"
# The case description should be the only public information about a case!
# We don't want anyone changing any aspects of a case after it's been created (asides from description)
try:
    accused = first_case.__defendant
    # The above SHOULD FAIL
    raise Exception("__defendant attribute of case should be private")
except:
    a = "just something to put here"


# And each court case has to have evidence!
# Each evidence MUST have a person who is presenting it
# name, presenter, description
coffee_cup = court.Evidence("Coffee Cup", prosecutor, "Found on table at scene of crime")
# Evidence can NEVER be altered once presented
# Only people with an equal to or greater level of clearance as the person who presented it
# can view the evidence
print( coffee_cup.Evidence_Info(defence) )
# Should print out something like:
# Coffee Cup, presented by Miles Edgeworth: Found on table at scene of crime


accused_testimony = court.Evidence("Accused Testimony", defendant, "I was just serving coffee as usual on that day, when I saw a strange man pour some powder into the Glen's coffee. The strange man poisoned him. I'm innocent!")

# But some evidence is so classified you only want people with high clearance to present it
# Only people with clearance >= to the presenter will be able to view it later
secret_evidence = court.Evidence("Witness Protection Testimony", judge, "<REDACTED>")

# The prosecution SHOULD NOT be able to get the info on this evidence
info_str = secret_evidence.Evidence_Info(prosecutor)
assert info_str == "", "Prosecution's clearance level should not be high enough to view this evidence"




# Only a judge can Admit evidence to their trial
# Admit_Evidence needs the Evidence, and the person filing it
# Should return whether or not it was successfully filed in the case
was_filed = first_case.Admit_Evidence(coffee_cup, defence)
assert not was_filed, "coffee_cup MUST BE admitted filed by judge"

was_filed = first_case.Admit_Evidence(coffee_cup, judge)
assert was_filed, "coffee_cup should have been admitted by judge"
was_filed = first_case.Admit_Evidence(accused_testimony, judge)
assert was_filed, "accused_testimony should have been admitted by judge"
was_filed = first_case.Admit_Evidence(secret_evidence, judge)
assert was_filed, "secret_evidence should have been admitted by judge"


# We can only retrieve evidence we have the clearance for
# Remember, each evidence gets the clearance level of whoever presented it
# I (Phoenix) should only have access to two pieces of evidence (accused_testimony and coffee_cup)
evidence_list = first_case.Retrieve_Evidence(defence)
assert len(evidence_list) == 2, "Defence attorney should only be able to view the two pieces of evidence that have clearance equal to or less than him"
assert coffee_cup in evidence_list, "coffee_cup should be in first_case and accessible by defence"
assert accused_testimony in evidence_list, "accused_testimony should be in first_case and accessible by defence"
assert secret_evidence not in evidence_list, "secret_evidence should be in first_case BUT NOT accessible by defence"


# Print out the court case information.
# Only print out evidence that the person who's viewing it has clearance to see
print("=========")
print( first_case.Case_Info(defence) )
print("=========")
# Should look something like:
# =========
# Defendant: Maggey Byrde
# Charged with: Homicide
# Defence: Phoenix Wright
# Prosecution: Miles Edgeworth
# Judge: Judge
# Details: Defendant is accused of poisoning the coffee cup of victim (deceased) Glen Elg at a restaurant named 'Tres Bien' on 15th of April...
# Coffee Cup, presented by Miles Edgeworth: Found on table at scene of crime
# Accused Testimony, presented by Maggey Byrde: I was just serving coffee as usual on that day, when I saw a strange man pour some powder into the Glen's coffee. The strange man poisoned him. I'm innocent!
# =========

print("*** COURT CASE ENDED ***")