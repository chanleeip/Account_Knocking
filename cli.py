from files import main
import typer

app = typer.Typer()

@app.command(help="Check if account exists on a website (ebay,espn,pinterest,quora,spotify)")
def run_main(email: str=typer.Option("-email","--e",prompt="Enter the email-id to check"), url: str=typer.Option("-url",'--u', prompt="Enter website name (ebay,espn,pinterest,quora,spotify)")):
   main.main(email,url)

if __name__ == "__main__":
    app()