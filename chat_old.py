import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True
    
    # Counts how many words are present in each predefined words
    for word in user_message:
        if word in recognised_words:
            message_certainity += 1
    
    # Calculate the percentage of recognised words in user message
    percentage = float(message_certainity) / float(len(recognised_words))
    
    # Check that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_message(message):
    highest_prob_list = []
    
    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    # Response ----------------------------------------
    response('Hello!', ['hello', 'hi', 'sup' 'hey', 'heyo'], single_response = True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you' 'hey', 'doing'], required_words = ['how'])
    response('Thank You!', ['i', 'love', 'code', 'palace'], required_words = ['code', 'palace'])
    
    response(long.R_EATING, ['what', 'you', 'eat'], required_words = ['you', 'eat'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response

while True:
    print('Bot: '+get_response(input('You: ')))