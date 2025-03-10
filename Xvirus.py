import threading

from util import *

class menus:
    def joiner_menu():
        utility.make_menu(f"Normal Mode", f"RestoreCord Mode {Fore.RED}(bypass captcha)")
        choice = utility.ask("Choice")
        if choice == '1':
            token_joiner()
        else:
            gui.not_free()
    
    def checker_menu():
        utility.make_menu("Cache Checker", "Custom Checker", "Server Checker")
        choice = utility.ask("Choice")
        if choice == '1':
            tokens = TokenManager.get_tokens()
            token_checker(tokens)
        elif choice == '2':
            path = utility.ask("Enter the custom path to load tokens from").strip()
            tokens = TokenManager.custom_path(path)
            token_checker(tokens)
        elif choice == '3':
            gui.not_free()

class gui:
    def get_tokens():
        f = config.read('xvirus_tokens')
        tokens = f.strip().splitlines()
        tokens = [token for token in tokens if token not in [" ", "", "\n"]]
        return tokens


    def get_proxies():
        f = config.read('xvirus_proxies')
        proxies = f.strip().splitlines()
        proxies = [proxy for proxy in proxies if proxy not in [" ", "", "\n"]]
        return proxies



    def not_free():
        Output.set_title("This Option Is Not Free")
        Output("info").notime("You can unlock this options by purchasing the premium version of xvirus!")
        Output.PETC()
    
    def WIP():
        Output.set_title("This Option Is A Work In Progress")
        Output("info").notime("This options is currently unavailable, please be patient and it will be added later.")
        Output.PETC()

    def print_menu():
        pc_username = config._get("xvirus_username")
        theme = config._get("xvirus_theme")

        theme = getattr(Fore, theme)
        lb = Fore.LIGHTBLACK_EX
        r = theme
        logo = f'''{r}
        
                                                                                  
                                         ,.   (   .      )        .      "        
                                       ("     )  )'     ,'        )  . (`     '`   
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  
                                    _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.. 
                                    ██╗  ██╗██╗   ██╗██╗██████╗ ██╗   ██╗ ██████╗ 
                                    ╚██╗██╔╝██║   ██║██║██╔══██╗██║   ██║██╔════╝ 
                                     ╚███╔╝ ╚██╗ ██╔╝██║██████╔╝██║   ██║╚█████╗  
                                     ██╔██╗  ╚████╔╝ ██║██╔══██╗██║   ██║ ╚═══██╗ 
                                    ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝ 
                                    ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  
                                                                                    
> [!] Settings                                                                                     Manage Tokens [TKN] <'''

        options = f'''{r} 
{r}              ({lb}01{r}) {lb}> Token Joiner         {r}({lb}06{r}) {lb}> Global Nick Changer              {r}({lb}11{r}) {lb}> GUI WIP{r}             
{r}              ({lb}02{r}) {lb}> Token Leaver         {r}({lb}07{r}) {lb}> Server Nick Changer              {r}({lb}12{r}) {lb}> Soundboard Spammer{r}
{r}              ({lb}03{r}) {lb}> Token Spammer        {r}({lb}08{r}) {lb}> HypeSquad Changer                {r}({lb}13{r}) {lb}> Token Typer{r}
{r}              ({lb}04{r}) {lb}> Multi Checker        {r}({lb}09{r}) {lb}> Bio Changer                      {r}({lb}14{r}) {lb}> Mass Report{r}
{r}              ({lb}05{r}) {lb}> Bypass Rules         {r}({lb}10{r}) {lb}> Pronouns Changer                 {r}({lb}15{r}) {lb}> WebHook Tool{r}  
           
'''

        ascii = pystyle.Center.XCenter(logo)
        ops = pystyle.Center.XCenter(options)

        print(ascii)
        print(ops)

    def main_menu():
        while True:
            theme = config._get("xvirus_theme")
            theme = getattr(Fore, theme)
            lb = Fore.LIGHTBLACK_EX
            r = theme
            utility.clear()
            Output.set_title(f"Xvirus {THIS_VERSION}")
            gui.print_menu()
            print(f'{r}┌──<root@Xvirus>─[~]')
            choicee = input(f'└──╼ $ {Fore.BLUE}').lstrip("0")
            choice = choicee.upper()

            try:
                options = {
                    '1': menus.joiner_menu,
                    '2': token_leaver,
                    '3': channel_spammer,
                    '4': menus.checker_menu,
                    '5': bypass_rules,
                    '6': global_nicker,
                    '7': server_nicker,
                    '8': hypesquad_changer,
                    '9': token_bio_changer,
                    '10': token_pron_changer,
                    '11': gui.WIP,
                    '12': soundboard_spammer,
                    '13': token_typer,
                    '14': mass_report,
                    '15': webhook_tool,
                    '!': settings,
                    'TKN': token_manager
                }
                choosen = options.get(choice)
                if choosen:

                    threading.Thread(target=check).start()
                    choosen()
                    time.sleep(1)
                else:
                    Output("bad").notime("Invalid choice, please try again!")
                    sleep(1)

            except Exception as e:
                Output("bad").notime(e)
                input()

            gui.main_menu()


if __name__ == "__main__":
    utility.clear()
    Output.set_title("Xvirus Loading")
    gui.main_menu()
