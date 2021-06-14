
import random
import time
def unitedKingdomElection():
    ##partyRegionalVote = {"Conservative":, "Labour":, "Scottish":, "Liberals":, "Democratic Unionists":, "Sinn Fein":, "Plaid Cymru":, "Social Democratics":, "Unionists":, "Greens":, "Scottish Greens":, "Independance":, "Alliance Party":, "Northern Irish Greens":, "Traditional Unionists":, "People B Profit":, "Welsh":, "Abolish Welsh":}

    northLondonP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    southLondonP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    southEastP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    southP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    westCountryP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    peninsulaP = ["Conservatives", "Labour", "Liberals", "Greens", "Indpendance"]
    angliaP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    southMidlandsP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    welshBorderP = ["Conservatives", "Labour", "Liberals", "Plaid Cymru", "Greens", "Independance", "Welsh", "Abolish Welsh"]
    westMidlandsP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    eastMidlandsP = ["Conservatives", "Labour", "Liberals", "Greens", "Indpendance"]
    yorkshireP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    lancashireP = ["Conservatives", "Labour", "Liberals", "Greens", "Independance"]
    northP = ["Conservatives", "Labour", "Scottish", "Liberals", "Greens", "Scottish Greens", "Independance"]
    southWalesP = ["Conservatives", "Labour", "Liberals", "Plaid Cymru", "Greens", "Independance", "Welsh", "Abolish Welsh"]
    northWalesP = ["Conservatives", "Labour", "Liberals", "Plaid Cymru", "Greens", "Independance", "Welsh", "Abolish Welsh"]
    scottishLowlandsP = ["Conservatives", "Labour", "Scottish", "Liberals", "Greens", "Scottish Greens", "Independance"]
    scottishHighlandsP = ["Conservatives", "Labour", "Scottish", "Liberals", "Greens", "Scottish Greens", "Independance"]
    northernIrelandP = ["Conservatives", "Labour", "Liberals", "Democratic Unionists", "Sinn Fein", "Social Democratics", "Unionists", "Greens", "Independance", "Alliance Party", "Northern Irish Greens", "Traditional Unionists", "People B Profit"]

    def currentVoteResults(voteresults):
        parties = {"Conservatives":voteresults.count("Conservatives"), "Labour":voteresults.count("Labour"), "Scottish":voteresults.count("Scottish"), "Liberals":voteresults.count("Liberals"), "Democratic Unionists":voteresults.count("Democratic Unionists"), "Sinn Fein":voteresults.count("Sinn Fein"), "Plaid Cymru":voteresults.count("Plaid Cymru"), "Social Democratics":voteresults.count("Social Democratics"), "Unionists":voteresults.count("Unionists"), "Greens":voteresults.count("Greens"), "Scottish Greens":voteresults.count("Scottish Greens"), "Independance":voteresults.count("Independance"), "Alliance Party":voteresults.count("Alliance Party"), "Northern Irish Greens":voteresults.count("Northern Irish Greens"), "Traditional Unionists":voteresults.count("Traditional Unionists"), "People B Profit":voteresults.count("People B Profit"), "Welsh":voteresults.count("Welsh"), "Abolish Welsh":voteresults.count("Abolish Welsh"), "N/A":voteresults.count("N/A")}
        winner = max(parties, key = parties.get)
        time.sleep(5)
        if parties[winner] < 5:
            print("The current leader is", winner, "with", parties[winner], "seats. All is yet to be decided.")
        elif parties[winner] > 4:
            print("The current leader is", winner, "with", parties[winner], "seats. They will most likely be the winners.")
        elif parties[winner] >= 10:
            print("The", winner, "have won the election with", parties[winner], "seats. No-one else can catch them!")
    voteresults = []
    class Region():
        def __init__(self, voters, parties, name):
            self.voter = voters
            self.parties = parties
            self.votes = []
            self.name = name
            self.counted = []
            self.highest = 0
            self.winner = -1
            self.tie = []
            print(self.name)
        def vote(self):
            for i in range(0, self.voter):
                self.voting = random.choice(self.parties)
                self.votes.append(self.voting)
            for x in range(len(self.parties)):
                partyname = self.votes.count(self.parties[x])
    ##            print(self.name, "have made", str(partyname), "votes for the", self.parties[x])
                self.counted.append(partyname)
            for i in range(len(self.counted)):
                if self.counted[i] > self.highest:
                    self.highest = self.counted[i]
                    self.winner = i
                elif self.counted[i] == self.highest:
                    self.tie.append(self.parties[i])
            if len(self.tie) == 0:
                print("The winner of the", self.name, "seat is the", self.parties[self.winner], "party.")
                self.winningparty = self.parties[self.winner]
            elif len(self.tie) > 0:
                print("There is no winner here.")
                self.tie.append(self.parties[self.winner])
                self.winningparty = "N/A"
        def declaring_victory(self, voteresults):
            if self.winningparty == "N/A":
                self.winningparty = random.choice(self.tie)
                print("By random choice, the winner of the", self.name, "seat is the", self.winningparty, "party.")
            voteresults.append(self.winningparty)


    northLondon = Region(13, northLondonP, "North London")
    northLondon.vote()
    northLondon.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    southLondon = Region(12, southLondonP, "South London")
    southLondon.vote()
    southLondon.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    southEast = Region(10, southEastP, "South East")
    southEast.vote()
    southEast.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    south = Region(8, southP, "South")
    south.vote()
    south.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    westCountry = Region(5, westCountryP, "West Country")
    westCountry.vote()
    westCountry.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    peninsula = Region(2, peninsulaP, "Peninsula")
    peninsula.vote()
    peninsula.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    anglia = Region(6, angliaP, "Anglia")
    anglia.vote()
    anglia.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    southMidlands = Region(7, southMidlandsP, "South Midlands")
    southMidlands.vote()
    southMidlands.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    welshBorder = Region(3, welshBorderP, "Welsh Border")
    welshBorder.vote()
    welshBorder.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    westMidlands = Region(12,  westMidlandsP, "West Midlands")
    westMidlands.vote()
    westMidlands.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    eastMidlands = Region(8, eastMidlandsP, "East Midlands")
    eastMidlands.vote()
    eastMidlands.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    yorkshire = Region(9, yorkshireP, "Yorkshire")
    yorkshire.vote()
    yorkshire.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    lancashire = Region(12, lancashireP, "Lancashire")
    lancashire.vote()
    lancashire.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    north = Region(4, northP, "North")
    north.vote()
    north.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    southWales = Region(11, southWalesP, "South Wales")
    southWales.vote()
    southWales.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    northWales = Region(9, northWalesP, "North Wales")
    northWales.vote()
    northWales.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    scottishLowlands = Region(12, scottishLowlandsP, "Scottish Lowlands")
    scottishLowlands.vote()
    scottishLowlands.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    scottishHighlands = Region(3, scottishHighlandsP, "Scottish Highlands")
    scottishHighlands.vote()
    scottishHighlands.declaring_victory(voteresults)
    currentVoteResults(voteresults)
    time.sleep(2)
    print()
    northernIreland = Region(4, northernIrelandP, "Northern Ireland")
    northernIreland.vote()
    northernIreland.declaring_victory(voteresults)
    time.sleep(2)
    print()

    print()

    parties = {"Conservatives":voteresults.count("Conservatives"), "Labour":voteresults.count("Labour"), "Scottish":voteresults.count("Scottish"), "Liberals":voteresults.count("Liberals"), "Democratic Unionists":voteresults.count("Democratic Unionists"), "Sinn Fein":voteresults.count("Sinn Fein"), "Plaid Cymru":voteresults.count("Plaid Cymru"), "Social Democratics":voteresults.count("Social Democratics"), "Unionists":voteresults.count("Unionists"), "Greens":voteresults.count("Greens"), "Scottish Greens":voteresults.count("Scottish Greens"), "Independance":voteresults.count("Independance"), "Alliance Party":voteresults.count("Alliance Party"), "Northern Irish Greens":voteresults.count("Northern Irish Greens"), "Traditional Unionists":voteresults.count("Traditional Unionists"), "People B Profit":voteresults.count("People B Profit"), "Welsh":voteresults.count("Welsh"), "Abolish Welsh":voteresults.count("Abolish Welsh"), "N/A":voteresults.count("N/A")}
    competitors = ["Conservatives", "Labour", "Scottish", "Liberals", "Democratic Unionists", "Sinn Fein", "Plaid Cymru", "Social Democratics", "Unionists", "Greens", "Scottish Greens", "Independance", "Alliance Party", "Northern Irish Greens", "Traditional Unionists", "People B Profit", "Welsh", "Abolish Welsh"]
    winner = max(parties, key = parties.get)
    print("The winning party is the", winner, "party with", parties[winner], "seats in parliament.")
    for i in range(len(parties)):
        if parties[competitors[i-1]] > 0:
            if parties[competitors[i-1]] == 1:
                print(competitors[i-1], "have", parties[competitors[i-1]], "seat in parliament.")
            if parties[competitors[i-1]] > 1:
                print(competitors[i-1], "have", parties[competitors[i-1]], "seats in parliament.")
        time.sleep(2)

def unitedStatesElection():
    choiceOfVote = ["Major", "Major", "Major", "Major", "Minor", "Minor", "Independant"]
    majorParties = ["Republicans", "Democrats"]
    minorParties = ["Libertarians", "Vermont Progress", "NY Indpendant"]
    independantCandidates = ["Wiktor Colley", "Kaylee Berger", "Carrie Orr", "Haniya Lord", "Ronan Ryder", "Franky Higgs", "Umar O'Moore", "Sophie-Louise Bain", "Inaayah Cortes", "Robin McKenna", "Asa Snyder", "Diesel Hanson", "Kyal Wilks", "Faizan Stafford", "Sue Richard", "Jarrad Benson", "Jay Beattie", "Rikki Meadows", "Willie Shaw", "Genevieve Whitley", "Emer Worthington", "Roseanne Firth", "Fletcher Hough", "Alby Muir", "Maizie Coulson"]
    voteresults = []
    electoralCollegeVotes = {"Republicans" : 0, "Democrats" : 0, "Libertarians" : 0, "Vermont Progress" : 0, "NY Indpendant" : 0, "Wiktor Colley" : 0, "Kaylee Berger" : 0, "Carrie Orr" : 0, "Haniya Lord" : 0, "Ronan Ryder" : 0, "Franky Higgs" : 0, "Umar O'Moore" : 0, "Sophie-Louise Bain" : 0, "Inaayah Cortes" : 0, "Robin McKenna" : 0, "Asa Snyder" : 0, "Diesel Hanson" : 0, "Kyal Wilks" : 0, "Faizan Stafford" : 0, "Sue Richard" : 0, "Jarrad Benson" : 0, "Jay Beattie" : 0, "Rikki Meadows" : 0, "Willie Shaw" : 0, "Genevieve Whitley" : 0, "Emer Worthington" : 0, "Roseanne Firth" : 0, "Fletcher Hough" : 0, "Alby Muir" : 0, "Maizie Coulson" : 0}
    candidates = ["Republicans", "Democrats", "Libertarians", "Vermont Progress", "NY Indpendant", "Wiktor Colley", "Kaylee Berger", "Carrie Orr", "Haniya Lord", "Ronan Ryder", "Franky Higgs", "Umar O'Moore", "Sophie-Louise Bain", "Inaayah Cortes", "Robin McKenna", "Asa Snyder", "Diesel Hanson", "Kyal Wilks", "Faizan Stafford", "Sue Richard", "Jarrad Benson", "Jay Beattie", "Rikki Meadows", "Willie Shaw", "Genevieve Whitley", "Emer Worthington", "Roseanne Firth", "Fletcher Hough", "Alby Muir", "Maizie Coulson"]
    def currentResults(electoralCollegeVotes):
        leader = max(electoralCollegeVotes, key = electoralCollegeVotes.get)
        print("The current leader is", leader, "with", electoralCollegeVotes[leader], "electoral college votes.")
        print("REPUBLICANS :", electoralCollegeVotes["Republicans"])
        print("DEMOCRATS :", electoralCollegeVotes["Democrats"])
        time.sleep(2)
    def finalResults(electoralCollegeVotes, candidates):
        for i in range(len(electoralCollegeVotes)):
            partyname = candidates[i]
            votes = electoralCollegeVotes[partyname]
            if votes > 0:
                print(partyname.upper(), ":", votes)
        winner = max(electoralCollegeVotes, key = electoralCollegeVotes.get)
        print("The winner of the White House is", winner)
    class State():
        def __init__(self, independantCandidates, name, electoralWorth):
            self.noOfVoters = 50
            self.independantCandidates = []
            for i in range(2):
                selected = random.choice(independantCandidates)
                self.independantCandidates.append(selected)
            self.name = name
            self.votes = []
            self.counted = []
            self.highest = 0
            self.tie = []
            self.worth = electoralWorth
        def vote(self, choiceOfVote, majorParties, minorParties):
            for i in range(self.noOfVoters):
                selection = random.choice(choiceOfVote)
                if selection == "Major":
                    vote = random.choice(majorParties)
                    self.votes.append(vote)
                if selection == "Minor":
                    vote = random.choice(minorParties)
                    self.votes.append(vote)
                if selection == "Independant":
                    vote = random.choice(self.independantCandidates)
                    self.votes.append(vote)
            self.candidates = ["Republicans", "Democrats", "Libertarians", "Vermont Progress", "NY Indpendant", "Wiktor Colley", "Kaylee Berger", "Carrie Orr", "Haniya Lord", "Ronan Ryder", "Franky Higgs", "Umar O'Moore", "Sophie-Louise Bain", "Inaayah Cortes", "Robin McKenna", "Asa Snyder", "Diesel Hanson", "Kyal Wilks", "Faizan Stafford", "Sue Richard", "Jarrad Benson", "Jay Beattie", "Rikki Meadows", "Willie Shaw", "Genevieve Whitley", "Emer Worthington", "Roseanne Firth", "Fletcher Hough", "Alby Muir", "Maizie Coulson"]
        def declaration(self, electoralCollegeVotes):
            self.winner = ""
            for i in range(len(self.candidates)):
                partyname = self.candidates[i]
                partyvotes = self.votes.count(partyname)
                self.counted.append(partyvotes)
                if partyvotes > self.highest:
                    self.highest = partyvotes
                    self.winner = partyname
            electoralCollegeVotes[self.winner] = electoralCollegeVotes[self.winner] + self.worth
            print()
            print("The winner of", self.name, "is", self.winner, "and have won", self.worth, "electoral college votes.")
            print()
            time.sleep(5)
    alabama = State(independantCandidates, "Alabama", 9)
    alabama.vote(choiceOfVote, majorParties, minorParties)
    alabama.declaration(electoralCollegeVotes)

    currentResults(electoralCollegeVotes)
    
    alaska = State(independantCandidates, "Alaska", 3)
    alaska.vote(choiceOfVote, majorParties, minorParties)
    alaska.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    arizona = State(independantCandidates, "Arizona", 11)
    arizona.vote(choiceOfVote, majorParties, minorParties)
    arizona.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    arkansas = State(independantCandidates, "Arkansas", 6)
    arkansas.vote(choiceOfVote, majorParties, minorParties)
    arkansas.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    california = State(independantCandidates, "California", 55)
    california.vote(choiceOfVote, majorParties, minorParties)
    california.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    colorado = State(independantCandidates, "Colorado", 9)
    colorado.vote(choiceOfVote, majorParties, minorParties)
    colorado.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    connecticut = State(independantCandidates, "Connecticut", 7)
    connecticut.vote(choiceOfVote, majorParties, minorParties)
    connecticut.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    delaware = State(independantCandidates, "Delaware", 3)
    delaware.vote(choiceOfVote, majorParties, minorParties)
    delaware.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    washingtonDC = State(independantCandidates, "District of Columbia", 9)
    washingtonDC.vote(choiceOfVote, majorParties, minorParties)
    washingtonDC.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    florida = State(independantCandidates, "Florida", 29)
    florida.vote(choiceOfVote, majorParties, minorParties)
    florida.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    georgia = State(independantCandidates, "Georgia", 16)
    georgia.vote(choiceOfVote, majorParties, minorParties)
    georgia.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    hawaii = State(independantCandidates, "Hawaii", 4)
    hawaii.vote(choiceOfVote, majorParties, minorParties)
    hawaii.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    idaho = State(independantCandidates, "Idaho", 4)
    idaho.vote(choiceOfVote, majorParties, minorParties)
    idaho.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    illinois = State(independantCandidates, "Illinois", 20)
    illinois.vote(choiceOfVote, majorParties, minorParties)
    illinois.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    indiana = State(independantCandidates, "Indiana", 11)
    indiana.vote(choiceOfVote, majorParties, minorParties)
    indiana.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    iowa = State(independantCandidates, "Iowa", 6)
    iowa.vote(choiceOfVote, majorParties, minorParties)
    iowa.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    kansas = State(independantCandidates, "Kansas", 6)
    kansas.vote(choiceOfVote, majorParties, minorParties)
    kansas.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    kentucky = State(independantCandidates, "Kentucky", 8)
    kentucky.vote(choiceOfVote, majorParties, minorParties)
    kentucky.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    louisiana = State(independantCandidates, "Louisiana", 8)
    louisiana.vote(choiceOfVote, majorParties, minorParties)
    louisiana.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    maine = State(independantCandidates, "Maine", 4)
    maine.vote(choiceOfVote, majorParties, minorParties)
    maine.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    maryland = State(independantCandidates, "Maryland", 10)
    maryland.vote(choiceOfVote, majorParties, minorParties)
    maryland.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    massachusetts = State(independantCandidates, "Massachusetts", 11)
    massachusetts.vote(choiceOfVote, majorParties, minorParties)
    massachusetts.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    michigan = State(independantCandidates, "Michigan", 16)
    michigan.vote(choiceOfVote, majorParties, minorParties)
    michigan.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    minnesota = State(independantCandidates, "Minnesota", 10)
    minnesota.vote(choiceOfVote, majorParties, minorParties)
    minnesota.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    mississippi = State(independantCandidates, "Mississippi", 6)
    mississippi.vote(choiceOfVote, majorParties, minorParties)
    mississippi.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    missouri = State(independantCandidates, "Missouri", 10)
    missouri.vote(choiceOfVote, majorParties, minorParties)
    missouri.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    montana = State(independantCandidates, "Montana", 3)
    montana.vote(choiceOfVote, majorParties, minorParties)
    montana.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    nebraska = State(independantCandidates, "Nebraska", 5)
    nebraska.vote(choiceOfVote, majorParties, minorParties)
    nebraska.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    nevada = State(independantCandidates, "Nevada", 6)
    nevada.vote(choiceOfVote, majorParties, minorParties)
    nevada.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    newHampshire = State(independantCandidates, "New Hampshire", 4)
    newHampshire.vote(choiceOfVote, majorParties, minorParties)
    newHampshire.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    newJersey = State(independantCandidates, "New Jersey", 14)
    newJersey.vote(choiceOfVote, majorParties, minorParties)
    newJersey.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    newMexico = State(independantCandidates, "New Mexico", 5)
    newMexico.vote(choiceOfVote, majorParties, minorParties)
    newMexico.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    newYork = State(independantCandidates, "New York", 29)
    newYork.vote(choiceOfVote, majorParties, minorParties)
    newYork.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    northCarolina = State(independantCandidates, "North Carolina", 15)
    northCarolina.vote(choiceOfVote, majorParties, minorParties)
    northCarolina.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    northDakota = State(independantCandidates, "North Dakota", 3)
    northDakota.vote(choiceOfVote, majorParties, minorParties)
    northDakota.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    ohio = State(independantCandidates, "Ohio", 18)
    ohio.vote(choiceOfVote, majorParties, minorParties)
    ohio.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    oklahoma = State(independantCandidates, "Oklahoma", 7)
    oklahoma.vote(choiceOfVote, majorParties, minorParties)
    oklahoma.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    oregon = State(independantCandidates, "Oregon", 7)
    oregon.vote(choiceOfVote, majorParties, minorParties)
    oregon.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    pennsylvania = State(independantCandidates, "Pennsylvania", 20)
    pennsylvania.vote(choiceOfVote, majorParties, minorParties)
    pennsylvania.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    rhodeIsland = State(independantCandidates, "Rhode Island", 4)
    rhodeIsland.vote(choiceOfVote, majorParties, minorParties)
    rhodeIsland.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    southCarolina = State(independantCandidates, "South Carolina", 9)
    southCarolina.vote(choiceOfVote, majorParties, minorParties)
    southCarolina.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    southDakota = State(independantCandidates, "South Dakota", 3)
    southDakota.vote(choiceOfVote, majorParties, minorParties)
    southDakota.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    tennessee = State(independantCandidates, "Tennessee", 11)
    tennessee.vote(choiceOfVote, majorParties, minorParties)
    tennessee.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    texas = State(independantCandidates, "Texas", 38)
    texas.vote(choiceOfVote, majorParties, minorParties)
    texas.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    utah = State(independantCandidates, "Utah", 6)
    utah.vote(choiceOfVote, majorParties, minorParties)
    utah.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    vermont = State(independantCandidates, "Vermont", 3)
    vermont.vote(choiceOfVote, majorParties, minorParties)
    vermont.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    virginia = State(independantCandidates, "Virginia", 13)
    virginia.vote(choiceOfVote, majorParties, minorParties)
    virginia.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    washington = State(independantCandidates, "Washington", 12)
    washington.vote(choiceOfVote, majorParties, minorParties)
    washington.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    westVirginia = State(independantCandidates, "West Virginia", 5)
    westVirginia.vote(choiceOfVote, majorParties, minorParties)
    westVirginia.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    wisconsin = State(independantCandidates, "Wisconsin", 10)
    wisconsin.vote(choiceOfVote, majorParties, minorParties)
    wisconsin.declaration(electoralCollegeVotes)
    
    currentResults(electoralCollegeVotes)
    

    wyoming = State(independantCandidates, "Wyoming", 3)
    wyoming.vote(choiceOfVote, majorParties, minorParties)
    wyoming.declaration(electoralCollegeVotes)

    finalResults(electoralCollegeVotes, candidates)

def australiaElection():
##    print("This hasn't been coded yet, thus cannot be simulated")
    majorcandidates = ["Lib-Nats", "Labor"]
    minorcandidates = ["Liberals", "Nationals", "Greens", "Central", "Katter", "One Nation", "Jacqui Lambie"]
    choiceOfCandidate = [majorcandidates, majorcandidates, majorcandidates, majorcandidates, minorcandidates, minorcandidates, minorcandidates] #4:3 ratio
    votes = []
    for i in range(500):
        majorcandidates = ["Lib-Nats", "Labor"]
        minorcandidates = ["Liberals", "Nationals", "Greens", "Central", "Katter", "One Nation", "Jacqui Lambie"]
        individualvote = []
        while len(individualvote) < 5:
            if len(majorcandidates) > 0:
                choosing = random.choice(choiceOfCandidate)
                if choosing == majorcandidates:
                    vote = random.randint(0, len(majorcandidates) - 1)
                    votename = majorcandidates[vote]
                if choosing == minorcandidates:
                    vote = random.randint(0, len(minorcandidates) - 1)
                    votename = minorcandidates[vote]
            else:
                vote = random.randint(0, len(minorcandidates) - 1)
                votename = minorcandidates[vote]
            if votename not in individualvote:
                individualvote.append(votename)
        votes.append(individualvote)
##    def counting(votes):
##        candidates = {"Lib-Nats" : 0, "Labor" : 0, "Liberals" : 0, "Nationals" : 0, "Greens" : 0, "Central" : 0, "Katter" : 0, "One Nation" : 0, "Jacqui Lambie" : 0}
##        candidateChoice = ["Lib-Nats", "Labor", "Liberals", "Nationals", "Greens", "Central", "Katter", "One Nation", "Jacqui Lambie"]
##        def firstChoice(votes, candidates):
##            choice = []
##            for i in range(len(votes)):
##                voteCast = False
##                if votes[i][0] in candidates:
##                    first = votes[i][0]
##                    choice.append(first)
##                    voteCast = True
##                else:
##                    while voteCast == False:
##                        for x in range(len(votes[i]) - 1):
##                            if votes[i][x + 1]:
##                                first = votes[i][x + 1]
##                                choice.append(first)
##                                voteCast = True
##            return choice
##        choice = firstChoice(votes, candidates)
##        winnerFound = False
##        def voteCounting(candidateChoice, candidates, choice):
##            for i in range(len(candidates)):
##                partyname = candidateChoice[i]
##                partyvotes = choice.count(partyname)
##                candidates[partyname] = candidates[partyname] + partyvotes
##            if candidates[max(candidates, key = candidates.get)] > 250:
##                winnerFound == True
##                winner = max(candidates, key = candidates.get)
##                print("The winner of this year's Australian Election is", winner)
##            else:
##                winnerFound = False
##            return candidates, winnerFound
##        def removal(candidates):
##            loser = min(candidates, key = candidates.get)
##            print("The party with the least votes is", loser)
##            del(candidates[loser])
##            candidateChoice.remove(loser)
##            if len(candidateChoice) == 1:
##                winnerFound = True
##                winner = candidateChoice[0]
##                print("The winner of this year's Australian Election is", winner)
##            return winnerFound
##        while winnerFound == False:
##            candidates, winnerFound = voteCounting(candidateChoice, candidates, choice)
##            winnerFound = removal(candidates)
##            choice = firstChoice(votes, candidates)
##    counting(votes)
    candidates = {"Lib-Nats" : 0, "Labor" : 0, "Liberals" : 0, "Nationals" : 0, "Greens" : 0, "Central" : 0, "Katter" : 0, "One Nation" : 0, "Jacqui Lambie" : 0}
    candidateChoice = ["Lib-Nats", "Labor", "Liberals", "Nationals", "Greens", "Central", "Katter", "One Nation", "Jacqui Lambie"]
    choice1 = []
    choice2 = []
    choice3 = []
    choice4 = []
    choice5 = []
    eliminated = []
    for i in range(len(votes)):
        firstChoice = votes[i][0]
        secondChoice = votes[i][1]
        thirdChoice = votes[i][2]
        fourthChoice = votes[i][3]
        fifthChoice = votes[i][4]
        choice1.append(firstChoice)
        choice2.append(secondChoice)
        choice3.append(thirdChoice)
        choice4.append(fourthChoice)
        choice5.append(fifthChoice)
    choice = choice1
    for i in range(len(candidateChoice)):
        partyname = candidateChoice[i]
        partyvotes = choice.count(partyname)
        candidates[partyname] = candidates[partyname] + partyvotes
    winnerDeclared = False
    #first run-off
    if candidates[max(candidates, key = candidates.get)] > 250:
        winnerDeclared = True
        winner = max(candidates, key = candidates.get)
        print(candidates)
    elif len(candidateChoice) == 1:
        winnerDeclared = True
        winner = candidateChoice[0]
        print(candidates)
    else:
        winnerDeclared = False
        loser = min(candidates, key = candidates.get)
        loserVotes = candidates[loser]
        print(candidates)
        eliminated.append(loser)
        del(candidates[loser])
        candidateChoice.remove(loser)
        print("The party eliminated in round 1 is", loser)
    #second run-off
    time.sleep(2)
    if winnerDeclared == False:
        choice *= 0
        for i in range(len(choice1)):
            if loserVotes != 0:
                if choice1[i] not in candidateChoice:
                    print(choice1[i], "->", choice2[i])
                    choice.append(choice2[i])
                    loserVotes -= 1
                else:
                    choice.append(choice1[i])
            else:
                choice.append(choice1[i])
        for i in range(len(candidateChoice)):
            partyname = candidateChoice[i]
            partyvotes = choice.count(partyname)
            candidates[partyname] = candidates[partyname] + partyvotes
        winnerDeclared = False
        if candidates[max(candidates, key = candidates.get)] > 250:
            winnerDeclared = True
            winner = max(candidates, key = candidates.get)
            print(candidates)
        elif len(candidateChoice) == 1:
            winnerDeclared = True
            winner = candidateChoice[0]
            print(candidates)
        else:
            winnerDeclared = False
            loser = min(candidates, key = candidates.get)
            print(candidates)
            eliminated.append(loser)
            del(candidates[loser])
            candidateChoice.remove(loser)
            print("The party eliminated in round 2 is", loser)
    #third run-off
    time.sleep(2)
    if winnerDeclared == False:
        choice = []
        for i in range(len(choice1)):
            if choice1[i] in eliminated:
                if choice2[i] in eliminated:
                    choice.append(choice3[i])
                else:
                    choice.append(choice2[i])
            else:
                choice.append(choice1[i])
        for i in range(len(candidateChoice)):
            partyname = candidateChoice[i]
            partyvotes = choice.count(partyname)
            candidates[partyname] = candidates[partyname] + partyvotes
        winnerDeclared = False
        if candidates[max(candidates, key = candidates.get)] > 250:
            winnerDeclared = True
            winner = max(candidates, key = candidates.get)
            print(candidates)
        elif len(candidateChoice) == 1:
            winnerDeclared = True
            winner = candidateChoice[0]
            print(candidates)
        else:
            winnerDeclared = False
            loser = min(candidates, key = candidates.get)
            print(candidates)
            eliminated.append(loser)
            del(candidates[loser])
            candidateChoice.remove(loser)
            print("The party eliminated in round 3 is", loser)
    #fourth run-off
    time.sleep(2)
    if winnerDeclared == True:
        choice = []
        for i in range(len(choice1)):
            if choice1[i] in eliminated:
                if choice2[i] in eliminated:
                    if choice3[i] in eliminated:
                        choice.append(choice4[i])
                    else:
                        choice.append(choice3[i])
                else:
                    choice.append(choice2[i])
            else:
                choice.append(choice1[i])
        for i in range(len(candidateChoice)):
            partyname = candidateChoice[i]
            partyvotes = choice.count(partyname)
            candidates[partyname] = candidates[partyname] + partyvotes
        winnerDeclared = False
        if candidates[max(candidates, key = candidates.get)] > 250:
            winnerDeclared = True
            winner = max(candidates, key = candidates.get)
            print(candidates)
        elif len(candidateChoice) == 1:
            winnerDeclared = True
            winner = candidateChoice[0]
            print(candidates)
        else:
            winnerDeclared = False
            loser = min(candidates, key = candidates.get)
            print(candidates)
            eliminated.append(loser)
            del(candidates[loser])
            candidateChoice.remove(loser)
            print("The party eliminated in round 4 is", loser)
    #fifth run-off
    time.sleep(2)
    if winnerDeclared == False:
        choice = []
        for i in range(len(choice1)):
            if choice1[i] in eliminated:
                if choice2[i] in eliminated:
                    if choice3[i] in eliminated:
                        if choice4[i] in eliminated:
                            choice.append(choice5[i])
                        else:
                            choice.append(choice4[i])
                    else:
                        choice.append(choice3[i])
                else:
                    choice.append(choice2[i])
            else:
                choice.append(choice1[i])
        for i in range(len(candidateChoice)):
            partyname = candidateChoice[i]
            partyvotes = choice.count(partyname)
            candidates[partyname] = candidates[partyname] + partyvotes
        winnerDeclared = False
        if candidates[max(candidates, key = candidates.get)] > 250:
            winnerDeclared = True
            winner = max(candidates, key = candidates.get)
            print(candidates)
        elif len(candidateChoice) == 1:
            winnerDeclared = True
            winner = candidateChoice[0]
            print(candidates)
        else:
            winnerDeclared = True
            winner = max(candidates, key = candidates.get)
            print(candidates)
    print("The winner of this year's Australian Election is", winner, "with", candidates[winner], "votes.")
    
def sodorElection():
    print("This hasn't been coded yet, thus cannot be simulated")
currentDate = 2019
ukdate = 2023
usadate = 2020
australiadate = 2022
sodordate = 2020
while currentDate < 2051:
    print("_ _ _ _ _ _ _ _ _ _")
    print(currentDate)
    print("_ _ _ _ _ _ _ _ _ _")
    if ukdate < currentDate:
        ukdate = ukdate + 4
    if ukdate == currentDate:
        print("______________________________")
        print("UNITED KINGDOM ELECTION", currentDate)
        print("______________________________")
        unitedKingdomElection()
        time.sleep(2)
    if usadate < currentDate:
        usadate = usadate + 4
    if usadate == currentDate:
        print("______________________________")
        print("UNITED STATES ELECTION", currentDate)
        print("______________________________")
        unitedStatesElection()
        time.sleep(2)
    if australiadate < currentDate:
        australiadate = australiadate + 3
    if australiadate == currentDate:
        print("______________________________")
        print("AUSTRALIA ELECTION", currentDate)
        print("______________________________")
        australiaElection()
        time.sleep(0.5)
    if sodordate < currentDate:
        sodordate = sodordate + 5
    if sodordate == currentDate:
        print("______________________________")
        print("SODOR ELECTION", currentDate)
        print("______________________________")
        sodorElection()
        time.sleep(2)
    currentDate += 1
    time.sleep(0.5)
time.sleep(10)
