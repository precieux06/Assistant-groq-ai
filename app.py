import os
from groq import Groq
from dotenv import load_dotenv

# Charge les variables d'environnement
load_dotenv()

# Initialise le client Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def main():
    """Fonction principale."""
    
    # MODIFIEZ ICI : Posez votre question !
    user_query = "Veillez faire votre demande à cet endroit..."
    
    print("🤖 Assistant Groq - Démarrage...\n")
    print(f"Votre question : {user_query}\n")
    print("Réponse : ")
    
    try:
        completion = client.chat.completions.create(
            model="moonshotai/kimi-k2-instruct",
            messages=[{"role": "user", "content": user_query}],
            temperature=0.6,
            max_completion_tokens=1024,
            stream=True,
        )

        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
            
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        print("\n🔍 Vérifiez votre clé API dans le fichier .env")

if __name__ == "__main__":
    main()
