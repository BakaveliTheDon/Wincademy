# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line


language_swiss = 'German'
religion_swiss = 'Roman Catholic'
language_spain = 'Castilian Spanish'
religion_spain = 'Roman Catholic'
capital_spain = 'Madrid'
capital_swiss = 'Bern'
GDP_swiss = 590.71
GDP_spain = 1714.86
ppl_growth_spain = -0.03
ppl_growth_swiss = 0.65
ppl_count_swiss = 8453550
ppl_count_spain = 47260584

print(language_swiss == language_spain)
print(religion_swiss == religion_spain)
print(len(capital_spain) != len(capital_swiss))
print(GDP_swiss > GDP_spain)
print(ppl_growth_spain and ppl_growth_swiss < 1)
# print(ppl_growth_swiss < 1)
print(ppl_count_spain > 10000000 or ppl_count_swiss > 10000000)
comp_spain = ppl_count_spain > 10000000
comp_swiss = ppl_count_swiss > 10000000
# print(comp_spain)
# print(comp_swiss)
if comp_spain == True and comp_swiss == False:
    exactly = True
    print(exactly)
    
