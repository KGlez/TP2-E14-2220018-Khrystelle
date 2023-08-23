from gametasks import printInstructions, getUserScore,updateUserScore
from gameclasses import Game, MathGame, BinaryGame

try:
    mathInstructions = '''
    Dans ce jeu, nous vous donnerons une simple question arithmetiques
    Chaque bonne réponse vous donnez un point.
    Pas de point négatif en cas de mauvaise réponse.
    '''
    binaryInstructions = '''
    Dans ce jeu, nous vous donnerons un nombre en base 10.
    Votre tâches consistera à la convertir en base 2.
    Chaque bonne réponse vous donnez un point.
    Pas de point négatif en cas de mauvaise réponse.
    '''
    mg = MathGame()
    bg = BinaryGame()
    userName = input("\nEntrez votre nom: ")
    score = int(getUserScore(userName))
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False
    print("\nBonjour %s, Bienvenue dans le jeu." %(userName))
    print("Votre score actuel est de %d." %(score))
    userChoice = 0

    while userChoice != '-1':
        game = input("\nJeu de Maths (1) ou Jeu Binaire (2)?: ")
        while game != '1' and game != '2':
            print("Vous n'avez pas entrez un choix valide. Recommencez s'il vous plait")
            game = input("\nJeu de Maths (1) ou Jeu Binaire (2)?: ")
        numPrompt = input("\nCombien de partie souhaitez-vous jouer ? (Chaque partie comprend 4 questions) (1 à 10 parties)")
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("Vous n'avez pas entrez un choix valide. Recommencez s'il vous plait.")
                numPrompt = input("\nCombien de partie souhaitez-vous jouer ? (Chaque partie comprend 4 questions) (1 à 10 parties)")
        if game == '1':
            mg.noOfQuestions = num
            printInstructions(mathInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score = score + bg.generateQuestions( )
        print("\nVotre score actuel est de %d." %(score))
        userChoice = input("\nAppuyez sur Entrez pour continuer ou -1 pour quitter:")
    updateUserScore(newUser, userName, str(score))
except Exception as e:
    print("An unknown error occurred. Program will exit.")
    print("Error: ", e)