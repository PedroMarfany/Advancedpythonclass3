""""
Script to Make updates in Github
"""
import click
import pandas as pandas

click.command(short_help= "Parser to import dataset")
click.option("-f", "--filename", required = True, help = "File to import")
def main():
    """
    Main Function
    """

    pass

    df = pd.read_csv(filename)
    print(df.shape)

 if _name_ == "_main_":
    main()