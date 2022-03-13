from tabnanny import check
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def unique_koala_facts(i):
    
    facts = []
    iteration = 0
    while i != len(facts):
        
        fact = random_koala_fact()     
        iteration += 1
        if fact not in facts:
            
            facts.append(fact)    
            print(f'fact {len(facts)} added')   

          
        if iteration >= 1000:
            break

    return facts        
    # return 'task completed', len(facts)    
        

      

      
    
    
def num_joey_facts():
   
   facts = []
   fact_count = 0
   joey_count = 0
   fact = random_koala_fact()

   while fact_count != 10:

       check_fact = random_koala_fact() 

       if fact == check_fact:
           fact_count += 1
           print(fact_count)

    #    if fact not in facts:
    #        facts.append(fact)   

       if 'joey' in check_fact:
           if check_fact not in facts:
            facts.append(check_fact) 
            joey_count += 1

   return joey_count
           
#    joey_count = sum('joey' in word for word in facts)


       
    #    if 'joey' in check_fact:
    #        fact_count += 1
       
    #    if check_fact in facts:

    #         fact_count += 1
    #         print(f' this is {fact_count}')
    #         print(f'this is facts length {len(facts)}')    
        
   

   return joey_count, len(facts), fact_count
            



def koala_weight():

    weight = ''
    facts = []

    while weight == '':

        fact = random_koala_fact()
        facts.append(fact)
      
        for fact in facts:
            if 'kg' in fact:
                print(fact)
                splitted = fact.split()
                for words in splitted:
                    if 'kg' in words:
                        weight = int(words.split('kg')[0])

                return weight








# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

# print(unique_koala_facts(20))
num_joey_facts()
# koala_weight()