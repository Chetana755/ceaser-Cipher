alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
def caesar(text,shift_number,cipher):
    end_text=""
    if cipher==2:
        shift_number*=-1
    for char in text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=position+shift_number
            end_text+=alphabets[new_position]
        else:
            end_text+=char
    print(f"Here is the ciphered text: {end_text}")
end=False
while not end:
    print("options\n1.encode\t 2.decode\t 3.exit")
    cipher=int(input("Enter your choice: "))
    if cipher==3:
        print("Thank you!")
        break
    text=input("Type your message: ").lower()
    shift=int(input("Type the shift number: "))
    shift=shift%26
    caesar(text,shift,cipher)
