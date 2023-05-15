from django.shortcuts import render
from django.http import HttpResponse
from .forms import targetForm, guessForm

def start(request):
    # First loading the page
    if request.method == "GET":
        status = "Welcome to Wordish!"

        return render(request, "start.html", {"status":status})
    
    # Validating the target word
    if "target_text" not in request.POST or (len(request.POST["target_text"]) != 5 or not request.POST["target_text"].isalpha()):
            status = "Invalid Input!"
            return render(request, "start.html", {"status":status})
    
    target = request.POST["target_text"].lower()
    
    context = {}
    context["status"] = "Enter a Guess!"
    context["target"] = target
    context["color"] = "green"

    return render(request, "game.html", context)
    

def game(request, guesses=[], colors=[]):

    context= {}
    context["status"] = "Enter a Guess!"

    target = request.POST.get('target').lower()
    context['target'] = target

    guess = request.POST["guess_text"].lower()

    # Validating the Guess Text
    if "guess_text" not in request.POST or (len(request.POST["guess_text"]) != 5 or not request.POST["guess_text"].isalpha()):
          status = "Invalid Guess!"

          return render(request, "game.html", {"status":status, "guesses":guesses, "colors":colors})
    
    
    # Entering a guess if the game is not over
    guesses.append(guess)
    context["guesses"] = guesses

    # Getting the colors
    curr_color = color(guess, target)
    colors.append(curr_color)
    context["colors"] = colors
    

    # Checking if the game is over
    if (target in guesses) and len(guesses) <= 6:
        context["status"] = "You won!"
    elif len(guesses) >= 6 and (target not in guesses):
         context["status"] = f"You lose! The word was {target}."     

    
    return render(request, "game.html", context)

def color(guess, target):

    d = {}
    for letter in target:
         d[letter] = 1 + d.get(letter, 0)
    
    res = []
    for i in range(len(guess)):
        if guess[i] == target[i]:
             d[guess[i]] -= 1
             res.append("green")
        elif guess[i] != target[i] and guess[i] in d and d[guess[i]] > 0:
             res.append("yellow")
        else:
             res.append("grey")

    for i in range(len(res)):
         if res[i] == "yellow" and d[guess[i]] == 0:
              res[i] = "grey"

    return res
    


         



    













