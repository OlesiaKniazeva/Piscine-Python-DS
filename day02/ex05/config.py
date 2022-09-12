num_of_steps = 9

def parameters():
    file = 'data.csv'
    head = True

    return file, head

def file_result_data():
    file_name = 'result.txt'
    return file_name

def message(all_data, amount, probability, foresast):
    result = f'''Report
    We have made {all_data} observations from tossing a coin: {amount[0]} of them were tails and {amount[1]} of
    them were heads. The probabilities are {probability[0]:.2f}% and {probability[1]:.2f}%, respectively. Our
    forecast is that in the next {num_of_steps} observations we will have: {foresast[0]} tail and {foresast[1]} heads.
    '''
    return result