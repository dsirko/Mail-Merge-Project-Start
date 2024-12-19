#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

def read_example(lines):
    with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
        ex_letter = starting_letter.read()

        for line in lines:
            filename = f'Output/ReadyToSend/letter_to_{line}.txt'
            strip_line = line.strip()
            new_ex_letter = ex_letter.replace(PLACEHOLDER, strip_line)
            print(new_ex_letter)
            
            with open(filename, 'w') as f:
                f.write(new_ex_letter)

    return "Done"
        

def read_names():
    with open('Input/Names/invited_names.txt', 'r') as file:
        lines = file.readlines()
        return lines


if __name__ == "__main__":
    print(read_example(read_names()))

