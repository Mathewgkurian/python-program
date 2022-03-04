7.	Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character. [eg: onion -> oni$n]



def repl(str): s=str[0]
data=str.replace(s,'$') data=s+data[1:]
return data print(repl("onion"))

