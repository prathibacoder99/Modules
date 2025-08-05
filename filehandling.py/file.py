with open("document.txt","w")as f:
    f.write("Training means teaching a model from scratch using huge datasets.\n")
    f.write("Fine-tuning means adjusting a pre-trained model on a smaller, specific dataset.\n")
with open("document.txt", "r") as f:
        content = f.read()
        print(content)
with open("document.txt", "a") as f:
    f.write("Examples: ChatGPT, LLaMA, Falcon, Mistral, BERT, etc.\n")
with open("document.txt", "r") as f:
    content = f.read()
    print(content)
with open("document.txt","r")as f:
    lines = f.readlines()
new_lines = [line.replace("Training", "Learning") for line in lines]
with open("document.txt", "w") as f:
    f.writelines(new_lines)
with open("document.txt", "r") as f:
    content = f.read()
    print(content)



