import os
import sys
import shutil

currentWorkingDir = os.getcwd()


def makeSassEnv():
    print(currentWorkingDir)

    ### Folder List ###
    sassDir = ["base", "components", "layout",
               "pages", "themes", "abstracts", "vendors"]
    createSassFolder = os.mkdir('sass')
    createCSSFolder = os.mkdir('css')
    createCSSFolder = os.mkdir('img')
    os.chdir(currentWorkingDir + "//sass")
    print(os.getcwd())
    for i in sassDir:
        os.mkdir(i)

# creating index.html and main.css in the css folder


def makeFiles():
    sass = "//sass"

    # index.html
    os.chdir(currentWorkingDir)
    open("index.html", "w+")

    # css
    css = "//css"
    os.chdir(currentWorkingDir + css)
    open("main.css", "w+")

    ######################################

    # abstracts
    abstracts = "//abstracts"
    os.chdir(currentWorkingDir + sass + abstracts)
    open("_functions.scss", "w+")
    open("_mixins.scss", "w+")
    open("_variables.scss", "w+")

    # base
    base = "//base"
    os.chdir(currentWorkingDir + sass + base)
    open("_base.scss", "w+")
    open("_typography.scss", "w+")
    open("_utilities.scss", "w+")
    open("_animations.scss", "w+")

    # layout
    layout = "//layout"
    os.chdir(currentWorkingDir + sass + layout)
    open("_header.scss", "w+")
    open("_footer.scss", "w+")
    open("_grid.scss", "w+")
    open("_navigation.scss", "w+")

##############################################
# Delete All the files created


def delete():
    shutil.rmtree(currentWorkingDir + "//sass")
    shutil.rmtree(currentWorkingDir + "//css")
    shutil.rmtree(currentWorkingDir + "//img")
    os.remove("index.html")
    print("\n\n\tEverything is now deleted\n\n")

#############################################
# Creating the main.scss file with imports


def mainSCSS():
    # Navigate to sass
    sass = "//sass"
    os.chdir(currentWorkingDir + sass)
    # Create the main.scss file
    mainSass = open("main.scss", "w")
    nl = "\n"
    # abstracts
    functions = "@import \"abstracts/functions\";\n"
    variables = "@import \"abstracts/variables\";\n"
    mixins = "@import \"abstracts/mixins\";\n"
    # base
    animations = "@import \"base/animations\";\n"
    base = "@import \"base/base\";\n"
    typography = "@import \"base/typography\";\n"
    utilities = "@import \"base/utilities\";\n"
    # layout
    header = "@import \"layout/header\";\n"
    grid = "@import \"layout/grid\";\n"
    footer = "@import \"layout/footer\";\n"
    navigation = "@import \"layout/navigation\";\n"
    # writing the above into the main.scss file
    mainSass.write(functions + variables + mixins + nl + animations + base +
                   typography + utilities + nl + header + grid + footer + navigation + nl)

# Execute the creation of Sass


def create():
    makeSassEnv()
    makeFiles()
    mainSCSS()
    print("\n\n\tSass environment created\n\n")


def sassExecution():
    sassQuestion = input(
        "\n\tPress C to create SASS folders. \n \tPress D to delete all SASS folders\n\tPress anyhting else to QUIT :-> \t")
    print(type(sassQuestion))
    print(sassQuestion)
    if sassQuestion.upper() == "C":
        create()
    elif sassQuestion.upper() == "D":
        delete()
    else:
        print("\n\tYou have chosen to quit\n\n\n")
        raise SystemExit

sassExecution()
