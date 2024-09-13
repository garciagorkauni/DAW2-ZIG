def gehiengo_absolutua (votes):
    # Create a dict with the votes of each team
    votes_result = {alderdi:votes.count(alderdi) for alderdi in votes}

    # Look for the most if there is
    for alderdi, vote_number in votes_result.items():
        if vote_number > len(votes)/2:
            return "{} alderdiak gehiengo absolutua lortu du {} botoekin {}-tik.".format(alderdi, vote_number, len(votes))

    return "Inork ez dauka gehiengo absoluturik"

def main():
    # Define test values
    votes = ('A', 'B', 'A', 'C', 'A', 'B', 'A')
    
    # Show the result to the user
    print(gehiengo_absolutua(votes))

if __name__ == "__main__":
    main()