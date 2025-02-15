from botasaurus.request import request, Request
from lxml import html
import argparse
import shutil
import os

@request(cache=False,output=None)
def scrape_infopedia(request: Request, data):
    word = data.get("word")
    url = f"https://www.infopedia.pt/dicionarios/lingua-portuguesa/{word}"
    
    response = request.get(url)
    
    if response.status_code != 200:
        return {"word": word, "error": "Erro ao acessar o site. Verifique sua conexão ou tente novamente mais tarde."}
    
    tree = html.fromstring(response.content)
    
    try:
        type_of = tree.xpath("//div[@class='dolDivisaoCatgram']/span[@class='dolCatgramTbcat']/text()")
        definitions = tree.xpath("//div[@class='dolAcepsRightCell']/span[@class='dolAcepsSubacep']/span[@class='dolSubacepTraduz']/span[@class='dolTraduzTrad']/text()")
        definition_numbers = tree.xpath("//div[@class='dolAcepsNum']/span/text()")
        
        formatted_definitions = [f"{num} {defn}" for num, defn in zip(definition_numbers, definitions)]
        formatted_definitions = [defn.encode('latin1').decode('utf-8') for defn in formatted_definitions]
        
        return {
            "word": word,
            "type": type_of[0].strip() if type_of else "N/A",
            "definitions": formatted_definitions if formatted_definitions else ["Nenhuma definição encontrada."],
        }
    except IndexError:
        return {"word": word, "error": "Nenhuma definição encontrada."}

def remove_pycache():
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")

def main():
    parser = argparse.ArgumentParser(description="Dicionário CLI Diz-Me")
    parser.add_argument("command", type=str, help="Comando a executar (ajuda ou porfavor)")
    parser.add_argument("palavras", nargs="*", type=str, help="Palavras a pesquisar no dicionário")
    args = parser.parse_args()
    
    if args.command == "ajuda":
        print("""
========================================================================================================================
Dicionário CLI Diz-Me
========================================================================================================================
python diz-me.py ajuda -> devolve esta lista de comandos
python diz-me.py porfavor <palavra1> <palavra2> ... -> devolve os conjuntos de dados associados às palavras na Infopédia
========================================================================================================================
        """)
    elif args.command == "porfavor" and args.palavras:
        for palavra in args.palavras:
            result = scrape_infopedia({"word": palavra})
            print("\n========================================================================================================================")
            print(f"Palavra: {result.get('word')}")
            if "error" in result:
                print(f"Erro: {result['error']}")
            else:
                print(f"Tipo: {result.get('type')}")
                print("Definições:")
                for definition in result.get("definitions", []):
                    print(f"- {definition}")
            print("========================================================================================================================\n")
    else:
        print("Comando inválido. Use 'python diz-me.py ajuda' para ver os comandos disponíveis.")
      
    remove_pycache()

main()
