from owla.helper.customer_cli import customer
try:
    import click
except Exception as e:
    print(e)

@click.group()
def cli():
    """
    \b
         ___           _       
        /___\__      _| | __ _ 
       //  //\ \ /\ / / |/ _` |
      / \_//  \ V  V /| | (_| |
      \___/    \_/\_/ |_|\__,_|

    \u001b[34mOwla\u001b[0m is our implementation of an online taxi retail platform like Ola.
    """
    pass

cli.add_command(customer)