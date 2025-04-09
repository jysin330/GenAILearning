import tiktoken

encoder =tiktoken.encoding_for_model("gpt-4o")
print(f"encoder n vocab {encoder.n_vocab}") # 2,00,019 --> 200k
text = "The cat Sat On The Mat"
tokens = encoder.encode(text)
print(f'Tokens : {tokens}') # [976, 19288, 22232, 2160, 623, 9926]

my_tokens =  [976, 19288, 22232, 2160, 623, 9926]

decoded = encoder.decode(my_tokens)
print(f"Decoded : {decoded}")
