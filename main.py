import os
import platform
import subprocess
import time
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

def normal():
    print("--- EXECUTANDO FLUXO NORMAL ---\n")

    # 1. Geração da chave e nonce locais
    key = ChaCha20Poly1305.generate_key()
    nonce = os.urandom(12) # Vai criar um valor único aleatório
    cipher = ChaCha20Poly1305(key) # Criar um objecto com essa chave

    # 2. Mensagem a ser cifrada
    mensagem = b"Informacao confidencial"
    print(f"Mensagem original: {mensagem.decode('utf-8')}")

    # 3. Cifragem (sem dados associados AAD)
    cifrado = cipher.encrypt(nonce, mensagem, None)
    print(f"Mensagem Cifrada (hex): {cifrado.hex()}")

    # 4. Decifragem
    original = cipher.decrypt(nonce, cifrado, None)
    print(f"Mensagem decifrada (texto): {original.decode('utf-8')}")


def testes():
    print("--- EXECUTANDO TESTES DE SEGURANÇA ---\n")

    # 0. Definir dados associados opcionais (AAD)
    aad = b"turma=EIN;tipo=original"

    # 1. Geração da chave e nonce locais para os testes
    key = ChaCha20Poly1305.generate_key()
    nonce = os.urandom(12) # Vai criar um valor único aleatório
    cipher = ChaCha20Poly1305(key) # Criar um objecto com essa chave

    mensagem = b"Informacao confidencial"
    print(f"Mensagem original: {mensagem.decode('utf-8')}")

    # Cifrando com AAD
    cifrado = cipher.encrypt(nonce, mensagem, aad)
    print(f"Mensagem Cifrada (hex): {cifrado.hex()}\n")

    # Decifragem normal para validação inicial
    original = cipher.decrypt(nonce, cifrado, aad)
    print(f"Decifragem normal bem-sucedida: {original.decode('utf-8')}\n")

    print(">>> TESTANDO TENTATIVAS DE VIOLAÇÃO:")

    # Teste 1: alterar um byte do texto cifrado/tag
    alterado = bytearray(cifrado)
    alterado[0] ^= 1
    try:
        cipher.decrypt(nonce, bytes(alterado), aad)
        print("ATENCAO: a mensagem alterada foi aceite (Falha de segurança!)")
    except InvalidTag:
        print("Esperado: alteracao no texto cifrado detectada com sucesso.")

    # Teste 2: usar AAD diferente
    try:
        cipher.decrypt(nonce, cifrado, b"turma=EIN;tipo=alterado")
        print("ATENCAO: AAD alterado foi aceite (Falha de segurança!)")
    except InvalidTag:
        print("Esperado: AAD alterado detectado com sucesso.")

    # Teste 3: usar nonce diferente
    nonce_errado = bytes([nonce[0] ^ 1]) + nonce[1:]
    try:
        cipher.decrypt(nonce_errado, cifrado, aad)
        print("ATENCAO: nonce errado foi aceite (Falha de segurança!)")
    except InvalidTag:
        print("Esperado: nonce errado detectado com sucesso.")

#Função destinada a limpar a tela do terminal
def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)

def exibir_menu():
    while True:
        limpar_tela()
        print("==============================")
        print("    CHACHA20 IMPLEMENTAÇÃO    ")
        print("==============================")
        print("1. Execução Normal (Cifra/Decifra)")
        print("2. Testes de Segurança (Falhas)")
        print("0. Sair")
        print("==============================")

        escolha = input("Selecione uma opção: ")

        if escolha == "1":
            limpar_tela()
            normal()
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == "2":
            limpar_tela()
            testes()
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == "0":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida! Tente novamente.")
            time.sleep(1.5)

def main():
    exibir_menu()

if __name__ == "__main__":
    main()