
# def determine_stars(average_score):
#     star_rating = ""
#     if average_score >= 9:
#         star_rating = "*****"
    
#     elif average_score <= 8.9 and average_score >= 8.0:
#         star_rating = "****"

#     elif average_score <= 7.9 and average_score >= 7.0:
#         star_rating = "***"

#     elif average_score <= 6.9 and average_score >= 6.0:
#         star_rating = "**"

#     elif average_score <= 5.9 and average_score >= 5.0:
#         star_rating = "*"

#     else:  
#         star_rating = "0 stars"

#     print("Your score of", average_score, "gives you", star_rating)

# # TODO
# determine_stars(4.9)

max_valid_score_inputs = 5
critic_score_sum = 0
invalid_score_inputs = 0
input_attempts = 0
while input_attempts - invalid_score_inputs < 5:
    critic_score = float(input("Enter critic's score between 0 and 10: "))
    input_attempts += 1
    if critic_score > 10 or critic_score < 0:
        invalid_score_inputs += 1
        print("Error: Invalid score")
    else:
        critic_score_sum += critic_score
        
        